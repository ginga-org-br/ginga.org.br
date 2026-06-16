---
title: "Elemento &lt;port&gt;"
---

### Definição e uso { data-search-exclude }

Nós compostos de NCL, representados por [&lt;body&gt;](body.md), [&lt;context&gt;](context.md) e
[&lt;switch&gt;](switch.md) elementos, encapsula seus componentes filhos.  Interfaces de
componentes filhos não são visíveis para relacionamentos definidos fora do
nó composto, a menos que essas interfaces sejam externalizadas, usando o
[&lt;port&gt;](port.md) ou [&lt;switchPort&gt;](switchport.md) elementos.

O elemento [&lt;port&gt;](port.md) especifica uma porta de nó composto com seu respectivo
mapeamento para uma interface (atributo *interface*) de um de seus
componentes (especificados pelo atributo *component*).  Como de costume, se o
O atributo *interface* não é especificado, //todo o conteúdo
âncora // é assumido.

### Sintaxe { data-search-exclude }

| Elemento | Atributos | Conteúdo | Pai |
| --- | --- | --- | --- |
| [&lt;port&gt;](port.md) | <u>*id*</u>, <u>*componente*</u>, *interface* | -- | [&lt;context&gt;](context.md) ou [&lt;body&gt;](body.md) |

### Atributos { data-search-exclude }

| Nome | Valor | Descrição |
| --- | --- | --- |
| *id* | Pode receber qualquer valor de string que comece com uma letra ou sublinhado e que contenha apenas letras, dígitos, <"."> e <"_">. | O atributo *id* identifica exclusivamente o elemento dentro de um documento. |
| *componente* | IDREF. | O atributo *component* identifica um elemento filho da composição, que pode ser um objeto de mídia ou outro objeto composto, através de seu valor *id*. |
| *interface* | <p>String.</p><p>O valor padrão é a âncora de todo o conteúdo.</p> | O atributo *interface* identifica exclusivamente uma interface ([&lt;area&gt;](area.md), [&lt;property&gt;](property.md), [&lt;port&gt;](port.md) ou [&lt;switchPort&gt;](switchport.md)) de um elemento filho da composição, por meio de seu valor *id* ou *name*.  O padrão é toda a âncora de conteúdo do componente referido. |