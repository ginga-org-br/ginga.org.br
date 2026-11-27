---
title: "Elemento &lt;meta&gt;"
---

# &lt;meta&gt;

Explore o exemplo de `<meta>` abaixo:

<div class="ginga-playground-container">

<nav class="ginga-playground-tabs" role="tablist" aria-label="Exemplos do Ginga Playground">
  <button type="button" class="ginga-playground-tab" role="tab" aria-selected="true" data-playground-src="https://ginga.org.br/gingaf/playground/?app=https://raw.githubusercontent.com/ginga-org-br/gingaf/refs/heads/main/examples/ginga.org.br/meta.ncl">meta.ncl</button>
</nav>

<iframe
  class="ginga-playground"
  src="https://ginga.org.br/gingaf/playground/?app=https://raw.githubusercontent.com/ginga-org-br/gingaf/refs/heads/main/examples/ginga.org.br/meta.ncl"
  loading="lazy"
  allow="autoplay; fullscreen">
</iframe>

</div>

O elemento [&lt;meta&gt;](meta.md) contém meta informações sobre um documento NCL. Isso
não é utilizado pelo reprodutor NCL para apresentação da aplicação, mas pode ser
usado para outros agentes de usuário NCL.

O elemento [&lt;meta&gt;](meta.md) especifica um único par propriedade-valor.

### Sintaxe { data-search-exclude }

| Elemento | Atributos | Conteúdo | Pai |
| --- | --- | --- | --- |
| [&lt;meta&gt;](meta.md) | <u>*nome*</u>, <u>*conteúdo*</u> | -- | [&lt;body&gt;](body.md) ou [&lt;context&gt;](context.md) |

### Atributos { data-search-exclude }

| Nome | Valor | Descrição |
| --- | --- | --- |
| *nome* | Corda. | Nome dos metadados. |
| *conteúdo* | Corda. | Valor de metadados. |