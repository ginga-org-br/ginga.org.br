---
title: "Elemento &lt;compoundStatement&gt;"
---

# &lt;compoundStatement&gt;

Explore o exemplo de `<compoundStatement>` abaixo:

<div class="ginga-playground-container">

<nav class="ginga-playground-tabs" role="tablist" aria-label="Exemplos do Ginga Playground">
  <button type="button" class="ginga-playground-tab" role="tab" aria-selected="true" data-playground-src="https://ginga.org.br/gingaf/playground/?app=https://raw.githubusercontent.com/ginga-org-br/gingaf/refs/heads/main/examples/ginga.org.br/compoundStatement.ncl">compoundStatement.ncl</button>
</nav>

<iframe
  class="ginga-playground"
  src="https://ginga.org.br/gingaf/playground/?app=https://raw.githubusercontent.com/ginga-org-br/gingaf/refs/heads/main/examples/ginga.org.br/compoundStatement.ncl"
  loading="lazy"
  allow="autoplay; fullscreen">
</iframe>

</div>

O elemento [&lt;compoundStatement&gt;](compoundstatement.md) define uma expressão lógica entre seus
elementos filhos ([&lt;assessmentStatement&gt;](assessmentstatement.md) e [&lt;compoundStatement&gt;](compoundstatement.md)) por
por meio de um atributo booleano *operador*.

O atributo *isNegated* pode ser definido para especificar que um
O elemento filho [&lt;compoundStatement&gt;](compoundstatement.md) deve ser negado antes do booleano
operação é avaliada.

### Sintaxe { data-search-exclude }

| Elemento | Atributos | Conteúdo | Pai |  |
| --- | --- | --- | --- | --- |
| [&lt;compoundStatement&gt;](compoundstatement.md) | <u>*operador*</u>, *isNegated* | ([&lt;assessmentStatement&gt;](assessmentstatement.md) | [&lt;compoundStatement&gt;](compoundstatement.md))+ | [&lt;compoundCondition&gt;](compoundcondition.md) ou [&lt;compoundStatement&gt;](compoundstatement.md) |

### Atributos { data-search-exclude }

| Nome | Valor | Descrição |
| --- | --- | --- |
| *operador* | "e" ou "ou". | O atributo *operator* define a expressão lógica entre os elementos filhos [&lt;compoundStatement&gt;](compoundstatement.md). |
| *éNegado* | <p>"verdadeiro" ou "falso".</p><p>O valor padrão é "falso".</p> | O atributo *isNegated* define se os elementos filhos [&lt;compoundStatement&gt;](compoundstatement.md) devem ser negados antes que a instrução seja avaliada. |
