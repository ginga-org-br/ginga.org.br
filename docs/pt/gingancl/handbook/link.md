---
title: "Elemento &lt;link&gt;"
---

### Definição e uso { data-search-exclude }

O elemento [&lt;link&gt;](../link/) define um relacionamento entre mídia e composição
objetos.

Um elemento [&lt;link&gt;](../link/) pode ter um atributo *id*, que exclusivamente
identifica o elemento dentro de um documento e deve ter um
Atributo *xconnector*, que se refere a um URI do conector.

O referido elemento [&lt;causalConnector&gt;](../causalconnector/) define a relação sem
especificando quem desempenha os papéis de relacionamento.  Quem joga é definido usando
Elementos [&lt;bind&gt;](../bind/), filhos do elemento [&lt;link&gt;](../link/).

### Sintaxe { data-search-exclude }

| Elemento | Atributos | Conteúdo | Pai |
| --- | --- | --- | --- |
| [&lt;link&gt;](../link/) | *id*, <u>*xconector*</u> | ([&lt;linkParam&gt;](../linkparam/)*, [&lt;bind&gt;](../bind/)+) | [&lt;body&gt;](../body/) ou [&lt;context&gt;](../context/) ou [&lt;switch&gt;](../switch/) |

### Atributos { data-search-exclude }

| Nome | Valor | Descrição |
| --- | --- | --- |
| *id* | Pode receber qualquer valor de string que comece com uma letra ou sublinhado e que contenha apenas letras, dígitos, <"."> e <"_">. | O atributo *id* identifica exclusivamente o elemento dentro de um documento. |
| *xconector* | <p>String.</p><p>O valor deve ter o formato:</p><ol><li class="level1"><div class="li">"alias#connector_id", ou "documentURI_value#connector_id", para conectores definidos em um documento externo importado, ou</div></li><li class="level1"><div class="li">"connector_id", o *id* do conector para conectores definidos no documento em si.</div></li> | O atributo *xconnector* refere-se a um conector definido como elemento descendente de [&lt;connectorBase&gt;](../connectorbase/) em um documento externo importado. |