---
title: "Element &lt;compoundStatement&gt;"
---

# &lt;compoundStatement&gt;

Explore the `<compoundStatement>` example below:

<div class="ginga-playground-container">

<nav class="ginga-playground-tabs" role="tablist" aria-label="Ginga Playground examples">
  <button type="button" class="ginga-playground-tab" role="tab" aria-selected="true" data-playground-src="https://ginga.org.br/gingaf/playground/?app=https://raw.githubusercontent.com/ginga-org-br/gingaf/refs/heads/main/examples/ginga.org.br/compoundStatement.ncl">compoundStatement.ncl</button>
</nav>

<iframe
  class="ginga-playground"
  src="https://ginga.org.br/gingaf/playground/?app=https://raw.githubusercontent.com/ginga-org-br/gingaf/refs/heads/main/examples/ginga.org.br/compoundStatement.ncl"
  loading="lazy"
  allow="autoplay; fullscreen">
</iframe>

</div>

The [&lt;compoundStatement&gt;](compoundstatement.md) element defines a logical expression among its
child elements ([&lt;assessmentStatement&gt;](assessmentstatement.md) and [&lt;compoundStatement&gt;](compoundstatement.md)) by
means of a Boolean *operator* attribute.

The *isNegated* attribute may be defined to specify that a
[&lt;compoundStatement&gt;](compoundstatement.md) child element must be negated before the Boolean
operation is evaluated.

### Syntax { data-search-exclude }

| Element | Attributes | Content | Parent |  |
| --- | --- | --- | --- | --- |
| [&lt;compoundStatement&gt;](compoundstatement.md) | <u>*operator*</u>, *isNegated* | ([&lt;assessmentStatement&gt;](assessmentstatement.md) | [&lt;compoundStatement&gt;](compoundstatement.md))+ | [&lt;compoundCondition&gt;](compoundcondition.md) or [&lt;compoundStatement&gt;](compoundstatement.md) |

### Attributes { data-search-exclude }

| Name | Value | Description |
| --- | --- | --- |
| *operator* | "and" or "or". | The *operator* attribute defines the logical expression among the [&lt;compoundStatement&gt;](compoundstatement.md) child elements. |
| *isNegated* | <p>"true" or "false".</p><p>The default value is "false".</p> | The *isNegated* attribute defines if the [&lt;compoundStatement&gt;](compoundstatement.md) child elements must be negated before the statement is evaluated. |
