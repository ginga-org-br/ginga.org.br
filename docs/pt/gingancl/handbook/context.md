---
title: "Elemento &lt;context&gt;"
---

### Definição e uso { data-search-exclude }

O elemento [&lt;context&gt;](context.md) permite estruturar uma aplicação NCL. O
elemento pode conter elementos com conteúdo de mídia (elementos [&lt;media&gt;](media.md)),
chamados objetos de mídia, outros elementos [&lt;context&gt;](context.md) aninhados, elementos
agrupamento de alternativas de conteúdo ([&lt;switch&gt;](switch.md) elementos) e relacionamentos
([&lt;link&gt;](link.md) elementos) entre todos os objetos representados pelo
elementos mencionados.

Deve-se ressaltar que o elemento [&lt;body&gt;](body.md) é considerado um elemento especial
tipo de contexto, aquele que representa toda a aplicação.

O elemento [&lt;context&gt;](context.md) pode referir-se a outro [&lt;context&gt;](context.md) ou a um
elemento [&lt;body&gt;](body.md) importado. Neste caso, ele herda a especificação de
o referido elemento.

### Sintaxe { data-search-exclude }

| Elemento | Atributos | Conteúdo | Pai |
| --- | --- | --- | --- |
| [&lt;context&gt;](context.md) | <u>*id*</u>, *consulte* | ([&lt;port&gt;](port.md) &#124; [&lt;property&gt;](property.md) &#124; [&lt;media&gt;](media.md) &#124; [&lt;context&gt;](context.md) &#124; [&lt;link&gt;](link.md) &#124; [&lt;switch&gt;](switch.md) &#124; [&lt;meta&gt;](meta.md) &#124; [&lt;metadata&gt;](metadata.md))* | [&lt;body&gt;](body.md), [&lt;context&gt;](context.md) ou [&lt;switch&gt;](switch.md) |

### Atributos { data-search-exclude }

| Nome | Valor | Descrição |
| --- | --- | --- |
| *id* | Pode receber qualquer valor de string que comece com uma letra ou sublinhado e que contenha apenas letras, dígitos, <"."> e <"_">. | O atributo *id* identifica exclusivamente o elemento dentro de um documento. |
| *consulte* | IDREF ou a string "alias#id" onde "id" é um valor IDREF. | <p>O atributo *refer* refere-se a um elemento *id* que será reutilizado.  Um elemento que se refere a outro elemento não pode ser reutilizado; isto é, seu valor *id* não pode ser o valor de qualquer atributo *refer*.  O elemento referido deve ser um elemento [&lt;context&gt;](context.md) ou um elemento [&lt;body&gt;](body.md) importado.</p><p>O elemento referido e o elemento que se refere a ele devem ser considerados iguais em relação à especificação de seus dados.</p> <p>Se o nó referido (elemento [&lt;context&gt;](context.md) ou [&lt;body&gt;](body.md)) é definido em um documento D importado, o valor do atributo *refer* deve ter o formato "alias#id", onde "alias" é o valor do atributo *alias* associado ao documento D importado.</p> |
