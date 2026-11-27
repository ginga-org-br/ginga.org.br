---
title: "Elemento &lt;ruleBase&gt;"
---

# &lt;ruleBase&gt;

Explore o exemplo de `<ruleBase>` abaixo:

<div class="ginga-playground-container">

<nav class="ginga-playground-tabs" role="tablist" aria-label="Exemplos do Ginga Playground">
  <button type="button" class="ginga-playground-tab" role="tab" aria-selected="true" data-playground-src="https://ginga.org.br/gingaf/playground/?app=https://raw.githubusercontent.com/ginga-org-br/gingaf/refs/heads/main/examples/ginga.org.br/ruleBase.ncl">ruleBase.ncl</button>
</nav>

<iframe
  class="ginga-playground"
  src="https://ginga.org.br/gingaf/playground/?app=https://raw.githubusercontent.com/ginga-org-br/gingaf/refs/heads/main/examples/ginga.org.br/ruleBase.ncl"
  loading="lazy"
  allow="autoplay; fullscreen">
</iframe>

</div>

O elemento [&lt;ruleBase&gt;](rulebase.md) agrupa um conjunto de regras especificadas em [&lt;rule&gt;](rule.md)
e [&lt;compositeRule&gt;](compositerule.md) elementos.  A especificação de regras em NCL 3.0
foi feito em um módulo separado, porque eles são úteis para definir
componentes alternativos ou descritores alternativos.

### Sintaxe { data-search-exclude }

| Elemento | Atributos | Conteúdo | Pai |  |  |
| --- | --- | --- | --- | --- | --- |
| [&lt;ruleBase&gt;](rulebase.md) | *id* | ([&lt;importBase&gt;](importbase.md) | [&lt;compositeRule&gt;](compositerule.md) | [&lt;rule&gt;](rule.md))+ | [&lt;head&gt;](head.md) |

### Atributos { data-search-exclude }

| Nome | Valor | Descrição |
| --- | --- | --- |
| *id* | Pode receber qualquer valor de string que comece com uma letra ou sublinhado e que contenha apenas letras, dígitos, <"."> e <"_">. | O atributo *id* identifica exclusivamente o elemento dentro de um documento. |
