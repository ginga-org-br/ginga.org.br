---
title: "Elemento &lt;mapping&gt;"
---

# &lt;mapping&gt;

Explore o exemplo de `<mapping>` abaixo:

<div class="ginga-playground-container">

<nav class="ginga-playground-tabs" role="tablist" aria-label="Exemplos do Ginga Playground">
  <button type="button" class="ginga-playground-tab" role="tab" aria-selected="true" data-playground-src="https://ginga.org.br/gingaf/playground/?app=https://raw.githubusercontent.com/ginga-org-br/gingaf/refs/heads/main/examples/ginga.org.br/mapping.ncl">mapping.ncl</button>
</nav>

<iframe
  class="ginga-playground"
  src="https://ginga.org.br/gingaf/playground/?app=https://raw.githubusercontent.com/ginga-org-br/gingaf/refs/heads/main/examples/ginga.org.br/mapping.ncl"
  loading="lazy"
  allow="autoplay; fullscreen">
</iframe>

</div>

Um elemento de mapeamento define um caminho de [&lt;switchPort&gt;](switchport.md) para uma interface
(atributo de interface) de um dos componentes do switch (especificado por seu
atributo do componente).

### Sintaxe { data-search-exclude }

| Elemento | Atributos | Conteúdo | Pai |
| --- | --- | --- | --- |
| [&lt;mapping&gt;](mapping.md) | <u>*componente*</u>, *interface* | -- | [&lt;switchPort&gt;](switchport.md) |

### Atributos { data-search-exclude }

| Nome | Valor | Descrição |
| --- | --- | --- |
| *componente* | IDREF. | O atributo *component* identifica exclusivamente um elemento filho do switch, através de seu valor *id*. |
| *interface* | <p>String.</p><p>O valor padrão é a âncora de todo o conteúdo.</p> | O atributo *interface* identifica exclusivamente uma interface ([&lt;area&gt;](area.md), [&lt;property&gt;](property.md), [&lt;port&gt;](port.md) ou [&lt;switchPort&gt;](switchport.md)) de um elemento filho de [&lt;switch&gt;](switch.md), por meio de seu valor *id* ou nome. |