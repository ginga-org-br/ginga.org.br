---
title: "Elemento &lt;defaultComponent&gt;"
---

### Definição e uso { data-search-exclude }

O elemento [&lt;defaultComponent&gt;](defaultcomponent.md) identifica o componente filho padrão
do elemento [&lt;switch&gt;](switch.md) que deve ser selecionado se todas as regras vinculadas a
componentes mapeados do elemento [&lt;switchPort&gt;](switchport.md), por meio do qual o
O elemento [&lt;switch&gt;](switch.md) foi ativado, são avaliados como falsos.

### Sintaxe { data-search-exclude }

| Elemento | Atributos | Conteúdo | Pai |
| --- | --- | --- | --- |
| [&lt;defaultComponent&gt;](defaultcomponent.md) | <u>*componente*</u> | -- | [&lt;switch&gt;](switch.md) ou [&lt;descriptorSwitch&gt;](descriptorswitch.md) |

### Atributos { data-search-exclude }

| Nome | Valor | Descrição |
| --- | --- | --- |
| *componente* | IDREF. | O atributo *defaultComponent* identifica exclusivamente um elemento filho do elemento [&lt;switch&gt;](switch.md). |