---
title: "Element &lt;assessmentStatement&gt;"
---

### Definition and Usage { data-search-exclude }

The [&lt;assessmentStatement&gt;](assessmentstatement.md) element is used to compare variable values
specified in [&lt;attributeAssessment&gt;](attributeassessment.md) elements, or to compare the values
of these variables with absolute values specified in [&lt;valueAssessment&gt;](valueassessment.md)
elements.

The [&lt;assessmentStatement&gt;](assessmentstatement.md) element has a *comparator* attribute
that compares the values inferred from its child elements
([&lt;attributeAssessment&gt;](attributeassessment.md) elements and [&lt;valueAssessment&gt;](valueassessment.md) elements).

### Syntax { data-search-exclude }

| Element | Attributes | Content | Parent |  |
| --- | --- | --- | --- | --- |
| [&lt;assessmentStatement&gt;](assessmentstatement.md) | <u>*comparator*</u> | ([&lt;attributeAssessment&gt;](attributeassessment.md), ([&lt;attributeAssessment&gt;](attributeassessment.md) | [&lt;valueAssessment&gt;](valueassessment.md))) | [&lt;compoundCondition&gt;](compoundcondition.md) or [&lt;compoundStatement&gt;](compoundstatement.md) |

### Attributes { data-search-exclude }

| Name | Value | Description |
| --- | --- | --- |
| *comparator* | "eq", "ne", "gt", "lt", "gte", or "lte". | The *comparator* attribute compares the values inferred from the child elements of the [&lt;assessmentStatement&gt;](assessmentstatement.md) element. |
