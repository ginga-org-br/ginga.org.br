---
title: "Elemento &lt;bindParam&gt;"
---

### Definição e uso { data-search-exclude }

O elemento [&lt;bindParam&gt;](../bindparam/) é usado para atribuir um valor a um parâmetro
definido pelo elemento [&lt;connectorParam&gt;](../connectorparam/) do [&lt;causalConnector&gt;](../causalconnector/)
elemento referido pelo elemento pai [&lt;link&gt;](../link/).  O escopo do
o valor atribuído é limitado ao elemento pai [&lt;bind&gt;](../bind/).

Em um elemento [&lt;bindParam&gt;](../bindparam/) o atributo *name* refere-se ao nome
de um parâmetro de conector, enquanto o atributo *value* define um valor
a ser atribuído ao respectivo parâmetro.

### Sintaxe { data-search-exclude }

| Elemento | Atributos | Conteúdo | Pai |
| --- | --- | --- | --- |
| [&lt;bindParam&gt;](../bindparam/) | <u>*nome*</u>, <u>*valor*</u> | -- | [&lt;bind&gt;](../bind/) |

### Atributos { data-search-exclude }

| Nome | Valor | Descrição |
| --- | --- | --- |
| *nome* | Pode receber qualquer valor de string que comece com uma letra ou sublinhado e que contenha apenas letras, dígitos, <"."> e <"_">. | O atributo *name* identifica exclusivamente o parâmetro dentro do referido elemento [&lt;causalConnector&gt;](../causalconnector/). |
| *valor* | Depende do parâmetro definido pelo elemento [&lt;connectorParam&gt;](../connectorparam/). | O atributo *value* identifica exclusivamente o parâmetro dentro do elemento [&lt;causalConnector&gt;](../causalconnector/) referido. |