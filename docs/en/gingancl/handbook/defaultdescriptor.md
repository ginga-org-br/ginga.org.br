---
title: "Element &lt;defaultDescriptor&gt;"
---

# &lt;defaultDescriptor&gt;

Explore the `<defaultDescriptor>` example below:

<div class="ginga-playground-container">

<nav class="ginga-playground-tabs" role="tablist" aria-label="Ginga Playground examples">
  <button type="button" class="ginga-playground-tab" role="tab" aria-selected="true" data-playground-src="https://ginga.org.br/gingaf/playground/?app=https://raw.githubusercontent.com/ginga-org-br/gingaf/refs/heads/main/examples/ginga.org.br/defaultDescriptor.ncl">defaultDescriptor.ncl</button>
</nav>

<iframe
  class="ginga-playground"
  src="https://ginga.org.br/gingaf/playground/?app=https://raw.githubusercontent.com/ginga-org-br/gingaf/refs/heads/main/examples/ginga.org.br/defaultDescriptor.ncl"
  loading="lazy"
  allow="autoplay; fullscreen">
</iframe>

</div>

The [&lt;defaultDescriptor&gt;](defaultdescriptor.md) element identifies the default child
[&lt;descriptor&gt;](descriptor.md) element of the [&lt;descriptorSwitch&gt;](descriptorswitch.md) element that must
be selected if all rules are evaluated as false.

### Syntax { data-search-exclude }

| Element | Attributes | Content | Parent |
| --- | --- | --- | --- |
| [&lt;defaultDescriptor&gt;](defaultdescriptor.md) | <u>*descriptor*</u> | -- | [&lt;descriptorSwitch&gt;](descriptorswitch.md) |

### Attributes { data-search-exclude }

| Name | Value | Description |
| --- | --- | --- |
| *descriptor* | IDREF. | The *descriptor* attribute refers to a [&lt;descriptor&gt;](descriptor.md) element. |
