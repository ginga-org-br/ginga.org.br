---
title: "Elemento &lt;connectorBase&gt;"
---

# &lt;connectorBase&gt;

Explore o exemplo de `<connectorBase>` abaixo:

<div class="ginga-playground-container">

<nav class="ginga-playground-tabs" role="tablist" aria-label="Exemplos do Ginga Playground">
  <button type="button" class="ginga-playground-tab" role="tab" aria-selected="true" data-playground-src="https://ginga.org.br/gingaf/playground/?app=https://raw.githubusercontent.com/ginga-org-br/gingaf/refs/heads/main/examples/ginga.org.br/connectorBase.ncl">connectorBase.ncl</button>
</nav>

<iframe
  class="ginga-playground"
  src="https://ginga.org.br/gingaf/playground/?app=https://raw.githubusercontent.com/ginga-org-br/gingaf/refs/heads/main/examples/ginga.org.br/connectorBase.ncl"
  loading="lazy"
  allow="autoplay; fullscreen">
</iframe>

</div>

O elemento [&lt;connectorBase&gt;](connectorbase.md) agrupa relações definidas usando conectores.

Os conectores podem ser definidos diretamente no elemento [&lt;connectorBase&gt;](connectorbase.md) que é
filho do elemento [&lt;head&gt;](head.md) de uma aplicação NCL.  No entanto, desde o
definição de conectores pode ser difícil para usuários não especialistas, a ideia é
ter especialistas definindo conectores, armazenando-os em bibliotecas (conector
bases) que podem ser importadas e disponibilizá-las a terceiros para
criando links.

### Sintaxe { data-search-exclude }

| Elemento | Atributos | Conteúdo | Pai |  |
| --- | --- | --- | --- | --- |
| [&lt;connectorBase&gt;](connectorbase.md) | *id* | ([&lt;importBase&gt;](importbase.md) | [&lt;causalConnector&gt;](causalconnector.md))* | [&lt;head&gt;](head.md) |

### Atributos { data-search-exclude }

| Nome | Valor | Descrição |
| --- | --- | --- |
| *id* | Pode receber qualquer valor de string que comece com uma letra ou sublinhado e que contenha apenas letras, dígitos, <"."> e <"_">. | O atributo *id* identifica exclusivamente o elemento dentro de um documento. |
