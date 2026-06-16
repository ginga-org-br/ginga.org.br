---
title: "Elemento &lt;property&gt;"
---

# &lt;property&gt;

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

| Nombre | Valor | Descripción |
| --- | --- | --- |
| style | URI. | El localizador de un archivo de hoja de estilo que especifica otras propiedades para el objeto. |
| player | Cadena. | <p>Identifica la herramienta de presentación que se utilizará.</p>  <p>Si no se especifica, el reproductor está determinado por el tipo de objeto, definido por el atributo *type* del elemento [&lt;media&gt;](media.md), o se infiere por la extensión de archivo del valor del atributo *src* del elemento [&lt;media&gt;](media.md).</p> |
| reusePlayer | <p>"true" o "false".</p><p>El valor predeterminado es "false".</p> | Especifica si se debe instanciar un nuevo reproductor ("false") o si se debe utilizar un reproductor ya instanciado ("true"). |
| playerLife | <p>"close" o "keep".</p>  <p>El valor predeterminado es "close".</p> | Especifica qué sucederá con la instancia del reproductor al final de la presentación del objeto. |
| deviceClass | <p>"systemScreen(i)" o "systemAudio(i)", donde *i* es un entero no negativo.</p><p>El valor predeterminado es la misma clase de dispositivo que ejecuta el reproductor NCL.</p> | <p>Especifica la clase de dispositivo donde se presentará el objeto multimedia.</p>   <p>Existen dos tipos diferentes de clases de dispositivos: activa y pasiva. En una clase activa, un dispositivo es capaz de ejecutar algunos reproductores multimedia para presentaciones de elementos [&lt;media&gt;](media.md). En una clase pasiva, no se requiere que un dispositivo ejecute reproductores multimedia, solo que exhiba un mapa de bits o una secuencia de muestras de audio recibidas de otro dispositivo.</p>   <p>Los valores "systemScreen(1)" y "systemAudio(1)" están reservados para clases pasivas, y "systemScreen(2)" y "systemAudio(2)" están reservados para clases activas.</p> |
| explicitDur | <p>La propiedad "explicitDur" se especifica de acuerdo con una de las siguientes sintaxis:</p>   <ol>  <li>"Hours:Minutes:Seconds.Fraction", donde "Hours" es un entero en el intervalo \[0,23\], "Minutes" es un entero en el intervalo \[0,59\], "Seconds" es un entero en el intervalo \[0,59\] y "Fraction" es un entero positivo.</li>  <li>Seconds"s", donde Seconds es un número real positivo.</li>  </ol>   <p>Para medios continuos, el valor predeterminado se establece en la duración del contenido; de lo contrario, debe establecerse en nulo (*nil*).</p> | Define la duración explícita de un objeto. |
| focusIndex | <p>Entero positivo.</p>  <p>Cuando esta propiedad no está definida, el objeto se considera como si no pudiera recibir foco.</p> | <p>Especifica un índice para el elemento [&lt;media&gt;](media.md) al que se puede aplicar el foco.</p>   <p>Nota: Cuando se selecciona un elemento en foco presionando la tecla de activación ("SELECT" o "ENTER"), el control de foco se pasará al renderizador (reproductor) del elemento [&lt;media&gt;](media.md). El reproductor puede entonces seguir sus propias reglas de navegación. El control de foco volverá al reproductor NCL cuando se presione la tecla de retroceso (*back*). En este caso, el foco pasa al elemento identificado por la propiedad "service.currentFocus" del nodo de configuraciones (elemento [&lt;media&gt;](media.md) del tipo "application/x-ncl-settings").</p> |
| moveLeft | Entero positivo. | Especifica un valor igual al valor *focusIndex* asociado al elemento al que se debe aplicar el foco cuando se presiona la tecla de flecha izquierda. Cuando el foco se aplica a un elemento con la propiedad *visible* establecida en "false", o a un elemento que no se está presentando, el foco actual no se mueve. |
| moveRight | Entero positivo. | Especifica un valor igual al valor *focusIndex* asociado al elemento al que se debe aplicar el foco cuando se presiona la tecla de flecha derecha. Cuando el foco se aplica a un elemento con la propiedad *visible* establecida en "false", o a un elemento que no se está presentando, el foco actual no se mueve. |
| moveUp | Entero positivo. | Especifica un valor igual al valor *focusIndex* asociado al elemento al que se debe aplicar el foco cuando se presiona la tecla de flecha arriba. Cuando el foco se aplica a un elemento con la propiedad *visible* establecida en "false", o a un elemento que no se está presentando, el foco actual no se mueve. |
| moveDown | Entero positivo. | Especifica un valor igual al valor *focusIndex* asociado al elemento al que se debe aplicar el foco cuando se presiona la tecla de flecha abajo. Cuando el foco se aplica a un elemento con la propiedad *visible* establecida en "false", o a un elemento que no se está presentando, el foco actual no se mueve. |

#### Propiedades predefinidas para &lt;media&gt; elementos con contenido visual { data-search-exclude }

| Nombre | Valor | Descripción |
| --- | --- | --- |
| top | <p>Un número real en el rango \[0,100\] que termina con el carácter "%" (por ejemplo, 30%), o un valor entero no negativo que especifica el atributo en píxeles. Para valores en píxeles, el calificador de unidad "px" puede omitirse.</p>   <p>El valor predeterminado es "0%", si el valor de *bottom* no está especificado.</p> | Posición superior del contenido, expresada como un porcentaje de la dimensión de altura del dispositivo de exhibición, o como un valor absoluto. Coloca la posición superior del contenido a exhibir a la distancia especificada desde el borde superior del dispositivo de exhibición. |
| bottom | <p>Si se especifican los valores "top" y "height", debe calcularse en función de estos valores. De lo contrario, debe ser un número real en el rango \[0,100\] que termina con el carácter "%" (por ejemplo, 30%), o un valor entero no negativo que especifica el atributo en píxeles. Para valores en píxeles, el calificador de unidad "px" puede omitirse.</p>   <p>El valor predeterminado es "0%", si el valor del atributo no puede calcularse a partir de los atributos *height* y *top*.</p> | Posición inferior del contenido, expresada como un porcentaje de la dimensión de altura del dispositivo de exhibición, o como un valor absoluto. Coloca la posición inferior del contenido a exhibir a la distancia especificada desde el borde inferior del dispositivo de exhibición. |
| left | <p>Un número real en el rango \[0,100\] que termina con el carácter "%" (por ejemplo, 30%), o un valor entero no negativo que especifica el atributo en píxeles. Para valores en píxeles, el calificador de unidad "px" puede omitirse.</p>   <p>El valor predeterminado es "0%", si el valor de *right* no está especificado.</p> | Posición izquierda del contenido, expresada como un porcentaje de la dimensión de ancho del dispositivo de exhibición, o como un valor absoluto. Coloca la posición izquierda del contenido a exhibir a la distancia especificada desde el borde izquierdo del dispositivo de exhibición. |
| right | <p>Si se especifican los valores *left* y *width*, debe calcularse en función de estos valores. De lo contrario, debe ser un número real en el rango \[0,100\] que termina con el carácter "%" (por ejemplo, 30%), o un valor entero no negativo que especifica el atributo en píxeles. Para valores en píxeles, el calificador de unidad "px" puede omitirse.</p>   <p>El valor predeterminado es "0%", si el valor del atributo no puede calcularse a partir de los atributos *width* y *left*.</p> | Posición derecha del contenido, expresada como un porcentaje de la dimensión de ancho del dispositivo de exhibición, o como un valor absoluto. Coloca la posición derecha del contenido a exhibir a la distancia especificada desde el borde derecho del dispositivo de exhibición. |
| width | <p>Un número real en el rango \[0,100\] que termina con el carácter "%" (por ejemplo, 30%), o un valor entero no negativo que especifica el atributo en píxeles. Para valores en píxeles, el calificador de unidad "px" puede omitirse.</p>   <p>El valor predeterminado es "0%".</p> | Ancho del contenido a exhibir, expresado como un porcentaje de la dimensión de ancho del dispositivo de exhibición, o como un valor absoluto. |
| height | <p>Un número real en el rango \[0,100\] que termina con el carácter "%" (por ejemplo, 30%), o un valor entero no negativo que especifica el atributo en píxeles. Para valores en píxeles, el calificador de unidad "px" puede omitirse.</p>   <p>El valor predeterminado es "0%".</p> | Altura del contenido a exhibir, expresada como un porcentaje de la dimensión de altura del dispositivo de exhibición, o como un valor absoluto. |
| location | Consulte las propiedades "left" y "top". | Dos números separados por coma, cada uno siguiendo la regla especificada para las propiedades "left" y "top", respectivamente. |
| size | Consulte las propiedades "width" y "height". | Dos números separados por coma, cada uno siguiendo la regla especificada para las propiedades "width" y "height", respectivamente. |
| bounds | Consulte las propiedades "left", "top", "width" y "height". | Cuatro números separados por coma, cada uno siguiendo la regla especificada para las propiedades "left", "top", "width" y "height", respectivamente. |
| background | <p>"white", "black", "silver", "gray", "red", "maroon", "fuchsia", "purple", "lime", "green", "yellow", "olive", "blue", "navy", "aqua" o "teal". También puede ser el valor reservado "transparent".</p>   <p>El valor predeterminado es "transparent".</p> | El color de fondo utilizado para rellenar el área de una región donde se muestra el contenido multimedia que no está ocupada por el propio contenido. |
| rgbChromakey | <p>Color RGB definido mediante notación hexadecimal (hex) para la combinación de valores de color Rojo, Verde y Azul (RGB). El valor más bajo que se puede asignar a una de las fuentes de luz es 0 (hex 00). El valor más alto es 255 (hex FF).</p>   <p>También puede definirse mediante las palabras reservadas: "white", "black", "silver", "gray", "red", "maroon", "fuchsia", "purple", "lime", "green", "yellow", "olive", "blue", "navy", "aqua" o "teal".</p> | El color RGB que se establecerá como transparente. |
| visible | <p>"true" o "false".</p><p>El valor predeterminado es "false".</p> | <p>Permite que la presentación del objeto sea visible u oculta.</p>   <p>Cuando la propiedad *visible* asociada con un elemento [&lt;context&gt;](context.md) o [&lt;body&gt;](body.md) es igual a "true", se tiene en cuenta la propiedad *visible* de cada elemento secundario de la composición para definir cómo se exhibirá cada uno de ellos.</p>   <p>Cuando la propiedad *visible* asociada con un elemento [&lt;context&gt;](context.md) o [&lt;body&gt;](body.md) es igual a "false", todos los elementos secundarios de la composición se exhiben como ocultos.</p>   <p>Cabe señalar que un objeto con una propiedad *visible* igual a "false", es decir, un objeto exhibido como oculto, no puede tener ninguna de sus anclas de contenido seleccionada mientras el valor de la propiedad *visible* persista como "false".</p>   <p>Cuando un documento tiene su elemento [&lt;body&gt;](body.md) con su propiedad *visible* establecida en "false" y su evento de presentación está en estado pausado, se dice que el documento está en espera (*stand-by*). En el estándar ISDB-T, cuando solo hay una aplicación en ejecución y esta aplicación está en *stand-by*, el video principal del servicio se dimensiona al 100% de la pantalla y el audio principal se establece al 100% de su volumen.</p> |
| transparency | <p>Un número real en el rango \[0,1\] o un número real en el rango \[0,100\] que termina con el carácter "%" (por ejemplo, "30%").</p>   <p>El valor predeterminado es "0%".</p> | Indica el grado de transparencia de la presentación de un objeto: "1" o "100%" significa transparencia total y "0" o "0%" significa opaco. |
| fit | <p>"fill", "hidden", "meet", "meetBest" o "slice".</p>  <p>El valor predeterminado es "fill".</p> | <p>Indica cómo se presentará un objeto.</p>   <p>"fill": escala el contenido multimedia del objeto para que toque todos los bordes del cuadro definido por las propiedades "width" y "height" del objeto.</p>   <p>"hidden": si la "height" ("width") intrínseca del contenido multimedia es menor que la propiedad "height" ("width"), el objeto debe renderizarse comenzando desde el borde "top" ("left") y rellenar el resto de la "height" ("width") con el color de fondo; si la "height" ("width") intrínseca del contenido multimedia es mayor que la propiedad "height" ("width"), el objeto debe renderizarse comenzando desde el borde superior (izquierdo) hasta alcanzar la altura (ancho) definida en la propiedad; la parte del contenido multimedia debajo (a la derecha) de la altura (ancho) se recorta.</p>   <p>"meet": escala el objeto multimedia visual preservando su relación de aspecto hasta que su altura o ancho sea igual al valor especificado por las propiedades "height" o "width". La esquina superior izquierda del contenido multimedia se posiciona en las coordenadas superiores izquierdas del cuadro; el espacio vacío a la derecha o abajo debe rellenarse con el color de fondo.</p>   <p>"meetBest": la semántica es idéntica a "meet", excepto que la imagen no se escala más allá del 100% en ninguna dimensión. "slice": escala el contenido multimedia visual preservando su relación de aspecto hasta que su altura o ancho sean iguales al valor especificado en las propiedades "height" y "width" y el cuadro de presentación definido esté completamente lleno. Algunas partes del contenido pueden recortarse. El exceso de ancho se recorta desde la derecha del objeto multimedia. El exceso de altura se recorta desde la parte inferior del objeto multimedia.</p> |
| scroll | <p>"none", "horizontal", "vertical", "both" o "automatic".</p>  <p>El valor predeterminado es 0.</p> | Permite especificar cómo se configura el desplazamiento (*scroll*) en una región de exhibición. |
| zIndex | <p>Un número entero en el rango \[0,255\].</p>  <p>El valor predeterminado es 0.</p> | El atributo *zIndex* especifica la precedencia de superposición, donde los objetos con mayores valores de *zIndex* se apilan encima de los objetos con menores valores de *zIndex*. |
| plan | <p>"video", "graphic" o "background".</p>   <p>El valor predeterminado es "video" para medios cuyo atributo *src* hace referencia a un PES de un flujo de transporte, o "graphic" para todos los demás casos.</p> | Define en qué plano de una pantalla estructurada se colocará un objeto. |
| focusBorderColor | <p>"white", "black", "silver", "gray", "red", "maroon", "fuchsia", "purple", "lime", "green", "yellow", "olive", "blue", "navy", "aqua" o "teal".</p>   <p>El valor predeterminado está definido por la propiedad "default.focusBorderColor" del objeto *settings*.</p> | Define el color para decorar la región de la pantalla donde se presenta el objeto en foco, antes de ser seleccionado. |
| selBorderColor | <p>"white", "black", "silver", "gray", "red", "maroon", "fuchsia", "purple", "lime", "green", "yellow", "olive", "blue", "navy", "aqua" o "teal".</p>   <p>El valor predeterminado está definido por la propiedad "default.selBorderColor" del objeto *settings*.</p> | Define el color para decorar la región de la pantalla donde se presenta el objeto en foco, después de ser seleccionado. |
| focusBorderWidth | <p>Entero.</p>  <p>El valor predeterminado está definido por la propiedad "default.focusBorderWidth" del objeto *settings*.</p> | Ancho (en píxeles) aplicado al borde de un elemento en foco (0 significa que no aparecerá ningún borde, valores positivos significan que el borde está fuera del contenido del objeto y valores negativos significan que el borde se dibuja sobre el contenido del objeto). |
| focusBorderTransparency | <p>Un valor real entre 0 y 1, o un valor real en el rango \[0,100\] que termina con el carácter "%" (por ejemplo, "30%").</p>   <p>El valor predeterminado está definido por la propiedad "default.focusBorderTransparency" del objeto *settings*.</p> | Transparencia aplicada al borde de un elemento en foco, con "1" o "100%" significando transparencia total y "0" o "0%" significando ninguna transparencia. |
| focusSrc | <p>Los siguientes son valores válidos:</p><ul><li><code>file:///file_path/#fragment_identifier</code>  -- para archivos locales,</li><li><code>http://server_identifier/file_path/#fragment_identifier</code>  -- para archivos remotos descargados mediante el protocolo HTTP,</li><li><code>https://server_identifier/file_path/#fragment_identifier</code>  -- para archivos remotos descargados mediante el protocolo HTTPS,</li><li><code>rtsp://server_identifier/file_path/#fragment_identifier</code>  -- para flujos descargados mediante el protocolo RTSP,</li><li><code>rtp://server_identifier/file_path/#fragment_identifier</code>  -- para flujos descargados mediante el protocolo RTP,</li><li><code>ncl-mirror://media_element_identifier</code> -- para un flujo de contenido idéntico al que está en presentación por otro elemento [&lt;media&gt;](media.md),</li><li><code>sbtvd-ts:</code> o <code>isdb-ts:</code>  o <code>ts://program_number.component_tag</code> -- para flujos elementales recibidos del flujo de transporte.</li></ul><p>Para el atributo *focusSrc* cuyo valor identifica el esquema "sbtvd-ts", "isdb-ts" o "ts", el "program_number.component_tag" puede sustituirse por las siguientes palabras reservadas:</p><ul><li>"video" -- correspondiente al ES de video primario presentado en el plano de video,</li><li>"audio"  -- correspondiente al ES de audio primario,</li><li>"text" -- correspondiente al ES de texto primario,</li><li>"video(i)" -- correspondiente al *i*-ésimo menor "component_tag" de ES de video listado en la PMT de los servicios sintonizados,</li><li>"audio(i)" -- correspondiente al *i*-ésimo menor "component_tag" de ES de audio listado en la PMT de los servicios sintonizados, o</li><li>"text(i)" -- correspondiente al *i*-ésimo menor "component_tag" de ES de texto listado en la PMT de los servicios sintonizados.</li></ul> | Especifica una fuente multimedia alternativa para presentarse, en lugar de la presentación actual, si un elemento recibe el foco. Este atributo sigue las mismas reglas que el atributo *src* del elemento [&lt;media&gt;](media.md). |
| focusSelSrc | Igual que para *focusSrc*. | Especifica una fuente multimedia alternativa para presentarse, en lugar de la presentación actual, cuando se selecciona un elemento en foco presionando la tecla de activación ("SELECT" o "ENTER"). Este atributo sigue las mismas reglas que el atributo *src* del elemento [&lt;media&gt;](media.md). |
| freeze | "true" o "false". El valor predeterminado es "false". | Define qué sucederá con un objeto al final de su presentación, si el contenido final se congela ("true") o no ("false"). El valor predeterminado es "false". |
| transIn, transOut | <p>Lista de (type, subtype, dur, startProgress, endProgress, direction, fadeColor, horzRepeat, vertRepeat, borderWidth, borderColor) separados por punto y coma donde:</p>  <ul>  <li> El *type* obligatorio puede ser: "barWipe", "irisWipe", "clockWipe", "snakeWipe" o "fade". Para ver la lista completa de los tipos de transición predefinidos, consulte: http://www.w3.org/TR/SMIL2/smil-transitions.html#TransitionEffects-Appendix.</li>  <li>Los valores obligatorios de *subtype* dependen de los valores de *type*, según se define: "leftToRight" para "barWipe", "rectangle" para "irisWipe", "clockwiseTwelve" para "clockWipe", "topLeftHorizontal" para "snakeWipe" y "crossfade" para "fade". Para ver la lista completa de los subtipos de transición predefinidos, consulte: http://www.w3.org/TR/SMIL2/smil-transitions.html#TransitionEffects-Appendix.</li>  <li>El atributo *dur* se especifica de acuerdo con una de las siguientes sintaxis: (i) "Hours:Minutes:Seconds.Fraction", donde "Hours" es un entero en el intervalo \[0,23\], "Minutes" es un entero en el intervalo \[0,59\], "Seconds" es un entero en el intervalo \[0,59\] y "Fraction" es un entero positivo; (ii) Seconds"s", donde "Seconds" es un número real positivo. El valor predeterminado es "0s".</li>  <li>*startProgress* y *endProgress* son números reales en el rango \[0,1\].</li>  <li>Los valores de *direction* son "forward" y "reverse".</li>  <li>*fadeColor* es "white", "black", "silver", "gray", "red", "maroon", "fuchsia", "purple", "lime", "green", "yellow", "olive", "blue", "navy", "aqua" o "teal".</li>  <li>*horzRepeat* y *vertRepeat* son enteros positivos.</li>  <li>*borderWidth* es un entero no negativo.</li>  <li>*borderColor* es "white", "black", "silver", "gray", "red", "maroon", "fuchsia", "purple", "lime", "green", "yellow", "olive", "blue", "navy", "aqua" o "teal".</li>  </ul>   <p>El valor predeterminado de la propiedad es la cadena vacía. Si se especifica un tipo de transición, entonces:</p>  <ul>  <li>la duración predeterminada de "dur" es "1s",</li>  <li>el valor predeterminado de "startProgress" es 0,</li>  <li>el valor predeterminado de "endProgress" es 1,</li>  <li>el valor predeterminado de "direction" es "forward",</li>  <li>el valor predeterminado de "fadeColor" es "black",</li>  <li>el valor predeterminado de "horzRepeat" es 1,</li>  <li>el valor predeterminado de "vertRepeat" es 1,</li>  <li>el valor predeterminado de "borderWidth" es 0,</li>  <li>el valor predeterminado de "borderColor" es "black".</li>  </ul> | <p>El valor de *transIn* y *transOut* es una lista de transiciones separadas por punto y coma.</p>   <p>El propósito de la lista separada por punto y coma es permitir a los autores especificar un conjunto de transiciones de respaldo si la transición preferida no está disponible. La primera transición de la lista debe ejecutarse si el agente de usuario ha implementado esta transición. Si no está disponible, se debe ejecutar la segunda transición de la lista, y así sucesivamente.</p>   <p>Los atributos *type* y *subtype* definen la transición. El atributo *dur* especifica la duración de la transición.</p>   <p>El atributo *startProgress* especifica la cantidad de progreso de la transición en la que comenzar la ejecución. Por ejemplo, podemos querer comenzar un *crossfade* con la imagen de destino ya desvanecida en un 30%. En este caso, *startProgress* sería 0.3.</p>   <p>El atributo *endProgress* especifica la cantidad de progreso de la transición en la que finalizar la ejecución. El valor de este atributo debe ser mayor o igual que el valor del atributo *startProgress*. Si *endProgress* es igual a *startProgress*, la transición permanece en un progreso fijo durante toda su duración.</p>   <p>El atributo *direction* especifica la dirección en la que se ejecutará la transición. Tenga en cuenta que no todas las transiciones tendrán interpretaciones inversas significativas. Por ejemplo, un *crossfade* no es una transición geométrica y, por lo tanto, no tiene interpretación de dirección inversa. En las transiciones que no tienen interpretación inversa se debe ignorar el atributo *direction* y asumir el valor predeterminado "forward".</p>   <p>Si el valor del atributo *type* es "fade" y el valor del atributo *subtype* es "fadeToColor" o "fadeFromColor", el atributo *fadeColor* especifica el color final o inicial del desvanecimiento. Si el valor del atributo *type* no es "fade", o el valor del atributo *subtype* no es "fadeToColor" o "fadeFromColor", se ignora el atributo *fadeColor*.</p>   <p>Si el valor del atributo *type* no es "fade", se pueden especificar los siguientes atributos:</p>   <p>El atributo *horzRepeat* especifica cuántas veces realizar el patrón de transición a lo largo del eje horizontal.</p>   <p>El atributo *vertRepeat* especifica cuántas veces realizar el patrón de transición a lo largo del eje vertical.</p>   <p>El atributo *borderWidth* especifica el ancho de un borde generado a lo largo de un borde de barrido (*wipe*).</p>   <p>El atributo *borderColor* especifica el contenido del borde generado a lo largo de un borde de barrido (*wipe*). Si el valor de este atributo es un color, el borde generado se rellena con este color. Si el valor de este atributo es "blend", el borde generado es una mezcla aditiva (o desenfoque) de las fuentes multimedia.</p> |

#### Propiedades predefinidas para &lt;media&gt; elementos con contenido multimedia continuo (solo lectura) { data-search-exclude }

| Nombre | Valor | Descripción |
| --- | --- | --- |
| ID de contenido | <p>String.</p><p>(Establecido solo por el reproductor NCL.)</p> <p>El valor predeterminado es nulo.</p> | La propiedad "contentId" está asociada a objetos de medios continuos cuyo contenido se define haciendo referencia a un flujo elemental. Tiene *null* como valor inicial y se establece en el valor del identificador transportado en el descriptor de referencia NPT (en un campo del mismo nombre: contentId), tan pronto como se inicia el objeto de medios continuos asociado. |
| en espera | <p>"true" o "false".</p> <p>(Establecido solo por el reproductor NCL).</p> <p>El valor predeterminado es "falso".</p> | La propiedad "en espera" se establece en "verdadero" mientras que un contenido de objeto de medios continuos ya iniciado que hace referencia a una secuencia elemental es interrumpido temporalmente por otro contenido entrelazado, en la misma secuencia elemental. |

#### Propiedades predefinidas para &lt;media&gt;  elementos con contenido audible { data-search-exclude }

| Nombre | Valor | Descripción |
| --- | --- | --- |
| nivel de sonido | Un número real en el rango \[0,1\] o un número real en el rango \[0,100\] que termina con el carácter "%" (por ejemplo, "30%").  <p>El valor predeterminado es 1.</p> | Volumen de audio relativo al audio grabado. |
| nivel de equilibrio | Un número real en el rango \[-1,1\] o un número real en el rango \[-100,100\] que termina con el carácter "%" (por ejemplo, "30%").  <p>El valor predeterminado es 0.</p> | Nivel de balance del audio (-1 a la izquierda y +1 a la derecha). |
| nivel de agudos | Un número real en el rango \[0,1\] o un número real en el rango \[0,100\] que termina con el carácter "%" (por ejemplo, "30%").  <p>El valor predeterminado es 1.</p> | Configuración de agudos, relativa al audio grabado. |
| nivel de bajo | Un número real en el rango \[0,1\] o un número real en el rango \[0,100\] que termina con el carácter "%" (por ejemplo, "30%").  <p>El valor predeterminado es 1.</p> | Configuración de graves, relativa al audio grabado. |
| congelar | <p>"verdadero" o "falso".</p><p>El valor predeterminado es "falso".</p> | Esta propiedad define lo que sucederá con un objeto al final de su presentación, si el contenido final está congelado ("verdadero") o no ("falso"). |
| transIn, transOut | Una lista del formato "(type,subtype,dur,startProgress,endProgress)" donde: <ul> <li>"tipo" es "desvanecimiento" de forma predeterminada, </li> <li>"subtipo" es "desvanecido" de forma predeterminada, </li> <li>La propiedad "explicitDur" se especifica de acuerdo con uno de los siguientes sintaxis: <ol> <li>"Horas:Minutos:Segundos.Fracción", donde "Horas" es un número entero en el intervalo \[0,23\], "Minutos" es un número entero en el intervalo \[0,59\], "Segundos" es un número entero en el intervalo \[0,59\] y "Fracción" es un número entero positivo.</li> <li>Segundos"s", donde Segundos es un número real positivo.</li> </ol></li> <li>"startProgress" es un número real en el rango \[0,1\], y "endProgress" es un número real en el rango \[0,1\].</li> </ul> <p>El valor predeterminado de la propiedad es la cadena vacía. Si se especifica una transición, entonces:</p> <ul> <li>"dur" la duración predeterminada es "1s",</li> <li>El valor predeterminado de "startProgress" es 0, </li> <li> El valor predeterminado de "endProgress" es 1.</li> </ul> | <p>El tipo de *transIn* y *transOut* siempre es "fundido" y el *subtipo* siempre es "fundido" y está definido de forma predeterminada.</p> <p>El atributo *dur* especifica la duración de la transición.</p> <p>El atributo *startProgress* especifica la cantidad de progreso a través de la transición en la que comenzar la ejecución.</p> <p>El atributo *endProgress* especifica la cantidad de progreso a través de la transición en la que finalizar la ejecución. El valor de este atributo debe ser mayor o igual al valor del atributo *startProgress*. Si *endProgress* es igual a *startProgress*, entonces la transición permanece en un progreso fijo mientras dure la transición.</p> |

#### Propiedades predefinidas para &lt;media&gt;  elementos con contenido textual { data-search-exclude }

| Nombre | Valor | Descripción |
| --- | --- | --- |
| fontColor | <p>"white", "black", "silver", "gray", "red", "maroon", "fuchsia", "purple", "lime", "green", "yellow", "olive", "blue", "navy", "aqua" o "teal".</p>  <p>El valor predeterminado es "white".</p> | Define el color de la fuente. |
| fontFamily | <p>Una lista priorizada de nombres de familias de fuentes y/o nombres de familias genéricas.</p>   <p>Existen dos tipos de nombres de familias de fuentes:</p>  <ul>  <li>"family-name": el nombre de una familia de fuentes de preferencia, o</li>  <li>"generic-family": se definen las siguientes familias genéricas: "serif", "sans-serif", "cursive", "fantasy" o "monospace".</li>  </ul>   <p>El valor predeterminado de esta propiedad depende del sistema.</p> | Los valores de la lista están separados por una coma para indicar que son alternativas. |
| textAlign | <p>"left", "right", "center" o "justify".</p>  <p>El valor predeterminado es "left".</p> | Esta propiedad describe cómo se alinea el contenido de texto. |
| fontStyle | <p>"normal" o "italic".</p><p>El valor predeterminado es "normal".</p> | Define el estilo de la fuente. |
| fontSize | <p>Entero positivo que termina con los caracteres "px" o "pt", para el tamaño relativo de la fuente expresado en píxeles, o el tamaño absoluto de la fuente expresado en puntos, respectivamente.</p>  <p>El valor predeterminado de esta propiedad depende del sistema.</p> | Establece el tamaño de la fuente en un tamaño fijo en píxeles o en puntos. |
| fontVariant | <p>"small-caps" o "normal".</p><p>El valor predeterminado es "normal".</p> | Define un tipo de variación dentro de una familia de fuentes. |
| fontWeight | <p>"normal" o "bold".</p><p>El valor predeterminado es "normal".</p> | Esta propiedad selecciona el grosor (peso) de la fuente. |
| freeze | <p>"true" o "false".</p><p>El valor predeterminado es "false".</p> | Esta propiedad define qué sucederá con un objeto al final de su presentación, si el contenido final se congela ("true") o no ("false"). |
| transIn, transOut | <p>Lista de (type, subtype, dur, startProgress, endProgress, direction, fadeColor, horzRepeat, vertRepeat, borderWidth, borderColor) separados por punto y coma donde:</p>  <ul>  <li> El *type* obligatorio puede ser: "barWipe", "irisWipe", "clockWipe", "snakeWipe" o "fade". Para ver la lista completa de los tipos de transición predefinidos, consulte: http://www.w3.org/TR/SMIL2/smil-transitions.html#TransitionEffects-Appendix.</li>  <li>Los valores obligatorios de *subtype* dependen de los valores de *type*, según se define: "leftToRight" para "barWipe", "rectangle" para "irisWipe", "clockwiseTwelve" para "clockWipe", "topLeftHorizontal" para "snakeWipe" y "crossfade" para "fade". Para ver la lista completa de los subtipos de transición predefinidos, consulte: http://www.w3.org/TR/SMIL2/smil-transitions.html#TransitionEffects-Appendix.</li>  <li>El atributo *dur* se especifica de acuerdo con una de las siguientes sintaxis: (i) "Hours:Minutes:Seconds.Fraction", donde "Hours" es un entero en el intervalo \[0,23\], "Minutes" es un entero en el intervalo \[0,59\], "Seconds" es un entero en el intervalo \[0,59\] y "Fraction" es un entero positivo; (ii) Seconds"s", donde "Seconds" es un número real positivo. El valor predeterminado es "0s".</li>  <li>*startProgress* y *endProgress* son números reales en el rango \[0,1\].</li>  <li>Los valores de *direction* son "forward" y "reverse".</li>  <li>*fadeColor* es "white", "black", "silver", "gray", "red", "maroon", "fuchsia", "purple", "lime", "green", "yellow", "olive", "blue", "navy", "aqua" o "teal".</li>  <li>*horzRepeat* y *vertRepeat* son enteros positivos.</li>  <li>*borderWidth* es un entero no negativo.</li>  <li>*borderColor* es "white", "black", "silver", "gray", "red", "maroon", "fuchsia", "purple", "lime", "green", "yellow", "olive", "blue", "navy", "aqua" o "teal".</li>  </ul>   <p>El valor predeterminado de la propiedad es la cadena vacía. Si se especifica un tipo de transición, entonces:</p>  <ul>  <li>la duración predeterminada de "dur" es "1s",</li>  <li>el valor predeterminado de "startProgress" es 0,</li>  <li>el valor predeterminado de "endProgress" es 1,</li>  <li>el valor predeterminado de "direction" es "forward",</li>  <li>el valor predeterminado de "fadeColor" es "black",</li>  <li>el valor predeterminado de "horzRepeat" es 1,</li>  <li>el valor predeterminado de "vertRepeat" es 1,</li>  <li>el valor predeterminado de "borderWidth" es 0,</li>  <li>el valor predeterminado de "borderColor" es "black".</li>  </ul> | <p>El valor de *transIn* y *transOut* es una lista de transiciones separadas por punto y coma.</p>   <p>El propósito de la lista separada por punto y coma es permitir a los autores especificar un conjunto de transiciones de respaldo si la transición preferida no está disponible. La primera transición de la lista debe ejecutarse si el agente de usuario ha implementado esta transición. Si no está disponible, se debe ejecutar la segunda transición de la lista, y así sucesivamente.</p>   <p>Los atributos *type* y *subtype* definen la transición. El atributo *dur* especifica la duración de la transición.</p>   <p>El atributo *startProgress* especifica la cantidad de progreso de la transición en la que comenzar la ejecución. Por ejemplo, podemos querer comenzar un *crossfade* con la imagen de destino ya desvanecida en un 30%. En este caso, *startProgress* sería 0.3.</p>   <p>El atributo *endProgress* especifica la cantidad de progreso de la transición en la que finalizar la ejecución. El valor de este atributo debe ser mayor o igual que el valor del atributo *startProgress*. Si *endProgress* es igual a *startProgress*, la transición permanece en un progreso fijo durante toda su duración.</p>   <p>El atributo *direction* especifica la dirección en la que se ejecutará la transición. Tenga en cuenta que no todas las transiciones tendrán interpretaciones inversas significativas. Por ejemplo, un *crossfade* no es una transición geométrica y, por lo tanto, no tiene interpretación de dirección inversa. En las transiciones que no tienen interpretación inversa se debe ignorar el atributo *direction* y asumir el valor predeterminado "forward".</p>   <p>Si el valor del atributo *type* es "fade" y el valor del atributo *subtype* es "fadeToColor" o "fadeFromColor", el atributo *fadeColor* especifica el color final o inicial del desvanecimiento. Si el valor del atributo *type* no es "fade", o el valor del atributo *subtype* no es "fadeToColor" o "fadeFromColor", se ignora el atributo *fadeColor*.</p>   <p>Si el valor del atributo *type* no es "fade", se pueden especificar los siguientes atributos:</p>   <p>El atributo *horzRepeat* especifica cuántas veces realizar el patrón de transición a lo largo del eje horizontal.</p>   <p>El atributo *vertRepeat* especifica cuántas veces realizar el patrón de transición a lo largo del eje vertical.</p>   <p>El atributo *borderWidth* especifica el ancho de un borde generado a lo largo de un borde de barrido (*wipe*).</p>   <p>El atributo *borderColor* especifica el contenido del borde generado a lo largo de un borde de barrido (*wipe*). Si el valor de este atributo es un color, el borde generado se rellena con este color. Si el valor de este atributo es "blend", el borde generado es una mezcla aditiva (o desenfoque) de las fuentes multimedia.</p> |

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
| default.focusBorderTransparency | Número en el rango \[0,1\] o \[0,100\], que termina con el carácter "%" (por ejemplo, "30%"), donde "1" o "100%" significa transparencia total y "0" o "0%" significa sin transparencia. | Transparencia predeterminada aplicada al borde de un elemento enfocado. |
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
