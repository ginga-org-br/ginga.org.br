---
title: "Element &lt;attributeAssessment&gt;"
---

### Definition and Usage { data-search-exclude }

The [&lt;attributeAssessment&gt;](attributeassessment.md) element is used to define a variable to be
evaluated, in [&lt;assessmentStatement&gt;](assessmentstatement.md) elements, against other variable
values or an absolute value.

The variable can be a property specifies in a [&lt;property&gt;](property.md) element, or
can be a (presentation, selection or attribution) event attribute:
occurrences, repetition or state (which has the following values:
"occurring", "paused", or "sleeping").

The [&lt;attributeAssessment&gt;](attributeassessment.md)element has a *role* attribute, which
has to be unique in the connector role set.  This attribute is the connector
interface point, which is associated to node interfaces ([&lt;port&gt;](port.md),
[&lt;area&gt;](area.md), [&lt;property&gt;](property.md) or [&lt;switchPort&gt;](switchport.md) elements) by a [&lt;link&gt;](link.md)
that refers to the connector.

The variable defined by the element depends on its *eventType*
attribute and its *attributeType* attribute:

  * If the eventType value is "presentation", the *attributeType*
    attribute may specifyas variable:the "occurrences" or "repetition" event
    attributes,or the "state" event state.

  * If the eventType is "attribution" the *attributeType* may have the
    values:  "nodeProperty" (specifying a node property), "occurrences",
    "repetition" or "state".

  * If the eventType value is "selection", the [&lt;attributeAssessment&gt;](attributeassessment.md)can
    also define to which selection apparatus (for example, keyboard keys or
    remote control keys) it refers, through its *key* attribute.  The
    *attributeType* attribute may have the values:  "occurrences"
    (default) or "state".

An offset value may be added to an [&lt;attributeAssessment&gt;](attributeassessment.md) before its
comparison in an [&lt;assessmentStatement&gt;](assessmentstatement.md) element.  For example, an offset
may be added to an *attributeassessment* to specify: "the screen
vertical position plus 50 pixels".

### Syntax { data-search-exclude }

| Element | Attributes | Content | Parent |
| --- | --- | --- | --- |
| [&lt;attributeAssessment&gt;](attributeassessment.md) | <u>*role*</u>, <u>*eventType*</u>, *key*, *attributeType*, *offset* | -- | [&lt;assessmentStatement&gt;](assessmentstatement.md) |

### Attributes { data-search-exclude }

| Name | Value | Description |
| --- | --- | --- |
| *role* | String. | The *role* attribute defines a connector interface point, which is associated to node interfaces by a link that refers to the connector.  The *role* value must be unique within the set of roles of the connector. |
| *eventType* | "presentation", "selection", or "attribution". | The *eventType* attribute identifies the type of event for the action or condition. |
| *key* | At least the following values (case sensitive) must be accepted for the key attribute: "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "*", "#", "MENU", "INFO", "GUIDE", "CURSOR_DOWN", "CURSOR_LEFT", "CURSOR_RIGHT", "CURSOR_UP", "CHANNEL_DOWN", "CHANNEL_UP", "VOLUME_DOWN", "VOLUME_UP", "ENTER", "RED", "GREEN", "YELLOW", "BLUE", "BACK", "EXIT", "POWER", "REWIND", "STOP", "EJECT", "PLAY", "RECORD", and "PAUSE". | The *key* attribute identifies the selection key used for the selection. |
| *attributeType* | <p>"nodeProperty" (only in the case of *eventType*="attribution"), "occurrences", "repetition", or "state".</p><p>The default values are: "nodeProperty" if *eventType*="attribution", or "occurrences" if *eventType*="selection".</p> | The *attributeType* attribute identifies the variable to be evaluated in a [&lt;assessmentStatement&gt;](assessmentstatement.md) element. |
| *offset* | String. | The *offset* attribute specifies a value to be added to the selected variable before its evaluation in a [&lt;assessmentStatement&gt;](assessmentstatement.md) element. |
