---
title: "Elemento &lt;assessmentStatement&gt;"
---

### Definição e uso { data-search-exclude }

O elemento [&lt;assessmentStatement&gt;](../assessmentstatement/) é usado para comparar valores de variáveis
especificado em elementos [&lt;attributeAssessment&gt;](../attributeassessment/) ou para comparar os valores
dessas variáveis com valores absolutos especificados em [&lt;valueAssessment&gt;](../valueassessment/)
elementos.

O elemento [&lt;assessmentStatement&gt;](../assessmentstatement/) possui um atributo *comparator*
que compara os valores inferidos de seus elementos filhos
([&lt;attributeAssessment&gt;](../attributeassessment/) elementos e [&lt;valueAssessment&gt;](../valueassessment/) elementos).

### Sintaxe { data-search-exclude }

| Elemento | Atributos | Conteúdo | Pai |  |
| --- | --- | --- | --- | --- |
| [&lt;assessmentStatement&gt;](../assessmentstatement/) | <u>*comparador*</u> | ([&lt;attributeAssessment&gt;](../attributeassessment/), ([&lt;attributeAssessment&gt;](../attributeassessment/) | [&lt;valueAssessment&gt;](../valueassessment/))) | [&lt;compoundCondition&gt;](../compoundcondition/) ou [&lt;compoundStatement&gt;](../compoundstatement/) |

### Atributos { data-search-exclude }

| Nome | Valor | Descrição |
| --- | --- | --- |
| *comparador* | "eq", "ne", "gt", "lt", "gte" ou "lte". | O atributo *comparator* compara os valores inferidos dos elementos filhos do elemento [&lt;assessmentStatement&gt;](../assessmentstatement/). |
