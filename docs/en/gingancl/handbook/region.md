---
title: "Element &lt;region&gt;"
---

### Definition and Usage { data-search-exclude }

The [&lt;region&gt;](region.md) element defines the initial values for the left, right,
top, bottom, height, width, and zIndex properties of a [&lt;media&gt;](media.md) element
that indirectly refers to it by using a [&lt;descriptor&gt;](descriptor.md) element.

The position of a region, as specified by its *top*, *bottom*,
*left*, and *right* attributes, is always relative to the parent
geometry, which is defined by the parent [&lt;region&gt;](region.md) element, or the total
device area in the case of first nesting level regions.

The *top* and *left* attributes are the primary region
positioning attributes.  They place the left-top corner of the region in the
specified distance away from the left-top edge of the parent region (or the
device left-top edge in the case of the outermost region).  Sometimes,
explicitly setting the *bottom* and *right* attributes is
helpful.  Their values state the distance between the region's  right-bottom
corner and the right-bottom corner of the parent region (or the device
right-bottom edge in the case of the outermost region).

![](/assets/region.png)

Child regions cannot stay outside the area established by their parent
regions.

The *zIndex* attribute specifies the region superposition precedence,
where regions with greater *zIndex* values are stacked on top of
regions with smaller *zIndex* values.

### Syntax { data-search-exclude }

| Element | Attributes | Content | Parent |
| --- | --- | --- | --- |
| [&lt;region&gt;](region.md) | <u>*id*</u>, *title*, *left*, *right*, *top*, *bottom*, *height*, *width*, *zIndex* | ([&lt;region&gt;](region.md))* | [&lt;regionBase&gt;](regionbase.md) or [&lt;region&gt;](region.md) |

### Attributes { data-search-exclude }

| Name | Value | Description |
| --- | --- | --- |
| *id* | It may receive any string value that begins with a letter or an underscore and that only contains letters, digits, <".">, and <"_">. | The *id* attribute uniquely identifies the element within a document. |
| *title* | String. | The *title* attribute contains advisory information.  Values of the *title* attribute may be rendered by user agents in a variety of ways. |
| *left* | <p>A real number in the range \[0,100\] ending with the character <"%"> (e.g. "30%"), or a positive integer specifying the attribute value in pixels.  For pixel values, the "px" unit qualifier may be omitted.</p><p>The default value is "0%", if the attribute value cannot be computed from the *width* and *right* attributes.</p> | Left position of the content relative to its parent region (or the device in the case of the outermost region), expressed as a percentage of the parent region *width* dimension (or the device width in the case of the outermost region), or as an absolute value.It places the left position of the region in the specified distance away from the left edge of the parent region (or the device left edge in the case of the outermost region). |
| *right* | <p>A real number in the range \[0,100\] ending with the character <"%"> (e.g. "30%"), or a positive integer specifying the attribute value in pixels.  For pixel values, the "px" unit qualifier may be omitted.</p><p>The default value is "0%", if the attribute value cannot be computed from the *width* and *left* attributes.</p> | Right position of the content relative to its parent region (or the device in the case of the outermost region), expressed as a percentage of the parent region *width* dimension (or the device width in the case of the outermost region), or as an absolute value.It places the right position of the region in the specified distance away from the right edge of the parent region (or the device right edge in the case of the outermost region). |
| *top* | <p>A real number in the range \[0,100\] ending with the character <"%"> (e.g. "30%"), or a positive integer specifying the attribute value in pixels.  For pixel values, the "px" unit qualifier may be omitted.</p><p>The default value is "0%", if the attribute value cannot be computed from the *height* and *bottom* attributes.</p> | Top position of the content relative to its parent region (or the device in the case of the outermost region), expressed as a percentage of the parent region *height* dimension (or the device height in the case of the outermost region), or as an absolute value.It places the top position of the region in the specified distance away from the top edge of the parent region (or the device top edge in the case of the outermost region). |
| *bottom* | <p>A real number in the range \[0,100\] ending with the character <"%"> (e.g. "30%"), or a positive integer specifying the attribute value in pixels.  For pixel values, the "px" unit qualifier may be omitted.</p><p>The default value is "0%", if the attribute value cannot be computed from the *height* and *top* attributes.</p> | Bottom position of the content relative to its parent region (or the device in the case of the outermost region), expressed as a percentage of the parent region *height* dimension (or the device height in the case of the outermost region), or as an absolute value.It places the bottom position of the region in the specified distance away from the bottom edge of the parent region (or the device bottom edge in the case of the outermost region). |
| *height* | <p>A real number in the range \[0,100\] ending with the character <"%"> (e.g. "30%"), or a positive integer specifying the attribute value in pixels.  For pixel values, the "px" unit qualifier may be omitted.</p><p>The default value is "100%" of the parent region *height* dimension (or the device height in the case of the outermost region).</p> | Height of the content to be exhibited, expressed as a percentage of the parent region *height* dimension (or the device height in the case of the outermost region), or as an absolute value. |
| *width* | <p>A real number in the range \[0,100\] ending with the character <"%"> (e.g. "30%"), or a positive integer specifying the attribute value in pixels.  For pixel values, the "px" unit qualifier may be omitted.</p><p>The default value is "100%" of the parent region *width* dimension (or the device width in the case of the outermost region).</p> | Width of the content to be exhibited, expressed as a percentage of the parent region *width* dimension (or the device width in the case of the outermost region), or as an absolute value. |
| *zIndex* | <p>An integer number in the range \[0,255\].</p><p>The default value is 0.</p> | The *zIndex* attribute specifies the superposition precedence, where objects with greater *zIndex* values are stacked on top of objects with smaller *zIndex* values. |
