---
title: "Element &lt;area&gt;"
---

### Definition and Usage { data-search-exclude }

The [&lt;area&gt;](area.md) element allows for defining a content anchor (a subset of
information units of a [&lt;media&gt;](media.md) element's content) that may be used in
relationships with other objects in an NCL application.

Content anchors may represent:

  * spatial portions of images: through the *coords* attribute;
  * temporal portions of continuous media content (audio, video, etc.):
    through the *begin* and *end* attributes, or based on the
    number of audio samples or video frames, through the *first* and
    *last* attributes, which indicate the initial and final
    sample/frame;
  * temporal and spatial portions of videos: through the *coords*,
    *begin*, and *end* attributes; or through the
    *coords*, *first*, and *last* attributes;
  * textual segments: through the *beginText*, *beginPosition*,
    *endText*, and *endPosition* attributes, that define the
    beginning and end strings, and their occurrence in the text
    respectively;
  * a string that is used by the media player to identify a content region
    (for example, a function or method in an imperative media object, an
    interface in a declarative media object, like an HTML anchor, a port in
    a media object with an NCL application as a content, etc.): through the
    *label* attribute;
  * a clip in the content of a declarative hypermedia object: using the
    *clip * attribute.

Every [&lt;media&gt;](media.md), [&lt;context&gt;](context.md), [&lt;body&gt;](body.md), and [&lt;switch&gt;](switch.md) element
has a content anchor with a region representing the whole content of the
node defined by default.  This anchor is called "whole content anchor".
Except for media objects with imperative code content (for example, those
whose MIME type is "application/x-ncl-NCLua"), every time an NCL component
is referred without specifying one of its anchors, the whole content anchor
is assumed.

### Syntax { data-search-exclude }

| Element | Attributes | Content | Parent |
| --- | --- | --- | --- |
| [&lt;area&gt;](area.md) | <u>*id*</u>, *coords*, *begin*, *end*, *beginText*, *endText*, *beginPosition*, *endPosition*, *first*, *last*, *label*, *clip* | -- | [&lt;media&gt;](media.md) |

### Attributes { data-search-exclude }

| Name | Value | Description |
| --- | --- | --- |
| *id* | It may receive any string value that begins with a letter or an underscore and that only contains letters, digits, <".">, and <"_">. | The *id* attribute uniquely identifies the element within a document. |
| *coords* | <p>A list of values of the form "left-x, top-y, right-x, bottom-y" where each value is either:</p><ol><li class="level1"><div class="li">a real number in the range \[0,100\] ending with the character <"%"> (e.g. "30%"), or</div></li><li class="level1"><div class="li">a positive integer specifying the value in pixels. For pixel values, the "px" unit qualifier may be omitted.</div></li></ol> | <p>The *coords* attribute specifies the position of a rectangular area on the screen.</p><p>Coordinates are relative to the top, left corner of the object content.</p><p>The values are separated by commas.</p><p>The order of values is "left-x", "top-y", "right-x", and "bottom-y".</p><p>When the "left-x" and "right-x" are expressed as a percentage, the value is relative to the width property of the media object.</p><p>When the "top-y" and "bottom-y" are expressed as a percentage, the value is relative to the height property of the media object.</p> |
| *begin* | <p>Except for the [&lt;media&gt;](media.md) element of the "application/x-ncl-time" type, the *begin* attribute shall be specified according with one of the following syntax:</p><ol><li class="level1"><div class="li"><"<nowiki>Hours:Minutes:Seconds.Fraction</nowiki>">, where "Hours" is an integer in the \[0,23\] interval, "Minutes" is an integer in the \[0,59\] interval, "Seconds" is an integer in the 0,59 interval, and "Fraction" is a positive integer,</div></li><li class="level1"><div class="li">Seconds<"s">, where "Seconds" is a positive real number.</div></li></ol><p>For the [&lt;media&gt;](media.md) element of the "application/x-ncl-time" type, the *begin* attribute shall be specified according with the following syntax: <"<nowiki>Year:Month:Day:Hours:Minutes:Seconds.Fraction</nowiki>">, according to the country time zone. The NCL user agent is responsible for translating the value for the country time zone to the one corresponding to the UTC.</p><p>If the *end* attribute is defined, but without an explicit definition for the *begin* attribute, the start of the whole media content presentation shall be considered as the anchor beginning.</p><p>In the case of a media element of the "application/x-ncl-time" type, the *begin* attribute must always be defined and it assumes an absolute UTC value.</p> | The *begin* attribute specifies the beginning of the temporal anchor. |
| *end* | Same as for *begin*. | The *end* attribute specifies the end of the temporal anchor. |
| *beginText* | <p>String.</p><p>If the beginning of the content anchor region is not defined, the beginning of the text content is assumed.</p> | The *beginText* and *beginPosition* attributes specifies the beginning of the text anchor. The *beginText* defines a string in the text. |
| *endText* | String. | The *endText* and *endPosition* attributes specifies the end of the text anchor. The *endText* defines a string in the text. |
| *beginPosition* | Positive integer.  The default value is 1. | The *beginText* and *beginPosition* attributes specifies the beginning of the text anchor. The *beginPosition* defines the occurrence of the string in the text. |
| *endPosition* | Positive integer.  The default value is the position of the last character in string. | The *endText* and the *endPosition* attributes specifies the end of the text anchor. The *endPosition* defines the occurrence of the string in the text. |
| *first* | <p>The *first* attribute shall be specified according with one of the following syntax:</p><ol><li class="level1"><div class="li">Samples<"s">, where Samples is a positive integer,</div></li><li class="level1"><div class="li">Frames<"f">, where Frames is a positive integer, or</div></li><li class="level1"><div class="li">NPT<"npt"> where NPT is the Normal Play Time value.</div></li></ol><p>If the *last* attribute is defined, but without an explicit definition for the *first* attribute, the start of the whole media content presentation shall be considered as the anchor beginning.</p> | -- |
| *last* | <p>The *last* attribute shall be specified according with one of the following syntax:</p><ol><li class="level1"><div class="li">Samples<"s">, where Samples is a positive integer,</div></li><li class="level1"><div class="li">Frames<"f">, where Frames is a positive integer, or</div></li><li class="level1"><div class="li">NPT<"npt"> where NPT is the Normal Play Time value.</div></li></ol><p>If the *first* attribute is defined, but the *last* attribute is not specified, the end of the whole media content presentation shall be assumed as the anchor ending.</p> | -- |
| *label* | String. | The *label* attribute identifies a content region, for example, a function in an imperative media object, or an interface in a declarative media object, like an HTML anchor, or a port in a media object with an NCL application as content, etc. |
| *clip* | <p>String.</p><p>The value depends on the declarative hypermedia object type. For NCL media objects, the clip value is a triple <"(chainId,beginOffset,endOffset)"> that is used by the NCL media player to identify an NCL application [&lt;port&gt;](port.md) through which a temporal chain begins, and the beginning and the end time in this temporal chain.</p><p>For [&lt;media&gt;](media.md) elements with NCL code content the following defaults are defined:</p><ol><li class="level1"><div class="li">"chainId" is the whole content anchor of the [&lt;body&gt;](body.md) element,</div></li><li class="level1"><div class="li">"beginOffset" is "0s", and</div></li><li class="level1"><div class="li">"endOffset" is the end time of the temporal chain.</div></li></ol> | The *clip* identifies a stream clip in the content of a declarative hypermedia object |
