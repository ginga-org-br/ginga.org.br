---
title: "Elemento &lt;transition&gt;"
---

### Definición y uso { data-search-exclude }

El elemento [&lt;transition&gt;](transition.md) permite definir una plantilla de transición.

### Sintaxis { data-search-exclude }

| Elemento | Atributos | Contenido | Padre |
| --- | --- | --- | --- |
| [&lt;transition&gt;](transition.md) | <u>*id*</u>, <u>*tipo*</u>, *subtipo*, *dur*, *startProgress*, *endProgress*, *dirección*, *fadeColor*, *horzRepeat*, *vertRepeat*, *borderWidth*, *colordelborde* | -- | [&lt;transitionBase&gt;](transitionbase.md) |

### Atributos { data-search-exclude }

| Nombre | Valor | Descripción |
| --- | --- | --- |
| *identificación* | Puede recibir cualquier valor de cadena que comience con una letra o un guión bajo y que solo contenga letras, dígitos, <"."> y <"_">. | El atributo *id* identifica de forma única el elemento dentro de un documento. |
| *tipo* | "barWipe", "irisWipe", "clockWipe", "snakeWipe" o "fade".  Estos son los valores requeridos.  Para obtener la lista completa de tipos de transición predefinidos, consulte: http://www.w3.org/TR/SMIL2/smil-transitions.html#TransitionEffects-Appendix. | Los atributos *tipo* y *subtipo* definen la transición. |
| *subtipo* | Los valores de subtipo requeridos dependen del valor de tipo.  Para "barWipe", el subtipo requerido es "leftToRight", para "irisWipe" es "rectangle", para "clockWipe" es "clockWipe", para "snakeWipe" es "topLeftHorizontal" y para "fade" es "crossfade".  La lista completa se puede encontrar en http://www.w3.org/TR/SMIL2/smil-transitions.html#TransitionEffects-Appendix.  Los valores de subtipo requeridos también son los valores predeterminados. | Los atributos *tipo* y *subtipo* definen la transición. |
| *dur* | El atributo *dur* se especifica de acuerdo con una de las siguientes sintaxis: (i) "Horas:Minutos:Segundos.Fracción", donde "Horas" es un número entero en el intervalo \[0,23\], "Minutos" es un número entero en el intervalo \[0,59\], "Minutos" es un número entero en el intervalo \[0,59\] y "Fracción" es un valor positivo entero; (ii) Segundos<"s">, donde "Segundos" es un número real positivo.  El valor predeterminado es "1s". | El atributo *dur* especifica la duración de la transición. |
| *inicioProgreso* | Un número real en el rango \[0,1\].  El valor predeterminado es 0. | El atributo *startProgress* especifica la cantidad de progreso a través de la transición en la que comenzar la ejecución. Por ejemplo, es posible que queramos comenzar un fundido cruzado con la imagen de destino ya con un 30% de fundido. En este caso, *startProgress* sería 0,3. |
| *finProgreso* | Un número real en el rango \[0,1\].  El valor predeterminado es 0. | El atributo *endProgress* especifica la cantidad de progreso a través de la transición en la que finalizará la ejecución.  El valor de este atributo será mayor o igual que el valor del atributo *startProgress*. Si *endProgress* es igual a *startProgress*, entonces la transición permanece en un progreso fijo mientras dure la transición. |
| *dirección* | "hacia adelante" o "hacia atrás".  El valor predeterminado es "adelante". | Especifica la dirección en la que se ejecutará la transición.  Tenga en cuenta que no todas las transiciones tendrán interpretaciones inversas significativas.  Por ejemplo, un fundido cruzado no es una transición geométrica y, por lo tanto, no tiene interpretación de dirección inversa. Las transiciones que no tienen una interpretación inversa tienen su atributo de dirección ignorado y se asume el valor predeterminado de "hacia adelante". |
| *color desvanecido* | "blanco", "negro", "plateado", "gris", "rojo", "granate", "fucsia", "púrpura", "lima", "verde", "amarillo", "oliva", "azul", "azul marino", "aqua" o "verde azulado".  El valor predeterminado es "negro". | Si el valor del atributo *type* es "fade" y el valor del atributo *subtype* es "fadeToColor" o "fadeFromColor", entonces el atributo *fadeColor* especifica el color final o inicial del desvanecimiento. Si el valor del atributo *type* no es "fade", o el valor del atributo *subtype* no es "fadeToColor" o "fadeFromColor", entonces se ignorará el atributo *fadeColor*. |
| *horzRepetir* | Entero positivo.  El valor predeterminado es 1. | Este atributo es válido sólo si el valor del atributo *type* no es "desvanecido".  Especifica cuántas veces realizar el patrón de transición a lo largo del eje horizontal. |
| *vertRepetir* | Entero positivo.  El valor predeterminado es 1. | Este atributo es válido sólo si el valor del atributo *type* no es "desvanecido".  Especifica cuántas veces realizar el patrón de transición a lo largo del eje vertical. |
| *ancho de borde* | Entero positivo.  El valor predeterminado es 0. | Este atributo es válido sólo si el valor del atributo *type* no es "desvanecido".  Especifica el ancho de un borde generado a lo largo de un borde de limpieza. |
| *colordelborde* | "blanco", "negro", "plateado", "gris", "rojo", "granate", "fucsia", "púrpura", "lima", "verde", "amarillo", "oliva", "azul", "azul marino", "aqua" o "verde azulado".  El valor predeterminado es "negro". | Este atributo es válido sólo si el valor del atributo de tipo no es "desvanecido".  Especifica el contenido del borde generado a lo largo de un borde de limpieza. Si el valor de este atributo es un color, entonces el borde generado a lo largo del borde de barrido o deformación se rellena con este color. Si el valor de este atributo es "combinación", entonces el borde generado a lo largo de la combinación de barrido es una combinación aditiva (o desenfoque) de las fuentes multimedia. |
