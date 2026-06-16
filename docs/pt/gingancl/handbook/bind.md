---
title: "Elemento &lt;bind&gt;"
---

### Definição e uso { data-search-exclude }

O elemento [&lt;bind&gt;](bind.md) permite associar uma interface de um objeto a um
função de conector.

Se a função do conector referida vier de um elemento [&lt;simpleAction&gt;](simpleaction.md)
cujo *eventType* é igual a "atribuição" e cujo
*actionType* é igual a "start" e se o valor especificado for
"$anyName", o valor atribuído é recuperado da propriedade associada
com a função "anyName" e definido por um elemento filho [&lt;bind&gt;](bind.md) no
mesmo elemento [&lt;link&gt;](link.md).  Se este valor não puder ser recuperado, nenhuma atribuição
é feito.

### Sintaxe { data-search-exclude }

| Elemento | Atributos | Conteúdo | Pai |
| --- | --- | --- | --- |
| [&lt;bind&gt;](bind.md) | <u>*função*</u>, <u>*componente*</u>, *interface*, *descritor* | [&lt;bindParam&gt;](bindparam.md)* | [&lt;link&gt;](link.md) |

### Atributos { data-search-exclude }

| Nome | Valor | Descrição |
| --- | --- | --- |
| *papel* | Corda | The *role* attribute refers to a connector role. |
| *componente* | IDREF. | O atributo *component* refere-se a um elemento [&lt;media&gt;](media.md), ou a um elemento [&lt;context&gt;](context.md), ou a um elemento [&lt;body&gt;](body.md), ou a um elemento [&lt;switch&gt;](switch.md).  Esses elementos devem ser elementos filhos da mesma composição na qual o elemento [&lt;link&gt;](link.md) está definido ou devem ser a composição na qual o elemento [&lt;link&gt;](link.md) está definido. |
| *interface* | <p>String.</p><p>O valor padrão é a âncora de todo o conteúdo.</p> | O atributo *interface* refere-se a um [&lt;area&gt;](area.md), [&lt;port&gt;](port.md) ou [&lt;switchPort&gt;](switchport.md), do objeto identificado pelo atributo *component*, referindo-se ao seu atributo *id*; ou refere-se a um [&lt;property&gt;](property.md), do objeto identificado pelo atributo *component*, referindo-se ao seu atributo *name*. |
| *descritor* | IDREF. | O atributo *descriptor* refere-se a um elemento [&lt;descriptor&gt;](descriptor.md). |