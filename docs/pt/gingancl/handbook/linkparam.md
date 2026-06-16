---
title: "Elemento &lt;linkParam&gt;"
---

### Definição e uso { data-search-exclude }

O elemento [&lt;linkParam&gt;](linkparam.md) é usado para atribuir um valor a um parâmetro
definido pelo elemento [&lt;connectorParam&gt;](connectorparam.md) do [&lt;causalConnector&gt;](causalconnector.md)
elemento referido pelo elemento pai [&lt;link&gt;](link.md).  O escopo do
o valor atribuído é todo o elemento pai [&lt;link&gt;](link.md).

Em um elemento [&lt;linkParam&gt;](linkparam.md), o atributo *name* refere-se ao nome
de um parâmetro de conector enquanto o atributo *value* define um valor
atribuído a este parâmetro.

### Sintaxe { data-search-exclude }

| Elemento | Atributos | Conteúdo | Pai |
| --- | --- | --- | --- |
| [&lt;linkParam&gt;](linkparam.md) | <u>*nome*</u>, <u>*valor*</u> | -- | [&lt;link&gt;](link.md) |

### Atributos { data-search-exclude }

| Nome | Valor | Descrição |
| --- | --- | --- |
| *nome* | Pode receber qualquer valor de string que comece com uma letra ou sublinhado e que contenha apenas letras, dígitos, <"."> e <"_">. | O atributo *name* identifica exclusivamente o parâmetro dentro do referido elemento [&lt;causalConnector&gt;](causalconnector.md). |
| *valor* | Depende do parâmetro definido pelo elemento [&lt;connectorParam&gt;](connectorparam.md). | O atributo *value* define um valor para o parâmetro.  O valor é, portanto, válido para toda a definição de [&lt;link&gt;](link.md). |