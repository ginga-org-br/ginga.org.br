---
title: "Element &lt;importBase&gt;"
---

### Definition and Usage { data-search-exclude }

The [&lt;importBase&gt;](importbase.md) element allows for incorporating an entity base
(represented by [&lt;connectorBase&gt;](connectorbase.md), [&lt;regionBase&gt;](regionbase.md),
[&lt;descriptorBase&gt;](descriptorbase.md), [&lt;ruleBase&gt;](rulebase.md) or [&lt;transitionBase&gt;](transitionbase.md)
elementsdefined in an external document) to another already-defined
base. ItsdocumentURIattribute refers to a URI corresponding to the NCL
document containing the base to be imported. The alias attribute specifies a
name to be used as prefix when referring to elements of this imported
base. The reference must have the format: <nowiki>alias#element_id</nowiki>.

The import operation is transitive, that is, if baseA imports baseB that
imports baseC, then baseA imports baseC. However, the alias defined for
baseC inside baseB is not considered by baseA.

The following constraints must be satisfied:

  * the [&lt;descriptorBase&gt;](descriptorbase.md) element may have a child [&lt;importBase&gt;](importbase.md)
    element referring to a URI corresponding to another NCL document
    containing the descriptor base to be imported and nested. When a
    descriptor base is imported, the region base, the transition base and
    the rule base, when present in the imported document, are also
    automatically imported to the corresponding region and rule bases of the
    importing document;
  * the [&lt;connectorBase&gt;](connectorbase.md) element may have a child [&lt;importBase&gt;](importbase.md)
    element referring to a URI corresponding to another connector base to be
    imported and nested;
  * the [&lt;transitionBase&gt;](transitionbase.md) element may have a child [&lt;importBase&gt;](importbase.md)
    element referring to a URI corresponding to another transition base to
    be imported and nested;
  * the [&lt;ruleBase&gt;](rulebase.md) element may have a child [&lt;importBase&gt;](importbase.md) element
    referring to a URI corresponding to another NCL document containing the
    rule base to be imported and nested;
  * the [&lt;regionBase&gt;](regionbase.md) element may have a child [&lt;importBase&gt;](importbase.md) element
    referring to a URI corresponding to another NCL document containing the
    region base to be imported and nested. As the referred document URI can
    have more than one region base, the base to be imported must be
    identified by assigning its idvalue to the baseId attribute of the
    [&lt;importBase&gt;](importbase.md) element. On importing a [&lt;regionBase&gt;](regionbase.md), an
    attribute named region may be specified within the [&lt;importBase&gt;](importbase.md)
    element. When present, this attribute identifies the id of a
    [&lt;region&gt;](region.md) element declared in a [&lt;regionBase&gt;](regionbase.md) element of the
    host document (the document that does the importing operation). As a
    consequence, all child [&lt;region&gt;](region.md) elements of the imported
    [&lt;regionBase&gt;](regionbase.md) shall be considered as child [&lt;region&gt;](region.md) elements of
    the region referred by the [&lt;importBase&gt;](importbase.md)’s region attribute. If not
    specified, the child [&lt;region&gt;](region.md) elements of the imported
    [&lt;regionBase&gt;](regionbase.md) shall be considered direct children of the host
    document [&lt;regionBase&gt;](regionbase.md) element.

### Syntax { data-search-exclude }

| Element | Attributes | Content | Parent |
| --- | --- | --- | --- |
| [&lt;importBase&gt;](importbase.md) | <u>*alias*</u>, <u>*documentURI*</u>, *region*, *baseId* | -- | [&lt;ruleBase&gt;](rulebase.md) or [&lt;transitionBase&gt;](transitionbase.md) or [&lt;regionBase&gt;](regionbase.md) or [&lt;descriptorBase&gt;](descriptorbase.md) or [&lt;connectorBase&gt;](connectorbase.md) |

### Attributes { data-search-exclude }

| Name | Value | Description |
| --- | --- | --- |
| *alias* | It may receive any string value that begins with a letter or an underscore and that only contains letters, digits, <".">, and <"_">. | The *alias* attribute specifies a name to be used as prefix when referring to elements of the imported base.  The *alias* value must be unique in a document ands its scope is constrained to the document that has defined the alias attribute. |
| *documentURI* | URI. | The *documentURI* attribute is the locator for the NCL document from where the base or document will be imported. |
| *region* | IDREF. | The *region* attribute may be used when importing a [&lt;regionBase&gt;](regionbase.md).  It identifies a [&lt;region&gt;](region.md) element of the importing document that will nest (will be the parent region) all imported [&lt;region&gt;](region.md) elements. |
| *baseId* | IDREF. | The *baseId* attribute may be used when importing a [&lt;regionBase&gt;](regionbase.md).  It defines the [&lt;regionBase&gt;](regionbase.md) element to be imported through its *id* value. |
