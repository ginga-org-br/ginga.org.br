---
title: "Element &lt;switchPort&gt;"
---

### Definition and Usage { data-search-exclude }

The [&lt;switchPort&gt;](switchport.md) element defines a mapping to a subset of the
[&lt;switch&gt;](switch.md) element's components.  All references to an internal switch
component must be made through a [&lt;switchPort&gt;](switchport.md) element or, by default,
to the [&lt;switch&gt;](switch.md) element without specifying any [&lt;switchPort&gt;](switchport.md). In
this last case, it is considered as if the reference is made to a default
[&lt;switchPort&gt;](switchport.md) that contains mapping elements to each child object of the
switch and referring to their whole content anchors.

### Syntax { data-search-exclude }

| Element | Attributes | Content | Parent |
| --- | --- | --- | --- |
| [&lt;switchPort&gt;](switchport.md) | <u>*id*</u> | [&lt;mapping&gt;](mapping.md)+ | [&lt;switch&gt;](switch.md) |

### Attributes { data-search-exclude }

| Name | Value | Description |
| --- | --- | --- |
| *id* | It may receive any string value that begins with a letter or an underscore and that only contains letters, digits, <".">, and <"_">. | The *id* attribute uniquely identifies the element within a document. |
