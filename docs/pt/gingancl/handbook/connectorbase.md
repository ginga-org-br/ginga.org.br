---
title: "Elemento &lt;connectorBase&gt;"
---

### Definição e uso { data-search-exclude }

O elemento [&lt;connectorBase&gt;](../connectorbase/) agrupa relações definidas usando conectores.

Os conectores podem ser definidos diretamente no elemento [&lt;connectorBase&gt;](../connectorbase/) que é
filho do elemento [&lt;head&gt;](../head/) de uma aplicação NCL.  No entanto, desde o
definição de conectores pode ser difícil para usuários não especialistas, a ideia é
ter especialistas definindo conectores, armazenando-os em bibliotecas (conector
bases) que podem ser importadas e disponibilizá-las a terceiros para
criando links.

### Sintaxe { data-search-exclude }

| Elemento | Atributos | Conteúdo | Pai |  |
| --- | --- | --- | --- | --- |
| [&lt;connectorBase&gt;](../connectorbase/) | *id* | ([&lt;importBase&gt;](../importbase/) | [&lt;causalConnector&gt;](../causalconnector/))* | [&lt;head&gt;](../head/) |

### Atributos { data-search-exclude }

| Nome | Valor | Descrição |
| --- | --- | --- |
| *id* | Pode receber qualquer valor de string que comece com uma letra ou sublinhado e que contenha apenas letras, dígitos, <"."> e <"_">. | O atributo *id* identifica exclusivamente o elemento dentro de um documento. |
