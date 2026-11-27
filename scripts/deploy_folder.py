import os
from pathlib import Path
import subprocess
import sys


ROOT_DIR = Path(__file__).resolve().parent.parent
DEFAULT_SITE_DIR = ROOT_DIR / "site"


def find_mount_dir(target_dir):
    curr = Path(os.path.realpath(target_dir))
    while str(curr) != "/" and str(curr):
        if os.path.ismount(curr):
            return str(curr)
        parent = curr.parent
        if parent == curr:
            break
        curr = parent
    return None


def get_fstype(mount_dir):
    try:
        res = subprocess.run(
            ["findmnt", "-n", "-o", "FSTYPE", mount_dir],
            capture_output=True,
            text=True,
            check=False,
        )
        if res.returncode == 0:
            return res.stdout.strip()
    except FileNotFoundError:
        pass
    return ""


def deploy_folder(deploy_target, site_dir=DEFAULT_SITE_DIR):
    target = (deploy_target or "").strip()
    if not target:
        print("\033[0;31mError: GINGA_ORG_DEPLOY is not set.\033[0m", file=sys.stderr)
        return 1

    mount_dir = find_mount_dir(target)
    if mount_dir is None:
        print(
            f"\033[0;31mError: {target} is not mounted (remote FTPES mount not detected).\033[0m"
        )
        return 1

    fstype = get_fstype(mount_dir)
    if not any(tok in fstype.lower() for tok in ("fuse", "rclone", "ftp")):
        print(
            f"\033[0;33mWarning: {mount_dir} filesystem type is '{fstype}' (expected remote FTPES / rclone).\033[0m"
        )

    site_path = f"{str(Path(site_dir)).rstrip('/')}/"
    res = subprocess.run(
        [
            "rsync",
            "-rlptcO",
            "--delete-after",
            "--inplace",
            "--exclude",
            "/gingaf",
            "--out-format=%o %n",
            site_path,
            target,
        ],
        check=False,
    )
    if res.returncode != 0:
        return res.returncode

    print("\033[0;32mDeployment completed successfully.\033[0m")
    return 0


def main(argv=None):
    args = sys.argv[1:] if argv is None else list(argv)
    deploy_target = args[0] if args else os.environ.get("GINGA_ORG_DEPLOY", "")
    return deploy_folder(deploy_target)


if __name__ == "__main__":
    raise SystemExit(main())
