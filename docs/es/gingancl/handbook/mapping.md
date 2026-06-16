---
title: "Elemento &lt;mapping&gt;"
---

### Definición y uso { data-search-exclude }

Un elemento de mapeo define una ruta desde [&lt;switchPort&gt;](switchport.md) a una interfaz
(atributo de interfaz) de uno de los componentes del conmutador (especificado por su
atributo del componente).

### Sintaxis { data-search-exclude }

| Elemento | Atributos | Contenido | Padre |
| --- | --- | --- | --- |
| [&lt;mapping&gt;](mapping.md) | <u>*componente*</u>, *interfaz* | -- | [&lt;switchPort&gt;](switchport.md) |

### Atributos { data-search-exclude }

| Nombre | Valor | Descripción |
| --- | --- | --- |
| *componente* | IDREF. | El atributo *component* identifica de forma única un elemento secundario del conmutador, a través de su valor *id*. |
| *interfaz* | <p>String.</p><p>El valor predeterminado es el ancla de contenido completo.</p> | El atributo *interface* identifica de forma única una interfaz ([&lt;area&gt;](area.md), [&lt;property&gt;](property.md), [&lt;port&gt;](port.md) o [&lt;switchPort&gt;](switchport.md)) de un elemento secundario de [&lt;switch&gt;](switch.md), a través de su *id* o valor de nombre. |