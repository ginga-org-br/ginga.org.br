---
title: "Element &lt;rule&gt;"
---

### Definition and Usage { data-search-exclude }

The [&lt;rule&gt;](rule.md) element defines simple rules for defining either alternative
components or alternative descriptors.

The *id* attribute is the rule identifier.  A rule is established by
comparing (*comparator* attribute) a variable (*var* attribute)
value with an absolute value.  The variable shall be a property of the
settings node ([&lt;media&gt;](media.md) element of application/x-ncl-settings type),
that is, the *var* attribute must have as its valuea property name of
the [&lt;media&gt;](media.md) element of "application/x-ncl-settings" type.

### Syntax { data-search-exclude }

| Element | Attributes | Content | Parent |
| --- | --- | --- | --- |
| [&lt;rule&gt;](rule.md) | *id*, <u>*var*</u>, <u>*comparator*</u>, <u>*value*</u> | -- | [&lt;ruleBase&gt;](rulebase.md) or [&lt;compositeRule&gt;](compositerule.md) |

### Attributes { data-search-exclude }

| Name | Value | Description |
| --- | --- | --- |
| *id* | It may receive any string value that begins with a letter or an underscore and that only contains letters, digits, <".">, and <"_">. | The *id* attribute uniquely identifies the element within a document. |
| *var* | It may receive any string value that begins with a letter or an underscore and that only contains letters, digits, <".">, and <"_">. | The *var* attribute uniquely identifies a property name of the settings node ([&lt;media&gt;](media.md) element of "application/x-ncl-settings" type). |
| *comparator* | "eq", "ne", "gt", "lt", "gte", or "lte". | The *comparator* attribute compares the value of the property specified by the *var* attribute with the absolute value specified in the *value* attribute. |
| *value* | String. | The *value* attribute defines a value to be compared with the property value referred by the *var* attribute. |
