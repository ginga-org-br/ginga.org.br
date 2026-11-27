---
title: "Elemento &lt;compositeRule&gt;"
---

# &lt;compositeRule&gt;

Explore o exemplo de `<compositeRule>` abaixo:

<div class="ginga-playground-container">

<nav class="ginga-playground-tabs" role="tablist" aria-label="Exemplos do Ginga Playground">
  <button type="button" class="ginga-playground-tab" role="tab" aria-selected="true" data-playground-src="https://ginga.org.br/gingaf/playground/?app=https://raw.githubusercontent.com/ginga-org-br/gingaf/refs/heads/main/examples/ginga.org.br/compositeRule.ncl">compositeRule.ncl</button>
</nav>

<iframe
  class="ginga-playground"
  src="https://ginga.org.br/gingaf/playground/?app=https://raw.githubusercontent.com/ginga-org-br/gingaf/refs/heads/main/examples/ginga.org.br/compositeRule.ncl"
  loading="lazy"
  allow="autoplay; fullscreen">
</iframe>

</div>

O elemento [&lt;compositeRule&gt;](compositerule.md) define uma expressão lógica entre seus
elementos filhos ([&lt;rule&gt;](rule.md) e [&lt;compositeRule&gt;](compositerule.md)) por meio de um booleano
atributo do operador.

### Sintaxe { data-search-exclude }

| Elemento | Atributos | Conteúdo | Pai |  |
| --- | --- | --- | --- | --- |
| [&lt;compositeRule&gt;](compositerule.md) | <u>*id*</u>, <u>*operador*</u> | ([&lt;compositeRule&gt;](compositerule.md) | [&lt;rule&gt;](rule.md))+ | [&lt;ruleBase&gt;](rulebase.md) ou [&lt;compositeRule&gt;](compositerule.md) |

### Atributos { data-search-exclude }

| Nome | Valor | Descrição |
| --- | --- | --- |
| *id* | Pode receber qualquer valor de string que comece com uma letra ou sublinhado e que contenha apenas letras, dígitos, <"."> e <"_">. | O atributo *id* identifica exclusivamente o elemento dentro de um documento. |
| *operador* | "e" ou "ou". | O atributo *operator* define uma expressão lógica entre os elementos filhos do elemento [&lt;compositeRule&gt;](compositerule.md). |
