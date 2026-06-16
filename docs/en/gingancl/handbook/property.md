---
title: "Element &lt;property&gt;"
---

### Definition and Usage { data-search-exclude }

The [&lt;property&gt;](property.md) element defines a property or a group of properties for
its parent [&lt;media&gt;](media.md), [&lt;context&gt;](context.md), [&lt;body&gt;](body.md), or [&lt;switch&gt;](switch.md)
elements. These properties may be used in relationships with other objects
of an NCL application, if the externable attribute of the [&lt;property&gt;](property.md)
element has "true" as its value.

The [&lt;property&gt;](property.md) element defines the name attribute, which indicates the
name of the property or property group, and the value attribute.  The parent
element may not have more than one [&lt;property&gt;](property.md) element with the same
name attribute value.

The *value* attribute is optional and defines an initial value for the
property declared in the *name* attribute. When the value is not
specified, the property is initialized with the value defined in homonym
attributes of the [&lt;descriptor&gt;](descriptor.md) or [&lt;region&gt;](region.md) elements associated
with the parent element that defines the [&lt;property&gt;](property.md), or else with a
default value (that depends on the value of the name attribute). When the
value is specified in the [&lt;property&gt;](property.md) element, it has precedence over
the value defined in homonym attributes of the [&lt;descriptor&gt;](descriptor.md) or
[&lt;region&gt;](region.md) elements associated with the parent element that defines the
[&lt;property&gt;](property.md).

### Syntax { data-search-exclude }

| Element | Attributes | Content | Parent |
| --- | --- | --- | --- |
| [&lt;property&gt;](property.md) | *name*, *value*, *externable* | -- | [&lt;media&gt;](media.md) or [&lt;context&gt;](context.md) or [&lt;body&gt;](body.md) |

### Attributes { data-search-exclude }

| Name | Value | Description |
| --- | --- | --- |
| *name* | It may receive any string value that begins with a letter or an underscore and that only contains letters, digits, "." and "_". | The *name* attribute uniquely identifies the property within its parent element. |
| *value* | Depends on the name value. | The *value* attribute defines an initial value for the *name* attribute. |
| *externable* | "false" or "true".  The default value is: "true" if the property is defined in a [&lt;property&gt;](property.md) element, or "false" if the property is defined in a [&lt;descriptor&gt;](descriptor.md) element. | The *externable* attribute determines if a property can (externable="true") or cannot (externable="false") be used in relationships. |

### Predefined Properties { data-search-exclude }

Several reserved words are used to specify properties with pre-defined
semantic known by NCL players. These properties, their semantic, their
possible values and their default values are presented below.

#### Predefined properties for all &lt;media&gt; elements { data-search-exclude }

| Name | Value | Description |
| --- | --- | --- |
| style | URI. | The locator of a stylesheet file that specifies other properties for the  object. |
| player | String. | <p>Identifies the presentation tool to be used.</p>  <p>If not specified, the player is determined by the object type, defined  by the *type* attribute of the [&lt;media&gt;](media.md) element, or inferred by  the file extension of the *src* attribute value of the [&lt;media&gt;](media.md)  element.</p> |
| reusePlayer | <p>"true" or "false".</p><p>The default value is "false".</p> | Specifies if a new player must be instantiated ("false") or if a player  already instantiated must be used ("true"). |
| playerLife | <p>"close" or "keep".</p>  <p>The default value is "close.</p> | Specifies what will happen to the player instance at the end of the  object presentation. |
| deviceClass | <p>"systemScreen(i)" or "systemAudio(i)", where *i* is a  non-negative integer.</p><p>The default value is the same device class  that runs the NCL player.</p> | <p>Specifies the device class where the media object will be  presented.</p>   <p>There are two different types of device classes: active and  passive. In an active class, a device is able to run some media players  for [&lt;media&gt;](media.md) element presentations. In a passive class, a device is  not required to run media players, only to exhibit a bit map or a sequence  of audio samples received from another device.</p>   <p>The "systemScreen(1)" and "systemAudio(1)" are reserved to passive  classes, and "systemScreen(2)" and "systemAudio(2)" are reserved to active  classes.</p> |
| explicitDur | <p>The "explicitDur" property is specified according with one of the  following syntax:</p>   <ol>  <li class="level1"><div class="li">"Hours:Minutes:Seconds.Fraction", where "Hours" is an integer in the  \[0,23\] interval, "Minutes" is an integer in the \[0,59\] interval,  "Seconds" is an integer in the \[0,59\] interval, and "Fraction" is a  positive integer.</div></li>  <li class="level1"><div class="li">Seconds"s", where Seconds is a positive real number.</div></li>  </ol>   <p>For continuous media, the default value is set to the duration of the  content, otherwise, it must be set to nil.</p> | Gives the duration of an object. |
| focusIndex | <p>Positive integer.</p>  <p>When this property is not defined, the object is considered as if no  focus could be set to it.</p> | <p>Specifies an index for the [&lt;media&gt;](media.md) element to which the focus  may be applied.</p>   <p>Note: When an element on focus is selected by pressing the "activate  (select or enter) key", the focus control shall be passed to the  [&lt;media&gt;](media.md) element renderer (player). The player may then follow its own  rules for navigation. The focus control shall be passed back to the NCL  Player when the "back key" is pressed. In this case, the focus goes to the  element identified by the the "service.currentFocus" property of the  settings node ([&lt;media&gt;](media.md) element of "application/x-ncl-settings"  type).</p> |
| moveLeft | Positive integer. | Specifies a value equal to the *focusIndex* value associated to the  element to which the focus should be applied when the "left arrow key" is  pressed. When the focus is applied to an element with the visible property  set to false, or to an element that it is not being presented, the current  focus does not move. |
| moveRight | Positive integer. | Specifies a value equal to the *focusIndex* value associated to the  element to which the focus should be applied when the "right arrow key" is  pressed. When the focus is applied to an element with the visible property  set to false, or to an element that it is not being presented, the current  focus does not move. |
| moveUp | Positive integer. | Specifies a value equal to the *focusIndex* value associated to the  element to which the focus should be applied when the "up arrow key" is  pressed. When the focus is applied to an element with the visible property  set to false, or to an element that it is not being presented, the current  focus does not move. |
| moveDown | Positive integer. | Specifies a value equal to the *focusIndex* value associated to an  element to which the focus should be applied when the "down arrow key" is  pressed. When the focus is applied to an element with the visible property  set to false, or to an element that it is not being presented, the current  focus does not move. |

#### Predefined properties for &lt;media&gt; elements with visual content { data-search-exclude }

| Name | Value | Description |
| --- | --- | --- |
| top | <p>A real number in the range \[0,100\] ending with the character <"%">  (e.g. 30%), or an integer non-negative value specifying the attribute in  pixels. For pixel values, the "px" unit qualifier may be omitted.</p>   <p>The default value is "0%", if the *bottom* value is not  specified.</p> | Top position of the content, expressed as a percentage of the exhibition  device height dimension, or as an absolute value. It places the top  position of the content to be exhibited in the specified distance away  from the top edge of the exhibition device. |
| bottom | <p>If the "top" and "height" values are specified, it must be computed  based on these values. Otherwise, it must be a real number in the range  \[0,100\] ending with the character <"%"> (e.g. 30%), or an integer  non-negative value specifying the attribute in pixels. For pixel values,  the "px" unit qualifier may be omitted.</p>   <p>The default value is "0%", if the attribute value cannot be computed  from the *height* and *top* attributes.</p> | Bottom position of the content, expressed as a percentage of the  exhibition device height dimension, or as an absolute value. It places the  bottom position of the content to be exhibited in the specified distance  away from the bottom edge of the exhibition device. |
| left | <p>A real number in the range \[0,100\] ending with the character <"%">  (e.g. 30%), or an integer non-negative value specifying the attribute in  pixels. For pixel values, the "px" unit qualifier may be omitted.</p>   <p>The default value is "0%", if the *right* value is not  specified.</p> | Left position of the content, expressed as a percentage of the exhibition  device width dimension, or as an absolute value. It places the left  position of the content to be exhibited in the specified distance away  from the left edge of the exhibition device. |
| right | <p>If the left and width values are specified, it must be computed based  on these values. Otherwise, it must be a real number in the range  \[0,100\] ending with the character <"%"> (e.g. 30%), or an integer  non-negative value specifying the attribute in pixels. For pixel values,  the "px" unit qualifier may be omitted.</p>   <p>The default value is "0%", if the attribute value cannot be computed  from the *width* and *left* attributes.</p> | Right position of the content, expressed as a percentage of the  exhibition device width dimension, or as an absolute value. It places the  right position of the content to be exhibited in the specified distance  away from the right edge of the exhibition device. |
| width | <p>A real number in the range \[0,100\] ending with the character <"%">  (e.g. 30%), or an integer non-negative value specifying the attribute in  pixels. For pixel values, the "px" unit qualifier may be omitted.</p>   <p>The default value is "0%".</p> | Width of the content to be exhibited, expressed as a percentage of the  exhibition device width dimension, or as an absolute value. |
| height | <p>A real number in the range \[0,100\] ending with the character <"%">  (e.g. 30%), or an integer non-negative value specifying the attribute in  pixels. For pixel values, the "px" unit qualifier may be omitted.</p>   <p>The default value is "0%".</p> | Height of the content to be exhibited, expressed as a percentage of the  exhibition device height dimension, or as an absolute value. |
| location | See "left" and "top" properties. | Two numbers separated by comma, each one following the rule specified for  "left" and "top" properties, respectively. |
| size | See "width" and "height" properties. | Two numbers separated by comma, each one following the rule specified for  "width" and "height" properties, respectively. |
| bounds | See "left", "top", "width", and "height" properties. | Four numbers separated by comma, each one following the rule specified  for "left", "top", "width", and "height" properties, respectively. |
| background | <p>"white", "black", "silver", "gray", "red", "maroon", fuchsia",  "purple", "lime", "green", "yellow", "olive", "blue", "navy", "aqua", or  "teal". It may also be the reserved value "transparent".</p>   <p>The default value is "transparent".</p> | The background color used to fill the area of a region for displaying the  media content that is not filled by the content itself. |
| rgbChromakey | <p>RGB color defined using a hexadecimal (hex) notation for the  combination of Red, Green, and Blue color values (RGB). The lowest value  that can be given to one of the light sources is 0 (hex 00). The highest  value is 255 (hex FF).</p>   <p>It may also be defined by the reserved words: "white", "black",  "silver", "gray", "red", "maroon", fuchsia", "purple", "lime", "green",  "yellow", "olive", "blue", "navy", "aqua", or "teal".</p> | The RGB color to be set as transparent. |
| visible | <p>"true" or "false".</p><p>The default value is "false".</p> | <p>Allows the object presentation to be seen or hidden.</p>   <p>When the visible property associated with a [&lt;context&gt;](context.md) or  [&lt;body&gt;](body.md) element is equal to "true", the visible property of each child  element of the composition is taken into account to define how each of  these child element will be exhibited.</p>   <p>When the visible property associated with a [&lt;context&gt;](context.md) or  [&lt;body&gt;](body.md) element is equal to "false", all child elements of the  composition are exhibited as hidden.</p>   <p>It should be remarked that an object  with a visible property equal to "false", that is, an object exhibited as  hidden, may not have any of its content anchors selected while the visible  property value persists as "false".</p>   <p>When a document has its [&lt;body&gt;](body.md)  element with its visible property set to "false" and its presentation  event is in the paused state, the document is said to be in stand-by. In  ISDB-T standard, when there is only one application in execution and this  application is in stand-by, the service's main video is dimensioned to  100% of the screen, and the main audio is set to 100% of its volume.</p> |
| transparency | <p>A real number in the range \[0,1\] or a real number in the range  \[0,100\] ending with the character <"%"> (e.g. "30%").</p>   <p>The default value is "0%".</p> | Indicates the degree of transparency of an object presentation: "1" or  "100%" means full transparency and "0" or "0%" means opaque. |
| fit | <p>"fill", "hidden", "meet", "meetBest", or "slice".</p>  <p>The default value is "fill".</p> | <p>Indicates how an object will be presented.</p>   <p>"fill": scale the object's media content so that it touches all edges  of the box defined by the object's "width" and "height" properties.</p>   <p>"hidden": if the intrinsic "height" ("width") of the media content is  smaller than the "height" ("width") property, the object must be rendered  starting from the "top" ("left") edge and have the remaining "height"  ("width") filled up with the background color; if the intrinsic "height"  ("width") of the media content is greater than the "height" ("width")  property, the object must be rendered starting from the top (left) edge  until the height (width) defined in the property is reached; the part of  the media content below (to right of) the height (width) is clipped.</p>   <p>"meet": scale the visual media object while preserving its aspect  ratio until its height or width is equal to the value specified by the  "height" or "width" properties. The media content left-top corner is  positioned at the top-left coordinates of the box; the empty space at the  right or the bottom must be filled up with the background color.</p>   <p>"meetBest": the semantic is identical to "meet", except that the  image is not scaled greater than 100% in either dimension. "slice": scale  the visual media content while preserving its aspect ratio until its  height or width are equal to the value specified in the "height" and  "width" properties and the defined presentation box is completely  filled. Some parts of the content may get clipped. Overflow width is  clipped from the right of the media object. Overflow height is clipped  from the bottom of the media object.</p> |
| scroll | <p>"none", "horizontal", "vertical", "both", or "automatic".</p>  <p>The default value is 0.</p> | Allows for the specification of how the scroll is configured in an  exhibition region. |
| zIndex | <p>An integer number in the range \[0,255\].</p>  <p>The default value is 0.</p> | The *zIndex* attribute specifies the superposition precedence,  where objects with greater *zIndex* values are stacked on top of  objects with smaller *zIndex* values. |
| plan | <p>"video", "graphic", or "background".</p>   <p>The default is "video" for media with *src* attribute referring  to a PES of a transport stream, or "graphic" for all other cases.</p> | Defines in which plan of a structured screen an object will be placed. |
| focusBorderColor | <p>"white", "black", "silver", "gray", "red", "maroon", fuchsia",  "purple", "lime", "green", "yellow", "olive", "blue", "navy", "aqua", or  "teal".</p>   <p>The default value is defined by the "default.focusBorderColor"  property of the *settings* object.</p> | Defines the color to decorate the screen region where the object on focus  is being presented, before it is selected. |
| selBorderColor | <p>"white", "black", "silver", "gray",""red", "maroon", fuchsia",  "purple", "lime", "green", "yellow", "olive", "blue", "navy", "aqua", or  "teal".</p>   <p>The default value is defined by the "default.selBorderColor" property  of the *settings* object.</p> | Defines the color to decorate the screen region where the object on focus  is being presented, after it is selected. |
| focusBorderWidth | <p>Integer.</p>  <p>The default value is defined by the "default.focusBorderWidth"  property of the *settings* object.</p> | Width (in pixels) applied to the border of an element in focus (0 means  that no border will appear, positive values means that the border is  outside the object content, and negative values means that the border is  drawn over the object content). |
| focusBorderTransparency | <p>A real value between 0 and 1, or a real value in the range \[0,100\]  ending with the character <"%"> (e.g. "30%").</p>   <p>The default value is defined by the "default.focusBorderTransparency"  property of the *settings* object.</p> | Transparency applied to the border of an element in focus, with "1" or  "100%" meaning full transparency and "0" or "0%" meaning no  transparency. |
| focusSrc | <p>The following are valid  values:</p><ul><li class="level1"><div class="li"><"<nowiki>file:/*file_path/#fragment_identifier</nowiki>">  -- for local  files,</div></li><li class="level1"><div class="li"><"<nowiki>http:*server_identifier/file_path/#fragment_identifier</nowiki>">  -- for remote files downloaded using the HTTP  protocol,</div></li><li class="level1"><div class="li"><"<nowiki>https://server_identifier/file_path/#fragment_identifier</nowiki>">  -- for remote files downloaded using the HTTPS  protocol,</div></li><li class="level1"><div class="li"><"<nowiki>rtsp://server_identifier/file_path/#fragment_identifier</nowiki>">  -- for streams downloaded using the RTSP  protocol,</div></li><li class="level1"><div class="li"><"<nowiki>rtp://server_identifier/file_path/#fragment_identifier</nowiki>">  -- for streams downloaded using the RTP  protocol,</div></li><li class="level1"><div class="li"><"<nowiki>ncl-mirror://media_element_identifier</nowiki>"> -- for  a content flow identical to the one in presentation by another  [&lt;media&gt;](media.md) element,</div></li><li class="level1"><div class="li"><"<nowiki>sbtvd-ts:</nowiki>"> or <"<nowiki>isdb-ts:</nowiki>">  or <"<nowiki>ts://program_number.component_tag</nowiki>"> -- for elementary streams  received from the transport stream.</div></li></ul><p>For *focusSrc*  attribute whose value identifies the <"sbtvd-ts">, <"isdb-ts">, or <"ts">  scheme, the "program_number.component_tag", can be substituted by the  following reserved words:</p><ul><li class="level1"><div class="li">"video" -- corresponding  to the primary video ES being presented on the video plan,</div></li><li class="level1"><div class="li">"audio"  -- corresponding to the primary audio ES,</div></li><li class="level1"><div class="li">"text" -- corresponding  to the primary text ES,</div></li><li class="level1"><div class="li">"video(i)" -- corresponding to the  *i*-th smaller video ES "component_tag" listed in the PMT of the  tuned services,</div></li><li class="level1"><div class="li">"audio(i)" -- corresponding to the *i*-th  smaller audio ES "component_tag" listed in the PMT of the tuned services,  or</div></li><li class="level1"><div class="li">"text(i)" -- corresponding to the *i*-th smaller text ES  "component_tag" listed in the PMT of the tuned services.</div></li></ul> | Specifies an alternative media source to be presented, instead of the  current presentation, if an element receives the focus. This attribute  follows the same rules of the *src* attribute of the [&lt;media&gt;](media.md)  element. |
| focusSelSrc | Same as for *focusSrc*. | Specifies an alternative media source to be presented, instead of the  current presentation, when an element on focus is selected by pressing the  activation (select or enter) key. This attribute follows the same rules of  the *src* attribute of the [&lt;media&gt;](media.md) element. |
| freeze | "true" or "false". The default value is "false". | Defines what will happen with an object at the end of its presentation,  if the end content is frozen ("true") or not ("false"). Defaults to  "false" |
| transIn, transOut | <p>List of (type, subtype, dur, startProgress, endProgress, direction,  fadeColor, horzRepeat, vertRepeat, borderWidth, borderColor) separated by  semicolons where:</p>  <ul>  <li class="level1"><div class="li"> Required *type* can be: "barWipe", "irisWipe", "clockWipe",  "snakeWipe", or "fade". For the complete list of the predefined  transition types see:  http://www.w3.org/TR/SMIL2/smil-transitions.html#TransitionEffects-Appendix.</div></li>  <li class="level1"><div class="li">Required *subtype* values depend on the *type* values,  as defined: "leftToRight" for "barWipe", "rectangle" for "irisWipe",  "clockwiseTwelve" for "clockWipe", "topLeftHorizontal" for "snakeWipe",  and "crossfade" for "fade". For the complete list of the predefined  transition subtypes see:  http://www.w3.org/TR/SMIL2/smil-transitions.html#TransitionEffects-Appendix.</div></li>  <li class="level1"><div class="li">*dur* attribute is specified according with one of the  following syntax: (i) "Hours:Minutes:Seconds.Fraction", where "Hours" is  an integer in the \[0,23\] interval, "Minutes" is an integer in the  \[0,59\] interval, "Minutes" is an integer in the \[0,59\] interval, and  "Fraction" is a positive integer; (ii) Seconds<"s">, where "Seconds" is a  positive real number. The default value is "0s".</div></li>  <li class="level1"><div class="li">*startProgress* and *endProgress* are real number in the  range \[0,1\].</div></li>  <li class="level1"><div class="li">*direction* values are "forward" and "reverse".</div></li>  <li class="level1"><div class="li">*fadeColor* is "white", "black", "silver", "gray", "red",  "maroon", fuchsia", "purple", "lime", "green", "yellow", "olive", "blue",  "navy", "aqua", or "teal".</div></li>  <li class="level1"><div class="li">*horzRepeat* and *vertRepeat* is a positive integer.</div></li>  <li class="level1"><div class="li">*borderWidth* is a non-negative integer.</div></li>  <li class="level1"><div class="li">*borderColor* is "white", "black", "silver", "gray", "red",  "maroon", fuchsia", "purple", "lime", "green", "yellow", "olive", "blue",  "navy", "aqua", or "teal".</div></li>  </ul>   <p>The default value for the property is the empty string. If a  transition type is specified then:</p>  <ul>  <li class="level1"><div class="li">"dur" default duration is "1s",</div></li>  <li class="level1"><div class="li">"startProgress" default value is 0,</div></li>  <li class="level1"><div class="li">"endProgress" default value is 1,</div></li>  <li class="level1"><div class="li">"direction" default value is "forward",</div></li>  <li class="level1"><div class="li">"fadeColor" default value is "black",</div></li>  <li class="level1"><div class="li">"horzRepeat" default value is 1,</div></li>  <li class="level1"><div class="li">"vertRepeat" default value is 1,</div></li>  <li class="level1"><div class="li">"borderWidth" default value is 0,</div></li>  <li class="level1"><div class="li">"borderColor" default value is "black".</div></li>  </ul> | <p>The value of the *transIn* and *transOut* is a  semicolon-separated list of transitions.</p>   <p>The purpose of the semicolon-separated list is to allow authors to  specify a set of fallback transitions if the preferred transition is not  available. The first transition in the list should be performed if the  user-agent has implemented this transition. If this transition is not  available, then the second transition in the list should be performed, and  so on.</p>   <p>The *type* and *subtype* define the transition. The  *dur* attribute specifies the duration of the transition.</p>   <p>The *startProgress* attribute specifies the amount of progress  through the transition at which to begin execution. For instance, we can  want to begin a crossfade with the destination image being already 30%  faded in. For this case, *startProgress* would be 0.3.</p>   <p>The *endProgress* attribute specifies the amount of progress  through the transition at which to end execution. The value of this  attribute must be greater than or equal to the value of the  *startProgress* attribute. If *endProgress* is equal to  *startProgress*, then the transition remains at a fixed progress for  the duration of the transition.</p>   <p>The *direction* attribute specifies the direction the  transition will run. Note that not all transitions will have meaningful  reverse interpretations. For instance, a crossfade is not a geometric  transition, and therefore has no interpretation of reverse  direction. Transitions that do not have a reverse interpretation should  have the direction attribute ignored and the default value of "forward"  assumed.</p>   <p>If the value of the *type* attribute is "fade" and the value of  the subtype attribute is "fadeToColor" or "fadeFromColor", then the  *fadeColor* attribute specifies the ending or starting color of the  fade. If the value of the *type* attribute is not "fade", or the  value of the *subtype* attribute is not "fadeToColor" or  "fadeFromColor", then the *fadeColor* attribute is ignored.</p>   <p>If the value of the *type* attribute is not "fade", then the  following attributes can be specified:</p>   <p>The *horzRepeat* attribute specifies how many times to perform  the transition pattern along the horizontal axis.</p>   <p>The *vertRepeat* attribute specifies how many times to perform  the transition pattern along the vertical axis.</p>   <p>The *borderWidth* attribute specifies the width of a generated  border along a wipe edge.</p>   <p>The *borderColor* attribute specifies the  content of the generated border along a wipe edge. If the value of this  attribute is a color, then the generated border along the wipe or warp  edge is filled with this color. If the value of this attribute is "blend",  then the generated border along the wipe blend is an additive blend (or  blur) of the media sources.</p> |

#### Predefined properties for &lt;media&gt; elements  with continuous-media content (read-only) { data-search-exclude }

| Name | Value | Description |
| --- | --- | --- |
| contentId | <p>String.</p><p>(Set only by the NCL player.)</p>  <p>The default value is nil.</p> | The "contentId" property is associated to continuous-media objects whose  content is defined referring to an elementary stream. It has *null*  as its initial value and it is set to the identifier value transported in  the NPT reference descriptor (in a field of the same name: contentId), as  soon as the associated continuous-media object is started. |
| standby | <p>"true" or "false".</p>  <p>(Set only by the NCL player.)</p>  <p>The default value is "false".</p> | The "standby" property is set to "true" while an already started  continuous-media object content referring to an elementary stream is  temporarily interrupted by another interleaved content, in the same  elementary stream. |

#### Predefined properties for &lt;media&gt;  elements with audible contents { data-search-exclude }

| Name | Value | Description |
| --- | --- | --- |
| soundLevel | A real number in the range \[0,1\] or a real number in the range  \[0,100\] ending with the character <"%"> (e.g. "30%").  <p>The default value is 1.</p> | Audio volume relative to the recorded audio. |
| balanceLevel | A real number in the range \[-1,1\] or a real number in the range  \[-100,100\] ending with the character <"%"> (e.g. "30%").  <p>The default value is 0.</p> | Balance level of the audio (-1 to the left and +1 to the  right). |
| trebleLevel | A real number in the range \[0,1\] or a real number in the range  \[0,100\] ending with the character <"%"> (e.g. "30%").  <p>The default value is 1.</p> | Treble setting, relative to the recorded audio. |
| bassLevel | A real number in the range \[0,1\] or a real number in the range  \[0,100\] ending with the character <"%"> (e.g. "30%").  <p>The default value is 1.</p> | Bass setting, relative to the recorded audio. |
| freeze | <p>"true" or "false".</p><p>The default value is "false".</p> | This property defines what will happen with an object at the end of its  presentation, if the end content is frozen ("true") or not ("false"). |
| transIn, transOut | A list of the form <"(type,subtype,dur,startProgress,endProgress)">  where:  <ul>  <li class="level1"><div class="li">"type" is "fade" by default,</div></li>  <li class="level1"><div class="li">"subtype" is "fade" by default,</div></li>  <li class="level1"><div class="li">The "explicitDur" property is specified according with one of the  following syntax:</div></li>  <ol>  <li class="level1"><div class="li">"Hours:Minutes:Seconds.Fraction", where "Hours" is an integer in the  \[0,23\] interval, "Minutes" is an integer in the \[0,59\] interval,  "Seconds" is an integer in the \[0,59\] interval, and "Fraction" is a  positive integer.</div></li>  <li class="level1"><div class="li">Seconds"s", where Seconds is a positive real number.</div></li>  </ol>  <li class="level1"><div class="li">"startProgress" is a real number in the range \[0,1\], and  "endProgress" is a real number in the range \[0,1\].</div></li>  </ul>   <p>The default value for the property is the empty string. If a  transition is specified then:</p>  <ul>  <li class="level1"><div class="li">"dur" default duration is "1s",</div></li>  <li class="level1"><div class="li">"startProgress" default value is 0,</div></li>  <li class="level1"><div class="li"> "endProgress" default value is 1.</div></li>  </ul> | <p>The type of the *transIn* and *transOut* is always  "fade" and the *subtype* is always "fade" and is defined by  default.</p>   <p>The *dur* attribute specifies the duration of the transition.</p>   <p>The *startProgress* attribute specifies the amount of progress  through the transition at which to begin execution.</p>   <p>The *endProgress* attribute specifies the amount of progress  through the transition at which to end execution. The value of this  attribute must be greater than or equal to the value of the  *startProgress* attribute. If *endProgress* is equal to  *startProgress*, then the transition remains at a fixed progress for  the duration of the transition.</p> |

#### Predefined properties for &lt;media&gt;  elements with textual contents { data-search-exclude }

| Name | Value | Description |
| --- | --- | --- |
| fontColor | <p>"white", "black", "silver", "gray", red", "maroon", "fuchsia",  "purple", "lime", "green", "yellow", "olive", "blue", "navy", "aqua", or  "teal".</p>  <p>The default value is "white".</p> | Defines the font color. |
| fontFamily | <p>A prioritized list of font family names and/or generic family  names.</p>   <p>There are two types of font family names:</p>  <ul>  <li class="level1"><div class="li">"family-name" the name of a font family of choice, or</div></li>  <li class="level1"><div class="li">"generic-family"; the following generic families are defined:  "serif", "sans-serif", "cursive", "fantasy", or "monospace".</div></li>  </ul>   <p>The default value of this property is system-dependent.</p> | The list values are separated by a comma to indicate that  they are alternatives. |
| textAlign | <p>"left", "right", "center", or "justify".</p>  <p>The default value is "left".</p> | This property describes how text content is aligned. |
| fontStyle | <p>"normal" or "italic".</p><p>The default value is "normal".</p> | Defines the font style. |
| fontSize | <p>Positive integer ending with the character "px" or "pt", for  relative font size expressed in pixels, or absolute font size expressed in  points, respectively.</p>  <p>The default value of this property is system-dependent.</p> | Sets the font-size to a fixed size in pixel or in points. |
| fontVariant | <p>"small-caps" or "normal".</p><p>The default value is "normal".</p> | Defines a variation type within a font family. |
| fontWeight | <p>"normal" or "bold".</p><p>The default value is "normal".</p> | This property selects the weight of the font. |
| freeze | <p>"true" or "false".</p><p>The default value is "false".</p> | This property defines what will happen with an object at the end of its  presentation, if the end content is frozen ("true") or not ("false"). |
| transIn, transOut | <p>List of (type, subtype, dur, startProgress, endProgress, direction,  fadeColor, horzRepeat, vertRepeat, borderWidth, borderColor) separated by  semicolons where:</p>  <ul>  <li class="level1"><div class="li"> Required *type* can be: "barWipe", "irisWipe", "clockWipe",  "snakeWipe", or "fade". For the complete list of the predefined  transition types see:  http://www.w3.org/TR/SMIL2/smil-transitions.html#TransitionEffects-Appendix.</div></li>  <li class="level1"><div class="li">Required *subtype* values depend on the *type* values,  as defined: "leftToRight" for "barWipe", "rectangle" for "irisWipe",  "clockwiseTwelve" for "clockWipe", "topLeftHorizontal" for "snakeWipe",  and "crossfade" for "fade". For the complete list of the predefined  transition subtypes see:  http://www.w3.org/TR/SMIL2/smil-transitions.html#TransitionEffects-Appendix.</div></li>  <li class="level1"><div class="li">*dur* attribute is specified according with one of the  following syntax: (i) "Hours:Minutes:Seconds.Fraction", where "Hours" is  an integer in the \[0,23\] interval, "Minutes" is an integer in the  \[0,59\] interval, "Minutes" is an integer in the \[0,59\] interval, and  "Fraction" is a positive integer; (ii) Seconds<"s">, where "Seconds" is a  positive real number. The default value is "0s".</div></li>  <li class="level1"><div class="li">*startProgress* and *endProgress* are real number in the  range \[0,1\].</div></li>  <li class="level1"><div class="li">*direction* values are "forward" and "reverse".</div></li>  <li class="level1"><div class="li">*fadeColor* is "white", "black", "silver", "gray", "red",  "maroon", fuchsia", "purple", "lime", "green", "yellow", "olive", "blue",  "navy", "aqua", or "teal".</div></li>  <li class="level1"><div class="li">*horzRepeat* and *vertRepeat* is a positive integer.</div></li>  <li class="level1"><div class="li">*borderWidth* is a non-negative integer.</div></li>  <li class="level1"><div class="li">*borderColor* is "white", "black", "silver", "gray", "red",  "maroon", fuchsia", "purple", "lime", "green", "yellow", "olive", "blue",  "navy", "aqua", or "teal".</div></li>  </ul>   <p>The default value for the property is the empty string. If a  transition type is specified then:</p>  <ul>  <li class="level1"><div class="li">"dur" default duration is "1s",</div></li>  <li class="level1"><div class="li">"startProgress" default value is 0,</div></li>  <li class="level1"><div class="li">"endProgress" default value is 1,</div></li>  <li class="level1"><div class="li">"direction" default value is "forward",</div></li>  <li class="level1"><div class="li">"fadeColor" default value is "black",</div></li>  <li class="level1"><div class="li">"horzRepeat" default value is 1,</div></li>  <li class="level1"><div class="li">"vertRepeat" default value is 1,</div></li>  <li class="level1"><div class="li">"borderWidth" default value is 0,</div></li>  <li class="level1"><div class="li">"borderColor" default value is "black".</div></li>  </ul> | <p>The value of the *transIn* and *transOut* is a  semicolon-separated list of transitions.</p>   <p>The purpose of the semicolon-separated list is to allow authors to  specify a set of fallback transitions if the preferred transition is not  available. The first transition in the list should be performed if the  user-agent has implemented this transition. If this transition is not  available, then the second transition in the list should be performed, and  so on.</p>   <p>The *type* and *subtype* define the transition. The  *dur* attribute specifies the duration of the transition.</p>   <p>The *startProgress* attribute specifies the amount of progress  through the transition at which to begin execution. For instance, we can  want to begin a crossfade with the destination image being already 30%  faded in. For this case, *startProgress* would be 0.3.</p>   <p>The *endProgress* attribute specifies the amount of progress  through the transition at which to end execution. The value of this  attribute must be greater than or equal to the value of the  *startProgress* attribute. If *endProgress* is equal to  *startProgress*, then the transition remains at a fixed progress for  the duration of the transition.</p>   <p>The *direction* attribute specifies the direction the  transition will run. Note that not all transitions will have meaningful  reverse interpretations. For instance, a crossfade is not a geometric  transition, and therefore has no interpretation of reverse  direction. Transitions that do not have a reverse interpretation should  have the direction attribute ignored and the default value of "forward"  assumed.</p>   <p>If the value of the *type* attribute is "fade" and the value of  the subtype attribute is "fadeToColor" or "fadeFromColor", then the  *fadeColor* attribute specifies the ending or starting color of the  fade. If the value of the *type* attribute is not "fade", or the  value of the *subtype* attribute is not "fadeToColor" or  "fadeFromColor", then the *fadeColor* attribute is ignored.</p>   <p>If the value of the *type* attribute is not "fade", then the  following attributes can be specified:</p>   <p>The *horzRepeat* attribute specifies how many times to perform  the transition pattern along the horizontal axis.</p>   <p>The *vertRepeat* attribute specifies how many times to perform  the transition pattern along the vertical axis.</p>   <p>The *borderWidth* attribute specifies the width of a generated  border along a wipe edge.</p>   <p>The *borderColor* attribute specifies the  content of the generated border along a wipe edge. If the value of this  attribute is a color, then the generated border along the wipe or warp  edge is filled with this color. If the value of this attribute is "blend",  then the generated border along the wipe blend is an additive blend (or  blur) of the media sources.</p> |

#### Predefined properties for &lt;media&gt;  elements of "application/x-ncl-settings" type { data-search-exclude }

The *system* group.  Set of properties managed by the receiver system.
They may be read, but they may not have their values changed by an NCL
application, a Lua procedure or any other imperative or declarative code
procedure.  Receiver's native applications may change these properties'
values.  They must persist during all receiver life-cycle.

| Name | Value | Description |
| --- | --- | --- |
| system.language | ISO 639-1 code. | Audio language. |
| system.caption | ISO 639-1 code. | Caption language. |
| system.subtitle | ISO 639-1 code. | Subtitle Language. |
| system.returnBitRate(i) | Real number. | The whole bit rate of the interactive channel (i) in kilobytes per  second. |
| system.screenSize | (Integer, Integer). | Device screen size, in (lines, pixels/line), when a class is not  defined. |
| system.screenGraphicSize | (Integer, Integer). | Resolution set for the device's screen graphics plane, in (lines,  pixels/line), when a class is not defined. |
| system.audioType | "mono", "stereo", or "5.1". | Type of the device audio, when a class is not defined. |
| system.screenSize(i) | (Integer, Integer). | Screen size of the class (i) of devices, in (lines, pixels/line). |
| system.screenGraphicSize(i) | (Integer, Integer). | Resolution set for the screen graphics plane of the class (i) of devices,  in (lines, pixels/line). |
| system.audioType(i) | "mono", "stereo", or "5.1". | Type of the audio of the class (i) of devices. |
| system.devNumber(i) | Integer. | Number of exhibition devices registered in the class (i). |
| system.classType(i) | "passive" or "active". | Type of the class (i). |
| system.parentDeviceRegion(i) | Five numbers separated by comma; each one following the value rule  specified for "left", "top", "width", "height", and "zIndex" properties,  respectively. | Identifies a [&lt;region&gt;](region.md) element in another [&lt;regionBase&gt;](regionbase.md)  associated with the parent device that creates the bit map sent to the  passive-class devices (i); in the specified region the bit map sent must  also be exhibited. |
| system.info(i) | String. | List of class (i)'s media players. |
| system.classNumber | Integer. | Number of classes that has been defined. |
| system.CPU | Real number. | CPU performance in MIPS, regarding its capacity to run applications. |
| system.memory | Integer. | Minimum memory space in megabytes provided to applications. |
| system.operatingSystem | String (to be defined). | Type of the operating system. |
| system.luaVersion | String (to be defined). | Version of the Lua engine supported by the receiver. |
| system.ncl.version | String (to be defined). | NCL language version. |
| system.GingaNCL.version | String (to be defined). | Ginga-NCL environment version. |
| system.xyz | String. | Any property with the "system" prefix is reserved for future use. |

The *user* group.  Set of properties managed by the receiver system.
They may be read, but they may not have their values changed by an NCL
application, a Lua procedure or any other imperative or declarative code
procedure.  Receiver's native applications may change the properties'
values.  They must persist during all receiver life-cycle.

| Name | Value | Description |
| --- | --- | --- |
| user.age | Integer. | User age. |
| user.location | String. | User location. |
| user.genre | "m" (male) or "f" (female). | User genre. |
| user.xyz | String. | Any property with the "user" prefix is reserved for future use. |

The *default* group.  Set of properties managed by the receiver
system.  They may be read and have their values changed by an NCL
application, a Lua procedure or any other imperative or declarative code
procedure.  Receiver's native applications may change the properties'
values.  They must persist during all receiver life-cycle, however, they are
set to their initial values when a new channel is tuned.

| Name | Value | Description |
| --- | --- | --- |
| default.focusBorderColor | "white", "black", "silver", "gray", "red", "maroon", "fuchsia", "purple",  "lime", "green", "yellow", "olive", "blue", "navy", "aqua", or "teal". | Default color applied to the border of an element in focus. |
| default.selBorderColor | "white", "black", "silver", "gray", "red", "maroon", "fuchsia", "purple",  "lime", "green", "yellow", "olive", "blue", "navy", "aqua", or "teal". | Default color applied to the border of an element in focus when  activated. |
| default.focusBorderWidth | Integer. | Default width (in pixels) applied to the border of an element in focus. |
| default.focusBorderTransparency | Number in the range \[0,1\] or \[0,100\], ending with the character <"%">  (e.g. "30%"), with "1" or "100%" meaning full transparency and "0" or "0%"  meaning no transparency. | Default transparency applied to the border of an element in focus. |
| default.xyz | String. | Any property with the "default" prefix is reserved for future use. |

The *service* group.  Set of properties managed by the NCL formatter.
They may be read and have their values changed by an NCL application of the
same service.  They may be read but they may not have their values changed
by a Lua procedure or any other imperative or declarative code procedure.
Variable changes must be done using NCL commands.  They must persist at
least during the service life-cycle.

| Name | Value | Description |
| --- | --- | --- |
| service.currentFocus | Integer. | The *focusIndex* value of the [&lt;media&gt;](media.md) element on focus. |
| service.currentKeyMaster | String. | Identifier *id* of the [&lt;media&gt;](media.md) element that controls the  navigational keys; if the [&lt;media&gt;](media.md) element is not being presented or  is not paused, the navigational key control pertains to the NCL  formatter. |
| service.xyz | String. | Any property with the "service" prefix follow the rules specified for the  group. |

The *si* group.  Set of properties managed by the middleware.  They
may be read, but they may not have their values changed by an NCL
application, a Lua procedure or any other imperative or declarative code
procedure.  They must persist at least until the next channel tuning.

| Name | Value | Description |
| --- | --- | --- |
| si.numberOfServices | Integer. | Number of services available in the country for the tuned channel. Note:  The value for this variable should be obtained from the number of PMT  tables specified in the PAT table of the transport stream received in the  tuning channel (see ISO/IEC 13818-1:2007). The variable value should take  into account only the PMT tables whose fields country_code, specified in  the country_availability_descriptor (see Section 8.3.6 of ABNT NBR  15603-2:2007) related with the table, are equivalent to the value of the  "user.location" variable of the *settings* node. |
| si.numberOfPartialServices | Integer | Number of 1-seg services available in the country for the tuned  channel. Note: The value for this variable should be obtained from the  number of PMT tables specified in the PAT table of the transport stream  received in the tuning channel (see ISO/IEC 13818-1:2007). The variable  value should take into account only the PMT tables whose country_code  fields, specified in the country_availability_descriptor (see Section  8.3.6 of ABNT NBR 15603-2:2007) related with the table, are equal to the  value of the "user.location" variable of the *settings* node, and  whose program_number fields are equivalent to the service_id fields of the  partial_reception_descriptor related with the NIT tables. |
| si.channelNumber | Integer | Number of the tuned channel. Note: The value for this variable should be  obtained from the remote_control_key_id filed of the  ts_information_descriptor (see Section 8.3.42 of ABNT NBR 15603-2:2007) of  the NIT table (see Section 7.2.4 of ABNT NBR 15603-2:2007) that describes  the current service. |
| si.xyz | String | Any property with the "si" prefix follows the rules  specified for the group. |

The *channel* group.  Set of properties managed by the NCL formatter.
They may be read and have their values changed by an NCL application of the
same channel.  They may be read but they may not have their values changed
by a Lua procedure or any other imperative or declarative code procedure of
the same channel; variable changes must be done using NCL commands.  They
must persist at least until the next channel tuning.

| Name | Value | Description |
| --- | --- | --- |
| channel.keyCapture | String | Request of alphanumeric keys for NCL applications. |
| channel.virtualKeyboard | "true" or "false" | Request of a virtual keyboard for NCL applications. |
| channel.keyboardBounds | (Integer, Integer, Integer, Integer) | Virtual keyboard region (left, top, width, height). |
| channel.xyz | String | Any variable with the "channel" prefix follows the rules  specified for the group. |

The *shared*.  Set of properties managed by the NCL formatter.  They
may be read and have their values changed by an NCL application.  They may
be read but they may not have their values changed by a Lua procedure or any
other imperative or declarative code procedure; variable changes must be
done using NCL commands.  They must persist at least during the life-cycle
of the service that has defined them.

| Name | Value | Description |
| --- | --- | --- |
| shared.xyz | String | Any property with the "shared" prefix follows  the rules specified for the group. |

#### Reserved names for color definition { data-search-exclude }

<table class="inline">
<tbody>
<tr class="row0">
  <th>Color</th>
  <th>Name</th>
  <th>Hexadecimal</th>
  <th>(R,G,B)</th>
  <th>Hue</th>
  <th>(Saturation, Light)</th>
  <th>(Saturation, Value)</th>
</tr>
<tr>
<td bgcolor="#ffffff"/>
<td>White</td>
<td>#ffffff</td>
<td>(100%, 100%, 100%)</td>
<td>0&deg;</td>
<td>(0%, 100%)</td>
<td>(0%, 100%)</td>
</tr>

<tr>
<td bgcolor="#c0c0c0"/>
<td>Silver</td>
<td>#c0c0c0</td>
<td>(75%, 75%, 75%)</td>
<td>0&deg;</td>
<td>(0%, 75%)</td>
<td>(0%, 75%)</td>
</tr>

<tr>
<td bgcolor="#808080"/>
<td>Gray</td>
<td>#808080</td>
<td>(50%, 50%, 50%)</td>
<td>0&deg;</td>
<td>(0%, 50%)</td>
<td>(0%, 50%)</td>
</tr>

<tr>
<td bgcolor="#000000"/>
<td>Black</td>
<td>#000000</td>
<td>(0%, 0%, 0%)</td>
<td>0&deg;</td>
<td>(0%, 0%)</td>
<td>(0%, 0%)</td>
</tr>

<tr>
<td bgcolor="#ff0000"/>
<td>Red</td>
<td>#ff0000</td>
<td>(100%, 0%, 0%)</td>
<td>0&deg;</td>
<td>(100%, 50%)</td>
<td>(100%, 100%)</td>
</tr>

<tr>
<td bgcolor="#800000"/>
<td>Maroon</td>
<td>#800000</td>
<td>(50%, 0%, 0%)</td>
<td>0&deg;</td>
<td>(100%, 25%)</td>
<td>(100%, 50%)</td>
</tr>

<tr>
<td bgcolor="#ffff00"/>
<td>Yellow</td>
<td>#ffff00</td>
<td>(100%, 100%, 0%)</td>
<td>60&deg;</td>
<td>(100%, 50%)</td>
<td>(100%, 100%)</td>
</tr>

<tr>
<td bgcolor="#808000"/>
<td>Olive</td>
<td>#808000</td>
<td>(50%, 50%, 0%)</td>
<td>60&deg;</td>
<td>(100%, 25%)</td>
<td>(100%, 50%)</td>
</tr>

<tr>
<td bgcolor="#00ff00"/>
<td>Lime</td>
<td>#00ff00</td>
<td>(0%, 100%, 0%)</td>
<td>120&deg;</td>
<td>(100%, 50%)</td>
<td>(100%, 100%)</td>
</tr>

<tr>
<td bgcolor="#008000"/>
<td>Green</td>
<td>#008000</td>
<td>(0%, 50%, 0%)</td>
<td>120&deg;</td>
<td>(100%, 25%)</td>
<td>(100%, 50%)</td>
</tr>

<tr>
<td bgcolor="#00ffff"/>
<td>Aqua</td>
<td>#00ffff</td>
<td>(0%, 100%, 100%)</td>
<td>180&deg;</td>
<td>(100%, 50%)</td>
<td>(100%, 100%)</td>
</tr>

<tr>
<td bgcolor="#008080"/>
<td>Teal</td>
<td>#008080</td>
<td>(0%, 50%, 50%)</td>
<td>180&deg;</td>
<td>(100%, 25%)</td>
<td>(100%, 50%)</td>
</tr>

<tr>
<td bgcolor="#0000ff"/>
<td>Blue</td>
<td>#0000ff</td>
<td>(0%, 0%, 100%)</td>
<td>240&deg;</td>
<td>(100%, 50%)</td>
<td>(100%, 100%)</td>
</tr>

<tr>
<td bgcolor="#000080"/>
<td>Navy</td>
<td>#000080</td>
<td>(0%, 0%, 50%)</td>
<td>240&deg;</td>
<td>(100%, 25%)</td>
<td>(100%, 50%)</td>
</tr>

<tr>
<td bgcolor="#ff00ff"/>
<td>Fuchsia</td>
<td>#ff00ff</td>
<td>(100%, 0%, 100%)</td>
<td>300&deg;</td>
<td>(100%, 50%)</td>
<td>(100%, 100%)</td>
</tr>

<tr>
<td bgcolor="#800080"/>
<td>Purple</td>
<td>#800080</td>
<td>(50%, 0%, 50%)</td>
<td>300&deg;</td>
<td>(100%, 25%)</td>
<td>(100%, 50%)</td>
</tr>

</tbody>
</table>
