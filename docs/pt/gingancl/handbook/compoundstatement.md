---
title: "Elemento &lt;compoundStatement&gt;"
---

### Definição e uso { data-search-exclude }

O elemento [&lt;compoundStatement&gt;](compoundstatement.md) define uma expressão lógica entre seus
elementos filhos ([&lt;assessmentStatement&gt;](assessmentstatement.md) e [&lt;compoundStatement&gt;](compoundstatement.md)) por
por meio de um atributo booleano *operador*.

O atributo *isNegated* pode ser definido para especificar que um
O elemento filho [&lt;compoundStatement&gt;](compoundstatement.md) deve ser negado antes do booleano
operação é avaliada.

### Sintaxe { data-search-exclude }

| Elemento | Atributos | Conteúdo | Pai |  |
| --- | --- | --- | --- | --- |
| [&lt;compoundStatement&gt;](compoundstatement.md) | <u>*operador*</u>, *isNegated* | ([&lt;assessmentStatement&gt;](assessmentstatement.md) | [&lt;compoundStatement&gt;](compoundstatement.md))+ | [&lt;compoundCondition&gt;](compoundcondition.md) ou [&lt;compoundStatement&gt;](compoundstatement.md) |

### Atributos { data-search-exclude }

| Nome | Valor | Descrição |
| --- | --- | --- |
| *operador* | "e" ou "ou". | O atributo *operator* define a expressão lógica entre os elementos filhos [&lt;compoundStatement&gt;](compoundstatement.md). |
| *éNegado* | <p>"verdadeiro" ou "falso".</p><p>O valor padrão é "falso".</p> | O atributo *isNegated* define se os elementos filhos [&lt;compoundStatement&gt;](compoundstatement.md) devem ser negados antes que a instrução seja avaliada. |
