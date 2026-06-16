---
title: "Element &lt;connectorBase&gt;"
---

### Definition and Usage { data-search-exclude }

The [&lt;connectorBase&gt;](../connectorbase/) element groups relations defined using connectors.

Connectors can be directly defined in [&lt;connectorBase&gt;](../connectorbase/) element that is
child of the [&lt;head&gt;](../head/) element of an NCL application.  However, since the
definition of connectors may be difficult for non-expert users, the idea is
to have experts defining connectors, storing them in libraries (connector
bases) that may be imported, and making them available to others for
creating links.

### Syntax { data-search-exclude }

| Element | Attributes | Content | Parent |  |
| --- | --- | --- | --- | --- |
| [&lt;connectorBase&gt;](../connectorbase/) | *id* | ([&lt;importBase&gt;](../importbase/) | [&lt;causalConnector&gt;](../causalconnector/))* | [&lt;head&gt;](../head/) |

### Attributes { data-search-exclude }

| Name | Value | Description |
| --- | --- | --- |
| *id* | It may receive any string value that begins with a letter or an underscore and that only contains letters, digits, <".">, and <"_">. | The *id* attribute uniquely identifies the element within a document. |
