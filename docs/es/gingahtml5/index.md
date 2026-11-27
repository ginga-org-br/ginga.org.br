---
title: Sobre Ginga-HTML5
---

# Ginga-HTML5

Explore los ejemplos de Ginga-HTML5 a continuación:

<div class="ginga-playground-container">

<nav class="ginga-playground-tabs" role="tablist" aria-label="Ejemplos de Ginga Playground">
  <button type="button" class="ginga-playground-tab" role="tab" aria-selected="true" data-playground-src="https://ginga.org.br/gingaf/playground/?app=https://raw.githubusercontent.com/ginga-org-br/gingaf/refs/heads/main/examples/image.html">image.html</button>
  <button type="button" class="ginga-playground-tab" role="tab" aria-selected="false" data-playground-src="https://ginga.org.br/gingaf/playground/?app=https://raw.githubusercontent.com/ginga-org-br/gingaf/refs/heads/main/examples/current_service.html">current_service.html</button>
</nav>

<iframe
  class="ginga-playground"
  src="https://ginga.org.br/gingaf/playground/?app=https://raw.githubusercontent.com/ginga-org-br/gingaf/refs/heads/main/examples/image.html"
  loading="lazy"
  allow="autoplay; fullscreen">
</iframe>

</div>

Esta Norma (ABNT NBR 15606-10) estandariza un perfil común de HTML5, CSS y APIs de JavaScript que deben ser soportados por los dispositivos receptores de televisión digital interactiva. El objetivo de esta norma es definir un perfil que puedan utilizar los desarrolladores de aplicaciones interactivas, así como los requisitos necesarios para los implementadores del middleware Ginga. Esta norma no especifica extensiones propietarias a las tecnologías mencionadas, sino un subconjunto estandarizado para el desarrollo de aplicaciones para televisión interactiva (TV 2.5 y TV 3.0).

Esta Norma está destinada principalmente a las entidades que especifican receptores y/o estándares basados en Ginga-HTML5. También está destinada a los desarrolladores de aplicaciones que utilicen las funcionalidades de Ginga-HTML5 y sus APIs. La especificación del perfil HTML5 para el middleware Ginga tiene como objetivo asegurar la interoperabilidad de las aplicaciones en diferentes implementaciones de plataformas que lo soportan.

Esta Norma no especifica la forma en que el entorno de aplicación Ginga-HTML5 debe implementarse en un receptor conforme. Un fabricante de receptores puede implementar su máquina de presentación Ginga-HTML5 utilizando cualquier implementación, siempre que cumpla con los requisitos especificados.

## Arquitectura y Entorno de Ejecución

El entorno de presentación Ginga-HTML5 opera integrado con el núcleo común del middleware (*Ginga Common Core*), compartiendo recursos de sintonía, planos gráficos, video principal de radiodifusión y eventos de control remoto.

- **Plano Gráfico y Resolución**: Las aplicaciones HTML5 se renderizan en un plano gráfico con soporte para composición alfa (transparencia RGBA) superpuesto al plano de video de radiodifusión, operando típicamente en resoluciones lógicas de `1280x720` (HD) o `1920x1080` (Full HD).
- **Ciclo de Vida de la Aplicación**: Las aplicaciones se señalizan mediante tablas de información de aplicación (AIT - *Application Information Table*) en el flujo de transporte MPEG-2 TS o se entregan por banda ancha (híbrido broadcast-broadband), pudiendo iniciarse automáticamente (*autostart*), bajo demanda o finalizarse por señalización de la emisora.
- **Integración con Ginga-NCL**: Las aplicaciones HTML5 pueden ejecutarse de forma autónoma o incrustarse como nodos de medios declarativos ([&lt;media&gt;](../gingancl/handbook/media.md)) dentro de documentos Ginga-NCL.

## Perfil Técnico Soportado

| Capa | Especificaciones Soportadas |
| :--- | :--- |
| **Marcado** | HTML5 (W3C HTML5), incluyendo elementos semánticos, `<canvas>` 2D, `<video>`, `<audio>` y `<object>` para video de radiodifusión. |
| **Estilos** | CSS 2.1, CSS3 Color (opacidad/RGBA), CSS3 Backgrounds and Borders, CSS3 Transforms 2D, CSS3 Transitions, CSS3 Animations, Flexbox y Media Queries. |
| **Scripting** | ECMAScript (ES5.1 / ES6+), DOM Level 3 Events, XMLHttpRequest Level 2, Fetch API, Web Storage (`localStorage` / `sessionStorage`) y WebSockets. |
| **Formatos de Medios** | Imágenes PNG, JPEG, GIF y SVG; Audio AAC-LC y MP3; Video H.264/AVC (MP4 y MPEG-DASH) además del flujo elemental del canal sintonizado. |
| **Fuentes** | Soporte para `@font-face` (TrueType/OpenType y WOFF) además de la familia de fuentes predeterminada *Tiresias* / sans-serif del receptor. |

## Integración con Ginga-CC WebServices

Las aplicaciones HTML5 ejecutadas en Ginga interactúan con los recursos de radiodifusión, ajustes del receptor, reproductores multimedia y dispositivos secundarios mediante **Ginga-CC-WebServices** (ABNT NBR 15606-11), que estandariza las APIs REST y WebSocket expuestas por el núcleo común de Ginga.
