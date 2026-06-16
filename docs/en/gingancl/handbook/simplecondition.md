---
title: "Element &lt;simpleCondition&gt;"
---

### Definition and Usage { data-search-exclude }

The [&lt;simpleCondition&gt;](simplecondition.md) element defines a simple condition to trigger
actions in a causal relationship.

The [&lt;simpleCondition&gt;](simplecondition.md) element has a role *attribute*, whose value
shall be unique in the connector's role set.  The role is a connector
interface point, which is associated to node interfaces by a link that
refers to the connector.

A [&lt;simpleCondition&gt;](simplecondition.md) also defines an event type (*eventType*
attribute) and to which transition in the event state machine it refers
(*transition* attribute).  The *eventType* and
*transition* may be inferred by the role value, if reserved words are
used.  Otherwise, the *eventType* and *transition* attributes
are required.

Reserved condition role values associated to event state machines:

| Role Value | Transition Value | Event Type |
| --- | --- | --- |
| onBegin | starts | presentation |
| onEnd | stops | presentation |
| onAbort | aborts | presentation |
| onPause | pauses | presentation |
| onResume | resumes | presentation |
| onSelection | stops | selection |
| onBeginSelection | starts | selection |
| onEndSelection | stops | selection |
| onAbortSelection | paborts | selection |
| onPauseSelection | pauses | selection |
| onResumeSelection | resumes | selection |
| onBeginAttribution | starts | attribution |
| onEndAttribution | stops | attribution |
| onPauseAttribution | pauses | attribution |
| onResumeAttribution | resumes | attribution |
| onAbortAttribution | aborts | attribution |

If an *eventType* value is "selection", the role can also define to
which selection apparatus (for example, keyboard keys or remote control
keys) it refers, through its key attribute.  If this attribute is not
specified, the selection via a pointer device (mouse, touch screen,
navigational keys) is assumed.

The role cardinality specifies the minimal (min attribute) and maximal (max
attribute) number of participants that may play the role (that is, the
number of binds) when the [&lt;causalConnector&gt;](causalconnector.md) is used to create a
[&lt;link&gt;](link.md).  If the max value is greater than one, a qualifier
attributeshould be specified informing the logical relationship among the
simple condition binds: "or" or "and".  If the qualifier establishes the
"or" logical operator, the link action will be fired whenever any condition
occurs.  If the qualifier establishes the "and" logical operator, the link
action will be fired after all the simple conditions occurrences.

A delay attribute may also be defined for a [&lt;simpleCondition&gt;](simplecondition.md),
specifying that the condition is true after a time delay from the time the
transition occurs.

### Syntax { data-search-exclude }

| Element | Attributes | Content | Parent |
| --- | --- | --- | --- |
| [&lt;simpleCondition&gt;](simplecondition.md) | <u>*role*</u>, *delay*, *eventType*, *key*, *transition*, *min*, *max*, *qualifier* | -- | [&lt;causalConnector&gt;](causalconnector.md) or [&lt;compoundCondition&gt;](compoundcondition.md) |

### Attributes { data-search-exclude }

| Name | Value | Description |
| --- | --- | --- |
| *role* | String. | The *role* attribute defines a connector interface point, which is associated to node interfaces by a link that refers to the connector.  The *role* value must be unique within the set of roles of the connector. |
| *delay* | <p>The *delay* attribute is be specified according with one of the following syntax:</p><ol><li class="level1"><div class="li"><"<nowiki>Hours:Minutes:Seconds.Fraction</nowiki>">, where "Hours" is an integer in the \[0,23\] interval, "Minutes" is an integer in the \[0,59\] interval, "Seconds" is an integer in the 0,59 interval, and "Fraction" is a positive integer,</div></li><li class="level1"><div class="li">Seconds<"s">, where "Seconds" is a positive real number.</div></li></ol><p>The default value is "0s".</p> | The *delay* attribute defines a time delay, from the time the transition occurs, from which the [&lt;simpleCondition&gt;](simplecondition.md) must be considered satisfied. |
| *eventType* | "presentation", "selection", or "attribution". | The *eventType* attribute identifies the type of event for the action or condition. |
| *key* | At least the following values (case sensitive) must be accepted for the key attribute: "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "*", "#", "MENU", "INFO", "GUIDE", "CURSOR_DOWN", "CURSOR_LEFT", "CURSOR_RIGHT", "CURSOR_UP", "CHANNEL_DOWN", "CHANNEL_UP", "VOLUME_DOWN", "VOLUME_UP", "ENTER", "RED", "GREEN", "YELLOW", "BLUE", "BACK", "EXIT", "POWER", "REWIND", "STOP", "EJECT", "PLAY", "RECORD", and "PAUSE". | The *key* attribute identifies the selection key used for the selection. |
| *transition* | "starts", "stops", "aborts", "pauses", or "resumes". | The *transition* attribute specifies a transition in the event state-machine used to define the condition. |
| *min* | <p>Positive integer lesser than or equal to the *max* value.</p><p>The default value is 1.</p> | The *min* attribute defines the minimum number of participants that may play the role. |
| *max* | <p>Positive integer greater than or equal to the *min* value, or the "unbounded" value.</p><p>The default value is 1.</p> | The *max* attribute defines the maximum number of participants that may play the role. |
| *qualifier* | "and" or "or". | The *qualifier* attribute defines the logical relationship among the condition binds. |
