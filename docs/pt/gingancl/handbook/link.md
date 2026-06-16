---
title: "Elemento &lt;link&gt;"
---

### Definição e uso { data-search-exclude }

O elemento [&lt;link&gt;](link.md) define um relacionamento entre mídia e composição
objetos.

Um elemento [&lt;link&gt;](link.md) pode ter um atributo *id*, que exclusivamente
identifica o elemento dentro de um documento e deve ter um
Atributo *xconnector*, que se refere a um URI do conector.

O referido elemento [&lt;causalConnector&gt;](causalconnector.md) define a relação sem
especificando quem desempenha os papéis de relacionamento.  Quem joga é definido usando
Elementos [&lt;bind&gt;](bind.md), filhos do elemento [&lt;link&gt;](link.md).

### Sintaxe { data-search-exclude }

| Elemento | Atributos | Conteúdo | Pai |
| --- | --- | --- | --- |
| [&lt;link&gt;](link.md) | *id*, <u>*xconector*</u> | ([&lt;linkParam&gt;](linkparam.md)*, [&lt;bind&gt;](bind.md)+) | [&lt;body&gt;](body.md) ou [&lt;context&gt;](context.md) ou [&lt;switch&gt;](switch.md) |

### Atributos { data-search-exclude }

| Nome | Valor | Descrição |
| --- | --- | --- |
| *id* | Pode receber qualquer valor de string que comece com uma letra ou sublinhado e que contenha apenas letras, dígitos, <"."> e <"_">. | O atributo *id* identifica exclusivamente o elemento dentro de um documento. |
| *xconector* | <p>String.</p><p>O valor deve ter o formato:</p><ol><li class="level1"><div class="li">"alias#connector_id", ou "documentURI_value#connector_id", para conectores definidos em um documento externo importado, ou</div></li><li class="level1"><div class="li">"connector_id", o *id* do conector para conectores definidos no documento em si.</div></li> | O atributo *xconnector* refere-se a um conector definido como elemento descendente de [&lt;connectorBase&gt;](connectorbase.md) em um documento externo importado. |