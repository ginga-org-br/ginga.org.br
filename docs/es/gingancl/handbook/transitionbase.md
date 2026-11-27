---
title: "Elemento &lt;transitionBase&gt;"
---

# &lt;transitionBase&gt;

Explore el ejemplo de `<transitionBase>` a continuación:

<div class="ginga-playground-container">

<nav class="ginga-playground-tabs" role="tablist" aria-label="Ejemplos de Ginga Playground">
  <button type="button" class="ginga-playground-tab" role="tab" aria-selected="true" data-playground-src="https://ginga.org.br/gingaf/playground/?app=https://raw.githubusercontent.com/ginga-org-br/gingaf/refs/heads/main/examples/ginga.org.br/transitionBase.ncl">transitionBase.ncl</button>
</nav>

<iframe
  class="ginga-playground"
  src="https://ginga.org.br/gingaf/playground/?app=https://raw.githubusercontent.com/ginga-org-br/gingaf/refs/heads/main/examples/ginga.org.br/transitionBase.ncl"
  loading="lazy"
  allow="autoplay; fullscreen">
</iframe>

</div>

El elemento [&lt;transitionBase&gt;](transitionbase.md) agrupa un conjunto de [&lt;transition&gt;](transition.md)
elementos, cada uno de los cuales define un efecto de transición en [&lt;media&gt;](media.md) elementos
en presentación.

### Sintaxis { data-search-exclude }

| Elemento | Atributos | Contenido | Padre |
| --- | --- | --- | --- |
| [&lt;transitionBase&gt;](transitionbase.md) | *identificación* | ([&lt;importBase&gt;](importbase.md),[&lt;transition&gt;](transition.md))+ | [&lt;head&gt;](head.md) |

### Atributos { data-search-exclude }

| Nombre | Valor | Descripción |
| --- | --- | --- |
| *identificación* | Puede recibir cualquier valor de cadena que comience con una letra o un guión bajo y que solo contenga letras, dígitos, <"."> y <"_">. | El atributo *id* identifica de forma única el elemento dentro de un documento. |