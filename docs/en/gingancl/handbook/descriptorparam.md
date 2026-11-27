---
title: "Element &lt;descriptorParam&gt;"
---

# &lt;descriptorParam&gt;

Explore the `<descriptorParam>` example below:

<div class="ginga-playground-container">

<nav class="ginga-playground-tabs" role="tablist" aria-label="Ginga Playground examples">
  <button type="button" class="ginga-playground-tab" role="tab" aria-selected="true" data-playground-src="https://ginga.org.br/gingaf/playground/?app=https://raw.githubusercontent.com/ginga-org-br/gingaf/refs/heads/main/examples/ginga.org.br/descriptorParam.ncl">descriptorParam.ncl</button>
</nav>

<iframe
  class="ginga-playground"
  src="https://ginga.org.br/gingaf/playground/?app=https://raw.githubusercontent.com/ginga-org-br/gingaf/refs/heads/main/examples/ginga.org.br/descriptorParam.ncl"
  loading="lazy"
  allow="autoplay; fullscreen">
</iframe>

</div>

The [&lt;descriptorParam&gt;](descriptorparam.md) elements define initial values for properties of
a [&lt;media&gt;](media.md) element.The property is identified in the *name*
attribute of the [&lt;descriptorParam&gt;](descriptorparam.md) element and the value is defined in
the *value* attribute.

### Syntax { data-search-exclude }

| Element | Attributes | Content | Parent |
| --- | --- | --- | --- |
| [&lt;descriptorParam&gt;](descriptorparam.md) | <u>*name*</u>, <u>*value*</u> | -- | [&lt;descriptor&gt;](descriptor.md) |

### Attributes { data-search-exclude }

| Name | Value | Description |
| --- | --- | --- |
| *name* | It may receive any string value that begins with a letter or an underscore and that only contains letters, digits, <".">, and <"_">. | The *name* attribute identifies the property of the [&lt;media&gt;](media.md) element that refers to the [&lt;descriptor&gt;](descriptor.md) element parent of the [&lt;descriptorParam&gt;](descriptorparam.md) element. |
| *value* | Depends on the *name* value. | The *value* attribute defines an initial value for the property identified in the *name* attribute. |
