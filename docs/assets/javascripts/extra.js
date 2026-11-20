(function () {
  function getCurrentLang() {
    var path = window.location.pathname.toLowerCase();
    if (path.includes('/en/') || path.endsWith('/en')) return 'en';
    if (path.includes('/es/') || path.endsWith('/es')) return 'es';
    if (path.includes('/pt/') || path.endsWith('/pt')) return 'pt';
    var docLang = (document.documentElement.lang || '').toLowerCase();
    if (docLang.startsWith('en')) return 'en';
    if (docLang.startsWith('es')) return 'es';
    if (docLang.startsWith('pt')) return 'pt';
    return 'pt';
  }

  function matchesLang(item, lang) {
    if (!item) return false;
    var loc = (item.location || '').toLowerCase();
    if (loc.includes('/' + lang + '/') || loc.startsWith(lang + '/')) return true;
    if (Array.isArray(item.path) && item.path.length > 0) {
      var root = item.path[0].toLowerCase();
      if (lang === 'pt' && root.includes('portugu')) return true;
      if (lang === 'en' && root.includes('english')) return true;
      if (lang === 'es' && root.includes('español')) return true;
    }
    return false;
  }

  function escapeTag(str) {
    if (typeof str !== 'string') return str;
    if (str.startsWith('<') && str.endsWith('>')) {
      return '&lt;' + str.slice(1, -1) + '&gt;';
    }
    return str;
  }

  function processSearchItem(item) {
    if (!item) return item;
    if (item.title) {
      item.title = escapeTag(item.title);
    }
    if (Array.isArray(item.path)) {
      item.path = item.path.map(escapeTag);
    }
    return item;
  }

  if (typeof Worker !== 'undefined' && Worker.prototype) {
    var origPostMessage = Worker.prototype.postMessage;
    Worker.prototype.postMessage = function (message, transfer) {
      if (message && message.type === 0 && message.data && Array.isArray(message.data.items)) {
        var currentLang = getCurrentLang();
        message.data.items = message.data.items
          .filter(function (item) {
            return matchesLang(item, currentLang);
          })
          .map(processSearchItem);
      }
      return origPostMessage.apply(this, arguments);
    };
  }

  var originalFetch = window.fetch;
  if (originalFetch) {
    window.fetch = function (resource, init) {
      var url = (typeof resource === 'string' ? resource : (resource && (resource.url || resource.href))) || String(resource || '');
      if (url && url.includes('search.json')) {
        return originalFetch.apply(this, arguments).then(async function (response) {
          try {
            var currentLang = getCurrentLang();
            var clone = response.clone();
            var data = await clone.json();
            if (data && Array.isArray(data.items)) {
              data.items = data.items
                .filter(function (item) {
                  return matchesLang(item, currentLang);
                })
                .map(processSearchItem);
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

  function bindPlaygroundTabs(root) {
    if (!root || typeof root.querySelectorAll !== 'function') return;
    var containers = root.querySelectorAll('.ginga-playground-container');
    containers.forEach(function (container) {
      if (container.getAttribute('data-playground-bound') === 'true') return;
      container.setAttribute('data-playground-bound', 'true');
      var iframe = container.querySelector('iframe.ginga-playground');
      var tabs = container.querySelectorAll('.ginga-playground-tab');
      if (!iframe || !tabs.length) return;
      tabs.forEach(function (tab) {
        tab.addEventListener('click', function () {
          var nextSrc = tab.getAttribute('data-playground-src');
          tabs.forEach(function (t) {
            t.setAttribute('aria-selected', t === tab ? 'true' : 'false');
          });
          if (nextSrc && iframe.getAttribute('src') !== nextSrc) {
            iframe.setAttribute('src', nextSrc);
          }
        });
      });
    });
  }

  if (typeof document !== 'undefined' && typeof document.addEventListener === 'function') {
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', function () {
        bindPlaygroundTabs(document);
      });
    } else {
      bindPlaygroundTabs(document);
    }
  }
  if (typeof window !== 'undefined' && window.document$ && typeof window.document$.subscribe === 'function') {
    window.document$.subscribe(function (doc) {
      bindPlaygroundTabs(doc || document);
    });
  }
})();
