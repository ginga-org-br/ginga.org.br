---
title: "Element &lt;importNCL&gt;"
---

### Definition and Usage { data-search-exclude }

The [&lt;importNCL&gt;](importncl.md) element allows for incorporating another NCL document
specification.  As a consequence, all bases defined inside the imported NCL
document, as well as the document [&lt;body&gt;](body.md) element, are imported, all at
once.  The bases will be treated as if each one is imported by [&lt;importBase&gt;](importbase.md)
elements.  The imported [&lt;body&gt;](body.md) element will be treated as a [&lt;context&gt;](context.md)
element.  It should be stressed that the [&lt;importNCL&gt;](importncl.md) element does not
"include" the referred NCL document but only makes the referred document
visible to have its components reused by the document that has defined the
[&lt;importNCL&gt;](importncl.md) element.  Thus, the imported [&lt;body&gt;](body.md), as well as any of its
contained nodes, may be reused inside the [&lt;body&gt;](body.md) element of the importing
NCL document.

The *documentURI* attribute of the [&lt;importNCL&gt;](importncl.md) element refers to a URI
corresponding to the NCL document to be imported.   The *alias* attribute
specifies a name to be used as prefix when referring to elements of this
imported document.  The reference must have the format: alias#element_id.  It
is important to note that the same alias should be used when referring to
elements defined in the indirectly imported document bases ([&lt;regionBase&gt;](regionbase.md),
[&lt;connectorBase&gt;](connectorbase.md), [&lt;descriptorBase&gt;](descriptorbase.md), etc.).

The import operation is transitive, that is, if baseA imports baseB that
imports baseC, then baseA imports baseC.  However, the alias defined for
baseC inside baseBis not considered by baseA.

### Syntax { data-search-exclude }

| Element | Attributes | Content | Parent |
| --- | --- | --- | --- |
| [&lt;importNCL&gt;](importncl.md) | <u>*alias*</u>, <u>*documentURI*</u> | -- | [&lt;importedDocumentBase&gt;](importeddocumentbase.md) |

### Attributes { data-search-exclude }

| Name | Value | Description |
| --- | --- | --- |
| *alias* | It may receive any string value that begins with a letter or an underscore and that only contains letters, digits, <".">, and <"_">. | The *alias* attribute specifies a name to be used as prefix when referring to elements of the imported base.  The *alias* value must be unique in a document ands its scope is constrained to the document that has defined the alias attribute. |
| *documentURI* | URI. | The *documentURI* attribute is the locator for the NCL document from where the base or document will be imported. |
