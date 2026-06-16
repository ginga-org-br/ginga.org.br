---
title: "Element &lt;descriptorSwitch&gt;"
---

### Definition and Usage { data-search-exclude }

The [&lt;descriptorSwitch&gt;](descriptorswitch.md) element contains a set of alternative
descriptors to be associated with an object.  The choice is made during
presentation time.

Test rules used to choose the [&lt;descriptor&gt;](descriptor.md) element are defined by
[&lt;rule&gt;](rule.md) and [&lt;compositeRule&gt;](compositerule.md) elements; [&lt;bindRule&gt;](bindrule.md) child
elements associate these rules to child [&lt;descriptor&gt;](descriptor.md) elements of the
[&lt;descriptorSwitch&gt;](descriptorswitch.md) element.

The rules are evaluated in the order they are defined.  The first rule
evaluated as true determines the chosen [&lt;descriptor&gt;](descriptor.md) element.  If all
rules are evaluated as false, a default [&lt;descriptor&gt;](descriptor.md) element, defined
by the [&lt;defaultDescriptor&gt;](defaultdescriptor.md) element,is chosen; if the
[&lt;defaultDescriptor&gt;](defaultdescriptor.md) element is not defined no descriptor is selected
and the NCL player behaves as if the element does not exist.

### Syntax { data-search-exclude }

| Element | Attributes | Content | Parent |  |
| --- | --- | --- | --- | --- |
| [&lt;descriptorSwitch&gt;](descriptorswitch.md) | <u>*id*</u> | ([&lt;defaultDescriptor&gt;](defaultdescriptor.md)?, ([&lt;bindRule&gt;](bindrule.md) | [&lt;descriptor&gt;](descriptor.md))*) | [&lt;descriptorBase&gt;](descriptorbase.md) |

### Attributes { data-search-exclude }

| Name | Value | Description |
| --- | --- | --- |
| *id* | It may receive any string value that begins with a letter or an underscore and that only contains letters, digits, <".">, and <"_">. | The *id* attribute uniquely identifies the element within a document. |
