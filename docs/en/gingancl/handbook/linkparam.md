---
title: "Element &lt;linkParam&gt;"
---

### Definition and Usage { data-search-exclude }

The [&lt;linkParam&gt;](linkparam.md) element is used to attribute a value to a parameter
defined by the [&lt;connectorParam&gt;](connectorparam.md) element of the [&lt;causalConnector&gt;](causalconnector.md)
element referred by the parent [&lt;link&gt;](link.md) element.  The scope of the
attributed value is the whole parent [&lt;link&gt;](link.md) element.

In a [&lt;linkParam&gt;](linkparam.md) element, the *name* attribute refers to the name
of a connector parameter while the *value* attribute defines a value
to assigned to this parameter.

### Syntax { data-search-exclude }

| Element | Attributes | Content | Parent |
| --- | --- | --- | --- |
| [&lt;linkParam&gt;](linkparam.md) | <u>*name*</u>, <u>*value*</u> | -- | [&lt;link&gt;](link.md) |

### Attributes { data-search-exclude }

| Name | Value | Description |
| --- | --- | --- |
| *name* | It may receive any string value that begins with a letter or an underscore and that only contains letters, digit, <".">, and <"_">. | The *name* attribute uniquely identifies the parameter within the referred [&lt;causalConnector&gt;](causalconnector.md) element. |
| *value* | Depends on the parameter defined by the [&lt;connectorParam&gt;](connectorparam.md) element. | The *value* attribute defines a value for the parameter.  The value is thus valid for the whole [&lt;link&gt;](link.md) definition. |
