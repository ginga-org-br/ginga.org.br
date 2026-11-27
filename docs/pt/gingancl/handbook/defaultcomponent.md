---
title: "Elemento &lt;defaultComponent&gt;"
---

# &lt;defaultComponent&gt;

Explore o exemplo de `<defaultComponent>` abaixo:

<div class="ginga-playground-container">

<nav class="ginga-playground-tabs" role="tablist" aria-label="Exemplos do Ginga Playground">
  <button type="button" class="ginga-playground-tab" role="tab" aria-selected="true" data-playground-src="https://ginga.org.br/gingaf/playground/?app=https://raw.githubusercontent.com/ginga-org-br/gingaf/refs/heads/main/examples/ginga.org.br/defaultComponent.ncl">defaultComponent.ncl</button>
</nav>

<iframe
  class="ginga-playground"
  src="https://ginga.org.br/gingaf/playground/?app=https://raw.githubusercontent.com/ginga-org-br/gingaf/refs/heads/main/examples/ginga.org.br/defaultComponent.ncl"
  loading="lazy"
  allow="autoplay; fullscreen">
</iframe>

</div>

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