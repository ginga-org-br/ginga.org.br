---
title: "Elemento &lt;ruleBase&gt;"
---

### Definição e uso { data-search-exclude }

O elemento [&lt;ruleBase&gt;](../rulebase/) agrupa um conjunto de regras especificadas em [&lt;rule&gt;](../rule/)
e [&lt;compositeRule&gt;](../compositerule/) elementos.  A especificação de regras em NCL 3.0
foi feito em um módulo separado, porque eles são úteis para definir
componentes alternativos ou descritores alternativos.

### Sintaxe { data-search-exclude }

| Elemento | Atributos | Conteúdo | Pai |  |  |
| --- | --- | --- | --- | --- | --- |
| [&lt;ruleBase&gt;](../rulebase/) | *id* | ([&lt;importBase&gt;](../importbase/) | [&lt;compositeRule&gt;](../compositerule/) | [&lt;rule&gt;](../rule/))+ | [&lt;head&gt;](../head/) |

### Atributos { data-search-exclude }

| Nome | Valor | Descrição |
| --- | --- | --- |
| *id* | Pode receber qualquer valor de string que comece com uma letra ou sublinhado e que contenha apenas letras, dígitos, <"."> e <"_">. | O atributo *id* identifica exclusivamente o elemento dentro de um documento. |
