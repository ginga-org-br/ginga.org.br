---
title: "Element &lt;ruleBase&gt;"
---

### Definition and Usage { data-search-exclude }

The [&lt;ruleBase&gt;](../rulebase/) element groups a set of rules specified in [&lt;rule&gt;](../rule/)
and [&lt;compositeRule&gt;](../compositerule/) elements.  The specification of rules in NCL 3.0
was done in a separate module, because they are useful for defining either
alternative components or alternative descriptors.

### Syntax { data-search-exclude }

| Element | Attributes | Content | Parent |  |  |
| --- | --- | --- | --- | --- | --- |
| [&lt;ruleBase&gt;](../rulebase/) | *id* | ([&lt;importBase&gt;](../importbase/) | [&lt;compositeRule&gt;](../compositerule/) | [&lt;rule&gt;](../rule/))+ | [&lt;head&gt;](../head/) |

### Attributes { data-search-exclude }

| Name | Value | Description |
| --- | --- | --- |
| *id* | It may receive any string value that begins with a letter or an underscore and that only contains letters, digits, <".">, and <"_">. | The *id* attribute uniquely identifies the element within a document. |
