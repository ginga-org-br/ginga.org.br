---
title: "Element &lt;descriptorBase&gt;"
---

# &lt;descriptorBase&gt;

Explore the `<descriptorBase>` example below:

<div class="ginga-playground-container">

<nav class="ginga-playground-tabs" role="tablist" aria-label="Ginga Playground examples">
  <button type="button" class="ginga-playground-tab" role="tab" aria-selected="true" data-playground-src="https://ginga.org.br/gingaf/playground/?app=https://raw.githubusercontent.com/ginga-org-br/gingaf/refs/heads/main/examples/ginga.org.br/descriptorBase.ncl">descriptorBase.ncl</button>
</nav>

<iframe
  class="ginga-playground"
  src="https://ginga.org.br/gingaf/playground/?app=https://raw.githubusercontent.com/ginga-org-br/gingaf/refs/heads/main/examples/ginga.org.br/descriptorBase.ncl"
  loading="lazy"
  allow="autoplay; fullscreen">
</iframe>

</div>

The [&lt;descriptorBase&gt;](descriptorbase.md) element groups a set of [&lt;descriptor&gt;](descriptor.md)
elements, each of which defines initial values of [&lt;media&gt;](media.md) properties.

### Syntax { data-search-exclude }

| Element | Attributes | Content | Parent |  |  |
| --- | --- | --- | --- | --- | --- |
| [&lt;descriptorBase&gt;](descriptorbase.md) | *id* | ([&lt;importBase&gt;](importbase.md) | [&lt;descriptor&gt;](descriptor.md) | [&lt;descriptorSwitch&gt;](descriptorswitch.md))+ | [&lt;head&gt;](head.md) |

### Attributes { data-search-exclude }

| Name | Value | Description |
| --- | --- | --- |
| *id* | It may receive any string value that begins with a letter or an underscore and that only contains letters, digits, <".">, and <"_">. | The *id* attribute uniquely identifies the element within a document. |
