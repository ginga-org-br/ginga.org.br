---
title: "Element &lt;assessmentStatement&gt;"
---

### Definition and Usage { data-search-exclude }

The [&lt;assessmentStatement&gt;](../assessmentstatement/) element is used to compare variable values
specified in [&lt;attributeAssessment&gt;](../attributeassessment/) elements, or to compare the values
of these variables with absolute values specified in [&lt;valueAssessment&gt;](../valueassessment/)
elements.

The [&lt;assessmentStatement&gt;](../assessmentstatement/) element has a *comparator* attribute
that compares the values inferred from its child elements
([&lt;attributeAssessment&gt;](../attributeassessment/) elements and [&lt;valueAssessment&gt;](../valueassessment/) elements).

### Syntax { data-search-exclude }

| Element | Attributes | Content | Parent |  |
| --- | --- | --- | --- | --- |
| [&lt;assessmentStatement&gt;](../assessmentstatement/) | <u>*comparator*</u> | ([&lt;attributeAssessment&gt;](../attributeassessment/), ([&lt;attributeAssessment&gt;](../attributeassessment/) | [&lt;valueAssessment&gt;](../valueassessment/))) | [&lt;compoundCondition&gt;](../compoundcondition/) or [&lt;compoundStatement&gt;](../compoundstatement/) |

### Attributes { data-search-exclude }

| Name | Value | Description |
| --- | --- | --- |
| *comparator* | "eq", "ne", "gt", "lt", "gte", or "lte". | The *comparator* attribute compares the values inferred from the child elements of the [&lt;assessmentStatement&gt;](../assessmentstatement/) element. |
