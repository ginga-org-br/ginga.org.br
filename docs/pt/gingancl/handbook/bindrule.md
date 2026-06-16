---
title: "Elemento &lt;bindRule&gt;"
---

### Definição e uso { data-search-exclude }

O elemento [&lt;bindRule&gt;](bindrule.md) associa uma regra a um componente de um
Elemento [&lt;switch&gt;](switch.md) ou [&lt;descriptorSwitch&gt;](descriptorswitch.md), através de sua regra e
atributos constituintes, respectivamente.

### Sintaxe { data-search-exclude }

| Elemento | Atributos | Conteúdo | Pai |
| --- | --- | --- | --- |
| [&lt;bindRule&gt;](bindrule.md) | <u>*constituinte*</u>, <u>*regra*</u> | -- | [&lt;switch&gt;](switch.md) ou [&lt;descriptorSwitch&gt;](descriptorswitch.md) |

### Atributos { data-search-exclude }

| Nome | Valor | Descrição |
| --- | --- | --- |
| *constituinte* | IDREF. | O atributo *constituent* identifica exclusivamente um elemento filho do elemento [&lt;switch&gt;](switch.md) ou [&lt;descriptorSwitch&gt;](descriptorswitch.md), por meio de seu valor *id*. |
| *regra* | IDREF. | O atributo *rule* identifica exclusivamente uma regra definida por um elemento [&lt;rule&gt;](rule.md) ou *compositeRule*, através de seu valor *id*. |