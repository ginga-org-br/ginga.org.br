---
title: "Elemento &lt;defaultComponent&gt;"
---

# &lt;defaultComponent&gt;

Explore el ejemplo de `<defaultComponent>` a continuación:

<div class="ginga-playground-container">

<nav class="ginga-playground-tabs" role="tablist" aria-label="Ejemplos de Ginga Playground">
  <button type="button" class="ginga-playground-tab" role="tab" aria-selected="true" data-playground-src="https://ginga.org.br/gingaf/playground/?app=https://raw.githubusercontent.com/ginga-org-br/gingaf/refs/heads/main/examples/ginga.org.br/defaultComponent.ncl">defaultComponent.ncl</button>
</nav>

<iframe
  class="ginga-playground"
  src="https://ginga.org.br/gingaf/playground/?app=https://raw.githubusercontent.com/ginga-org-br/gingaf/refs/heads/main/examples/ginga.org.br/defaultComponent.ncl"
  loading="lazy"
  allow="autoplay; fullscreen">
</iframe>

</div>

El elemento [&lt;defaultComponent&gt;](defaultcomponent.md) identifica el componente secundario predeterminado
del elemento [&lt;switch&gt;](switch.md) que debe seleccionarse si todas las reglas vinculadas a
componentes mapeados del elemento [&lt;switchPort&gt;](switchport.md), a través del cual el
[&lt;switch&gt;](switch.md) elemento fue activado, se evalúan como falso.

### Sintaxis { data-search-exclude }

| Elemento | Atributos | Contenido | Padre |
| --- | --- | --- | --- |
| [&lt;defaultComponent&gt;](defaultcomponent.md) | <u>*componente*</u> | -- | [&lt;switch&gt;](switch.md) o [&lt;descriptorSwitch&gt;](descriptorswitch.md) |

### Atributos { data-search-exclude }

| Nombre | Valor | Descripción |
| --- | --- | --- |
| *componente* | IDREF. | El atributo *defaultComponent* identifica de forma única un elemento secundario del elemento [&lt;switch&gt;](switch.md). |