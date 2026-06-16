---
title: "Element &lt;linkParam&gt;"
---

### Definition and Usage { data-search-exclude }

The [&lt;linkParam&gt;](../linkparam/) element is used to attribute a value to a parameter
defined by the [&lt;connectorParam&gt;](../connectorparam/) element of the [&lt;causalConnector&gt;](../causalconnector/)
element referred by the parent [&lt;link&gt;](../link/) element.  The scope of the
attributed value is the whole parent [&lt;link&gt;](../link/) element.

In a [&lt;linkParam&gt;](../linkparam/) element, the *name* attribute refers to the name
of a connector parameter while the *value* attribute defines a value
to assigned to this parameter.

### Syntax { data-search-exclude }

| Element | Attributes | Content | Parent |
| --- | --- | --- | --- |
| [&lt;linkParam&gt;](../linkparam/) | <u>*name*</u>, <u>*value*</u> | -- | [&lt;link&gt;](../link/) |

### Attributes { data-search-exclude }

| Name | Value | Description |
| --- | --- | --- |
| *name* | It may receive any string value that begins with a letter or an underscore and that only contains letters, digit, <".">, and <"_">. | The *name* attribute uniquely identifies the parameter within the referred [&lt;causalConnector&gt;](../causalconnector/) element. |
| *value* | Depends on the parameter defined by the [&lt;connectorParam&gt;](../connectorparam/) element. | The *value* attribute defines a value for the parameter.  The value is thus valid for the whole [&lt;link&gt;](../link/) definition. |
