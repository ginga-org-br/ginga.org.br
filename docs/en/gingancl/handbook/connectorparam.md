---
title: "Element &lt;connectorParam&gt;"
---

### Definition and Usage { data-search-exclude }

The [&lt;connectorParam&gt;](connectorparam.md) element is used to parameterize connector
attribute values.  Any attribute defined by a [&lt;causalConnector&gt;](causalconnector.md) element
or by its descendent elements can have its value specified as a parameter
whose value is defined by the relationship that refers to the connector,
using [&lt;linkParam&gt;](linkparam.md) or [&lt;bindParam&gt;](bindparam.md) elements.

In a [&lt;connectorParam&gt;](connectorparam.md) element the *name* attribute defines the
parameter name and the *type* attribute the parameter type.

In order to specify that an attribute defined by the [&lt;causalConnector&gt;](causalconnector.md)
element or by its descendent elements receivesthe parameter value,it is
sufficient to defined the attribute value as the parameter name preceded by
the "$" symbol.  For instance, in order to parameterize the delay attribute
of a [&lt;simpleAction&gt;](simpleaction.md) element, a parameter called *actionDelay* is
defined and the value "$actionDelay" is used in the attribute
(*delay*="$actionDelay").

### Syntax { data-search-exclude }

| Element | Attributes | Content | Parent |
| --- | --- | --- | --- |
| [&lt;connectorParam&gt;](connectorparam.md) | <u>*name*</u>, *type* | -- | [&lt;causalConnector&gt;](causalconnector.md) |

### Attributes { data-search-exclude }

| Name | Value | Description |
| --- | --- | --- |
| *name* | It may receive any string value that begins with a letter or an underscore and that only contains letters, digits, <".">, and <"_">. | The *name* attribute uniquely identifies the parameter within a [&lt;causalConnector&gt;](causalconnector.md) element. |
| *type* | String. | The *type* defines a type for the parameter. |
