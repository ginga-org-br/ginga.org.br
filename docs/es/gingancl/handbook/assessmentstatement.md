---
title: "Elemento &lt;assessmentStatement&gt;"
---

# &lt;assessmentStatement&gt;

Explore el ejemplo de `<assessmentStatement>` a continuación:

<div class="ginga-playground-container">

<nav class="ginga-playground-tabs" role="tablist" aria-label="Ejemplos de Ginga Playground">
  <button type="button" class="ginga-playground-tab" role="tab" aria-selected="true" data-playground-src="https://ginga.org.br/gingaf/playground/?app=https://raw.githubusercontent.com/ginga-org-br/gingaf/refs/heads/main/examples/ginga.org.br/assessmentStatement.ncl">assessmentStatement.ncl</button>
</nav>

<iframe
  class="ginga-playground"
  src="https://ginga.org.br/gingaf/playground/?app=https://raw.githubusercontent.com/ginga-org-br/gingaf/refs/heads/main/examples/ginga.org.br/assessmentStatement.ncl"
  loading="lazy"
  allow="autoplay; fullscreen">
</iframe>

</div>

El elemento [&lt;assessmentStatement&gt;](assessmentstatement.md) se utiliza para comparar valores de variables
especificado en [&lt;attributeAssessment&gt;](attributeassessment.md) elementos, o para comparar los valores
de estas variables con valores absolutos especificados en [&lt;valueAssessment&gt;](valueassessment.md)
elementos.

El elemento [&lt;assessmentStatement&gt;](assessmentstatement.md) tiene un atributo *comparador*
que compara los valores inferidos de sus elementos secundarios
([&lt;attributeAssessment&gt;](attributeassessment.md) elementos y [&lt;valueAssessment&gt;](valueassessment.md) elementos).

### Sintaxis { data-search-exclude }

| Elemento | Atributos | Contenido | Padre |  |
| --- | --- | --- | --- | --- |
| [&lt;assessmentStatement&gt;](assessmentstatement.md) | <u>*comparador*</u> | ([&lt;attributeAssessment&gt;](attributeassessment.md), ([&lt;attributeAssessment&gt;](attributeassessment.md) | [&lt;valueAssessment&gt;](valueassessment.md))) | [&lt;compoundCondition&gt;](compoundcondition.md) o [&lt;compoundStatement&gt;](compoundstatement.md) |

### Atributos { data-search-exclude }

| Nombre | Valor | Descripción |
| --- | --- | --- |
| *comparador* | "eq", "ne", "gt", "lt", "gte" o "lte". | El atributo *comparador* compara los valores inferidos de los elementos secundarios del elemento [&lt;assessmentStatement&gt;](assessmentstatement.md). |
