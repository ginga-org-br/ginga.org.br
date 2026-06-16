---
title: "Elemento &lt;importNCL&gt;"
---

### Definição e uso { data-search-exclude }

O elemento [&lt;importNCL&gt;](importncl.md) permite incorporar outro documento NCL
especificação.  Como consequência, todas as bases definidas dentro do NCL importado
documento, bem como o elemento [&lt;body&gt;](body.md) do documento, são importados, todos em
uma vez.  As bases serão tratadas como se cada uma fosse importada por [&lt;importBase&gt;](importbase.md)
elementos.  O elemento [&lt;body&gt;](body.md) importado será tratado como um [&lt;context&gt;](context.md)
elemento.  Deve-se ressaltar que o elemento [&lt;importNCL&gt;](importncl.md) não
"inclui" o referido documento NCL mas apenas torna o referido documento
visível para ter seus componentes reutilizados pelo documento que definiu o
[&lt;importNCL&gt;](importncl.md) elemento.  Assim, o [&lt;body&gt;](body.md) importado, bem como qualquer um de seus
nós contidos, podem ser reutilizados dentro do elemento [&lt;body&gt;](body.md) da importação
Documento NCL.

O atributo *documentURI* do elemento [&lt;importNCL&gt;](importncl.md) refere-se a um URI
correspondente ao documento NCL a ser importado.   O atributo *alias*
especifica um nome a ser usado como prefixo ao se referir a elementos deste
documento importado.  A referência deve ter o formato: alias#element_id.  Isso
é importante observar que o mesmo alias deve ser usado ao se referir a
elementos definidos nas bases de documentos importados indiretamente ([&lt;regionBase&gt;](regionbase.md),
[&lt;connectorBase&gt;](connectorbase.md), [&lt;descriptorBase&gt;](descriptorbase.md), etc.).

A operação de importação é transitiva, ou seja, se a baseA importa a baseB que
importa baseC, então baseA importa baseC.  No entanto, o alias definido para
baseC dentro de baseBis não é considerada pela baseA.

### Sintaxe { data-search-exclude }

| Elemento | Atributos | Conteúdo | Pai |
| --- | --- | --- | --- |
| [&lt;importNCL&gt;](importncl.md) | <u>*alias*</u>, <u>*documentURI*</u> | -- | [&lt;importedDocumentBase&gt;](importeddocumentbase.md) |

### Atributos { data-search-exclude }

| Nome | Valor | Descrição |
| --- | --- | --- |
| *alias* | Pode receber qualquer valor de string que comece com uma letra ou sublinhado e que contenha apenas letras, dígitos, <"."> e <"_">. | O atributo *alias* especifica um nome a ser utilizado como prefixo quando se referir a elementos da base importada.  O valor *alias* deve ser exclusivo em um documento e seu escopo é restrito ao documento que definiu o atributo alias. |
| *documentURI* | URI. | O atributo *documentURI* é o localizador do documento NCL de onde a base ou documento será importado. |