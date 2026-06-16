---
title: "Elemento &lt;property&gt;"
---

### Definição e uso { data-search-exclude }

O elemento [&lt;property&gt;](property.md) define uma propriedade ou um grupo de propriedades para
seu pai [&lt;media&gt;](media.md), [&lt;context&gt;](context.md), [&lt;body&gt;](body.md) ou [&lt;switch&gt;](switch.md)
elementos. Essas propriedades podem ser usadas em relacionamentos com outros objetos
de uma aplicação NCL, se o atributo externo do [&lt;property&gt;](property.md)
elemento tem "true" como valor.

O elemento [&lt;property&gt;](property.md) define o atributo name, que indica o
nome da propriedade ou grupo de propriedades e o atributo de valor.  O pai
elemento não pode ter mais de um elemento [&lt;property&gt;](property.md) com o mesmo
valor do atributo nome.

O atributo *value* é opcional e define um valor inicial para o
propriedade declarada no atributo *nome*. Quando o valor não é
especificado, a propriedade é inicializada com o valor definido no homônimo
atributos dos elementos [&lt;descriptor&gt;](descriptor.md) ou [&lt;region&gt;](region.md) associados
com o elemento pai que define [&lt;property&gt;](property.md), ou então com um
valor padrão (que depende do valor do atributo name). Quando o
valor é especificado no elemento [&lt;property&gt;](property.md), ele tem precedência sobre
o valor definido nos atributos homônimos de [&lt;descriptor&gt;](descriptor.md) ou
[&lt;region&gt;](region.md) elementos associados ao elemento pai que define o
[&lt;property&gt;](property.md).

### Sintaxe { data-search-exclude }

| Elemento | Atributos | Conteúdo | Pai |
| --- | --- | --- | --- |
| [&lt;property&gt;](property.md) | *nome*, *valor*, *externável* | -- | [&lt;media&gt;](media.md) ou [&lt;context&gt;](context.md) ou [&lt;body&gt;](body.md) |

### Atributos { data-search-exclude }

| Nome | Valor | Descrição |
| --- | --- | --- |
| *nome* | Pode receber qualquer valor de string que comece com uma letra ou sublinhado e que contenha apenas letras, dígitos, "." e "_". | O atributo *name* identifica exclusivamente a propriedade dentro de seu elemento pai. |
| *valor* | Depende do valor do nome. | O atributo *value* define um valor inicial para o atributo *name*. |
| *externável* | "falso" ou "verdadeiro".  O valor padrão é: "true" se a propriedade estiver definida em um elemento [&lt;property&gt;](property.md) ou "false" se a propriedade estiver definida em um elemento [&lt;descriptor&gt;](descriptor.md). | O atributo *externable* determina se uma propriedade pode (externable="true") ou não (externable="false") ser usada em relacionamentos. |

### Propriedades predefinidas { data-search-exclude }

Várias palavras reservadas são usadas para especificar propriedades com valores pré-definidos
semântica conhecida pelos jogadores NCL. Essas propriedades, sua semântica, sua
os valores possíveis e seus valores padrão são apresentados abaixo.

#### Propriedades predefinidas para todas as &lt;media&gt; elementos { data-search-exclude }

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

#### Propriedades predefinidas para &lt;media&gt; elementos com conteúdo visual { data-search-exclude }

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

#### Propriedades predefinidas para &lt;media&gt; elementos com conteúdo de mídia contínua (somente leitura) { data-search-exclude }

| Nome | Valor | Descrição |
| --- | --- | --- |
| ID do conteúdo | <p>String.</p><p>(Definido apenas pelo player NCL.)</p> <p>O valor padrão é nulo.</p> | A propriedade "contentId" está associada a objetos de mídia contínua cujo conteúdo é definido referente a um fluxo elementar. Possui *null* como valor inicial e é definido como o valor do identificador transportado no descritor de referência NPT (em um campo de mesmo nome: contentId), assim que o objeto de mídia contínua associado é iniciado. |
| espera | <p>"true" ou "false".</p> <p>(Definido apenas pelo player NCL.)</p> <p>O valor padrão é "false".</p> | A propriedade "standby" é definida como "true" enquanto um conteúdo de objeto de mídia contínua já iniciado referente a um fluxo elementar é temporariamente interrompido por outro conteúdo intercalado, no mesmo fluxo elementar. |

#### Propriedades predefinidas para &lt;media&gt;  elementos com conteúdo audível { data-search-exclude }

| Nome | Valor | Descrição |
| --- | --- | --- |
| nível de som | Um número real no intervalo \[0,1\] ou um número real no intervalo \[0,100\] terminando com o caractere <"%"> (por exemplo, "30%").  <p>O valor padrão é 1.</p> | Volume de áudio relativo ao áudio gravado. |
| nível de equilíbrio | Um número real no intervalo \[-1,1\] ou um número real no intervalo \[-100,100\] terminando com o caractere <"%"> (por exemplo, "30%").  <p>O valor padrão é 0.</p> | Nível de equilíbrio do áudio (-1 à esquerda e +1 à direita). |
| nível agudo | Um número real no intervalo \[0,1\] ou um número real no intervalo \[0,100\] terminando com o caractere <"%"> (por exemplo, "30%").  <p>O valor padrão é 1.</p> | Configuração de agudos, relativa ao áudio gravado. |
| nível de graves | Um número real no intervalo \[0,1\] ou um número real no intervalo \[0,100\] terminando com o caractere <"%"> (por exemplo, "30%").  <p>O valor padrão é 1.</p> | Configuração de graves, relativa ao áudio gravado. |
| congelar | <p>"verdadeiro" ou "falso".</p><p>O valor padrão é "falso".</p> | Esta propriedade define o que acontecerá com um objeto ao final de sua apresentação, se o conteúdo final estiver congelado ("true") ou não ("false"). |
| transIn, transOut | Uma lista no formato <"(type,subtype,dur,startProgress,endProgress)"> onde: <ul> <li class="level1"><div class="li"> "type" é "fade" por padrão, </div></li> <li class="level1"><div class="li"> "subtipo" é "fade" por padrão,</div></li> <li class="level1"><div class="li">A propriedade "explicitDur" é especificada de acordo com um dos seguintes sintaxe:</div></li> <ol> <li class="level1"><div class="li">"Horas:Minutos:Segundos.Fração", onde "Horas" é um número inteiro no intervalo \[0,23\], "Minutos" é um número inteiro no intervalo \[0,59\], "Segundos" é um número inteiro no intervalo \[0,59\] e "Fração" é um número inteiro positivo.</div></li> <li class="level1"><div class="li">Seconds"s", onde Segundos é um real positivo number.</div></li> </ol> <li class="level1"><div class="li">"startProgress" é um número real no intervalo \[0,1\], e "endProgress" é um número real no intervalo \[0,1\].</div></li> </ul> <p>O valor padrão da propriedade é a string vazia. Se uma transição for especificada, então:</p> <ul> <li class="level1"><div class="li"> A duração padrão de "dur" é "1s",</div></li> <li class="level1"><div class="li"> O valor padrão de "startProgress" é 0,</div></li> <li class="level1"><div class="li"> O valor padrão de "endProgress" é 1.</div></li> </ul> | <p>O tipo de *transIn* e *transOut* é sempre "fade" e o *subtype* é sempre "fade" e é definido por padrão.</p> <p>O atributo *dur* especifica a duração da transição.</p> <p>O atributo *startProgress* especifica a quantidade de progresso durante a transição em que a execução deve ser iniciada.</p> <p>O atributo *endProgress* especifica a quantidade de progresso em que a transição deve ser finalizada. O valor deste atributo deve ser maior ou igual ao valor do atributo *startProgress*. Se *endProgress* for igual a *startProgress*, então a transição permanecerá em um progresso fixo durante a transição.</p> |

#### Propriedades predefinidas para &lt;media&gt;  elementos com conteúdo textual { data-search-exclude }

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

#### Propriedades predefinidas para &lt;media&gt;  elementos do tipo "application/x-ncl-settings" { data-search-exclude }

O grupo *sistema*.  Conjunto de propriedades gerenciadas pelo sistema receptor.
Eles podem ser lidos, mas não podem ter seus valores alterados por uma NCL
aplicação, um procedimento Lua ou qualquer outro código imperativo ou declarativo
procedimento.  Os aplicativos nativos do receptor podem alterar essas propriedades'
valores.  Eles devem persistir durante todo o ciclo de vida do receptor.

| Nome | Valor | Descrição |
| --- | --- | --- |
| idioma do sistema | Código ISO 639-1. | Linguagem de áudio. |
| sistema.caption | Código ISO 639-1. | Idioma da legenda. |
| sistema.subtitle | Código ISO 639-1. | Idioma da legenda. |
| sistema.returnBitRate(i) | Número real. | A taxa de bits total do canal interativo (i) em quilobytes por segundo. |
| sistema.screenSize | (Inteiro, Inteiro). | Tamanho da tela do dispositivo, em (linhas, pixels/linha), quando uma classe não está definida. |
| system.screenGraphicSize | (Inteiro, Inteiro). | Resolução definida para o plano gráfico da tela do dispositivo, em (linhas, pixels/linha), quando não há classe definida. |
| sistema.audioType | "mono", "estéreo" ou "5.1". | Tipo de áudio do dispositivo, quando uma classe não está definida. |
| sistema.screenSize(i) | (Inteiro, Inteiro). | Tamanho da tela da classe (i) de dispositivos, em (linhas, pixels/linha). |
| system.screenGraphicSize(i) | (Inteiro, Inteiro). | Resolução definida para o plano gráfico da tela da classe (i) de dispositivos, em (linhas, pixels/linha). |
| sistema.audioType(i) | "mono", "estéreo" ou "5.1". | Tipo de áudio da classe (i) de dispositivos. |
| sistema.devNumber(i) | Inteiro. | Número de dispositivos de exposição cadastrados na classe (i). |
| sistema.classType(i) | "passivo" ou "ativo". | Tipo da classe (i). |
| system.parentDeviceRegion(i) | Cinco números separados por vírgula; cada um seguindo a regra de valor especificada para as propriedades "left", "top", "width", "height" e "zIndex", respectivamente. | Identifica um elemento [&lt;region&gt;](region.md) em outro [&lt;regionBase&gt;](regionbase.md) associado ao dispositivo pai que cria o mapa de bits enviado aos dispositivos de classe passiva (i); na região especificada o mapa de bits enviado também deverá ser exibido. |
| sistema.info(i) | Corda. | Lista dos reprodutores de mídia da classe (i). |
| sistema.classNumber | Inteiro. | Número de classes que foram definidas. |
| sistema.CPU | Número real. | Desempenho da CPU no MIPS, quanto à sua capacidade de executar aplicações. |
| memória do sistema | Inteiro. | Espaço mínimo de memória em megabytes fornecido aos aplicativos. |
| sistema.sistema operacional | String (a ser definida). | Tipo do sistema operacional. |
| system.luaVersion | String (a ser definida). | Versão do mecanismo Lua suportada pelo receptor. |
| sistema.ncl.versão | String (a ser definida). | Versão da linguagem NCL. |
| sistema.GingaNCL.versão | String (a ser definida). | Versão do ambiente Ginga-NCL. |
| sistema.xyz | Corda. | Qualquer propriedade com o prefixo "sistema" é reservada para uso futuro. |

O grupo *usuário*.  Conjunto de propriedades gerenciadas pelo sistema receptor.
Eles podem ser lidos, mas não podem ter seus valores alterados por uma NCL
aplicação, um procedimento Lua ou qualquer outro código imperativo ou declarativo
procedimento.  Os aplicativos nativos do receptor podem alterar as propriedades
valores.  Eles devem persistir durante todo o ciclo de vida do receptor.

| Nome | Valor | Descrição |
| --- | --- | --- |
| usuário.idade | Inteiro. | Idade do usuário. |
| usuário.localização | Corda. | Localização do usuário. |
| usuário.gênero | "m" (masculino) ou "f" (feminino). | Gênero do usuário. |
| usuário.xyz | Corda. | Qualquer propriedade com o prefixo "usuário" é reservada para uso futuro. |

O grupo *padrão*.  Conjunto de propriedades gerenciadas pelo receptor
sistema.  Eles podem ser lidos e ter seus valores alterados por um NCL
aplicação, um procedimento Lua ou qualquer outro código imperativo ou declarativo
procedimento.  Os aplicativos nativos do receptor podem alterar as propriedades
valores.  Eles devem persistir durante todo o ciclo de vida do receptor, no entanto, são
ajustados para seus valores iniciais quando um novo canal é sintonizado.

| Nome | Valor | Descrição |
| --- | --- | --- |
| padrão.focusBorderColor | "branco", "preto", "prata", "cinza", "vermelho", "marrom", "fúcsia", "roxo", "limão", "verde", "amarelo", "oliva", "azul", "marinho", "água" ou "verde-azulado". | Cor padrão aplicada à borda de um elemento em foco. |
| padrão.selBorderColor | "branco", "preto", "prata", "cinza", "vermelho", "marrom", "fúcsia", "roxo", "limão", "verde", "amarelo", "oliva", "azul", "marinho", "água" ou "verde-azulado". | Cor padrão aplicada à borda de um elemento em foco quando ativado. |
| padrão.focusBorderWidth | Inteiro. | Largura padrão (em pixels) aplicada à borda de um elemento em foco. |
| default.focusBorderTransparency | Número no intervalo \[0,1\] ou \[0,100\], terminando com o caractere <"%"> (por exemplo, "30%"), com "1" ou "100%" significando transparência total e "0" ou "0%" significando nenhuma transparência. | Transparência padrão aplicada à borda de um elemento em foco. |
| padrão.xyz | Corda. | Qualquer propriedade com o prefixo "default" é reservada para uso futuro. |

O grupo *serviço*.  Conjunto de propriedades gerenciadas pelo formatador NCL.
Eles podem ser lidos e ter seus valores alterados por uma aplicação NCL do
mesmo serviço.  Eles podem ser lidos, mas não podem ter seus valores alterados
por um procedimento Lua ou qualquer outro procedimento de código imperativo ou declarativo.
As alterações de variáveis ​​devem ser feitas usando comandos NCL.  Eles devem persistir em
pelo menos durante o ciclo de vida do serviço.

| Nome | Valor | Descrição |
| --- | --- | --- |
| serviço.currentFocus | Inteiro. | O valor *focusIndex* do elemento [&lt;media&gt;](media.md) em foco. |
| serviço.currentKeyMaster | Corda. | Identificador *id* do elemento [&lt;media&gt;](media.md) que controla as chaves de navegação; se o elemento [&lt;media&gt;](media.md) não estiver sendo apresentado ou não estiver pausado, o controle da chave de navegação pertence ao formatador NCL. |
| serviço.xyz | Corda. | Qualquer propriedade com o prefixo "serviço" segue as regras especificadas para o grupo. |

O grupo *si*.  Conjunto de propriedades gerenciadas pelo middleware.  Eles
podem ser lidos, mas não podem ter seus valores alterados por um NCL
aplicação, um procedimento Lua ou qualquer outro código imperativo ou declarativo
procedimento.  Eles devem persistir pelo menos até a próxima sintonia de canal.

| Nome | Valor | Descrição |
| --- | --- | --- |
| si.numberOfServices | Inteiro. | Número de serviços disponíveis no país para o canal sintonizado. Nota: O valor desta variável deve ser obtido a partir do número de tabelas PMT especificadas na tabela PAT do fluxo de transporte recebido no canal de sintonia (ver ISO/IEC 13818-1:2007). O valor da variável deve levar em consideração apenas as tabelas PMT cujos campos country_code, especificados no descritor country_availability_descriptor (ver Seção 8.3.6 da ABNT NBR 15603-2:2007) relacionados à tabela, são equivalentes ao valor da variável "user.location" do nó *settings*. |
| si.numberOfPartialServices | Inteiro | Número de serviços de 1 segmento disponíveis no país para o canal sintonizado. Nota: O valor desta variável deve ser obtido a partir do número de tabelas PMT especificadas na tabela PAT do fluxo de transporte recebido no canal de sintonia (ver ISO/IEC 13818-1:2007). O valor da variável deve levar em consideração apenas as tabelas PMT cujos campos country_code, especificados no country_availability_descriptor (ver Seção 8.3.6 da ABNT NBR 15603-2:2007) relacionado à tabela, sejam iguais ao valor da variável "user.location" do nó *settings*, e cujos campos program_number sejam equivalentes aos campos service_id do parcial_reception_descriptor relacionado às tabelas NIT. |
| si.canalNumber | Inteiro | Número do canal sintonizado. Nota: O valor desta variável deve ser obtido no campo remote_control_key_id do descritor ts_information_descriptor (ver Seção 8.3.42 da ABNT NBR 15603-2:2007) da tabela NIT (ver Seção 7.2.4 da ABNT NBR 15603-2:2007) que descreve o serviço atual. |
| si.xyz | Corda | Qualquer propriedade com o prefixo "si" segue as regras especificadas para o grupo. |

O grupo *canal*.  Conjunto de propriedades gerenciadas pelo formatador NCL.
Eles podem ser lidos e ter seus valores alterados por uma aplicação NCL do
mesmo canal.  Eles podem ser lidos, mas não podem ter seus valores alterados
por um procedimento Lua ou qualquer outro procedimento de código imperativo ou declarativo de
o mesmo canal; alterações de variáveis ​​devem ser feitas usando comandos NCL.  Eles
deve persistir pelo menos até a próxima sintonia de canal.

| Nome | Valor | Descrição |
| --- | --- | --- |
| canal.keyCapture | Corda | Solicitação de chaves alfanuméricas para aplicações NCL. |
| canal.virtualTeclado | "verdadeiro" ou "falso" | Solicitação de teclado virtual para aplicações NCL. |
| canal.keyboardBounds | (Inteiro, Inteiro, Inteiro, Inteiro) | Região do teclado virtual (esquerda, superior, largura, altura). |
| canal.xyz | Corda | Qualquer variável com o prefixo "canal" segue as regras especificadas para o grupo. |

O *compartilhado*.  Conjunto de propriedades gerenciadas pelo formatador NCL.  Eles
podem ser lidos e ter seus valores alterados por uma aplicação NCL.  Eles podem
ser lidos, mas não podem ter seus valores alterados por um procedimento Lua ou qualquer
outro procedimento de código imperativo ou declarativo; mudanças de variáveis devem ser
feito usando comandos NCL.  Eles devem persistir pelo menos durante o ciclo de vida
do serviço que os definiu.

| Nome | Valor | Descrição |
| --- | --- | --- |
| compartilhado.xyz | Corda | Qualquer propriedade com o prefixo "compartilhado" segue as regras especificadas para o grupo. |

#### Nomes reservados para definição de cores { data-search-exclude }

<table class="inline">
<tbody>
<tr class="row0">
  <th>Cor</th>
  <th>Nome</th>
  <th>Hexadecimal</th>
  <th>(R,G,B)</th>
  <th>Matiz</th>
  <th>(Saturação, Luz)</th>
  <th>(Saturação, Valor)</th>
</tr>
<tr>
<td bgcolor="#ffffff"/>
<td>Branco</td>
<td>#ffffff</td>
<td>(100%, 100%, 100%)</td>
<td>0°;</td>
<td>(0%, 100%)</td>
<td>(0%, 100%)</td>
</tr>

<tr>
<td bgcolor="#c0c0c0"/>
<td>Prata</td>
<td>#c0c0c0</td>
<td>(75%, 75%, 75%)</td>
<td>0°;</td>
<td>(0%, 75%)</td>
<td>(0%, 75%)</td>
</tr>

<tr>
<td bgcolor="#808080"/>
<td>Cinza</td>
<td>#808080</td>
<td>(50%, 50%, 50%)</td>
<td>0°;</td>
<td>(0%, 50%)</td>
<td>(0%, 50%)</td>
</tr>

<tr>
<td bgcolor="#000000"/>
<td>Preto</td>
<td>#000000</td>
<td>(0%, 0%, 0%)</td>
<td>0°;</td>
<td>(0%, 0%)</td>
<td>(0%, 0%)</td>
</tr>

<tr>
<td bgcolor="#ff0000"/>
<td>Vermelho</td>
<td>#ff0000</td>
<td>(100%, 0%, 0%)</td>
<td>0°;</td>
<td>(100%, 50%)</td>
<td>(100%, 100%)</td>
</tr>

<tr>
<td bgcolor="#800000"/>
<td>Marrom</td>
<td>#800000</td>
<td>(50%, 0%, 0%)</td>
<td>0°;</td>
<td>(100%, 25%)</td>
<td>(100%, 50%)</td>
</tr>

<tr>
<td bgcolor="#ffff00"/>
<td>Amarelo</td>
<td>#ffff00</td>
<td>(100%, 100%, 0%)</td>
<td>60°;</td>
<td>(100%, 50%)</td>
<td>(100%, 100%)</td>
</tr>

<tr>
<td bgcolor="#808000"/>
<td>Olive</td>
<td>#808000</td>
<td>(50%, 50%, 0%)</td>
<td>60°;</td>
<td>(100%, 25%)</td>
<td>(100%, 50%)</td>
</tr>

<tr>
<td bgcolor="#00ff00"/>
<td>Lime</td>
<td>#00ff00</td>
<td>(0%, 100%, 0%)</td>
<td>120°;</td>
<td>(100%, 50%)</td>
<td>(100%, 100%)</td>
</tr>

<tr>
<td bgcolor="#008000"/>
<td>Verde</td>
<td>#008000</td>
<td>(0%, 50%, 0%)</td>
<td>120°;</td>
<td>(100%, 25%)</td>
<td>(100%, 50%)</td>
</tr>

<tr>
<td bgcolor="#00ffff"/>
<td>Aqua</td>
<td>#00ffff</td>
<td>(0%, 100%, 100%)</td>
<td>180°;</td>
<td>(100%, 50%)</td>
<td>(100%, 100%)</td>
</tr>

<tr>
<td bgcolor="#008080"/>
<td>Teal</td>
<td>#008080</td>
<td>(0%, 50%, 50%)</td>
<td>180°;</td>
<td>(100%, 25%)</td>
<td>(100%, 50%)</td>
</tr>

<tr>
<td bgcolor="#0000ff"/>
<td>Azul</td>
<td>#0000ff</td>
<td>(0%, 0%, 100%)</td>
<td>240°;</td>
<td>(100%, 50%)</td>
<td>(100%, 100%)</td>
</tr>

<tr>
<td bgcolor="#000080"/>
<td>Marinha</td>
<td>#000080</td>
<td>(0%, 0%, 50%)</td>
<td>240°;</td>
<td>(100%, 25%)</td>
<td>(100%, 50%)</td>
</tr>

<tr>
<td bgcolor="#ff00ff"/>
<td>Fúcsia</td>
<td>#ff00ff</td>
<td>(100%, 0%, 100%)</td>
<td>300°;</td>
<td>(100%, 50%)</td>
<td>(100%, 100%)</td>
</tr>

<tr>
<td bgcolor="#800080"/>
<td>Roxo</td>
<td>#800080</td>
<td>(50%, 0%, 50%)</td>
<td>300°;</td>
<td>(100%, 25%)</td>
<td>(100%, 50%)</td>
</tr>

</tbody>
</table>