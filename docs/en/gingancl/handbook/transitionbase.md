---
title: "Element &lt;transitionBase&gt;"
---

# &lt;transitionBase&gt;

Explore the `<transitionBase>` example below:

<div class="ginga-playground-container">

<nav class="ginga-playground-tabs" role="tablist" aria-label="Ginga Playground examples">
  <button type="button" class="ginga-playground-tab" role="tab" aria-selected="true" data-playground-src="https://ginga.org.br/gingaf/playground/?app=https://raw.githubusercontent.com/ginga-org-br/gingaf/refs/heads/main/examples/ginga.org.br/transitionBase.ncl">transitionBase.ncl</button>
</nav>

<iframe
  class="ginga-playground"
  src="https://ginga.org.br/gingaf/playground/?app=https://raw.githubusercontent.com/ginga-org-br/gingaf/refs/heads/main/examples/ginga.org.br/transitionBase.ncl"
  loading="lazy"
  allow="autoplay; fullscreen">
</iframe>

</div>

The [&lt;transitionBase&gt;](transitionbase.md) element groups a set of [&lt;transition&gt;](transition.md)
elements, each of which defines a transition effect on [&lt;media&gt;](media.md) elements
in presentation.

### Syntax { data-search-exclude }

| Element | Attributes | Content | Parent |
| --- | --- | --- | --- |
| [&lt;transitionBase&gt;](transitionbase.md) | *id* | ([&lt;importBase&gt;](importbase.md),[&lt;transition&gt;](transition.md))+ | [&lt;head&gt;](head.md) |

### Attributes { data-search-exclude }

| Name | Value | Description |
| --- | --- | --- |
| *id* | It may receive any string value that begins with a letter or an underscore and that only contains letters, digits, <".">, and <"_">. | The *id* attribute uniquely identifies the element within a document. |
