---
title: "Elemento &lt;compositeRule&gt;"
---

### Definição e uso { data-search-exclude }

O elemento [&lt;compositeRule&gt;](compositerule.md) define uma expressão lógica entre seus
elementos filhos ([&lt;rule&gt;](rule.md) e [&lt;compositeRule&gt;](compositerule.md)) por meio de um booleano
atributo do operador.

### Sintaxe { data-search-exclude }

| Elemento | Atributos | Conteúdo | Pai |  |
| --- | --- | --- | --- | --- |
| [&lt;compositeRule&gt;](compositerule.md) | <u>*id*</u>, <u>*operador*</u> | ([&lt;compositeRule&gt;](compositerule.md) | [&lt;rule&gt;](rule.md))+ | [&lt;ruleBase&gt;](rulebase.md) ou [&lt;compositeRule&gt;](compositerule.md) |

### Atributos { data-search-exclude }

| Nome | Valor | Descrição |
| --- | --- | --- |
| *id* | Pode receber qualquer valor de string que comece com uma letra ou sublinhado e que contenha apenas letras, dígitos, <"."> e <"_">. | O atributo *id* identifica exclusivamente o elemento dentro de um documento. |
| *operador* | "e" ou "ou". | O atributo *operator* define uma expressão lógica entre os elementos filhos do elemento [&lt;compositeRule&gt;](compositerule.md). |
