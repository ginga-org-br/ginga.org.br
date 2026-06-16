---
title: "Element &lt;descriptorParam&gt;"
---

### Definition and Usage { data-search-exclude }

The [&lt;descriptorParam&gt;](descriptorparam.md) elements define initial values for properties of
a [&lt;media&gt;](media.md) element.The property is identified in the *name*
attribute of the [&lt;descriptorParam&gt;](descriptorparam.md) element and the value is defined in
the *value* attribute.

### Syntax { data-search-exclude }

| Element | Attributes | Content | Parent |
| --- | --- | --- | --- |
| [&lt;descriptorParam&gt;](descriptorparam.md) | <u>*name*</u>, <u>*value*</u> | -- | [&lt;descriptor&gt;](descriptor.md) |

### Attributes { data-search-exclude }

| Name | Value | Description |
| --- | --- | --- |
| *name* | It may receive any string value that begins with a letter or an underscore and that only contains letters, digits, <".">, and <"_">. | The *name* attribute identifies the property of the [&lt;media&gt;](media.md) element that refers to the [&lt;descriptor&gt;](descriptor.md) element parent of the [&lt;descriptorParam&gt;](descriptorparam.md) element. |
| *value* | Depends on the *name* value. | The *value* attribute defines an initial value for the property identified in the *name* attribute. |
