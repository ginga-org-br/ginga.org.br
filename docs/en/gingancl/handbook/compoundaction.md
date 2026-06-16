---
title: "Element &lt;compoundAction&gt;"
---

### Definition and Usage { data-search-exclude }

The [&lt;compoundAction&gt;](compoundaction.md) element defines a logical expression among its
child elements ([&lt;simpleAction&gt;](simpleaction.md), [&lt;compoundAction&gt;](compoundaction.md)) by means of an
operator attribute that can receive the "par" or "seq" value.

Parallel ("par") and sequential ("seq") compound actions specify that the
execution of actions shall be performed in any order or in a specific order,
respectively.  When the sequential operator is used, actions shall be fired
in the specified order.  However, an action does not need to wait the
previous one to be finished.

A *delay* attribute may also be defined specifying that the compound
action must be applied after the specified delay.

### Syntax { data-search-exclude }

| Element | Attributes | Content | Parent |  |
| --- | --- | --- | --- | --- |
| [&lt;compoundAction&gt;](compoundaction.md) | <u>*operator*</u>, *delay* | ([&lt;simpleAction&gt;](simpleaction.md) | [&lt;compoundAction&gt;](compoundaction.md))+ | [&lt;causalConnector&gt;](causalconnector.md) or [&lt;compoundAction&gt;](compoundaction.md) |

### Attributes { data-search-exclude }

| Name | Value | Description |
| --- | --- | --- |
| *operator* | "seq" or "par". The default value is "par". | The *operator* defines the order that actions must be applied in the [&lt;compoundAction&gt;](compoundaction.md) child elements. |
| *delay* | <p>The *delay* attribute is be specified according with one of the following syntax:</p><ol><li class="level1"><div class="li"><"<nowiki>Hours:Minutes:Seconds.Fraction</nowiki>">, where "Hours" is an integer in the \[0,23\] interval, "Minutes" is an integer in the \[0,59\] interval, "Seconds" is an integer in the 0,59 interval, and "Fraction" is a positive integer,</div></li><li class="level1"><div class="li">Seconds<"s">, where "Seconds" is a positive real number.</div></li></ol><p>The default value is "0s".</p> | The *delay* attribute defines a time delay to be waited before triggering the [&lt;compoundAction&gt;](compoundaction.md). |
