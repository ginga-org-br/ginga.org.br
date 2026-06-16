---
title: "Element &lt;compositeRule&gt;"
---

### Definition and Usage { data-search-exclude }

The [&lt;compositeRule&gt;](../compositerule/) element defines a logical expression among its
child elements ([&lt;rule&gt;](../rule/) and [&lt;compositeRule&gt;](../compositerule/)) by means of a Boolean
operator attribute.

### Syntax { data-search-exclude }

| Element | Attributes | Content | Parent |  |
| --- | --- | --- | --- | --- |
| [&lt;compositeRule&gt;](../compositerule/) | <u>*id*</u>, <u>*operator*</u> | ([&lt;compositeRule&gt;](../compositerule/) | [&lt;rule&gt;](../rule/))+ | [&lt;ruleBase&gt;](../rulebase/) or [&lt;compositeRule&gt;](../compositerule/) |

### Attributes { data-search-exclude }

| Name | Value | Description |
| --- | --- | --- |
| *id* | It may receive any string value that begins with a letter or an underscore and that only contains letters, digits, <".">, and <"_">. | The *id* attribute uniquely identifies the element within a document. |
| *operator* | "and" or "or". | The *operator* attribute defines a logical expression among the child elements of the [&lt;compositeRule&gt;](../compositerule/) element. |
