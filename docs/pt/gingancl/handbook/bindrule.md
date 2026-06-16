---
title: "Elemento &lt;bindRule&gt;"
---

### Definição e uso { data-search-exclude }

O elemento [&lt;bindRule&gt;](../bindrule/) associa uma regra a um componente de um
Elemento [&lt;switch&gt;](../switch/) ou [&lt;descriptorSwitch&gt;](../descriptorswitch/), através de sua regra e
atributos constituintes, respectivamente.

### Sintaxe { data-search-exclude }

| Elemento | Atributos | Conteúdo | Pai |
| --- | --- | --- | --- |
| [&lt;bindRule&gt;](../bindrule/) | <u>*constituinte*</u>, <u>*regra*</u> | -- | [&lt;switch&gt;](../switch/) ou [&lt;descriptorSwitch&gt;](../descriptorswitch/) |

### Atributos { data-search-exclude }

| Nome | Valor | Descrição |
| --- | --- | --- |
| *constituinte* | IDREF. | O atributo *constituent* identifica exclusivamente um elemento filho do elemento [&lt;switch&gt;](../switch/) ou [&lt;descriptorSwitch&gt;](../descriptorswitch/), por meio de seu valor *id*. |
| *regra* | IDREF. | O atributo *rule* identifica exclusivamente uma regra definida por um elemento [&lt;rule&gt;](../rule/) ou *compositeRule*, através de seu valor *id*. |