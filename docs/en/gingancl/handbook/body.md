---
title: "Element &lt;body&gt;"
---

# &lt;body&gt;

Explore the `<body>` example below:

<div class="ginga-playground-container">

<nav class="ginga-playground-tabs" role="tablist" aria-label="Ginga Playground examples">
  <button type="button" class="ginga-playground-tab" role="tab" aria-selected="true" data-playground-src="https://ginga.org.br/gingaf/playground/?app=https://raw.githubusercontent.com/ginga-org-br/gingaf/refs/heads/main/examples/ginga.org.br/body.ncl">body.ncl</button>
</nav>

<iframe
  class="ginga-playground"
  src="https://ginga.org.br/gingaf/playground/?app=https://raw.githubusercontent.com/ginga-org-br/gingaf/refs/heads/main/examples/ginga.org.br/body.ncl"
  loading="lazy"
  allow="autoplay; fullscreen">
</iframe>

</div>

The [&lt;body&gt;](body.md) tag defines the document's body.

All media assets that define an NCL application together with relationships
among these assets are defined in child elements of the [&lt;body&gt;](body.md) element.

### Syntax { data-search-exclude }

| Element | Attributes | Content | Parent |
| --- | --- | --- | --- |
| [&lt;body&gt;](body.md) | *id* | ([&lt;port&gt;](port.md)  &#124; [&lt;property&gt;](property.md)  &#124; [&lt;media&gt;](media.md)  &#124; [&lt;context&gt;](context.md)  &#124; [&lt;switch&gt;](switch.md)  &#124; [&lt;link&gt;](link.md)  &#124; [&lt;meta&gt;](meta.md)  &#124; [&lt;metadata&gt;](metadata.md))* | [&lt;ncl&gt;](ncl.md) |

### Attributes { data-search-exclude }

| Name | Value | Description |
| --- | --- | --- |
| *id* | It may receive any string value that begins with a letter or an underscore and that only contains letters, digits, <".">, and <"_">. | The *id* attribute uniquely identifies the element within a document. |
