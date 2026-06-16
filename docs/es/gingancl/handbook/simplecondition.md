---
title: "Elemento &lt;simpleCondition&gt;"
---

### Definición y uso { data-search-exclude }

El elemento [&lt;simpleCondition&gt;](simplecondition.md) define una condición simple para activar
acciones en una relación causal.

El elemento [&lt;simpleCondition&gt;](simplecondition.md) tiene un rol *atributo*, cuyo valor
será único en el conjunto de roles del conector.  El rol es un conector.
punto de interfaz, que está asociado a las interfaces de los nodos mediante un enlace que
Se refiere al conector.

Un [&lt;simpleCondition&gt;](simplecondition.md) también define un tipo de evento (*eventType*
atributo) y a qué transición en la máquina de estado de eventos se refiere
(*atributo de transición*).  El *tipo de evento* y
*transición* puede ser inferida por el valor del rol, si se usan palabras reservadas.
usado.  De lo contrario, los atributos *eventType* y *transition*
son requeridos.

Valores de rol de condición reservada asociados a máquinas de estado de eventos:

| Valor del rol | Valor de transición | Tipo de evento |
| --- | --- | --- |
| al comenzar | comienza | presentación |
| al final | paradas | presentación |
| enAbortar | aborta | presentación |
| en pausa | pausas | presentación |
| enReanudar | currículums | presentación |
| en Selección | paradas | selección |
| onBeginSelección | comienza | selección |
| onEndSelection | paradas | selección |
| onAbortSelection | partos | selección |
| onPauseSelección | pausas | selección |
| enResumeSelection | currículums | selección |
| onBeginAtribución | comienza | atribución |
| onEndAtribución | paradas | atribución |
| onPauseAtribución | pausas | atribución |
| onResumeAttribution | currículums | atribución |
| onAbortAttribution | aborta | atribución |

Si un valor *eventType* es "selección", el rol también puede definirse como
qué aparato de selección (por ejemplo, teclas del teclado o control remoto)
claves) al que se refiere, a través de su atributo clave.  Si este atributo no es
especificado, la selección a través de un dispositivo puntero (ratón, pantalla táctil,
teclas de navegación).

La cardinalidad del rol especifica el mínimo (atributo mínimo) y el máximo (máx.
atributo) número de participantes que pueden desempeñar el rol (es decir, el
número de enlaces) cuando el [&lt;causalConnector&gt;](causalconnector.md) se utiliza para crear un
[&lt;link&gt;](link.md).  Si el valor máximo es mayor que uno, un calificador
Los atributos deben especificarse informando la relación lógica entre los
condición simple vincula: "o" o "y".  Si el calificador establece la
Operador lógico "o", la acción de enlace se activará siempre que se cumpla cualquier condición.
ocurre.  Si el calificador establece el operador lógico "y", el enlace
La acción se activará después de que ocurran todas las condiciones simples.

También se puede definir un atributo de retraso para [&lt;simpleCondition&gt;](simplecondition.md),
especificando que la condición es verdadera después de un retraso de tiempo desde el momento en que
se produce la transición.

### Sintaxis { data-search-exclude }

| Elemento | Atributos | Contenido | Padre |
| --- | --- | --- | --- |
| [&lt;simpleCondition&gt;](simplecondition.md) | <u>*rol*</u>, *retraso*, *eventType*, *key*, *transition*, *min*, *max*, *calificador* | -- | [&lt;causalConnector&gt;](causalconnector.md) o [&lt;compoundCondition&gt;](compoundcondition.md) |

### Atributos { data-search-exclude }

| Nombre | Valor | Descripción |
| --- | --- | --- |
| *rol* | Cadena. | El atributo *role* define un punto de interfaz de conector, que está asociado a las interfaces de nodo mediante un enlace que hace referencia al conector.  El valor *role* debe ser único dentro del conjunto de roles del conector. |
| *retraso* | <p>El atributo *retraso* se especificará de acuerdo con uno de los siguientes sintaxis:</p><ol><li class="level1"><div class="li"><"<nowiki>Horas:Minutos:Segundos.Fracción</nowiki>">, donde "Horas" es un número entero en el intervalo \[0,23\], "Minutos" es un número entero en el intervalo \[0,59\], "Segundos" es un número entero en el intervalo 0,59 y "Fracción" es un intervalo positivo entero,</div></li><li class="level1"><div class="li">Seconds<"s">, donde "Segundos" es un real positivo número.</div></li></ol><p>El valor predeterminado es "0s".</p> | El atributo *delay* define un retraso de tiempo, desde el momento en que ocurre la transición, a partir del cual [&lt;simpleCondition&gt;](simplecondition.md) debe considerarse satisfecho.
| *tipo de evento* | "presentación", "selección" o "atribución". | El atributo *eventType* identifica el tipo de evento para la acción o condición. |
| *clave* | Se deben aceptar al menos los siguientes valores (distingue entre mayúsculas y minúsculas) para el atributo clave: "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "*", "#", "MENÚ", "INFO", "GUÍA", "CURSOR_DOWN", "CURSOR_LEFT", "CURSOR_RIGHT", "CURSOR_UP", "CHANNEL_DOWN", "CHANNEL_UP", "VOLUME_DOWN", "VOLUME_UP", "ENTER", "ROJO", "VERDE", "AMARILLO", "AZUL", "ATRÁS", "SALIR", "ENCENDIDO", "REBOBINADO", "PARAR", "EXPULSAR", "REPRODUCIR", "GRABAR" y "PAUSAR". | El atributo *key* identifica la clave de selección utilizada para la selección. |
| *transición* | "inicia", "se detiene", "aborta", "pausa" o "se reanuda". | El atributo *transition* especifica una transición en la máquina de estado del evento utilizada para definir la condición. |
| *min* | <p>Entero positivo menor o igual al valor *max*.</p><p>El valor predeterminado es 1.</p> | El atributo *min* define el número mínimo de participantes que pueden desempeñar el rol. |
| *máximo* | <p>Entero positivo mayor o igual que el valor *min* o el valor "ilimitado". </p><p>El valor predeterminado es 1.</p> | El atributo *max* define el número máximo de participantes que pueden desempeñar el rol. |
| *calificador* | "y" o "o". | El atributo *calificador* define la relación lógica entre los enlaces de condición. |