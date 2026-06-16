---
title: "Element &lt;mapping&gt;"
---

### Definition and Usage { data-search-exclude }

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
