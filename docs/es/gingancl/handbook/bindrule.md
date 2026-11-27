---
title: "Elemento &lt;bindRule&gt;"
---

# &lt;bindRule&gt;

Explore el ejemplo de `<bindRule>` a continuación:

<div class="ginga-playground-container">

<nav class="ginga-playground-tabs" role="tablist" aria-label="Ejemplos de Ginga Playground">
  <button type="button" class="ginga-playground-tab" role="tab" aria-selected="true" data-playground-src="https://ginga.org.br/gingaf/playground/?app=https://raw.githubusercontent.com/ginga-org-br/gingaf/refs/heads/main/examples/ginga.org.br/bindRule.ncl">bindRule.ncl</button>
</nav>

<iframe
  class="ginga-playground"
  src="https://ginga.org.br/gingaf/playground/?app=https://raw.githubusercontent.com/ginga-org-br/gingaf/refs/heads/main/examples/ginga.org.br/bindRule.ncl"
  loading="lazy"
  allow="autoplay; fullscreen">
</iframe>

</div>

El elemento [&lt;bindRule&gt;](bindrule.md) asocia una regla con un componente de un
elemento [&lt;switch&gt;](switch.md) o [&lt;descriptorSwitch&gt;](descriptorswitch.md), a través de su regla y
atributos constituyentes, respectivamente.

### Sintaxis { data-search-exclude }

| Elemento | Atributos | Contenido | Padre |
| --- | --- | --- | --- |
| [&lt;bindRule&gt;](bindrule.md) | <u>*constituyente*</u>, <u>*regla*</u> | -- | [&lt;switch&gt;](switch.md) o [&lt;descriptorSwitch&gt;](descriptorswitch.md) |

### Atributos { data-search-exclude }

| Nombre | Valor | Descripción |
| --- | --- | --- |
| *constituyente* | IDREF. | El atributo *constituent* identifica de forma única un elemento secundario del elemento [&lt;switch&gt;](switch.md) o [&lt;descriptorSwitch&gt;](descriptorswitch.md), a través de su valor *id*. |
| *regla* | IDREF. | El atributo *rule* identifica de forma única una regla definida por un elemento [&lt;rule&gt;](rule.md) o *compositeRule*, a través de su valor *id*. |