---
title: "Element &lt;context&gt;"
---

### Definition and Usage { data-search-exclude }

The [&lt;context&gt;](context.md) element allows for structuring an NCL application. The
element may contain elements with media content ([&lt;media&gt;](media.md) elements),
called media objects, other nested [&lt;context&gt;](context.md) elements, elements
grouping content alternatives ([&lt;switch&gt;](switch.md) elements), and relationships
([&lt;link&gt;](link.md) elements) among all the objects represented by the
aforementioned elements.

It should be stressed that the [&lt;body&gt;](body.md) element is considered a special
kind of context, the one representing the whole application.

The [&lt;context&gt;](context.md) element may refer to another [&lt;context&gt;](context.md) or an
imported [&lt;body&gt;](body.md) element. In this case, it inherits the specification of
the referred element.

### Syntax { data-search-exclude }

| Element | Attributes | Content | Parent |
| --- | --- | --- | --- |
| [&lt;context&gt;](context.md) | <u>*id*</u>, *refer* | ([&lt;port&gt;](port.md) &#124; [&lt;property&gt;](property.md) &#124; [&lt;media&gt;](media.md) &#124; [&lt;context&gt;](context.md) &#124; [&lt;link&gt;](link.md) &#124; [&lt;switch&gt;](switch.md) &#124; [&lt;meta&gt;](meta.md) &#124; [&lt;metadata&gt;](metadata.md))* | [&lt;body&gt;](body.md), [&lt;context&gt;](context.md) or [&lt;switch&gt;](switch.md) |

### Attributes { data-search-exclude }

| Name | Value | Description |
| --- | --- | --- |
| *id* | It may receive any string value that begins with a letter or an underscore and that only contains letters, digits, <".">, and <"_">. | The *id* attribute uniquely identifies the element within a document. |
| *refer* | IDREF or the string "alias#id" where "id" is an IDREF value. | <p>The *refer* attribute refers to an element *id* that will be reused.  An element that refers to another element cannot be reused; that is, its *id* value cannot be the value of any *refer* attribute.  The referred element must be a [&lt;context&gt;](context.md) or an imported [&lt;body&gt;](body.md) element.</p><p>The referred element and the element that refers to it must be considered the same regarding their data specification.</p> <p>If the referred node ([&lt;context&gt;](context.md) or [&lt;body&gt;](body.md) element) is defined within an imported document D, the *refer* attribute value must have the format "alias#id", where "alias" is the value of the *alias* attribute associated with the imported D document.</p> |
