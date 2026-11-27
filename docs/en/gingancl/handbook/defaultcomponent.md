---
title: "Element &lt;defaultComponent&gt;"
---

# &lt;defaultComponent&gt;

Explore the `<defaultComponent>` example below:

<div class="ginga-playground-container">

<nav class="ginga-playground-tabs" role="tablist" aria-label="Ginga Playground examples">
  <button type="button" class="ginga-playground-tab" role="tab" aria-selected="true" data-playground-src="https://ginga.org.br/gingaf/playground/?app=https://raw.githubusercontent.com/ginga-org-br/gingaf/refs/heads/main/examples/ginga.org.br/defaultComponent.ncl">defaultComponent.ncl</button>
</nav>

<iframe
  class="ginga-playground"
  src="https://ginga.org.br/gingaf/playground/?app=https://raw.githubusercontent.com/ginga-org-br/gingaf/refs/heads/main/examples/ginga.org.br/defaultComponent.ncl"
  loading="lazy"
  allow="autoplay; fullscreen">
</iframe>

</div>

The [&lt;defaultComponent&gt;](defaultcomponent.md) element identifies the default child component
of the [&lt;switch&gt;](switch.md) element that must be selected if all rules bound to
mapped components of the [&lt;switchPort&gt;](switchport.md) element, through which the
[&lt;switch&gt;](switch.md) elementwas activated, are evaluated as false.

### Syntax { data-search-exclude }

| Element | Attributes | Content | Parent |
| --- | --- | --- | --- |
| [&lt;defaultComponent&gt;](defaultcomponent.md) | <u>*component*</u> | -- | [&lt;switch&gt;](switch.md) or [&lt;descriptorSwitch&gt;](descriptorswitch.md) |

### Attributes { data-search-exclude }

| Name | Value | Description |
| --- | --- | --- |
| *component* | IDREF. | The *defaultComponent* attribute uniquely identifies a child element of the [&lt;switch&gt;](switch.md) element. |
