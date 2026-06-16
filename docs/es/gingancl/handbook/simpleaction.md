---
title: "Elemento &lt;simpleAction&gt;"
---

### Definición y uso { data-search-exclude }

El elemento [&lt;simpleAction&gt;](simpleaction.md) define una acción simple desencadenada por el
Evaluación de una condición de relación causal.

El elemento [&lt;simpleAction&gt;](simpleaction.md) tiene un atributo *role*, cuyo valor
debe ser único en el conjunto de roles del conector. Un rol es una interfaz de conector.
punto, que está asociado a las interfaces del nodo mediante un enlace que hace referencia al
conector.

Un [&lt;simpleAction&gt;](simpleaction.md) también define un tipo de evento (*eventType*
atributo) y qué acción se debe aplicar a la máquina de estado del evento
refiere (atributo *actionType*). El *tipo de evento* y
Los valores *actionType* pueden ser inferidos por el valor del rol si están reservados.
Las palabras se utilizan como valores. De lo contrario, el *eventType* y
Los atributos *actionType* son obligatorios.

Valores de rol de acción reservada asociados a máquinas de estado de eventos:
| Valor del rol | Tipo de acción | Tipo de evento |
| --- | --- | --- |
| inicio | inicio | presentación |
| detener | detener | presentación |
| abortar | abortar | presentación |
| pausa | pausa | presentación |
| currículum | currículum | presentación |
| conjunto | inicio | atribución |

Si un valor *eventType* es "atribución", el [&lt;simpleAction&gt;](simpleaction.md)debe
también definir el valor a asignar, a través de su *valor*
atributo. Si el *valor* se especifica como "$anyName" (donde "$" es un
símbolo reservado y "anyName" es cualquier cadena, excepto nombres de roles reservados),
el valor asignado se recupera de la propiedad asociada con el
*rol* "anyName" y definido por un elemento secundario [&lt;bind&gt;](bind.md) del
[&lt;link&gt;](link.md) elemento que hace referencia al conector.  Si este valor no puede ser
recuperado, no se hace ninguna atribución.  Éste es el único caso posible de
[&lt;bind&gt;](bind.md) elemento que hace referencia a un rol que no está declarado explícitamente en un
conector.

La cardinalidad del rol especifica el mínimo (atributo *min*) y
número máximo (atributo *max*) de participantes que pueden jugar el
rol (es decir, el número de enlaces) cuando se utiliza [&lt;causalConnector&gt;](causalconnector.md)
para crear un [&lt;link&gt;](link.md). Si el valor máximo es mayor que uno, el
El atributo *calificador* se puede especificar informando a la lógica
relación entre los enlaces de acción simple: "par" o "seq". cuando el
Se utiliza el calificador secuencial "seq", las acciones deben activarse en el modo especificado.
orden. Sin embargo, una acción no necesita esperar a que se realice la anterior.
terminado para ser despedido. Cuando se utiliza el calificador paralelo "par",
Las acciones se pueden realizar en cualquier orden.

También se puede definir un atributo *retraso* para un [&lt;simpleAction&gt;](simpleaction.md),
especificando que la acción debe ser ejecutada sólo después de esperar la
tiempo especificado.

El [&lt;simpleAction&gt;](simpleaction.md) también puede definir un atributo *repetido* para ser
asignado al atributo *repeticiones* del evento, y un
*repeatDelay* se esperará antes de repetir la acción.

El elemento [&lt;simpleAction&gt;](simpleaction.md) también puede definir la duración y por
atributos si su valor *eventType* es "atribución" y sólo si el
La propiedad referida define valores numéricos o colores. Al configurar un nuevo
valor a una propiedad el cambio es instantáneo por defecto (*duración*
es 0), pero el cambio también puede realizarse durante un evento declarado explícitamente.
duración, especificada por el atributo *duración*. El cambio de la
El valor antiguo al nuevo puede ser lineal por defecto (*por* es
"indefinido"), o se realiza paso a paso, con el ritmo especificado por el
*por* atributo.

### Sintaxis { data-search-exclude }

| Elemento | Atributos | Contenido | Padre |
| --- | --- | --- | --- |
| [&lt;simpleAction&gt;](simpleaction.md) | <u>*role*</u>, *delay*, *eventType*, *actionType*, *value*, *min*, *max*, *qualifier*, *repeat*, *repeatDelay*, *duration*, *by* | -- | [&lt;causalConnector&gt;](causalconnector.md) o [&lt;compoundAction&gt;](compoundaction.md) |

### Atributos { data-search-exclude }

| Nombre | Valor | Descripción |
| --- | --- | --- |
| *rol* | Cadena. | El atributo *role* define un punto de interfaz de conector, que está asociado a las interfaces de nodo mediante un enlace que hace referencia al conector.  El valor *role* debe ser único dentro del conjunto de roles del conector. |
| *retraso* | <p>El atributo *retraso* se especificará de acuerdo con uno de los siguientes sintaxis:</p><ol><li class="level1"><div class="li"><"<nowiki>Horas:Minutos:Segundos.Fracción</nowiki>">, donde "Horas" es un número entero en el intervalo \[0,23\], "Minutos" es un número entero en el intervalo \[0,59\], "Segundos" es un número entero en el intervalo 0,59 y "Fracción" es un intervalo positivo entero,</div></li><li class="level1"><div class="li">Seconds<"s">, donde "Segundos" es un real positivo número.</div></li></ol><p>El valor predeterminado es "0s".</p> | El atributo *delay* define un retraso de tiempo que se debe esperar antes de activar la acción.
| *tipo de evento* | "presentación", "selección" o "atribución". | El atributo *eventType* identifica el tipo de evento para la acción o condición. |
| *tipo de acción* | "iniciar", "detener", "abortar", "pausar" o "reanudar". | El atributo *actionType* especifica la acción para desencadenar la transición correspondiente en la máquina de estado del evento referido. |
| *valor* | Cadena | El atributo *valor* define un valor que se establecerá en la propiedad vinculada a la acción simple de atribución. |
| *min* | <p>Entero positivo menor o igual al valor *max*.</p><p>El valor predeterminado es 1.</p> | El atributo *min* define el número mínimo de participantes que pueden desempeñar el rol. |
| *máximo* | <p>Entero positivo mayor o igual que el valor *min* o el valor "ilimitado". </p><p>El valor predeterminado es 1.</p> | El atributo *max* define el número máximo de participantes que pueden desempeñar el rol. |
| *calificador* | "seq" o "par".  El valor predeterminado es "par". | El atributo *calificador* define el orden en que se deben aplicar las acciones en los enlaces de acciones simples. |
| *repetir* | Entero positivo.  El valor predeterminado es 0 | El atributo *repeat* define un valor que se asignará al atributo de repeticiones del evento definido en el elemento [&lt;simpleAction&gt;](simpleaction.md). |
| *repeticiónDelay* | Lo mismo que para *retraso*. | El atributo *repeatDelay* especifica un intervalo de tiempo que se debe esperar antes de repetir la acción. |
| *duración* | El atributo *duración* se especifica como Segundos<"s">, donde "Segundos" es un número real positivo. | El atributo *duración* establece el tiempo que debe durar una atribución al cambiar del valor antiguo al nuevo. |
| *por* | <p>Un número real o "indefinido".</p><p>El valor predeterminado es "indefinido".</p> | El atributo *by* establece cómo se produce el cambio realizado por una acción de atribución de un valor antiguo al nuevo: si de forma lineal (by es "indefinido") o se realiza paso a paso, con el ritmo especificado por el atributo *by*. |
