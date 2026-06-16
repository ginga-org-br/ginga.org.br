---
title: "Element &lt;compoundStatement&gt;"
---

### Definition and Usage { data-search-exclude }

The [&lt;compoundStatement&gt;](../compoundstatement/) element defines a logical expression among its
child elements ([&lt;assessmentStatement&gt;](../assessmentstatement/) and [&lt;compoundStatement&gt;](../compoundstatement/)) by
means of a Boolean *operator* attribute.

The *isNegated* attribute may be defined to specify that a
[&lt;compoundStatement&gt;](../compoundstatement/) child element must be negated before the Boolean
operation is evaluated.

### Syntax { data-search-exclude }

| Element | Attributes | Content | Parent |  |
| --- | --- | --- | --- | --- |
| [&lt;compoundStatement&gt;](../compoundstatement/) | <u>*operator*</u>, *isNegated* | ([&lt;assessmentStatement&gt;](../assessmentstatement/) | [&lt;compoundStatement&gt;](../compoundstatement/))+ | [&lt;compoundCondition&gt;](../compoundcondition/) or [&lt;compoundStatement&gt;](../compoundstatement/) |

### Attributes { data-search-exclude }

| Name | Value | Description |
| --- | --- | --- |
| *operator* | "and" or "or". | The *operator* attribute defines the logical expression among the [&lt;compoundStatement&gt;](../compoundstatement/) child elements. |
| *isNegated* | <p>"true" or "false".</p><p>The default value is "false".</p> | The *isNegated* attribute defines if the [&lt;compoundStatement&gt;](../compoundstatement/) child elements must be negated before the statement is evaluated. |
