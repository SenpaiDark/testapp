const CACHE = "mayor4code-v3";
const STATIC_ASSETS = [
  "/",
  "/static/css/design-system.css",
  "/static/css/components.css",
  "/static/css/layout.css",
  "/static/css/pages.css",
  "/static/img/favicon.svg",
  "/static/manifest.json",
];

self.addEventListener("install", (event) => {
  event.waitUntil(
    caches.open(CACHE).then((cache) => {
      return cache.addAll(STATIC_ASSETS);
    })
  );
  self.skipWaiting();
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches.keys().then((keys) => {
      return Promise.all(
        keys.filter((k) => k !== CACHE).map((k) => caches.delete(k))
      );
    })
  );
  self.clients.claim();
});

self.addEventListener("fetch", (event) => {
  const url = new URL(event.request.url);

  // Cache-first for static assets
  if (
    url.pathname.startsWith("/static/") ||
    url.pathname === "/" ||
    url.pathname === "/manifest.json"
  ) {
    event.respondWith(
      caches.match(event.request).then((cached) => {
        return (
          cached ||
          fetch(event.request).then((res) => {
            return caches.open(CACHE).then((cache) => {
              cache.put(event.request, res.clone());
              return res;
            });
          })
        );
      })
    );
    return;
  }

  // Network-first for everything else (API, pages)
  event.respondWith(
    fetch(event.request)
      .then((res) => {
        return caches.open(CACHE).then((cache) => {
          cache.put(event.request, res.clone());
          return res;
        });
      })
      .catch(() => {
        return caches.match(event.request).then((cached) => {
          return (
            cached ||
            new Response("You appear to be offline. Please connect to the internet.", {
              status: 503,
              headers: { "Content-Type": "text/plain" },
            })
          );
        });
      })
  );
});