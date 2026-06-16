---
title: "Elemento &lt;attributeAssessment&gt;"
---

### Definición y uso { data-search-exclude }

El elemento [&lt;attributeAssessment&gt;](attributeassessment.md) se utiliza para definir una variable que se
evaluado, en [&lt;assessmentStatement&gt;](assessmentstatement.md) elementos, frente a otra variable
valores o un valor absoluto.

La variable puede ser una propiedad especificada en un elemento [&lt;property&gt;](property.md), o
puede ser un atributo de evento (presentación, selección o atribución):
ocurrencias, repetición o estado (que tiene los siguientes valores:
"en curso", "en pausa" o "inactivo").

El elemento [&lt;attributeAssessment&gt;](attributeassessment.md) tiene un atributo *rol*, que
tiene que ser único en el conjunto de roles del conector.  Este atributo es el conector.
punto de interfaz, que está asociado a las interfaces de nodo ([&lt;port&gt;](port.md),
[&lt;area&gt;](area.md), [&lt;property&gt;](property.md) o [&lt;switchPort&gt;](switchport.md) elementos) por un [&lt;link&gt;](link.md)
que se refiere al conector.

La variable definida por el elemento depende de su *eventType*
atributo y su atributo *attributeType*:

  * Si el valor de eventType es "presentación", el *attributeType*
    El atributo puede especificar como variable: las "ocurrencias" o el evento de "repetición".
    atributos, o el estado del evento "estado".

  * Si el eventType es "atribución", el *attributeType* puede tener el
    valores: "nodeProperty" (especificando una propiedad de nodo), "ocurrencias",
    "repetición" o "estado".

  * Si el valor de eventType es "selección", el [&lt;attributeAssessment&gt;](attributeassessment.md)puede
    definir también a qué aparato de selección (por ejemplo, teclas del teclado o
    llaves de control remoto) se refiere, a través de su atributo *key*.  el
    El atributo *attributeType* puede tener los valores: "ocurrencias"
    (predeterminado) o "estado".

Se puede agregar un valor de compensación a un [&lt;attributeAssessment&gt;](attributeassessment.md) antes de su
comparación en un elemento [&lt;assessmentStatement&gt;](assessmentstatement.md).  Por ejemplo, una compensación
se puede agregar a una *evaluación de atributos* para especificar: "la pantalla
posición vertical más 50 píxeles".

### Sintaxis { data-search-exclude }

| Elemento | Atributos | Contenido | Padre |
| --- | --- | --- | --- |
| [&lt;attributeAssessment&gt;](attributeassessment.md) | <u>*rol*</u>, <u>*eventType*</u>, *clave*, *attributeType*, *offset* | -- | [&lt;assessmentStatement&gt;](assessmentstatement.md) |

### Atributos { data-search-exclude }

| Nombre | Valor | Descripción |
| --- | --- | --- |
| *rol* | Cadena. | El atributo *role* define un punto de interfaz de conector, que está asociado a las interfaces de nodo mediante un enlace que hace referencia al conector.  El valor *role* debe ser único dentro del conjunto de roles del conector. |
| *tipo de evento* | "presentación", "selección" o "atribución". | El atributo *eventType* identifica el tipo de evento para la acción o condición. |
| *clave* | Se deben aceptar al menos los siguientes valores (distingue entre mayúsculas y minúsculas) para el atributo clave: "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "*", "#", "MENÚ", "INFO", "GUÍA", "CURSOR_DOWN", "CURSOR_LEFT", "CURSOR_RIGHT", "CURSOR_UP", "CHANNEL_DOWN", "CHANNEL_UP", "VOLUME_DOWN", "VOLUME_UP", "ENTER", "ROJO", "VERDE", "AMARILLO", "AZUL", "ATRÁS", "SALIR", "ENCENDIDO", "REBOBINADO", "PARAR", "EXPULSAR", "REPRODUCIR", "GRABAR" y "PAUSAR". | El atributo *key* identifica la clave de selección utilizada para la selección. |
| *tipo de atributo* | <p>"nodeProperty" (solo en el caso de *eventType*="atribución"), "ocurrencias", "repetición" o "estado".</p><p>Los valores predeterminados son: "nodeProperty" si *eventType*="atribución", u "ocurrencias" si *eventType*="selección".</p> | El atributo *attributeType* identifica la variable que se evaluará en un elemento [&lt;assessmentStatement&gt;](assessmentstatement.md). |
| *compensación* | Cadena. | El atributo *offset* especifica un valor que se agregará a la variable seleccionada antes de su evaluación en un elemento [&lt;assessmentStatement&gt;](assessmentstatement.md). |