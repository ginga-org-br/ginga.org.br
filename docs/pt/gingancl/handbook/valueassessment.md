---
title: "Elemento &lt;valueAssessment&gt;"
---

### Definição e uso { data-search-exclude }

O elemento [&lt;valueAssessment&gt;](../valueassessment/) é usado para definir um valor a ser comparado
em relação a outros valores de variáveis especificados por [&lt;attributeAssessment&gt;](../attributeassessment/)
elementos.

O elemento [&lt;valueAssessment&gt;](../valueassessment/) possui um atributo de valor que pode assumir um
valor de estado do evento ("ocorrendo", "pausado" ou "suspenso") ou qualquer valor a ser
comparado com uma propriedade de nó ou atributo de evento ("ocorrências" ou
"repetição").

### Sintaxe { data-search-exclude }

| Elemento | Atributos | Conteúdo | Pai |
| --- | --- | --- | --- |
| [&lt;valueAssessment&gt;](../valueassessment/) | <u>*valor*</u> | -- | [&lt;assessmentStatement&gt;](../assessmentstatement/) |

### Atributos { data-search-exclude }

| Nome | Valor | Descrição |
| --- | --- | --- |
| *valor* | <p>String.</p><p>Pode ser um valor de estado de evento ("ocorrendo", "pausado" ou "suspenso") ou qualquer valor a ser comparado com uma propriedade de nó ou atributo de evento ("ocorrências" ou "repetição").</p> | O atributo *value* define um valor a ser comparado em elementos [&lt;assessmentStatement&gt;](../assessmentstatement/). |