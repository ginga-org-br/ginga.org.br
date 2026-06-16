---
title: "Elemento &lt;switchPort&gt;"
---

### Definição e uso { data-search-exclude }

O elemento [&lt;switchPort&gt;](../switchport/) define um mapeamento para um subconjunto do
[&lt;switch&gt;](../switch/) componentes do elemento.  Todas as referências a um switch interno
componente deve ser feito através de um elemento [&lt;switchPort&gt;](../switchport/) ou, por padrão,
ao elemento [&lt;switch&gt;](../switch/) sem especificar nenhum [&lt;switchPort&gt;](../switchport/). Em
neste último caso, considera-se como se a referência fosse feita a um incumprimento
[&lt;switchPort&gt;](../switchport/) que contém elementos de mapeamento para cada objeto filho do
switch e referindo-se a todas as suas âncoras de conteúdo.

### Sintaxe { data-search-exclude }

| Elemento | Atributos | Conteúdo | Pai |
| --- | --- | --- | --- |
| [&lt;switchPort&gt;](../switchport/) | <u>*id*</u> | [&lt;mapping&gt;](../mapping/)+ | [&lt;switch&gt;](../switch/) |

### Atributos { data-search-exclude }

| Nome | Valor | Descrição |
| --- | --- | --- |
| *id* | Pode receber qualquer valor de string que comece com uma letra ou sublinhado e que contenha apenas letras, dígitos, <"."> e <"_">. | O atributo *id* identifica exclusivamente o elemento dentro de um documento. |