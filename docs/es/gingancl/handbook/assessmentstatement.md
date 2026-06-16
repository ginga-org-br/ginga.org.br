---
title: "Elemento &lt;assessmentStatement&gt;"
---

### Definición y uso { data-search-exclude }

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
