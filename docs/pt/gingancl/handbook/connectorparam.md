---
title: "Elemento &lt;connectorParam&gt;"
---

### Definição e uso { data-search-exclude }

O elemento [&lt;connectorParam&gt;](connectorparam.md) é usado para parametrizar o conector
valores de atributos.  Qualquer atributo definido por um elemento [&lt;causalConnector&gt;](causalconnector.md)
ou por seus elementos descendentes pode ter seu valor especificado como parâmetro
cujo valor é definido pelo relacionamento que se refere ao conector,
usando elementos [&lt;linkParam&gt;](linkparam.md) ou [&lt;bindParam&gt;](bindparam.md).

Em um elemento [&lt;connectorParam&gt;](connectorparam.md) o atributo *name* define o
nome do parâmetro e *type* atribuem o tipo de parâmetro.

Para especificar que um atributo definido por [&lt;causalConnector&gt;](causalconnector.md)
elemento ou por seus elementos descendentes recebe o valor do parâmetro, é
suficiente para definir o valor do atributo como o nome do parâmetro precedido por
o símbolo "$".  Por exemplo, para parametrizar o atributo delay
de um elemento [&lt;simpleAction&gt;](simpleaction.md), um parâmetro chamado *actionDelay* é
definido e o valor "$actionDelay" é usado no atributo
(*atraso*="$actionDelay").

### Sintaxe { data-search-exclude }

| Elemento | Atributos | Conteúdo | Pai |
| --- | --- | --- | --- |
| [&lt;connectorParam&gt;](connectorparam.md) | <u>*nome*</u>, *tipo* | -- | [&lt;causalConnector&gt;](causalconnector.md) |

### Atributos { data-search-exclude }

| Nome | Valor | Descrição |
| --- | --- | --- |
| *nome* | Pode receber qualquer valor de string que comece com uma letra ou sublinhado e que contenha apenas letras, dígitos, <"."> e <"_">. | O atributo *name* identifica exclusivamente o parâmetro dentro de um elemento [&lt;causalConnector&gt;](causalconnector.md). |
| *tipo* | Corda. | O *type* define um tipo para o parâmetro. |