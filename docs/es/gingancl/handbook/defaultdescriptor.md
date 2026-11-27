---
title: "Elemento &lt;defaultDescriptor&gt;"
---

# &lt;defaultDescriptor&gt;

Explore el ejemplo de `<defaultDescriptor>` a continuación:

<div class="ginga-playground-container">

<nav class="ginga-playground-tabs" role="tablist" aria-label="Ejemplos de Ginga Playground">
  <button type="button" class="ginga-playground-tab" role="tab" aria-selected="true" data-playground-src="https://ginga.org.br/gingaf/playground/?app=https://raw.githubusercontent.com/ginga-org-br/gingaf/refs/heads/main/examples/ginga.org.br/defaultDescriptor.ncl">defaultDescriptor.ncl</button>
</nav>

<iframe
  class="ginga-playground"
  src="https://ginga.org.br/gingaf/playground/?app=https://raw.githubusercontent.com/ginga-org-br/gingaf/refs/heads/main/examples/ginga.org.br/defaultDescriptor.ncl"
  loading="lazy"
  allow="autoplay; fullscreen">
</iframe>

</div>

El elemento [&lt;defaultDescriptor&gt;](defaultdescriptor.md) identifica al hijo predeterminado
[&lt;descriptor&gt;](descriptor.md) elemento del [&lt;descriptorSwitch&gt;](descriptorswitch.md) elemento que debe
se seleccionará si todas las reglas se evalúan como falsas.

### Sintaxis { data-search-exclude }

| Elemento | Atributos | Contenido | Padre |
| --- | --- | --- | --- |
| [&lt;defaultDescriptor&gt;](defaultdescriptor.md) | <u>*descriptor*</u> | -- | [&lt;descriptorSwitch&gt;](descriptorswitch.md) |

### Atributos { data-search-exclude }

| Nombre | Valor | Descripción |
| --- | --- | --- |
| *descriptor* | IDREF. | El atributo *descriptor* hace referencia a un elemento [&lt;descriptor&gt;](descriptor.md). |