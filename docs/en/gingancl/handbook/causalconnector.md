---
title: "Element &lt;causalConnector&gt;"
---

### Definition and Usage { data-search-exclude }

The [&lt;causalConnector&gt;](causalconnector.md) element represents a causal relation that may be
used for creating relationships ([&lt;link&gt;](link.md) elements) in NCL documents.  In
a causal relation, a condition must be satisfied in order to trigger an
action.

A [&lt;causalConnector&gt;](causalconnector.md) specifies a relation independently of
relationships, that is, it does not specify which nodes (represented by
[&lt;media&gt;](media.md), [&lt;context&gt;](context.md), [&lt;body&gt;](body.md), and [&lt;switch&gt;](switch.md) elements) will
interact through the relation.  A [&lt;link&gt;](link.md) element, in its turn,
represents a relationship of the type defined by its referred connector,
interconnecting different nodes.  Links representing the same type of
relation, but interconnecting different nodes, may reuse the same connector,
reusing all its previous specification.

A [&lt;causalConnector&gt;](causalconnector.md) defines, through its child elements, a set of
interface points, called roles.  A [&lt;link&gt;](link.md) element refers to a
[&lt;causalConnector&gt;](causalconnector.md) and defines a set of binds ([&lt;bind&gt;](bind.md) child
elements of the [&lt;link&gt;](link.md) element), which associate each link endpoint
(node interface) to a role of the referred connector.

Relations in NCL are based on events.  An NCL event is an occurrence in time
that may be instantaneous or have a measurable duration.  Each event defines
a state machine that is maintained by the NCL player (see Figure 1).
Moreover, every event has an associated attribute, named
*occurrences*, which counts how many times the event transits from
occurring to sleeping state during a document presentation.  Events of
presentation and attribution types have also an attribute named
*repetitions*, which counts how many times the event shall be
automatically restarted (transited from sleeping to occurring states) by the
NCL player.  This attribute may contain the "indefinite" value, leading to
an endless loop of the event occurrences until some external interruption.

![Figure 1: Event state machine.](/assets/state-machine.png)

NCL 3.0 EDTV profile defines the following types of events:

- presentation event: defined by the presentation of a subset of
    information units of a media object content.  Presentation events are
    specified in NCL on [&lt;area&gt;](area.md) elements, or on media nodes themselves
    (on their whole content anchors).  Presentation events may also be
    defined on composite nodes (represented by [&lt;body&gt;](body.md), [&lt;context&gt;](context.md),
    or [&lt;switch&gt;](switch.md) elements), representing the presentation of information
    units of any node inside the composite node);

- selection event: defined by the selection of a subset of information
    units of a media object content being presented.  Selection events are
    specified in NCL on [&lt;area&gt;](area.md) elements, or on media nodes themselves
    (on their whole content anchors);

- attribution event: defined by the attribution of a value to a property
    of a node (represented by a [&lt;media&gt;](media.md), [&lt;body&gt;](body.md), or [&lt;context&gt;](context.md)
    element), which must be declared in a [&lt;property&gt;](property.md) child element of
    the node; and

- composition event: defined by the presentation of the structure of a
    composite node (represented by a [&lt;body&gt;](body.md), [&lt;context&gt;](context.md), or
    [&lt;switch&gt;](switch.md) element).  Composition events are used to present the
    composite map (composite organization).  This functionality is optional
    in EDTV/BDTV profiles.

### Syntax { data-search-exclude }

| Element | Attributes | Content | Parent |  |  |
| --- | --- | --- | --- | --- | --- |
| [&lt;causalConnector&gt;](causalconnector.md) | <u>*id*</u> | ([&lt;connectorParam&gt;](connectorparam.md)*, ([&lt;simpleCondition&gt;](simplecondition.md) | [&lt;compoundCondition&gt;](compoundcondition.md)), ([&lt;simpleAction&gt;](simpleaction.md) | [&lt;compoundAction&gt;](compoundaction.md))) | [&lt;connectorBase&gt;](connectorbase.md) |

### Attributes { data-search-exclude }

| Name | Value | Description |
| --- | --- | --- |
| *id* | It may receive any string value that begins with a letter or an underscore and that only contains letters, digits, <".">, and <"_">. | The *id* attribute uniquely identifies the element within a document. |
