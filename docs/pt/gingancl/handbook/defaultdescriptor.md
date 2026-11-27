---
title: "Elemento &lt;defaultDescriptor&gt;"
---

# &lt;defaultDescriptor&gt;

Explore o exemplo de `<defaultDescriptor>` abaixo:

<div class="ginga-playground-container">

<nav class="ginga-playground-tabs" role="tablist" aria-label="Exemplos do Ginga Playground">
  <button type="button" class="ginga-playground-tab" role="tab" aria-selected="true" data-playground-src="https://ginga.org.br/gingaf/playground/?app=https://raw.githubusercontent.com/ginga-org-br/gingaf/refs/heads/main/examples/ginga.org.br/defaultDescriptor.ncl">defaultDescriptor.ncl</button>
</nav>

<iframe
  class="ginga-playground"
  src="https://ginga.org.br/gingaf/playground/?app=https://raw.githubusercontent.com/ginga-org-br/gingaf/refs/heads/main/examples/ginga.org.br/defaultDescriptor.ncl"
  loading="lazy"
  allow="autoplay; fullscreen">
</iframe>

</div>

O elemento [&lt;defaultDescriptor&gt;](defaultdescriptor.md) identifica o filho padrão
Elemento [&lt;descriptor&gt;](descriptor.md) do elemento [&lt;descriptorSwitch&gt;](descriptorswitch.md) que deve
ser selecionado se todas as regras forem avaliadas como falsas.

### Sintaxe { data-search-exclude }

| Elemento | Atributos | Conteúdo | Pai |
| --- | --- | --- | --- |
| [&lt;defaultDescriptor&gt;](defaultdescriptor.md) | <u>*descritor*</u> | -- | [&lt;descriptorSwitch&gt;](descriptorswitch.md) |

### Atributos { data-search-exclude }

| Nome | Valor | Descrição |
| --- | --- | --- |
| *descritor* | IDREF. | O atributo *descriptor* refere-se a um elemento [&lt;descriptor&gt;](descriptor.md). |