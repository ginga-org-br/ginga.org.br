---
title: "Elemento &lt;assessmentStatement&gt;"
---

### Definição e uso { data-search-exclude }

O elemento [&lt;assessmentStatement&gt;](assessmentstatement.md) é usado para comparar valores de variáveis
especificado em elementos [&lt;attributeAssessment&gt;](attributeassessment.md) ou para comparar os valores
dessas variáveis com valores absolutos especificados em [&lt;valueAssessment&gt;](valueassessment.md)
elementos.

O elemento [&lt;assessmentStatement&gt;](assessmentstatement.md) possui um atributo *comparator*
que compara os valores inferidos de seus elementos filhos
([&lt;attributeAssessment&gt;](attributeassessment.md) elementos e [&lt;valueAssessment&gt;](valueassessment.md) elementos).

### Sintaxe { data-search-exclude }

| Elemento | Atributos | Conteúdo | Pai |  |
| --- | --- | --- | --- | --- |
| [&lt;assessmentStatement&gt;](assessmentstatement.md) | <u>*comparador*</u> | ([&lt;attributeAssessment&gt;](attributeassessment.md), ([&lt;attributeAssessment&gt;](attributeassessment.md) | [&lt;valueAssessment&gt;](valueassessment.md))) | [&lt;compoundCondition&gt;](compoundcondition.md) ou [&lt;compoundStatement&gt;](compoundstatement.md) |

### Atributos { data-search-exclude }

| Nome | Valor | Descrição |
| --- | --- | --- |
| *comparador* | "eq", "ne", "gt", "lt", "gte" ou "lte". | O atributo *comparator* compara os valores inferidos dos elementos filhos do elemento [&lt;assessmentStatement&gt;](assessmentstatement.md). |
