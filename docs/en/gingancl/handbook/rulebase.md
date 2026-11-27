---
title: "Element &lt;ruleBase&gt;"
---

# &lt;ruleBase&gt;

Explore the `<ruleBase>` example below:

<div class="ginga-playground-container">

<nav class="ginga-playground-tabs" role="tablist" aria-label="Ginga Playground examples">
  <button type="button" class="ginga-playground-tab" role="tab" aria-selected="true" data-playground-src="https://ginga.org.br/gingaf/playground/?app=https://raw.githubusercontent.com/ginga-org-br/gingaf/refs/heads/main/examples/ginga.org.br/ruleBase.ncl">ruleBase.ncl</button>
</nav>

<iframe
  class="ginga-playground"
  src="https://ginga.org.br/gingaf/playground/?app=https://raw.githubusercontent.com/ginga-org-br/gingaf/refs/heads/main/examples/ginga.org.br/ruleBase.ncl"
  loading="lazy"
  allow="autoplay; fullscreen">
</iframe>

</div>

The [&lt;ruleBase&gt;](rulebase.md) element groups a set of rules specified in [&lt;rule&gt;](rule.md)
and [&lt;compositeRule&gt;](compositerule.md) elements.  The specification of rules in NCL 3.0
was done in a separate module, because they are useful for defining either
alternative components or alternative descriptors.

### Syntax { data-search-exclude }

| Element | Attributes | Content | Parent |  |  |
| --- | --- | --- | --- | --- | --- |
| [&lt;ruleBase&gt;](rulebase.md) | *id* | ([&lt;importBase&gt;](importbase.md) | [&lt;compositeRule&gt;](compositerule.md) | [&lt;rule&gt;](rule.md))+ | [&lt;head&gt;](head.md) |

### Attributes { data-search-exclude }

| Name | Value | Description |
| --- | --- | --- |
| *id* | It may receive any string value that begins with a letter or an underscore and that only contains letters, digits, <".">, and <"_">. | The *id* attribute uniquely identifies the element within a document. |
