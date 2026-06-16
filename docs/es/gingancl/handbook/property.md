---
title: "Elemento &lt;property&gt;"
---

### Definición y uso { data-search-exclude }

El elemento [&lt;property&gt;](property.md) define una propiedad o un grupo de propiedades para
su padre [&lt;media&gt;](media.md), [&lt;context&gt;](context.md), [&lt;body&gt;](body.md) o [&lt;switch&gt;](switch.md)
elementos. Estas propiedades se pueden utilizar en relaciones con otros objetos.
de una aplicación NCL, si el atributo externo de [&lt;property&gt;](property.md)
El elemento tiene "verdadero" como valor.

El elemento [&lt;property&gt;](property.md) define el atributo de nombre, que indica el
nombre de la propiedad o grupo de propiedades y el atributo de valor.  el padre
El elemento no puede tener más de un elemento [&lt;property&gt;](property.md) con el mismo
valor del atributo de nombre.

El atributo *valor* es opcional y define un valor inicial para el
propiedad declarada en el atributo *nombre*. Cuando el valor no es
especificada, la propiedad se inicializa con el valor definido en el homónimo
atributos de los elementos [&lt;descriptor&gt;](descriptor.md) o [&lt;region&gt;](region.md) asociados
con el elemento padre que define el [&lt;property&gt;](property.md), o bien con un
valor predeterminado (que depende del valor del atributo de nombre). cuando el
El valor se especifica en el elemento [&lt;property&gt;](property.md), tiene prioridad sobre
el valor definido en los atributos homónimos de [&lt;descriptor&gt;](descriptor.md) o
[&lt;region&gt;](region.md) elementos asociados con el elemento principal que define el
[&lt;property&gt;](property.md).

### Sintaxis { data-search-exclude }

| Elemento | Atributos | Contenido | Padre |
| --- | --- | --- | --- |
| [&lt;property&gt;](property.md) | *nombre*, *valor*, *externable* | -- | [&lt;media&gt;](media.md) o [&lt;context&gt;](context.md) o [&lt;body&gt;](body.md) |

### Atributos { data-search-exclude }

| Nombre | Valor | Descripción |
| --- | --- | --- |
| *nombre* | Puede recibir cualquier valor de cadena que comience con una letra o un guión bajo y que solo contenga letras, dígitos, "." y "_". | El atributo *nombre* identifica de forma única la propiedad dentro de su elemento principal. |
| *valor* | Depende del valor del nombre. | El atributo *valor* define un valor inicial para el atributo *nombre*. |
| *externable* | "falso" o "verdadero".  El valor predeterminado es: "verdadero" si la propiedad está definida en un elemento [&lt;property&gt;](property.md), o "falso" si la propiedad está definida en un elemento [&lt;descriptor&gt;](descriptor.md). | El atributo *externable* determina si una propiedad puede (externable="true") o no (externable="false") usarse en relaciones. |

### Propiedades predefinidas { data-search-exclude }

Se utilizan varias palabras reservadas para especificar propiedades con valores predefinidos.
semántica conocida por los jugadores de la NCL. Estas propiedades, su semántica, su
Los valores posibles y sus valores predeterminados se presentan a continuación.

#### Propiedades predefinidas para todos los &lt;media&gt; elementos { data-search-exclude }

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

#### Propiedades predefinidas para &lt;media&gt; elementos con contenido visual { data-search-exclude }

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

#### Propiedades predefinidas para &lt;media&gt; elementos con contenido multimedia continuo (solo lectura) { data-search-exclude }

| Nombre | Valor | Descripción |
| --- | --- | --- |
| ID de contenido | <p>String.</p><p>(Establecido solo por el reproductor NCL.)</p> <p>El valor predeterminado es nulo.</p> | La propiedad "contentId" está asociada a objetos de medios continuos cuyo contenido se define haciendo referencia a un flujo elemental. Tiene *null* como valor inicial y se establece en el valor del identificador transportado en el descriptor de referencia NPT (en un campo del mismo nombre: contentId), tan pronto como se inicia el objeto de medios continuos asociado. |
| en espera | <p>"true" o "false".</p> <p>(Establecido solo por el reproductor NCL).</p> <p>El valor predeterminado es "falso".</p> | La propiedad "en espera" se establece en "verdadero" mientras que un contenido de objeto de medios continuos ya iniciado que hace referencia a una secuencia elemental es interrumpido temporalmente por otro contenido entrelazado, en la misma secuencia elemental. |

#### Propiedades predefinidas para &lt;media&gt;  elementos con contenido audible { data-search-exclude }

| Nombre | Valor | Descripción |
| --- | --- | --- |
| nivel de sonido | Un número real en el rango \[0,1\] o un número real en el rango \[0,100\] que termina con el carácter <"%"> (por ejemplo, "30%").  <p>El valor predeterminado es 1.</p> | Volumen de audio relativo al audio grabado. |
| nivel de equilibrio | Un número real en el rango \[-1,1\] o un número real en el rango \[-100,100\] que termina con el carácter <"%"> (por ejemplo, "30%").  <p>El valor predeterminado es 0.</p> | Nivel de balance del audio (-1 a la izquierda y +1 a la derecha). |
| nivel de agudos | Un número real en el rango \[0,1\] o un número real en el rango \[0,100\] que termina con el carácter <"%"> (por ejemplo, "30%").  <p>El valor predeterminado es 1.</p> | Configuración de agudos, relativa al audio grabado. |
| nivel de bajo | Un número real en el rango \[0,1\] o un número real en el rango \[0,100\] que termina con el carácter <"%"> (por ejemplo, "30%").  <p>El valor predeterminado es 1.</p> | Configuración de graves, relativa al audio grabado. |
| congelar | <p>"verdadero" o "falso".</p><p>El valor predeterminado es "falso".</p> | Esta propiedad define lo que sucederá con un objeto al final de su presentación, si el contenido final está congelado ("verdadero") o no ("falso"). |
| transIn, transOut | Una lista del formato <"(type,subtype,dur,startProgress,endProgress)"> donde: <ul> <li class="level1"><div class="li">"tipo" es "desvanecimiento" de forma predeterminada, </div></li> <li class="level1"><div class="li">"subtipo" es "desvanecido" de forma predeterminada, </div></li> <li class="level1"><div class="li">La propiedad "explicitDur" se especifica de acuerdo con uno de los siguientes sintaxis:</div></li> <ol> <li class="level1"><div class="li">"Horas:Minutos:Segundos.Fracción", donde "Horas" es un número entero en el intervalo \[0,23\], "Minutos" es un número entero en el intervalo \[0,59\], "Segundos" es un número entero en el intervalo \[0,59\] y "Fracción" es un número entero positivo.</div></li> <li class="level1"><div class="li">Segundos"s", donde Segundos es un número real positivo.</div></li> </ol> <li class="level1"><div class="li">"startProgress" es un número real en el rango \[0,1\], y "endProgress" es un número real en el rango \[0,1\].</div></li> </ul> <p>El valor predeterminado de la propiedad es la cadena vacía. Si se especifica una transición, entonces:</p> <ul> <li class="level1"><div class="li">"dur" la duración predeterminada es "1s",</div></li> <li class="level1"><div class="li">El valor predeterminado de "startProgress" es 0, </div></li> <li class="level1"><div class="li"> El valor predeterminado de "endProgress" es 1.</div></li> </ul> | <p>El tipo de *transIn* y *transOut* siempre es "fundido" y el *subtipo* siempre es "fundido" y está definido de forma predeterminada.</p> <p>El atributo *dur* especifica la duración de la transición.</p> <p>El atributo *startProgress* especifica la cantidad de progreso a través de la transición en la que comenzar la ejecución.</p> <p>El atributo *endProgress* especifica la cantidad de progreso a través de la transición en la que finalizar la ejecución. El valor de este atributo debe ser mayor o igual al valor del atributo *startProgress*. Si *endProgress* es igual a *startProgress*, entonces la transición permanece en un progreso fijo mientras dure la transición.</p> |

#### Propiedades predefinidas para &lt;media&gt;  elementos con contenido textual { data-search-exclude }

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

#### Propiedades predefinidas para &lt;media&gt;  elementos de "aplicación/x-ncl-settings" tipo { data-search-exclude }

El grupo *sistema*.  Conjunto de propiedades gestionadas por el sistema receptor.
Se pueden leer, pero una NCL no puede cambiar sus valores.
aplicación, un procedimiento Lua o cualquier otro código imperativo o declarativo
procedimiento.  Las aplicaciones nativas del receptor pueden cambiar estas propiedades.
valores.  Deben persistir durante todo el ciclo de vida del receptor.

| Nombre | Valor | Descripción |
| --- | --- | --- |
| idioma.delsistema | Código ISO 639-1. | Idioma de audio. |
| sistema.caption | Código ISO 639-1. | Idioma de los subtítulos. |
| sistema.subtítulo | Código ISO 639-1. | Idioma de subtítulos. |
| sistema.returnBitRate(i) | Número real. | La velocidad de bits total del canal interactivo (i) en kilobytes por segundo. |
| sistema.tamañodepantalla | (Entero, Entero). | Tamaño de pantalla del dispositivo, en (líneas, píxeles/línea), cuando no se define una clase. |
| system.screenGraphicSize | (Entero, Entero). | Resolución establecida para el plano gráfico de la pantalla del dispositivo, en (líneas, píxeles/línea), cuando no se define una clase. |
| sistema.tipo de audio | "mono", "estéreo" o "5.1". | Tipo de dispositivo de audio, cuando no se define una clase. |
| sistema.tamañodepantalla(i) | (Entero, Entero). | Tamaño de pantalla de la clase (i) de dispositivos, en (líneas, píxeles/línea). |
| system.screenGraphicSize(i) | (Entero, Entero). | Resolución establecida para el plano gráfico de pantalla de la clase (i) de dispositivos, en (líneas, píxeles/línea). |
| sistema.audioType(i) | "mono", "estéreo" o "5.1". | Tipo de audio de la clase (i) de dispositivos. |
| sistema.devNumber(i) | Entero. | Número de dispositivos de exhibición registrados en la clase (i). |
| sistema.classType(i) | "pasivo" o "activo". | Tipo de clase (i). |
| system.parentDeviceRegion(i) | Cinco números separados por coma; cada uno siguiendo la regla de valor especificada para las propiedades "izquierda", "arriba", "ancho", "alto" y "zIndex", respectivamente. | Identifica un elemento [&lt;region&gt;](region.md) en otro [&lt;regionBase&gt;](regionbase.md) asociado con el dispositivo principal que crea el mapa de bits enviado a los dispositivos de clase pasiva (i); en la región especificada también se debe exhibir el mapa de bits enviado. |
| sistema.info(i) | Cadena. | Lista de reproductores multimedia de clase (i). |
| sistema.númerodeclase | Entero. | Número de clases que se han definido. |
| sistema.CPU | Número real. | Rendimiento de la CPU en MIPS, respecto a su capacidad para ejecutar aplicaciones. |
| memoria.delsistema | Entero. | Espacio mínimo de memoria en megabytes proporcionado a las aplicaciones. |
| sistema.sistemaoperativo | Cadena (por definir). | Tipo de sistema operativo. |
| system.luaVersión | Cadena (por definir). | Versión del motor Lua soportada por el receptor. |
| sistema.ncl.versión | Cadena (por definir). | Versión en idioma NCL. |
| sistema.GingaNCL.versión | Cadena (por definir). | Versión del entorno Ginga-NCL. |
| sistema.xyz | Cadena. | Cualquier propiedad con el prefijo "sistema" está reservada para uso futuro. |

El grupo *usuario*.  Conjunto de propiedades gestionadas por el sistema receptor.
Se pueden leer, pero una NCL no puede cambiar sus valores.
aplicación, un procedimiento Lua o cualquier otro código imperativo o declarativo
procedimiento.  Las aplicaciones nativas del receptor pueden cambiar las propiedades
valores.  Deben persistir durante todo el ciclo de vida del receptor.

| Nombre | Valor | Descripción |
| --- | --- | --- |
| edad.usuario | Entero. | Edad del usuario. |
| ubicación.usuario | Cadena. | Ubicación del usuario. |
| usuario.género | "m" (masculino) o "f" (femenino). | Género de usuario. |
| usuario.xyz | Cadena. | Cualquier propiedad con el prefijo "usuario" está reservada para uso futuro. |

El grupo *predeterminado*.  Conjunto de propiedades gestionadas por el receptor.
sistema.  Pueden ser leídos y modificados por una NCL.
aplicación, un procedimiento Lua o cualquier otro código imperativo o declarativo
procedimiento.  Las aplicaciones nativas del receptor pueden cambiar las propiedades
valores.  Deben persistir durante todo el ciclo de vida del receptor; sin embargo, son
se ajustan a sus valores iniciales cuando se sintoniza un nuevo canal.

| Nombre | Valor | Descripción |
| --- | --- | --- |
| default.focusBorderColor | "blanco", "negro", "plateado", "gris", "rojo", "granate", "fucsia", "púrpura", "lima", "verde", "amarillo", "oliva", "azul", "azul marino", "aqua" o "verde azulado". | Color predeterminado aplicado al borde de un elemento enfocado. |
| default.selBorderColor | "blanco", "negro", "plateado", "gris", "rojo", "granate", "fucsia", "púrpura", "lima", "verde", "amarillo", "oliva", "azul", "azul marino", "aqua" o "verde azulado". | Color predeterminado aplicado al borde de un elemento enfocado cuando se activa. |
| default.focusBorderWidth | Entero. | Ancho predeterminado (en píxeles) aplicado al borde de un elemento enfocado. |
| default.focusBorderTransparency | Número en el rango \[0,1\] o \[0,100\], que termina con el carácter <"%"> (por ejemplo, "30%"), donde "1" o "100%" significa transparencia total y "0" o "0%" significa sin transparencia. | Transparencia predeterminada aplicada al borde de un elemento enfocado. |
| predeterminado.xyz | Cadena. | Cualquier propiedad con el prefijo "predeterminado" está reservada para uso futuro. |

El grupo *servicio*.  Conjunto de propiedades gestionadas por el formateador NCL.
Se pueden leer y cambiar sus valores mediante una aplicación NCL del
mismo servicio.  Se pueden leer pero no se pueden cambiar sus valores.
mediante un procedimiento Lua o cualquier otro procedimiento de código imperativo o declarativo.
Los cambios de variables deben realizarse mediante comandos NCL.  Deben persistir en
al menos durante el ciclo de vida del servicio.

| Nombre | Valor | Descripción |
| --- | --- | --- |
| servicio.currentFocus | Entero. | El valor *focusIndex* del elemento [&lt;media&gt;](media.md) en foco. |
| servicio.currentKeyMaster | Cadena. | Identificador *id* del elemento [&lt;media&gt;](media.md) que controla las teclas de navegación; Si el elemento [&lt;media&gt;](media.md) no se presenta o no está en pausa, el control de la tecla de navegación pertenece al formateador NCL. |
| servicio.xyz | Cadena. | Cualquier propiedad con el prefijo "servicio" sigue las reglas especificadas para el grupo. |

El grupo *si*.  Conjunto de propiedades gestionadas por el middleware.  ellos
pueden leerse, pero es posible que una NCL no cambie sus valores
aplicación, un procedimiento Lua o cualquier otro código imperativo o declarativo
procedimiento.  Deben persistir al menos hasta la siguiente sintonización de canal.

| Nombre | Valor | Descripción |
| --- | --- | --- |
| si.númeroDeServicios | Entero. | Número de servicios disponibles en el país para el canal sintonizado. Nota: El valor de esta variable debe obtenerse del número de tablas PMT especificadas en la tabla PAT del flujo de transporte recibido en el canal de sintonización (ver ISO/IEC 13818-1:2007). El valor de la variable debe tener en cuenta sólo las tablas PMT cuyos campos código_país, especificados en el descriptor_disponibilidad_país (ver Sección 8.3.6 de la ABNT NBR 15603-2:2007) relacionados con la tabla, son equivalentes al valor de la variable "usuario.ubicación" del nodo *configuraciones*. |
| si.numberOfPartialServices | Entero | Número de servicios 1-seg disponibles en el país para el canal sintonizado. Nota: El valor de esta variable debe obtenerse del número de tablas PMT especificadas en la tabla PAT del flujo de transporte recibido en el canal de sintonización (ver ISO/IEC 13818-1:2007). El valor de la variable debe tener en cuenta sólo las tablas PMT cuyos campos country_code, especificados en el country_availability_descriptor (ver Sección 8.3.6 de la ABNT NBR 15603-2:2007) relacionados con la tabla, son iguales al valor de la variable "user.location" del nodo *settings*, y cuyos campos program_number son equivalentes a los campos service_id del descriptor_recepción_parcial relacionado con las tablas NIT. |
| si.númerodecanal | Entero | Número del canal sintonizado. Nota: El valor de esta variable debe obtenerse del archivo remote_control_key_id del ts_information_descriptor (ver Sección 8.3.42 de la ABNT NBR 15603-2:2007) de la tabla NIT (ver Sección 7.2.4 de la ABNT NBR 15603-2:2007) que describe el servicio actual. |
| si.xyz | Cadena | Cualquier propiedad con el prefijo "si" sigue las reglas especificadas para el grupo. |

El grupo *canal*.  Conjunto de propiedades gestionadas por el formateador NCL.
Se pueden leer y cambiar sus valores mediante una aplicación NCL del
mismo canal.  Se pueden leer pero no se pueden cambiar sus valores.
mediante un procedimiento Lua o cualquier otro procedimiento de código imperativo o declarativo de
el mismo canal; Los cambios de variables deben realizarse mediante comandos NCL.  ellos
debe persistir al menos hasta la siguiente sintonización de canal.

| Nombre | Valor | Descripción |
| --- | --- | --- |
| canal.keyCapture | Cadena | Solicitud de claves alfanuméricas para aplicaciones NCL. |
| canal.tecladovirtual | "verdadero" o "falso" | Solicitud de un teclado virtual para aplicaciones NCL. |
| canal.keyboardBounds | (Entero, Entero, Entero, Entero) | Región del teclado virtual (izquierda, arriba, ancho, alto). |
| canal.xyz | Cadena | Cualquier variable con el prefijo "canal" sigue las reglas especificadas para el grupo. |

El *compartido*.  Conjunto de propiedades gestionadas por el formateador NCL.  ellos
se pueden leer y cambiar sus valores mediante una aplicación NCL.  ellos pueden
ser leídos, pero sus valores no pueden cambiarse mediante un procedimiento Lua o cualquier
otro procedimiento de código imperativo o declarativo; Los cambios variables deben ser
hecho usando comandos NCL.  Deben persistir al menos durante el ciclo de vida.
del servicio que los ha definido.

| Nombre | Valor | Descripción |
| --- | --- | --- |
| compartido.xyz | Cadena | Cualquier propiedad con el prefijo "compartido" sigue las reglas especificadas para el grupo. |

#### Nombres reservados para la definición de color { data-search-exclude }

<table class="inline">
<tbody>
<tr class="row0">
  <th>Color</th>
  <th>Nombre</th>
  <th>Hexadecimal</th>
  <th>(R,G,B)</th>
  <th>Tono</th>
  <th>(Saturación, Luz)</th>
  <th>(Saturación, Valor)</th>
</tr>
<tr>
<td bgcolor="#ffffff"/>
<td>Blanco</td>
<td>#ffffff</td>
<td>(100%, 100%, 100%)</td>
<td>0&deg;</td>
<td>(0%, 100%)</td>
<td>(0%, 100%)</td>
</tr>

<tr>
<td bgcolor="#c0c0c0"/>
<td>Plata</td>
<td>#c0c0c0</td>
<td>(75%, 75%, 75%)</td>
<td>0&deg;</td>
<td>(0%, 75%)</td>
<td>(0%, 75%)</td>
</tr>

<tr>
<td bgcolor="#808080"/>
<td>Gris</td>
<td>#808080</td>
<td>(50%, 50%, 50%)</td>
<td>0&deg;</td>
<td>(0%, 50%)</td>
<td>(0%, 50%)</td>
</tr>

<tr>
<td bgcolor="#000000"/>
<td>Negro</td>
<td>#000000</td>
<td>(0%, 0%, 0%)</td>
<td>0&deg;</td>
<td>(0%, 0%)</td>
<td>(0%, 0%)</td>
</tr>

<tr>
<td bgcolor="#ff0000"/>
<td>Rojo</td>
<td>#ff0000</td>
<td>(100%, 0%, 0%)</td>
<td>0&deg;</td>
<td>(100%, 50%)</td>
<td>(100%, 100%)</td>
</tr>

<tr>
<td bgcolor="#800000"/>
<td>Granate</td>
<td>#800000</td>
<td>(50%, 0%, 0%)</td>
<td>0&deg;</td>
<td>(100%, 25%)</td>
<td>(100%, 50%)</td>
</tr>

<tr>
<td bgcolor="#ffff00"/>
<td>Amarillo</td>
<td>#ffff00</td>
<td>(100%, 100%, 0%)</td>
<td>60°</td>
<td>(100%, 50%)</td>
<td>(100%, 100%)</td>
</tr>

<tr>
<td bgcolor="#808000"/>
<td>Oliva</td>
<td>#808000</td>
<td>(50%, 50%, 0%)</td>
<td>60°</td>
<td>(100%, 25%)</td>
<td>(100%, 50%)</td>
</tr>

<tr>
<td bgcolor="#00ff00"/>
<td>Lime</td>
<td>#00ff00</td>
<td>(0%, 100%, 0%)</td>
<td>120°</td>
<td>(100%, 50%)</td>
<td>(100%, 100%)</td>
</tr>

<tr>
<td bgcolor="#008000"/>
<td>Verde</td>
<td>#008000</td>
<td>(0%, 50%, 0%)</td>
<td>120°</td>
<td>(100%, 25%)</td>
<td>(100%, 50%)</td>
</tr>

<tr>
<td bgcolor="#00ffff"/>
<td>Aqua</td>
<td>#00ffff</td>
<td>(0%, 100%, 100%)</td>
<td>180°</td>
<td>(100%, 50%)</td>
<td>(100%, 100%)</td>
</tr>

<tr>
<td bgcolor="#008080"/>
<td>Verde azulado</td>
<td>#008080</td>
<td>(0%, 50%, 50%)</td>
<td>180°</td>
<td>(100%, 25%)</td>
<td>(100%, 50%)</td>
</tr>

<tr>
<td bgcolor="#0000ff"/>
<td>Azul</td>
<td>#0000ff</td>
<td>(0%, 0%, 100%)</td>
<td>240°</td>
<td>(100%, 50%)</td>
<td>(100%, 100%)</td>
</tr>

<tr>
<td bgcolor="#000080"/>
<td>Marina</td>
<td>#000080</td>
<td>(0%, 0%, 50%)</td>
<td>240°</td>
<td>(100%, 25%)</td>
<td>(100%, 50%)</td>
</tr>

<tr>
<td bgcolor="#ff00ff"/>
<td>Fucsia</td>
<td>#ff00ff</td>
<td>(100%, 0%, 100%)</td>
<td>300°</td>
<td>(100%, 50%)</td>
<td>(100%, 100%)</td>
</tr>

<tr>
<td bgcolor="#800080"/>
<td>Púrpura</td>
<td>#800080</td>
<td>(50%, 0%, 50%)</td>
<td>300°</td>
<td>(100%, 25%)</td>
<td>(100%, 50%)</td>
</tr>

</tbody>
</table>