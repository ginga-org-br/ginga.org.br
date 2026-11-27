---
title: "Element &lt;mapping&gt;"
---

# &lt;mapping&gt;

Explore the `<mapping>` example below:

<div class="ginga-playground-container">

<nav class="ginga-playground-tabs" role="tablist" aria-label="Ginga Playground examples">
  <button type="button" class="ginga-playground-tab" role="tab" aria-selected="true" data-playground-src="https://ginga.org.br/gingaf/playground/?app=https://raw.githubusercontent.com/ginga-org-br/gingaf/refs/heads/main/examples/ginga.org.br/mapping.ncl">mapping.ncl</button>
</nav>

<iframe
  class="ginga-playground"
  src="https://ginga.org.br/gingaf/playground/?app=https://raw.githubusercontent.com/ginga-org-br/gingaf/refs/heads/main/examples/ginga.org.br/mapping.ncl"
  loading="lazy"
  allow="autoplay; fullscreen">
</iframe>

</div>

A mapping element defines a path from the [&lt;switchPort&gt;](switchport.md) to an interface
(interface attribute) of one of the switch components (specified by its
component attribute).

### Syntax { data-search-exclude }

| Element | Attributes | Content | Parent |
| --- | --- | --- | --- |
| [&lt;mapping&gt;](mapping.md) | <u>*component*</u>, *interface* | -- | [&lt;switchPort&gt;](switchport.md) |

### Attributes { data-search-exclude }

| Name | Value | Description |
| --- | --- | --- |
| *component* | IDREF. | The *component* attribute uniquely identifies a child element of the switch, through its *id* value. |
| *interface* | <p>String.</p><p>The default value is the whole content anchor.</p> | The *interface* attribute uniquely identifies an interface ([&lt;area&gt;](area.md), [&lt;property&gt;](property.md), [&lt;port&gt;](port.md), or [&lt;switchPort&gt;](switchport.md)) of a child element of the [&lt;switch&gt;](switch.md), through its *id* or name value. |
