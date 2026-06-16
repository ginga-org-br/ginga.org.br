---
title: "Element &lt;simpleAction&gt;"
---

### Definition and Usage { data-search-exclude }

The [&lt;simpleAction&gt;](simpleaction.md) element defines a simple action triggered by the
evaluation of a causal relationship condition.

The [&lt;simpleAction&gt;](simpleaction.md) element has a *role* attribute, whose value
must be unique in the connector’s role set. A role is a connector interface
point, which is associated to node interfaces by a link that refers to the
connector.

A [&lt;simpleAction&gt;](simpleaction.md) also defines an event type (*eventType*
attribute) and which action must be applied to the event state machine it
refers (*actionType* attribute). The *eventType* and
*actionType* values may be inferred by the role value if reserved
words are used as values. Otherwise, the *eventType* and
*actionType* attributes are required.

Reserved action role values associated to event state machines:
| Role Value | Action Type | Event Type |
| --- | --- | --- |
| start | start | presentation |
| stop | stop | presentation |
| abort | abort | presentation |
| pause | pause | presentation |
| resume | resume | presentation |
| set | start | attribution |

If an *eventType* value is "attribution", the [&lt;simpleAction&gt;](simpleaction.md)must
also define the value to be assigned, through its *value*
attribute. If the *value* is specified as "$anyName" (where "$" is a
reserved symbol and "anyName" is any string, except reserved role names),
the assigned value is retrieved from the property associated with the
*role* "anyName" and defined by a [&lt;bind&gt;](bind.md) child element of the
[&lt;link&gt;](link.md) element that refers the connector.  If this value cannot be
retrieved, no attribution is made.  This is the single possible case of a
[&lt;bind&gt;](bind.md) element referring to a role that is not explicitly declared in a
connector.

The role cardinality specifies the minimal (*min* attribute) and
maximal (*max* attribute) number of participants that may play the
role (that is, the number of binds) when the [&lt;causalConnector&gt;](causalconnector.md) is used
for creating a [&lt;link&gt;](link.md). If the max value is greater than one, the
*qualifier* attribute may be specified informing the logical
relationship among the simple action binds: "par" or "seq". When the
sequential "seq" qualifier is used, actions must be fired in the specified
order. However, an action does not need to wait the previous one to be
finished in order to be fired. When the parallel "par" qualifier is used,
actions can be performed in any order.

A *delay* attribute may also be defined for a [&lt;simpleAction&gt;](simpleaction.md),
specifying that the action must be fired only after waiting for the
specified time.

The [&lt;simpleAction&gt;](simpleaction.md) may also define a *repeat* attribute to be
assigned to the *repetitions* attribute of the event, and a
*repeatDelay* to be waited before repeating the action.

The [&lt;simpleAction&gt;](simpleaction.md) element may also define the duration and by
attributes if its *eventType* value is "attribution" and only if the
referred property defines numerical values or colors. When setting a new
value to a property the change is instantaneous by default (*duration*
is 0), but the change may also be carried out during an explicitly declared
duration, specified by the *duration* attribute. The change from the
old value to the new one may be linear by default (*by* is
"indefinite"), or carried out step by step, with the pace specified by the
*by* attribute.

### Syntax { data-search-exclude }

| Element | Attributes | Content | Parent |
| --- | --- | --- | --- |
| [&lt;simpleAction&gt;](simpleaction.md) | <u>*role*</u>, *delay*, *eventType*, *actionType*, *value*, *min*, *max*, *qualifier*, *repeat*, *repeatDelay*, *duration*, *by* | -- | [&lt;causalConnector&gt;](causalconnector.md) or [&lt;compoundAction&gt;](compoundaction.md) |

### Attributes { data-search-exclude }

| Name | Value | Description |
| --- | --- | --- |
| *role* | String. | The *role* attribute defines a connector interface point, which is associated to node interfaces by a link that refers to the connector.  The *role* value must be unique within the set of roles of the connector. |
| *delay* | <p>The *delay* attribute is be specified according with one of the following syntax:</p><ol><li class="level1"><div class="li"><"<nowiki>Hours:Minutes:Seconds.Fraction</nowiki>">, where "Hours" is an integer in the \[0,23\] interval, "Minutes" is an integer in the \[0,59\] interval, "Seconds" is an integer in the 0,59 interval, and "Fraction" is a positive integer,</div></li><li class="level1"><div class="li">Seconds<"s">, where "Seconds" is a positive real number.</div></li></ol><p>The default value is "0s".</p> | The *delay* attribute defines a time delay to be awaited before triggering the action. |
| *eventType* | "presentation", "selection", or "attribution". | The *eventType* attribute identifies the type of event for the action or condition. |
| *actionType* | "start", "stop", "abort", "pause", or "resume". | The *actionType* attribute specifies the action to trigger the corresponding transition in the event state machine of the referred event. |
| *value* | String | The *value* attribute defines a value to be set to the property bound to the attribution simple action. |
| *min* | <p>Positive integer lesser than or equal to the *max* value.</p><p>The default value is 1.</p> | The *min* attribute defines the minimum number of participants that may play the role. |
| *max* | <p>Positive integer greater than or equal to the *min* value, or the "unbounded" value.</p><p>The default value is 1.</p> | The *max* attribute defines the maximum number of participants that may play the role. |
| *qualifier* | "seq" or "par".  The default value is "par". | The *qualifier* attribute defines the order that actions must be applied in the simple action binds. |
| *repeat* | Positive integer.  The default value is 0 | The *repeat* attribute defines a value to be assigned to the repetitions attribute of the event defined in the [&lt;simpleAction&gt;](simpleaction.md) element. |
| *repeatDelay* | Same as for *delay*. | The *repeatDelay* attribute specifies a time interval to be waited before repeating the action. |
| *duration* | The *duration* attribute is specified as Seconds<"s">, where "Seconds" is a positive real number. | The *duration* attribute establishes the time an attribution must last when changing from the old value to the new one. |
| *by* | <p>A real number or "indefinite".</p><p>The default value is "indefinite".</p> | The *by* attribute establishes how the change made by an attribution action from an old value to the new one occurs: if linearly (by is "indefinite") or carried out step-by-step, with the pace specified by the *by* attribute. |
