---
title: "Elemento &lt;linkParam&gt;"
---

# &lt;linkParam&gt;

Explore el ejemplo de `<linkParam>` a continuación:

<div class="ginga-playground-container">

<nav class="ginga-playground-tabs" role="tablist" aria-label="Ejemplos de Ginga Playground">
  <button type="button" class="ginga-playground-tab" role="tab" aria-selected="true" data-playground-src="https://ginga.org.br/gingaf/playground/?app=https://raw.githubusercontent.com/ginga-org-br/gingaf/refs/heads/main/examples/ginga.org.br/linkParam.ncl">linkParam.ncl</button>
</nav>

<iframe
  class="ginga-playground"
  src="https://ginga.org.br/gingaf/playground/?app=https://raw.githubusercontent.com/ginga-org-br/gingaf/refs/heads/main/examples/ginga.org.br/linkParam.ncl"
  loading="lazy"
  allow="autoplay; fullscreen">
</iframe>

</div>

El elemento [&lt;linkParam&gt;](linkparam.md) se utiliza para atribuir un valor a un parámetro
definido por el elemento [&lt;connectorParam&gt;](connectorparam.md) de [&lt;causalConnector&gt;](causalconnector.md)
elemento referido por el elemento padre [&lt;link&gt;](link.md).  El alcance de la
El valor atribuido es todo el elemento principal [&lt;link&gt;](link.md).

En un elemento [&lt;linkParam&gt;](linkparam.md), el atributo *name* hace referencia al nombre
de un parámetro de conector mientras que el atributo *valor* define un valor
asignado a este parámetro.

### Sintaxis { data-search-exclude }

| Elemento | Atributos | Contenido | Padre |
| --- | --- | --- | --- |
| [&lt;linkParam&gt;](linkparam.md) | <u>*nombre*</u>, <u>*valor*</u> | -- | [&lt;link&gt;](link.md) |

### Atributos { data-search-exclude }

| Nombre | Valor | Descripción |
| --- | --- | --- |
| *nombre* | Puede recibir cualquier valor de cadena que comience con una letra o un guión bajo y que solo contenga letras, dígitos, <"."> y <"_">. | El atributo *name* identifica de forma única el parámetro dentro del elemento [&lt;causalConnector&gt;](causalconnector.md) al que se hace referencia. |
| *valor* | Depende del parámetro definido por el elemento [&lt;connectorParam&gt;](connectorparam.md). | El atributo *valor* define un valor para el parámetro.  Por tanto, el valor es válido para toda la definición [&lt;link&gt;](link.md). |