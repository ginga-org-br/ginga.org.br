---
title: "Element &lt;ncl&gt;"
---

# &lt;ncl&gt;

Explore the `<ncl>` example below:

<div class="ginga-playground-container">

<nav class="ginga-playground-tabs" role="tablist" aria-label="Ginga Playground examples">
  <button type="button" class="ginga-playground-tab" role="tab" aria-selected="true" data-playground-src="https://ginga.org.br/gingaf/playground/?app=https://raw.githubusercontent.com/ginga-org-br/gingaf/refs/heads/main/examples/ginga.org.br/ncl.ncl">ncl.ncl</button>
</nav>

<iframe
  class="ginga-playground"
  src="https://ginga.org.br/gingaf/playground/?app=https://raw.githubusercontent.com/ginga-org-br/gingaf/refs/heads/main/examples/ginga.org.br/ncl.ncl"
  loading="lazy"
  allow="autoplay; fullscreen">
</iframe>

</div>

The [&lt;ncl&gt;](ncl.md) tag represents the root of an NCL document.

The [&lt;ncl&gt;](ncl.md) tag is the container for all other NCL elements (except for
the `<?xml>` tag).

### Syntax { data-search-exclude }

| Element | Attributes | Content | Parent |
| --- | --- | --- | --- |
| [&lt;ncl&gt;](ncl.md) | <u>*id*</u>, *title*, *xmlns* | ([&lt;head&gt;](head.md)?, [&lt;body&gt;](body.md)?) | -- |

### Attributes { data-search-exclude }

| Name | Value | Description |
| --- | --- | --- |
| *id* | It may receive any string value that begins with a letter or an underscore and that only contains letters, digits, <".">, and <"_">. | The *id* attribute uniquely identifies the element within a document. |
| *title* | String. | The *title* attribute contains advisory information.  Values of the *title* attribute may be rendered by user agents in a variety of ways. |
| *xmlns* | "http://www.ncl.org.br/NCL3.0/EDTVProfile" or "http://www.ncl.org.br/NCL3.0/BDTVProfile" | The xmlns attribute declares an XML namespace---in other words, it declares the primary collection of XML-defined constructs the document uses. The attribute's value is the URL identifying where the namespace is officially defined. Two values are allowed for the *xmlns* attribute: "http://www.ncl.org.br/NCL3.0/EDTVProfile" and "http://www.ncl.org.br/NCL3.0/BDTVProfile", for the Enhanced and Basic DTV profiles, respectively. An NCL player shall know that the schemaLocation for these namespaces is, respectively: "http://www.ncl.org.br/NCL3.0/profiles/NCL30EDTV.xsd" and "http://www.ncl.org.br/NCL3.0/profiles/NCL30BDTV.xsd". |
