---
title: "Element &lt;port&gt;"
---

### Definition and Usage { data-search-exclude }

Composite nodes of NCL, represented by [&lt;body&gt;](body.md), [&lt;context&gt;](context.md), and
[&lt;switch&gt;](switch.md) elements, encapsulates their child components.  Interfaces of
child components are not visible to relationships defined outside of the
composite node, unless these interfaces are externalized, using the
[&lt;port&gt;](port.md) or [&lt;switchPort&gt;](switchport.md) elements.

The [&lt;port&gt;](port.md) element specifies a composite node port with its respective
mapping to an interface (*interface* attribute) of one of its
components (specified by the *component* attribute).  As usual, if the
*interface* attribute is not specified, the //whole content
anchor// is assumed.

### Syntax { data-search-exclude }

| Element | Attributes | Content | Parent |
| --- | --- | --- | --- |
| [&lt;port&gt;](port.md) | <u>*id*</u>, <u>*component*</u>, *interface* | -- | [&lt;context&gt;](context.md) or [&lt;body&gt;](body.md) |

### Attributes { data-search-exclude }

| Name | Value | Description |
| --- | --- | --- |
| *id* | It may receive any string value that begins with a letter or an underscore and that only contains letters, digits, <".">, and <"_">. | The *id* attribute uniquely identifies the element within a document. |
| *component* | IDREF. | The *component* attribute identifies a child element of the composition, which may be a media object or another composite-object, through its *id* value. |
| *interface* | <p>String.</p><p>The default value is the whole content anchor.</p> | The *interface* attribute uniquely identifies an interface ([&lt;area&gt;](area.md), [&lt;property&gt;](property.md), [&lt;port&gt;](port.md), or [&lt;switchPort&gt;](switchport.md)) of a child element of the composition, through its *id* or *name* value.  Defaults to the whole content anchor of the referred component. |
