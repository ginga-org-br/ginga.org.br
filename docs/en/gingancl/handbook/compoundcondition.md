---
title: "Element &lt;compoundCondition&gt;"
---

### Definition and Usage { data-search-exclude }

The [&lt;compoundCondition&gt;](compoundcondition.md) element defines a logical expression among its
child elements by means of its Boolean *operator* attribute.

A *delay* attribute may also be defined specifying that the compound
condition is true after a time delay from the expression relating its child
elements is true.

When an "and" compound condition relates more than one trigger condition
(that is, a condition that is satisfied in an infinitesimal time
instant–--as for example, the end of an object presentation), the compound
condition shall be considered true in the instant immediately after all the
trigger conditions are satisfied.

### Syntax { data-search-exclude }

| Element | Attributes | Content | Parent |  |  |
| --- | --- | --- | --- | --- | --- |
| [&lt;compoundCondition&gt;](compoundcondition.md) | <u>*operator*</u>, *delay* | (([&lt;simpleCondition&gt;](simplecondition.md) | [&lt;compoundCondition&gt;](compoundcondition.md))+,([&lt;assessmentStatement&gt;](assessmentstatement.md) | [&lt;compoundStatement&gt;](compoundstatement.md))*) | [&lt;causalConnector&gt;](causalconnector.md) or [&lt;compoundCondition&gt;](compoundcondition.md) |

### Attributes { data-search-exclude }

| Name | Value | Description |
| --- | --- | --- |
| *operator* | "and" or "or". | The *operator* attribute defines a logical expression among the [&lt;compoundCondition&gt;](compoundcondition.md) child elements. |
| *delay* | <p>The *delay* attribute is be specified according with one of the following syntax:</p><ol><li class="level1"><div class="li"><"<nowiki>Hours:Minutes:Seconds.Fraction</nowiki>">, where "Hours" is an integer in the \[0,23\] interval, "Minutes" is an integer in the \[0,59\] interval, "Seconds" is an integer in the 0,59 interval, and "Fraction" is a positive integer,</div></li><li class="level1"><div class="li">Seconds<"s">, where "Seconds" is a positive real number.</div></li></ol><p>The default value is "0s".</p> | The *delay* attribute defines that the [&lt;compoundCondition&gt;](compoundcondition.md) is true after a time delay from the expression relating its child elements is true. |
