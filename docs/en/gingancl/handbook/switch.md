---
title: "Element &lt;switch&gt;"
---

### Definition and Usage { data-search-exclude }

The [&lt;switch&gt;](../switch/) element allows for defining alternative objects
(represented by [&lt;media&gt;](../media/), [&lt;context&gt;](../context/) or other [&lt;switch&gt;](../switch/)
elements) to be presented.  The choice is madeduring presentation time.

Test rules used to choose the switch’schild component to be presented are
defined by [&lt;rule&gt;](../rule/) and [&lt;compositeRule&gt;](../compositerule/) elements; [&lt;bindRule&gt;](../bindrule/)
child elements associate these rules to child component objectsof the
[&lt;switch&gt;](../switch/) element.

A [&lt;switchPort&gt;](../switchport/) child element may define a mapping to a subset of the
switch’s child components.  When a link is bound to a [&lt;switchPort&gt;](../switchport/)
element,the rules bound to mapped components are evaluated in the order they
are defined.  The first rule evaluated as true determines the chosen object.
Ifall rules bound to mapped components are evaluated as false, a default
component, defined by the [&lt;defaultComponent&gt;](../defaultcomponent/)child element,is chosen; if
the [&lt;defaultComponent&gt;](../defaultcomponent/) element is not defined, no component is selected
for presentation and the NCL player behaves as if the selected component
does not exist.

All references to a switch’s child component are made through
[&lt;switchPort&gt;](../switchport/) elements or, by default, to the [&lt;switch&gt;](../switch/) element
without specifying any [&lt;switchPort&gt;](../switchport/).  In this case, it is considered as
if the reference is made to a default [&lt;switchPort&gt;](../switchport/) that contains
mapping elements to each child object of the switch and referring to its
whole content anchor.

From the moment a [&lt;switch&gt;](../switch/) is evaluated, it is considered resolved
until the end of the current switch presentation.

The [&lt;switch&gt;](../switch/) element may refer to another [&lt;switch&gt;](../switch/) element.  In
this case, it has the same specification of the referred element.

### Syntax { data-search-exclude }

| Element | Attributes | Content | Parent |
| --- | --- | --- | --- |
| [&lt;switch&gt;](../switch/) | <u>*id*</u>, *refer* | ([&lt;defaultComponent&gt;](../defaultcomponent/)?, ([&lt;switchPort&gt;](../switchport/) &#124; [&lt;bindRule&gt;](../bindrule/) &#124; [&lt;media&gt;](../media/) &#124; [&lt;context&gt;](../context/) &#124; [&lt;switch&gt;](../switch/))*) | [&lt;body&gt;](../body/), [&lt;context&gt;](../context/) or [&lt;switch&gt;](../switch/) |

### Attributes { data-search-exclude }

| Name | Value | Description |
| --- | --- | --- |
| *id* | It may receive any string value that begins with a letter or an underscore and that only contains letters, digits, <".">, and <"_">. | The *id* attribute uniquely identifies the element within a document. |
| *refer* | IDREF or the string "alias#id" where "id" is an IDREF value. | <p>The *refer* attribute refers to an element *id* that will be reused.  An element that refers to another element cannot be reused; that is, its *id* cannot be reused; that is, its *id* cannot be the value of any *refer* attribute.  The referred element shall be a [&lt;switch&gt;](../switch/) element.</p><p>The referred element and the element that refers to it shall be considered the same only regarding their data specification.</p><p>If the referred node is defined within an imported document D, the *refer* attribute value shall have the format "alias#id", where "alias" is the value of the *alias* attribute associated with the imported component D.</p> |
