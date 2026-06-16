// Language-scoped search result filter
(function () {
  function getCurrentLang() {
    const path = window.location.pathname.toLowerCase();
    if (path.includes('/en/') || path.endsWith('/en')) return 'en';
    if (path.includes('/es/') || path.endsWith('/es')) return 'es';
    if (path.includes('/pt/') || path.endsWith('/pt')) return 'pt';
    const docLang = (document.documentElement.lang || '').toLowerCase();
    if (docLang.startsWith('en')) return 'en';
    if (docLang.startsWith('es')) return 'es';
    if (docLang.startsWith('pt')) return 'pt';
    return 'pt';
  }

  const currentLang = getCurrentLang();

  function getItemLang(item) {
    if (!item) return null;
    const pathArr = item.path || (item.doc && item.doc.path) || (item.item && item.item.path);
    if (Array.isArray(pathArr) && pathArr.length > 0) {
      const top = String(pathArr[0]).toLowerCase();
      if (top.includes('portugu') || top === 'pt' || top === 'portugues') return 'pt';
      if (top.includes('english') || top === 'en' || top.includes('ingl')) return 'en';
      if (top.includes('español') || top.includes('espanol') || top === 'es' || top.includes('spanish')) return 'es';
    }
    const loc = item.location || (item.doc && item.doc.location) || (item.item && item.item.location) || '';
    if (typeof loc === 'string' && loc) {
      const cleanLoc = loc.toLowerCase();
      if (/(^|\/)(pt)(\/|$)/.test(cleanLoc)) return 'pt';
      if (/(^|\/)(en)(\/|$)/.test(cleanLoc)) return 'en';
      if (/(^|\/)(es)(\/|$)/.test(cleanLoc)) return 'es';
    }
    return null;
  }

  function filterItems(items) {
    if (!Array.isArray(items)) return items;
    return items.filter(function (item) {
      const lang = getItemLang(item);
      return !lang || lang === currentLang;
    });
  }

  // 1. Intercept fetch for search.json (handles String, URL, and Request objects)
  const originalFetch = window.fetch;
  if (originalFetch) {
    window.fetch = function (resource, init) {
      const url = (typeof resource === 'string' ? resource : (resource && (resource.url || resource.href))) || String(resource || '');
      if (url && url.includes('search.json')) {
        return originalFetch.apply(this, arguments).then(async function (response) {
          try {
            const clone = response.clone();
            const data = await clone.json();
            if (data && Array.isArray(data.items)) {
              data.items = filterItems(data.items);
            }
            return new Response(JSON.stringify(data), {
              status: response.status,
              statusText: response.statusText,
              headers: response.headers
            });
          } catch (e) {
            return response;
          }
        });
      }
      return originalFetch.apply(this, arguments);
    };
  }

  // 2. Intercept XMLHttpRequest for search.json
  const OriginalXHR = window.XMLHttpRequest;
  if (OriginalXHR) {
    function PatchedXHR() {
      const xhr = new OriginalXHR();
      let isSearchJson = false;
      const origOpen = xhr.open;
      xhr.open = function (method, url) {
        const urlStr = String(url || '');
        if (urlStr.includes('search.json')) {
          isSearchJson = true;
        }
        return origOpen.apply(this, arguments);
      };
      const origSend = xhr.send;
      xhr.send = function () {
        if (isSearchJson) {
          xhr.addEventListener('readystatechange', function () {
            if (xhr.readyState === 4 && xhr.status >= 200 && xhr.status < 300) {
              try {
                const data = JSON.parse(xhr.responseText);
                if (data && Array.isArray(data.items)) {
                  data.items = filterItems(data.items);
                  Object.defineProperty(xhr, 'responseText', { value: JSON.stringify(data), writable: true });
                  Object.defineProperty(xhr, 'response', { value: JSON.stringify(data), writable: true });
                }
              } catch (e) { }
            }
          });
        }
        return origSend.apply(this, arguments);
      };
      return xhr;
    }
    PatchedXHR.prototype = OriginalXHR.prototype;
    window.XMLHttpRequest = PatchedXHR;
  }

  // 3. Intercept Worker communications (both outgoing type 0 and incoming type 3)
  const NativeWorker = window.Worker;
  if (NativeWorker) {
    window.Worker = function (scriptURL, options) {
      const worker = new NativeWorker(scriptURL, options);
      const nativePostMessage = worker.postMessage;

      worker.postMessage = function (message, transfer) {
        if (message && message.type === 0 && message.data && Array.isArray(message.data.items)) {
          message.data.items = filterItems(message.data.items);
        }
        return nativePostMessage.apply(this, arguments);
      };

      function wrapMessageListener(originalListener) {
        return function (event) {
          if (event && event.data) {
            if (event.data.type === 3 && event.data.data && Array.isArray(event.data.data.items)) {
              event.data.data.items = filterItems(event.data.data.items);
            } else if (Array.isArray(event.data.items)) {
              event.data.items = filterItems(event.data.items);
            }
          }
          return originalListener.apply(this, arguments);
        };
      }

      const nativeAddEventListener = worker.addEventListener;
      worker.addEventListener = function (type, listener, options) {
        if (type === 'message' && typeof listener === 'function') {
          return nativeAddEventListener.call(this, type, wrapMessageListener(listener), options);
        }
        return nativeAddEventListener.apply(this, arguments);
      };

      let _onmessage = null;
      Object.defineProperty(worker, 'onmessage', {
        get: function () {
          return _onmessage;
        },
        set: function (fn) {
          if (typeof fn === 'function') {
            _onmessage = wrapMessageListener(fn);
            worker.addEventListener('message', _onmessage);
          } else {
            _onmessage = null;
          }
        },
        configurable: true,
        enumerable: true
      });

      return worker;
    };
    window.Worker.prototype = NativeWorker.prototype;
  }

  // 4. DOM MutationObserver fallback: Hide non-matching search result elements from UI
  if (typeof window !== 'undefined' && typeof document !== 'undefined') {
    document.addEventListener('DOMContentLoaded', function () {
      const observer = new MutationObserver(function () {
        const links = document.querySelectorAll('.md-search-result__link, .md-search-result__item a');
        links.forEach(function (link) {
          const href = (link.getAttribute('href') || '').toLowerCase();
          if (!href) return;
          let hrefLang = null;
          if (/(^|\/)(pt)(\/|$)/.test(href)) hrefLang = 'pt';
          else if (/(^|\/)(en)(\/|$)/.test(href)) hrefLang = 'en';
          else if (/(^|\/)(es)(\/|$)/.test(href)) hrefLang = 'es';

          if (hrefLang && hrefLang !== currentLang) {
            const itemContainer = link.closest('.md-search-result__item') || link.parentElement;
            if (itemContainer) {
              itemContainer.style.display = 'none';
            }
          }
        });
      });

      const container = document.querySelector('.md-search-result') || document.body;
      if (container) {
        observer.observe(container, { childList: true, subtree: true });
      }
    });
  }
})();
