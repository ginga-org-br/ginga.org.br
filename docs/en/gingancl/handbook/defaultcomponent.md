---
title: "Element &lt;defaultComponent&gt;"
---

### Definition and Usage { data-search-exclude }

The [&lt;defaultComponent&gt;](../defaultcomponent/) element identifies the default child component
of the [&lt;switch&gt;](../switch/) element that must be selected if all rules bound to
mapped components of the [&lt;switchPort&gt;](../switchport/) element, through which the
[&lt;switch&gt;](../switch/) elementwas activated, are evaluated as false.

### Syntax { data-search-exclude }

| Element | Attributes | Content | Parent |
| --- | --- | --- | --- |
| [&lt;defaultComponent&gt;](../defaultcomponent/) | <u>*component*</u> | -- | [&lt;switch&gt;](../switch/) or [&lt;descriptorSwitch&gt;](../descriptorswitch/) |

### Attributes { data-search-exclude }

| Name | Value | Description |
| --- | --- | --- |
| *component* | IDREF. | The *defaultComponent* attribute uniquely identifies a child element of the [&lt;switch&gt;](../switch/) element. |
