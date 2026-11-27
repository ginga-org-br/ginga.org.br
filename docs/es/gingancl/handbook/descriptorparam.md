---
title: "Elemento &lt;descriptorParam&gt;"
---

# &lt;descriptorParam&gt;

Explore el ejemplo de `<descriptorParam>` a continuación:

<div class="ginga-playground-container">

<nav class="ginga-playground-tabs" role="tablist" aria-label="Ejemplos de Ginga Playground">
  <button type="button" class="ginga-playground-tab" role="tab" aria-selected="true" data-playground-src="https://ginga.org.br/gingaf/playground/?app=https://raw.githubusercontent.com/ginga-org-br/gingaf/refs/heads/main/examples/ginga.org.br/descriptorParam.ncl">descriptorParam.ncl</button>
</nav>

<iframe
  class="ginga-playground"
  src="https://ginga.org.br/gingaf/playground/?app=https://raw.githubusercontent.com/ginga-org-br/gingaf/refs/heads/main/examples/ginga.org.br/descriptorParam.ncl"
  loading="lazy"
  allow="autoplay; fullscreen">
</iframe>

</div>

Los elementos [&lt;descriptorParam&gt;](descriptorparam.md) definen valores iniciales para las propiedades de
un elemento [&lt;media&gt;](media.md). La propiedad se identifica en el *nombre*
atributo del elemento [&lt;descriptorParam&gt;](descriptorparam.md) y el valor está definido en
el atributo *valor*.

### Sintaxis { data-search-exclude }

| Elemento | Atributos | Contenido | Padre |
| --- | --- | --- | --- |
| [&lt;descriptorParam&gt;](descriptorparam.md) | <u>*nombre*</u>, <u>*valor*</u> | -- | [&lt;descriptor&gt;](descriptor.md) |

### Atributos { data-search-exclude }

| Nombre | Valor | Descripción |
| --- | --- | --- |
| *nombre* | Puede recibir cualquier valor de cadena que comience con una letra o un guión bajo y que solo contenga letras, dígitos, <"."> y <"_">. | El atributo *name* identifica la propiedad del elemento [&lt;media&gt;](media.md) que hace referencia al elemento [&lt;descriptor&gt;](descriptor.md) padre del elemento [&lt;descriptorParam&gt;](descriptorparam.md). |
| *valor* | Depende del valor *nombre*. | El atributo *valor* define un valor inicial para la propiedad identificada en el atributo *nombre*. |