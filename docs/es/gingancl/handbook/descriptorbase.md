---
title: "Elemento &lt;descriptorBase&gt;"
---

# &lt;descriptorBase&gt;

Explore el ejemplo de `<descriptorBase>` a continuación:

<div class="ginga-playground-container">

<nav class="ginga-playground-tabs" role="tablist" aria-label="Ejemplos de Ginga Playground">
  <button type="button" class="ginga-playground-tab" role="tab" aria-selected="true" data-playground-src="https://ginga.org.br/gingaf/playground/?app=https://raw.githubusercontent.com/ginga-org-br/gingaf/refs/heads/main/examples/ginga.org.br/descriptorBase.ncl">descriptorBase.ncl</button>
</nav>

<iframe
  class="ginga-playground"
  src="https://ginga.org.br/gingaf/playground/?app=https://raw.githubusercontent.com/ginga-org-br/gingaf/refs/heads/main/examples/ginga.org.br/descriptorBase.ncl"
  loading="lazy"
  allow="autoplay; fullscreen">
</iframe>

</div>

El elemento [&lt;descriptorBase&gt;](descriptorbase.md) agrupa un conjunto de [&lt;descriptor&gt;](descriptor.md)
elementos, cada uno de los cuales define valores iniciales de [&lt;media&gt;](media.md) propiedades.

### Sintaxis { data-search-exclude }

| Elemento | Atributos | Contenido | Padre |  |  |
| --- | --- | --- | --- | --- | --- |
| [&lt;descriptorBase&gt;](descriptorbase.md) | *identificación* | ([&lt;importBase&gt;](importbase.md) | [&lt;descriptor&gt;](descriptor.md) | [&lt;descriptorSwitch&gt;](descriptorswitch.md))+ | [&lt;head&gt;](head.md) |

### Atributos { data-search-exclude }

| Nombre | Valor | Descripción |
| --- | --- | --- |
| *identificación* | Puede recibir cualquier valor de cadena que comience con una letra o un guión bajo y que solo contenga letras, dígitos, <"."> y <"_">. | El atributo *id* identifica de forma única el elemento dentro de un documento. |
