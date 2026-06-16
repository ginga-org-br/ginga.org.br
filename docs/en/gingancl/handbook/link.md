---
title: "Element &lt;link&gt;"
---

### Definition and Usage { data-search-exclude }

The [&lt;link&gt;](link.md) element defines a relationship among media and composite
objects.

A [&lt;link&gt;](link.md) element may have an *id* attribute, which uniquely
identifies the element within a document, and must have an
*xconnector* attribute, which refers to a connector URI.

The referred [&lt;causalConnector&gt;](causalconnector.md) element defines the relation without
specifying who plays the relation roles.  Who plays is defined using
[&lt;bind&gt;](bind.md) elements, children of the [&lt;link&gt;](link.md) element.

### Syntax { data-search-exclude }

| Element | Attributes | Content | Parent |
| --- | --- | --- | --- |
| [&lt;link&gt;](link.md) | *id*, <u>*xconnector*</u> | ([&lt;linkParam&gt;](linkparam.md)*, [&lt;bind&gt;](bind.md)+) | [&lt;body&gt;](body.md) or [&lt;context&gt;](context.md) or [&lt;switch&gt;](switch.md) |

### Attributes { data-search-exclude }

| Name | Value | Description |
| --- | --- | --- |
| *id* | It may receive any string value that begins with a letter or an underscore and that only contains letters, digits, <".">, and <"_">. | The *id* attribute uniquely identifies the element within a document. |
| *xconnector* | <p>String.</p><p>The value must have the format:</p><ol><li class="level1"><div class="li">"alias#connector_id", or "documentURI_value#connector_id", for connectors defined in an external imported document, or</div></li><li class="level1"><div class="li">"connector_id", the connector *id* for connectors defined in the document itself.</div></li> | The *xconnector* attribute refers to a connector defined as a descendant element of the [&lt;connectorBase&gt;](connectorbase.md) in an external imported document. |
