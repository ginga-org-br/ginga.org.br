---
title: "Elemento &lt;bind&gt;"
---

### Definición y uso { data-search-exclude }

El elemento [&lt;bind&gt;](../bind/) permite asociar una interfaz de un objeto con un
función de conector.

Si el rol del conector referido proviene de un elemento [&lt;simpleAction&gt;](../simpleaction/)
cuyo *eventType* es igual a "atribución", y cuyo
*actionType* es igual a "inicio", y si el valor especificado es
"$anyName", el valor asignado se recupera de la propiedad asociada
con el rol "anyName" y definido por un elemento secundario [&lt;bind&gt;](../bind/) en el
mismo elemento [&lt;link&gt;](../link/).  Si este valor no se puede recuperar, no hay atribución
está hecho.

### Sintaxis { data-search-exclude }

| Elemento | Atributos | Contenido | Padre |
| --- | --- | --- | --- |
| [&lt;bind&gt;](../bind/) | <u>*rol*</u>, <u>*componente*</u>, *interfaz*, *descriptor* | [&lt;bindParam&gt;](../bindparam/)* | [&lt;link&gt;](../link/) |

### Atributos { data-search-exclude }

| Nombre | Valor | Descripción |
| --- | --- | --- |
| *rol* | Cadena | El atributo *role* hace referencia a un rol de conector. |
| *componente* | IDREF. | El atributo *componente* hace referencia a un elemento [&lt;media&gt;](../media/), o a un elemento [&lt;context&gt;](../context/), o a un elemento [&lt;body&gt;](../body/), o a un elemento [&lt;switch&gt;](../switch/).  Estos elementos deben ser elementos secundarios de la misma composición en la que se define el elemento [&lt;link&gt;](../link/), o deben ser la composición en la que se define el elemento [&lt;link&gt;](../link/). |
| *interfaz* | <p>String.</p><p>El valor predeterminado es el ancla de contenido completo.</p> | El atributo *interfaz* se refiere a un [&lt;area&gt;](../area/), [&lt;port&gt;](../port/) o [&lt;switchPort&gt;](../switchport/), del objeto identificado por el atributo *componente*, haciendo referencia a su atributo *id*; o hace referencia a un [&lt;property&gt;](../property/), del objeto identificado por el atributo *componente*, haciendo referencia a su atributo *nombre*. |
| *descriptor* | IDREF. | El atributo *descriptor* hace referencia a un elemento [&lt;descriptor&gt;](../descriptor/). |