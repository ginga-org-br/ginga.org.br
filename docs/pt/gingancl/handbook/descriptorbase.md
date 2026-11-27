---
title: "Elemento &lt;descriptorBase&gt;"
---

# &lt;descriptorBase&gt;

Explore o exemplo de `<descriptorBase>` abaixo:

<div class="ginga-playground-container">

<nav class="ginga-playground-tabs" role="tablist" aria-label="Exemplos do Ginga Playground">
  <button type="button" class="ginga-playground-tab" role="tab" aria-selected="true" data-playground-src="https://ginga.org.br/gingaf/playground/?app=https://raw.githubusercontent.com/ginga-org-br/gingaf/refs/heads/main/examples/ginga.org.br/descriptorBase.ncl">descriptorBase.ncl</button>
</nav>

<iframe
  class="ginga-playground"
  src="https://ginga.org.br/gingaf/playground/?app=https://raw.githubusercontent.com/ginga-org-br/gingaf/refs/heads/main/examples/ginga.org.br/descriptorBase.ncl"
  loading="lazy"
  allow="autoplay; fullscreen">
</iframe>

</div>

O elemento [&lt;descriptorBase&gt;](descriptorbase.md) agrupa um conjunto de [&lt;descriptor&gt;](descriptor.md)
elementos, cada um dos quais define valores iniciais de propriedades [&lt;media&gt;](media.md).

### Sintaxe { data-search-exclude }

| Elemento | Atributos | Conteúdo | Pai |  |  |
| --- | --- | --- | --- | --- | --- |
| [&lt;descriptorBase&gt;](descriptorbase.md) | *id* | ([&lt;importBase&gt;](importbase.md) | [&lt;descriptor&gt;](descriptor.md) | [&lt;descriptorSwitch&gt;](descriptorswitch.md))+ | [&lt;head&gt;](head.md) |

### Atributos { data-search-exclude }

| Nome | Valor | Descrição |
| --- | --- | --- |
| *id* | Pode receber qualquer valor de string que comece com uma letra ou sublinhado e que contenha apenas letras, dígitos, <"."> e <"_">. | O atributo *id* identifica exclusivamente o elemento dentro de um documento. |
