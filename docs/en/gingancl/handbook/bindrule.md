---
title: "Element &lt;bindRule&gt;"
---

### Definition and Usage { data-search-exclude }

The [&lt;bindRule&gt;](bindrule.md) element associates a rule with a component of a
[&lt;switch&gt;](switch.md) or [&lt;descriptorSwitch&gt;](descriptorswitch.md) element, through its rule and
constituent attributes, respectively.

### Syntax { data-search-exclude }

| Element | Attributes | Content | Parent |
| --- | --- | --- | --- |
| [&lt;bindRule&gt;](bindrule.md) | <u>*constituent*</u>, <u>*rule*</u> | -- | [&lt;switch&gt;](switch.md) or [&lt;descriptorSwitch&gt;](descriptorswitch.md) |

### Attributes { data-search-exclude }

| Name | Value | Description |
| --- | --- | --- |
| *constituent* | IDREF. | The *constituent* attribute uniquely identifies a child element of the [&lt;switch&gt;](switch.md) or [&lt;descriptorSwitch&gt;](descriptorswitch.md) element, through its *id* value. |
| *rule* | IDREF. | The *rule* attribute uniquely identifies a rule defined by a [&lt;rule&gt;](rule.md) or *compositeRule* element, through its *id* value. |
