---
title: "Element &lt;bindParam&gt;"
---

### Definition and Usage { data-search-exclude }

The [&lt;bindParam&gt;](bindparam.md) element is used to attribute a value to a parameter
defined by the [&lt;connectorParam&gt;](connectorparam.md) element of the [&lt;causalConnector&gt;](causalconnector.md)
element referred by the parent [&lt;link&gt;](link.md) element.  The scope of the
attributed value is limited to the parent [&lt;bind&gt;](bind.md) element.

In a [&lt;bindParam&gt;](bindparam.md) element the *name* attribute refers to the name
of a connector parameter, while the *value* attribute defines a value
to be assigned to the respective parameter.

### Syntax { data-search-exclude }

| Element | Attributes | Content | Parent |
| --- | --- | --- | --- |
| [&lt;bindParam&gt;](bindparam.md) | <u>*name*</u>, <u>*value*</u> | -- | [&lt;bind&gt;](bind.md) |

### Attributes { data-search-exclude }

| Name | Value | Description |
| --- | --- | --- |
| *name* | It may receive any string value that begins with a letter or an underscore and that only contains letters, digits, <".">, and <"_">. | The *name* attribute uniquely identifies the parameter within the referred [&lt;causalConnector&gt;](causalconnector.md) element. |
| *value* | Depends on the parameter defined by the [&lt;connectorParam&gt;](connectorparam.md) element. | The *value* attribute uniquely identifies the parameter within the referred [&lt;causalConnector&gt;](causalconnector.md) element. |
