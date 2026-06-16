---
title: "Elemento &lt;area&gt;"
---

# &lt;area&gt;

El elemento [&lt;area&gt;](area.md) permite definir un ancla de contenido (un subconjunto de
unidades de información del contenido de un [&lt;media&gt;](media.md) elemento) que pueden usarse en
relaciones con otros objetos en una aplicación NCL.

Los anclajes de contenido pueden representar:

- porciones espaciales de imágenes: a través del atributo *coords*;
- porciones temporales de contenido multimedia continuo (audio, vídeo, etc.):
  a través de los atributos *begin* y *end*, o basándose en el
  número de muestras de audio o fotogramas de vídeo, hasta el *primero* y
  *último* atributo, que indica el inicio y el final.
  muestra/marco;
- porciones temporales y espaciales de videos: a través de las *coords*,
  atributos *comienzo* y *fin*; o a través del
  *coords*, *primero* y *último* atributos;
- segmentos textuales: a través de *beginText*, *beginPosition*,
  Atributos *endText* y *endPosition*, que definen el
  cadenas de inicio y fin, y su aparición en el texto
  respectivamente;
- una cadena que utiliza el reproductor multimedia para identificar una región de contenido
  (por ejemplo, una función o método en un objeto multimedia imperativo, un
  interfaz en un objeto de medios declarativo, como un ancla HTML, un puerto en
  un objeto multimedia con una aplicación NCL como contenido, etc.): a través del
  atributo *etiqueta*;
- un clip en el contenido de un objeto hipermedia declarativo: usando el
  *clip* atributo.

Cada elemento [&lt;media&gt;](media.md), [&lt;context&gt;](context.md), [&lt;body&gt;](body.md) y [&lt;switch&gt;](switch.md)
tiene un ancla de contenido con una región que representa todo el contenido del
Nodo definido por defecto.  Este ancla se llama "ancla de contenido completo".
Excepto para objetos multimedia con contenido de código imperativo (por ejemplo, aquellos
cuyo tipo MIME es "application/x-ncl-NCLua"), cada vez que un componente NCL
se hace referencia sin especificar uno de sus anclajes, todo el contenido ancla
se supone.

### Sintaxis { data-search-exclude }

| Elemento | Atributos | Contenido | Padre |
| --- | --- | --- | --- |
| [&lt;area&gt;](area.md) | <u>*id*</u>, *coords*, *begin*, *end*, *beginText*, *endText*, *beginPosition*, *endPosition*, *primero*, *último*, *etiqueta*, *clip* | -- | [&lt;media&gt;](media.md) |

### Atributos { data-search-exclude }

| Nombre | Valor | Descripción |
| --- | --- | --- |
| *id* | Puede recibir cualquier valor de cadena que comience con una letra o un guión bajo y que solo contenga letras, dígitos, "." y "_". | El atributo *id* identifica de forma única al elemento dentro de un documento. |
| *coords* | <p>Una lista de valores de la forma "left-x, top-y, right-x, bottom-y" donde cada valor es:</p><ol><li>un número real en el rango \[0,100\] que termina con el carácter "%" (por ejemplo, "30%"), o</li><li>un entero positivo que especifica el valor en píxeles. Para valores en píxeles, el calificador de unidad "px" puede omitirse.</li></ol> | <p>El atributo *coords* especifica la posición de un área rectangular en la pantalla.</p><p>Las coordenadas son relativas a la esquina superior izquierda del contenido del objeto.</p><p>Los valores están separados por comas.</p><p>El orden de los valores es "left-x", "top-y", "right-x" y "bottom-y".</p><p>Cuando "left-x" y "right-x" se expresan como un porcentaje, el valor es relativo a la propiedad de ancho (*width*) del objeto multimedia.</p><p>Cuando "top-y" y "bottom-y" se expresan como un porcentaje, el valor es relativo a la propiedad de altura (*height*) del objeto multimedia.</p> |
| *begin* | <p>Excepto para el elemento [&lt;media&gt;](media.md) del tipo "application/x-ncl-time", el atributo *begin* debe especificarse de acuerdo con una de las siguientes sintaxis:</p><ol><li>"Hours:Minutes:Seconds.Fraction", donde "Hours" es un entero en el intervalo \[0,23\], "Minutes" es un entero en el intervalo \[0,59\], "Seconds" es un entero en el intervalo \[0,59\] y "Fraction" es un entero positivo,</li><li>Seconds"s", donde "Seconds" es un número real positivo.</li></ol><p>Para el elemento [&lt;media&gt;](media.md) del tipo "application/x-ncl-time", el atributo *begin* debe especificarse de acuerdo con la siguiente sintaxis: "Year:Month:Day:Hours:Minutes:Seconds.Fraction", según la zona horaria del país. El agente de usuario NCL es responsable de traducir el valor de la zona horaria del país al correspondiente a UTC.</p><p>Si se define el atributo *end*, pero sin una definición explícita para el atributo *begin*, el inicio de la presentación de todo el contenido multimedia se considerará como el inicio del ancla.</p><p>En el caso de un elemento multimedia del tipo "application/x-ncl-time", el atributo *begin* siempre debe estar definido y asume un valor UTC absoluto.</p> | El atributo *begin* especifica el inicio del ancla temporal. |
| *end* | Igual que para *begin*. | El atributo *end* especifica el fin del ancla temporal. |
| *beginText* | <p>Cadena.</p><p>Si no se define el inicio de la región del ancla de contenido, se asume el inicio del contenido de texto.</p> | Los atributos *beginText* y *beginPosition* especifican el inicio del ancla de texto. El atributo *beginText* define una cadena en el texto. |
| *endText* | Cadena. | Los atributos *endText* y *endPosition* especifican el fin del ancla de texto. El atributo *endText* define una cadena en el texto. |
| *beginPosition* | Entero positivo. El valor predeterminado es 1. | Los atributos *beginText* y *beginPosition* especifican el inicio del ancla de texto. El atributo *beginPosition* define la aparición de la cadena en el texto. |
| *endPosition* | Entero positivo. El valor predeterminado es la posición del último carácter en la cadena. | Los atributos *endText* y *endPosition* especifican el fin del ancla de texto. El atributo *endPosition* define la aparición de la cadena en el texto. |
| *first* | <p>El atributo *first* debe especificarse de acuerdo con una de las siguientes sintaxis:</p><ol><li>Samples"s", donde Samples es un entero positivo,</li><li>Frames"f", donde Frames es un entero positivo, o</li><li>NPT"npt", donde NPT es el valor de Normal Play Time.</li></ol><p>Si se define el atributo *last*, pero sin una definición explícita para el atributo *first*, el inicio de la presentación de todo el contenido multimedia se considerará como el inicio del ancla.</p> | -- |
| *last* | <p>El atributo *last* debe especificarse de acuerdo con una de las siguientes sintaxis:</p><ol><li>Samples"s", donde Samples es un entero positivo,</li><li>Frames"f", donde Frames es un entero positivo, o</li><li>NPT"npt", donde NPT es el valor de Normal Play Time.</li></ol><p>Si se define el atributo *first*, pero no se especifica el atributo *last*, el final de la presentación de todo el contenido multimedia se asumirá como el fin del ancla.</p> | -- |
| *label* | Cadena. | El atributo *label* identifica una región de contenido, por ejemplo, una función en un objeto multimedia imperativo, una interfaz en un objeto multimedia declarativo, como un ancla HTML, o un puerto en un objeto multimedia con una aplicación NCL como contenido, etc. |
| *clip* | <p>Cadena.</p><p>El valor depende del tipo de objeto hipermedia declarativo. Para objetos multimedia NCL, el valor de *clip* es una terna "(chainId,beginOffset,endOffset)" que utiliza el reproductor multimedia NCL para identificar un elemento [&lt;port&gt;](port.md) de aplicación NCL a través del cual comienza una cadena temporal, y el tiempo de inicio y fin en esta cadena temporal.</p><p>Para elementos [&lt;media&gt;](media.md) con contenido de código NCL se definen los siguientes valores predeterminados:</p><ol><li>"chainId" es el ancla de contenido completo del elemento [&lt;body&gt;](body.md),</li><li>"beginOffset" es "0s", y</li><li>"endOffset" es el tiempo final de la cadena temporal.</li></ol> | El atributo *clip* identifica un clip de flujo en el contenido de un objeto hipermedia declarativo. |
