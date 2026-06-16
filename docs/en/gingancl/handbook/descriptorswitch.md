---
title: "Element &lt;descriptorSwitch&gt;"
---

### Definition and Usage { data-search-exclude }

The [&lt;descriptorSwitch&gt;](../descriptorswitch/) element contains a set of alternative
descriptors to be associated with an object.  The choice is made during
presentation time.

Test rules used to choose the [&lt;descriptor&gt;](../descriptor/) element are defined by
[&lt;rule&gt;](../rule/) and [&lt;compositeRule&gt;](../compositerule/) elements; [&lt;bindRule&gt;](../bindrule/) child
elements associate these rules to child [&lt;descriptor&gt;](../descriptor/) elements of the
[&lt;descriptorSwitch&gt;](../descriptorswitch/) element.

The rules are evaluated in the order they are defined.  The first rule
evaluated as true determines the chosen [&lt;descriptor&gt;](../descriptor/) element.  If all
rules are evaluated as false, a default [&lt;descriptor&gt;](../descriptor/) element, defined
by the [&lt;defaultDescriptor&gt;](../defaultdescriptor/) element,is chosen; if the
[&lt;defaultDescriptor&gt;](../defaultdescriptor/) element is not defined no descriptor is selected
and the NCL player behaves as if the element does not exist.

### Syntax { data-search-exclude }

| Element | Attributes | Content | Parent |  |
| --- | --- | --- | --- | --- |
| [&lt;descriptorSwitch&gt;](../descriptorswitch/) | <u>*id*</u> | ([&lt;defaultDescriptor&gt;](../defaultdescriptor/)?, ([&lt;bindRule&gt;](../bindrule/) | [&lt;descriptor&gt;](../descriptor/))*) | [&lt;descriptorBase&gt;](../descriptorbase/) |

### Attributes { data-search-exclude }

| Name | Value | Description |
| --- | --- | --- |
| *id* | It may receive any string value that begins with a letter or an underscore and that only contains letters, digits, <".">, and <"_">. | The *id* attribute uniquely identifies the element within a document. |
