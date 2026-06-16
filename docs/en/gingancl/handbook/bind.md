---
title: "Element &lt;bind&gt;"
---

### Definition and Usage { data-search-exclude }

The [&lt;bind&gt;](../bind/) element allows associating an interface of an object with a
connector role.

If the referred connector role comes from a [&lt;simpleAction&gt;](../simpleaction/) element
whose *eventType* is equal to "attribution", and whose
*actionType* is equal to "start", and if the specified value is
"$anyName", the assigned value is retrieved from the property associated
with the role "anyName" and defined by a [&lt;bind&gt;](../bind/) child element in the
same [&lt;link&gt;](../link/) element.  If this value cannot be retrieved, no attribution
is made.

### Syntax { data-search-exclude }

| Element | Attributes | Content | Parent |
| --- | --- | --- | --- |
| [&lt;bind&gt;](../bind/) | <u>*role*</u>, <u>*component*</u>, *interface*, *descriptor* | [&lt;bindParam&gt;](../bindparam/)* | [&lt;link&gt;](../link/) |

### Attributes { data-search-exclude }

| Name | Value | Description |
| --- | --- | --- |
| *role* | String | The *role* attribute refers to a connector role. |
| *component* | IDREF. | The *component* attribute refers to a [&lt;media&gt;](../media/) element, or to a [&lt;context&gt;](../context/) element, or to a [&lt;body&gt;](../body/) element, or to a [&lt;switch&gt;](../switch/) element.  These elements must be child elements of the same composition in which the [&lt;link&gt;](../link/) element is defined, or must be the composition in which the [&lt;link&gt;](../link/) element is defined. |
| *interface* | <p>String.</p><p>The default value is the whole content anchor.</p> | The *interface* attribute refers to an [&lt;area&gt;](../area/), [&lt;port&gt;](../port/), or [&lt;switchPort&gt;](../switchport/), of the object identified by the *component* attribute, by referring its *id* attribute; or refers to a [&lt;property&gt;](../property/), of the object identified by the *component* attribute, by referring its *name* attribute. |
| *descriptor* | IDREF. | The *descriptor* attribute refers to a [&lt;descriptor&gt;](../descriptor/) element. |
