---
title: "Element &lt;valueAssessment&gt;"
---

### Definition and Usage { data-search-exclude }

The [&lt;valueAssessment&gt;](valueassessment.md) element is used to define a value to be compared
against other variable values specified by [&lt;attributeAssessment&gt;](attributeassessment.md)
elements.

The [&lt;valueAssessment&gt;](valueassessment.md) element has a value attribute that may assume an
event state value ("occurring", "paused", or "sleeping"), or any value to be
compared with a node property or event attribute ("occurrences" or
"repetition").

### Syntax { data-search-exclude }

| Element | Attributes | Content | Parent |
| --- | --- | --- | --- |
| [&lt;valueAssessment&gt;](valueassessment.md) | <u>*value*</u> | -- | [&lt;assessmentStatement&gt;](assessmentstatement.md) |

### Attributes { data-search-exclude }

| Name | Value | Description |
| --- | --- | --- |
| *value* | <p>String.</p><p>It can be an event state value ("occurring", "paused", or "sleeping"), or any value to be compared with a node property or event attribute ("occurrences" or "repetition").</p> | The *value* attribute defines a value to be compared in [&lt;assessmentStatement&gt;](assessmentstatement.md) elements. |
