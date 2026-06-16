---
title: "Element &lt;descriptorParam&gt;"
---

### Definition and Usage { data-search-exclude }

The [&lt;descriptorParam&gt;](../descriptorparam/) elements define initial values for properties of
a [&lt;media&gt;](../media/) element.The property is identified in the *name*
attribute of the [&lt;descriptorParam&gt;](../descriptorparam/) element and the value is defined in
the *value* attribute.

### Syntax { data-search-exclude }

| Element | Attributes | Content | Parent |
| --- | --- | --- | --- |
| [&lt;descriptorParam&gt;](../descriptorparam/) | <u>*name*</u>, <u>*value*</u> | -- | [&lt;descriptor&gt;](../descriptor/) |

### Attributes { data-search-exclude }

| Name | Value | Description |
| --- | --- | --- |
| *name* | It may receive any string value that begins with a letter or an underscore and that only contains letters, digits, <".">, and <"_">. | The *name* attribute identifies the property of the [&lt;media&gt;](../media/) element that refers to the [&lt;descriptor&gt;](../descriptor/) element parent of the [&lt;descriptorParam&gt;](../descriptorparam/) element. |
| *value* | Depends on the *name* value. | The *value* attribute defines an initial value for the property identified in the *name* attribute. |
