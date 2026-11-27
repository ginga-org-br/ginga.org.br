---
title: "Elemento &lt;compositeRule&gt;"
---

# &lt;compositeRule&gt;

Explore el ejemplo de `<compositeRule>` a continuación:

<div class="ginga-playground-container">

<nav class="ginga-playground-tabs" role="tablist" aria-label="Ejemplos de Ginga Playground">
  <button type="button" class="ginga-playground-tab" role="tab" aria-selected="true" data-playground-src="https://ginga.org.br/gingaf/playground/?app=https://raw.githubusercontent.com/ginga-org-br/gingaf/refs/heads/main/examples/ginga.org.br/compositeRule.ncl">compositeRule.ncl</button>
</nav>

<iframe
  class="ginga-playground"
  src="https://ginga.org.br/gingaf/playground/?app=https://raw.githubusercontent.com/ginga-org-br/gingaf/refs/heads/main/examples/ginga.org.br/compositeRule.ncl"
  loading="lazy"
  allow="autoplay; fullscreen">
</iframe>

</div>

El elemento [&lt;compositeRule&gt;](compositerule.md) define una expresión lógica entre sus
elementos secundarios ([&lt;rule&gt;](rule.md) y [&lt;compositeRule&gt;](compositerule.md)) mediante un valor booleano
atributo del operador.

### Sintaxis { data-search-exclude }

| Elemento | Atributos | Contenido | Padre |  |
| --- | --- | --- | --- | --- |
| [&lt;compositeRule&gt;](compositerule.md) | <u>*id*</u>, <u>*operador*</u> | ([&lt;compositeRule&gt;](compositerule.md) | [&lt;rule&gt;](rule.md))+ | [&lt;ruleBase&gt;](rulebase.md) o [&lt;compositeRule&gt;](compositerule.md) |

### Atributos { data-search-exclude }

| Nombre | Valor | Descripción |
| --- | --- | --- |
| *identificación* | Puede recibir cualquier valor de cadena que comience con una letra o un guión bajo y que solo contenga letras, dígitos, <"."> y <"_">. | El atributo *id* identifica de forma única el elemento dentro de un documento. |
| *operador* | "y" o "o". | El atributo *operador* define una expresión lógica entre los elementos secundarios del elemento [&lt;compositeRule&gt;](compositerule.md). |
