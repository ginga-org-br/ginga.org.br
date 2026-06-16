---
title: "Elemento &lt;assessmentStatement&gt;"
---

### Definición y uso { data-search-exclude }

El elemento [&lt;assessmentStatement&gt;](../assessmentstatement/) se utiliza para comparar valores de variables
especificado en [&lt;attributeAssessment&gt;](../attributeassessment/) elementos, o para comparar los valores
de estas variables con valores absolutos especificados en [&lt;valueAssessment&gt;](../valueassessment/)
elementos.

El elemento [&lt;assessmentStatement&gt;](../assessmentstatement/) tiene un atributo *comparador*
que compara los valores inferidos de sus elementos secundarios
([&lt;attributeAssessment&gt;](../attributeassessment/) elementos y [&lt;valueAssessment&gt;](../valueassessment/) elementos).

### Sintaxis { data-search-exclude }

| Elemento | Atributos | Contenido | Padre |  |
| --- | --- | --- | --- | --- |
| [&lt;assessmentStatement&gt;](../assessmentstatement/) | <u>*comparador*</u> | ([&lt;attributeAssessment&gt;](../attributeassessment/), ([&lt;attributeAssessment&gt;](../attributeassessment/) | [&lt;valueAssessment&gt;](../valueassessment/))) | [&lt;compoundCondition&gt;](../compoundcondition/) o [&lt;compoundStatement&gt;](../compoundstatement/) |

### Atributos { data-search-exclude }

| Nombre | Valor | Descripción |
| --- | --- | --- |
| *comparador* | "eq", "ne", "gt", "lt", "gte" o "lte". | El atributo *comparador* compara los valores inferidos de los elementos secundarios del elemento [&lt;assessmentStatement&gt;](../assessmentstatement/). |
