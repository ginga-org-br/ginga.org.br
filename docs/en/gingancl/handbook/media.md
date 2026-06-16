---
title: "Element &lt;media&gt;"
---

### Definition and Usage { data-search-exclude }

The [&lt;media&gt;](media.md) element defines a media object containing: perceptual media
content; imperative code content; declarative code content; UTC content; or
global variables for the application. The object type is defined by the
*type* attribute or is inferred by the file extension used in the
*src* attribute.

Four special types are defined:

- The "application/x-ncl-NCL" (or "application/x-ginga-NCL") type is
    applied to [&lt;media&gt;](media.md) elements with NCL code content (note thus that
    an NCL application can embedded another NCL application).

- The "application/x-ncl-NCLua" (or "application/x-ginga-NCLua") type is
    applied to [&lt;media&gt;](media.md) elements with Lua imperative code content.

- The "application/x-ncl-settings" (or "application/x-ginga-settings") is
    applied to a special [&lt;media&gt;](media.md) element (there may be only one in an
    NCL document, but it may be reused as child element of other
    [&lt;context&gt;](context.md) elements) whose properties are global variables
    (properties defined by the document author or reserved environment
    properties managed by the system) that may be manipulated by the NCL
    document processor. The media object of "application/x-ncl-settings" type
    does not have content to be exhibited. Once an NCL application is
    started, the properties of this media object are available for rule
    evaluations defined by [&lt;rule&gt;](rule.md) elements. In order to use these
    properties in [&lt;link&gt;](link.md) element definitions, they must be explicitly
    declared.

- The application/x-ncl-time (or application/x-ginga-time) type shall be
    applied to a special [&lt;media&gt;](media.md) element (there may be only one in an
    NCL document, but it may be reused as child element of other
    [&lt;context&gt;](context.md) elements), whose content is the UTC. When it is started,
    the UTC content is not exhibited; however, it can be used to define
    content anchors by using [&lt;area&gt;](area.md) elements. Note that any continuous
    [&lt;media&gt;](media.md) element with no source specified can be used to define a
    clock relative to the [&lt;media&gt;](media.md) element start time.

#### Reuse of media objects { data-search-exclude }

Excepting [&lt;media&gt;](media.md) elements of "application/x-ncl-NCL" and
"application/x-ncl-NCLua" types, a [&lt;media&gt;](media.md) element may refer to another
[&lt;media&gt;](media.md) element of the same document or to an imported [&lt;media&gt;](media.md)
element. All attributes and child elements defined by the referred element
are inherited by the referring element, except the *focusIndex*
attribute. All attributes and child elements defined by the referring
element must be ignored by the NCL player, except the following attributes
and child elements:

- *id* attribute, which shall be defined.

- *instance* attribute, which may be defined, otherwise has "new" as
    its default string value;

- Child [&lt;area&gt;](area.md) elements may be added. If the new added [&lt;area&gt;](area.md)
    element has the same *id* attribute of an already existent
    [&lt;area&gt;](area.md) element (defined in the reused [&lt;media&gt;](media.md) element), the
    new added [&lt;area&gt;](area.md) is ignored by the NCL player.

- Child [&lt;property&gt;](property.md) elements may be added. If the new added
    [&lt;property&gt;](property.md) element has the same name attribute of an already
    existing [&lt;property&gt;](property.md) element (defined in the reused [&lt;media&gt;](media.md)
    element), the new added [&lt;property&gt;](property.md)is ignored by the NCL player.

The referred element and the element that refers to it shall be considered
the same, regarding its data specification. They shall also be considered
the same regarding their presentation, if the instance attribute receives
the "instSame" or "gradSame" values.

The following semantics must be respected when reusing a [&lt;media&gt;](media.md)
element. Assume the set of [&lt;media&gt;](media.md) elements composed of the referred
[&lt;media&gt;](media.md) element and all the referring [&lt;media&gt;](media.md) elements.

- If any element of the subset formed by the referred [&lt;media&gt;](media.md) element
    and all other [&lt;media&gt;](media.md) elements having the instance attribute equal
    to "instSame" or "gradSame" is scheduled to be presented, all other
    elements in this subset, which are not descendants of a [&lt;switch&gt;](switch.md)
    element, are also assumed as scheduled for presenting, and more than
    that, when they are being presented, they are represented by the same
    presentation instance. Descendant elements of a [&lt;switch&gt;](switch.md) element
    have the same behavior if the rules needed to present them are
    satisfied, otherwise they are not scheduled for presenting.
  - If the instance attribute is equal to "instSame", all scheduled nodes
      of the subset are immediately presented through a unique instance
      (start instruction applied on all of them) if a start instruction is
      applied in any of them.
  - If the instance attribute is equal to "gradSame", all scheduled nodes
      of the subset are presented through a unique instance, but now
      gradually, as soon as start instructions are applied on them, coming
      from a link, etc.
  - As each [&lt;media&gt;](media.md) element starts its presentation,the  common
      instance in presentation must notify the events associated with
      its [&lt;area&gt;](area.md) and [&lt;property&gt;](property.md) elements.

- The [&lt;media&gt;](media.md) elements in the set that have instance attribute values
    equal to "new" are not scheduled for presenting if any other element in
    the set is scheduled to be presented. When they are individually
    scheduled for presenting, no other element in the set is
    affected. Moreover, new independent presentation instances shall be
    created at each individual presentation starting.

### Syntax { data-search-exclude }

| Element | Attributes | Content | Parent |
| --- | --- | --- | --- |
| [&lt;media&gt;](media.md) | <u>*id*</u>, *src*, *type*, *refer*, *instance*, *descriptor* | ([&lt;area&gt;](area.md) &#124; [&lt;property&gt;](property.md))* | [&lt;body&gt;](body.md), [&lt;context&gt;](context.md) or [&lt;switch&gt;](switch.md) |

### Attributes { data-search-exclude }

| Name | Value | Description |
| --- | --- | --- |
| *id* | It may receive any string value that begins with a letter or an underscore and that only contains letters, digits, <".">, and <"_">. | The *id* attribute uniquely identifies the element within a document. |
| *src* | <p>The following are valid values:</p><ul><li class="level1"><div class="li"><"<nowiki>file:/*file_path/#fragment_identifier</nowiki>"> -- for local files,</div></li><li class="level1"><div class="li"><"<nowiki>http:*server_identifier/file_path/#fragment_identifier</nowiki>"> -- for remote files downloaded using the HTTP protocol,</div></li><li class="level1"><div class="li"><"<nowiki>https://server_identifier/file_path/#fragment_identifier</nowiki>"> -- for remote files downloaded using the HTTPS protocol,</div></li><li class="level1"><div class="li"><"<nowiki>rtsp://server_identifier/file_path/#fragment_identifier</nowiki>"> -- for streams downloaded using the RTSP protocol,</div></li><li class="level1"><div class="li"><"<nowiki>rtp://server_identifier/file_path/#fragment_identifier</nowiki>"> -- for streams downloaded using the RTP protocol,</div></li><li class="level1"><div class="li"><"<nowiki>ncl-mirror://media_element_identifier</nowiki>"> -- for a content flow identical to the one in presentation by another [&lt;media&gt;](media.md) element,</div></li><li class="level1"><div class="li"><"<nowiki>sbtvd-ts:</nowiki>"> or <"<nowiki>isdb-ts:</nowiki>"> or <"<nowiki>ts://program_number.component_tag</nowiki>"> -- for elementary streams received from the transport stream.</div></li></ul><p>For *src* attribute whose value identifies the <"sbtvd-ts">, <"isdb-ts">, or <"ts"> scheme, the "program_number.component_tag", can be substituted by the following reserved words:</p><ul><li class="level1"><div class="li">"video" -- corresponding to the primary video ES being presented on the video plan,</div></li><li class="level1"><div class="li">"audio" -- corresponding to the primary audio ES,</div></li><li class="level1"><div class="li">"text" -- corresponding to the primary text ES,</div></li><li class="level1"><div class="li">"video(i)" -- corresponding to the *i*-th smaller video ES "component_tag" listed in the PMT of the tuned services,</div></li><li class="level1"><div class="li">"audio(i)" -- corresponding to the *i*-th smaller audio ES "component_tag" listed in the PMT of the tuned services, or</div></li><li class="level1"><div class="li">"text(i)" -- corresponding to the *i*-th smaller text ES "component_tag" listed in the PMT of the tuned services.</div></li></ul> | The *src* attribute is the locator for the media object content. |
| *type* | <p>String.</p><p>It shall follow MIME Media Types format.  Four special types are defined: "application/x-ncl-NCL" (or "application/x-ginga-NCL"), "application/x-ncl-NCLua" (or "application/x-ginga-NCLua"), "application/x-ncl-settings" (or "application/x-ginga-settings"), and "application/x-ncl-time" (or "application/x-ginga-time").</p> | The *type* attribute shall follow MIME Media Types format (or, more simply, mimetypes). A mimetype is a string that defines the class of media (audio, video, image, text, application) and a media encoding type (such as jpeg, mpeg, etc.). Mimetypes may be registered or informal. Registered mimetypes are controlled by the IANA. Informal mimetypes are not registered with IANA, but are defined by common agreement; they usually have an "x-" before the media type name. |
| *refer* | IDREF or the string "alias#id" where "id" is an IDREF value. | <p>The *refer* attribute refers to a [&lt;media&gt;](media.md) element *id* that will be reused. An element that refers to another element cannot be reused; that is, its *id* cannot be the value of any *refer* attribute. The referred element must be a [&lt;media&gt;](media.md) element.</p><p>The referred element and the element that refers to it is considered the same regarding their data specification.</p><p>If the referred media object is defined within an imported document D, the refer attribute value must have the format "alias#id", where "alias" is the value of the alias attribute associated with the imported D document.</p> |
| *instance* | "new", "instSame", or "gradSame". | Specifies the reuse type.  The "new" value defines a new presentation instance but inheriting the specification of the referred [&lt;media&gt;](media.md) element.  The "instSame" value defines a same presentation instance that is immediately started as soon as the referred [&lt;media&gt;](media.md) element or any other [&lt;media&gt;](media.md) elements referring to it with instance attribute equal to "instSame" is started, or if a start instruction is applied on it.  The "gradSame" value defines a same presentation instance that is started as soon an start instruction is applied on it, coming from a link, etc. |
| *descriptor* | IDREF. | The *descriptor* attribute refers to a [&lt;descriptor&gt;](descriptor.md) element. |
