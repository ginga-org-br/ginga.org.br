---
title: "Elemento &lt;port&gt;"
---

### Definición y uso { data-search-exclude }

Nodos compuestos de NCL, representados por [&lt;body&gt;](body.md), [&lt;context&gt;](context.md) y
[&lt;switch&gt;](switch.md) elementos, encapsula sus componentes secundarios.  Interfaces de
Los componentes secundarios no son visibles para las relaciones definidas fuera del
nodo compuesto, a menos que estas interfaces estén externalizadas, utilizando el
[&lt;port&gt;](port.md) o [&lt;switchPort&gt;](switchport.md) elementos.

El elemento [&lt;port&gt;](port.md) especifica un puerto de nodo compuesto con su respectivo
mapeo a una interfaz (*atributo de interfaz*) de uno de sus
componentes (especificados por el atributo *componente*).  Como de costumbre, si el
El atributo *interfaz* no está especificado, //todo el contenido
anclaje// se supone.

### Sintaxis { data-search-exclude }

| Elemento | Atributos | Contenido | Padre |
| --- | --- | --- | --- |
| [&lt;port&gt;](port.md) | <u>*id*</u>, <u>*componente*</u>, *interfaz* | -- | [&lt;context&gt;](context.md) o [&lt;body&gt;](body.md) |

### Atributos { data-search-exclude }

| Nombre | Valor | Descripción |
| --- | --- | --- |
| *identificación* | Puede recibir cualquier valor de cadena que comience con una letra o un guión bajo y que solo contenga letras, dígitos, <"."> y <"_">. | El atributo *id* identifica de forma única el elemento dentro de un documento. |
| *componente* | IDREF. | El atributo *componente* identifica un elemento hijo de la composición, que puede ser un objeto multimedia u otro objeto compuesto, a través de su valor *id*. |
| *interfaz* | <p>String.</p><p>El valor predeterminado es el ancla de contenido completo.</p> | El atributo *interface* identifica de forma única una interfaz ([&lt;area&gt;](area.md), [&lt;property&gt;](property.md), [&lt;port&gt;](port.md) o [&lt;switchPort&gt;](switchport.md)) de un elemento secundario de la composición, a través de su valor *id* o *name*.  El valor predeterminado es todo el ancla de contenido del componente al que se hace referencia. |