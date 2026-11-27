---
title: "Elemento &lt;importedDocumentBase&gt;"
---

# &lt;importedDocumentBase&gt;

Explore el ejemplo de `<importedDocumentBase>` a continuación:

<div class="ginga-playground-container">

<nav class="ginga-playground-tabs" role="tablist" aria-label="Ejemplos de Ginga Playground">
  <button type="button" class="ginga-playground-tab" role="tab" aria-selected="true" data-playground-src="https://ginga.org.br/gingaf/playground/?app=https://raw.githubusercontent.com/ginga-org-br/gingaf/refs/heads/main/examples/ginga.org.br/importedDocumentBase.ncl">importedDocumentBase.ncl</button>
</nav>

<iframe
  class="ginga-playground"
  src="https://ginga.org.br/gingaf/playground/?app=https://raw.githubusercontent.com/ginga-org-br/gingaf/refs/heads/main/examples/ginga.org.br/importedDocumentBase.ncl"
  loading="lazy"
  allow="autoplay; fullscreen">
</iframe>

</div>

El elemento [&lt;importedDocumentBase&gt;](importeddocumentbase.md) especifica un conjunto de NCL importados.
documentos.

### Sintaxis { data-search-exclude }

| Elemento | Atributos | Contenido | Padre |
| --- | --- | --- | --- |
| [&lt;importedDocumentBase&gt;](importeddocumentbase.md) | *identificación* | ([&lt;importNCL&gt;](importncl.md))+ | [&lt;head&gt;](head.md) |

### Atributos { data-search-exclude }

| Nombre | Valor | Descripción |
| --- | --- | --- |
| *identificación* | Puede recibir cualquier valor de cadena que comience con una letra o un guión bajo y que solo contenga letras, dígitos, <"."> y <"_">. | El atributo *id* identifica de forma única el elemento dentro de un documento. |