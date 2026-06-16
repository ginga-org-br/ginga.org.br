---
title: "Element &lt;compoundStatement&gt;"
---

### Definition and Usage { data-search-exclude }

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
