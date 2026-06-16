---
title: "Elemento &lt;context&gt;"
---

### Definición y uso { data-search-exclude }

El elemento [&lt;context&gt;](context.md) permite estructurar una aplicación NCL. el
El elemento puede contener elementos con contenido multimedia ([&lt;media&gt;](media.md) elementos),
llamados objetos multimedia, otros elementos [&lt;context&gt;](context.md) anidados, elementos
agrupación de alternativas de contenido (elementos [&lt;switch&gt;](switch.md)) y relaciones
([&lt;link&gt;](link.md) elementos) entre todos los objetos representados por el
elementos antes mencionados.

Cabe destacar que el elemento [&lt;body&gt;](body.md) se considera un elemento especial
tipo de contexto, el que representa toda la aplicación.

El elemento [&lt;context&gt;](context.md) puede hacer referencia a otro [&lt;context&gt;](context.md) o un
elemento [&lt;body&gt;](body.md) importado. En este caso, hereda la especificación de
el elemento referido.

### Sintaxis { data-search-exclude }

| Elemento | Atributos | Contenido | Padre |
| --- | --- | --- | --- |
| [&lt;context&gt;](context.md) | <u>*id*</u>, *referir* | ([&lt;port&gt;](port.md)  &#124; [&lt;property&gt;](property.md)  &#124; [&lt;media&gt;](media.md)  &#124; [&lt;context&gt;](context.md)  &#124; [&lt;link&gt;](link.md)  &#124; [&lt;switch&gt;](switch.md)  &#124; [&lt;meta&gt;](meta.md)  &#124; [&lt;metadata&gt;](metadata.md))* | [&lt;body&gt;](body.md), [&lt;context&gt;](context.md) o [&lt;switch&gt;](switch.md) |

### Atributos { data-search-exclude }

| Nombre | Valor | Descripción |
| --- | --- | --- |
| *identificación* | Puede recibir cualquier valor de cadena que comience con una letra o un guión bajo y que solo contenga letras, dígitos, <"."> y <"_">. | El atributo *id* identifica de forma única el elemento dentro de un documento. |
| *referir* | IDREF o la cadena "alias#id" donde "id" es un valor IDREF. | <p>El atributo *refer* hace referencia a un elemento *id* que será reutilizado.  Un elemento que hace referencia a otro elemento no se puede reutilizar; es decir, su valor *id* no puede ser el valor de ningún atributo *refer*.  El elemento referido debe ser un [&lt;context&gt;](context.md) o un elemento [&lt;body&gt;](body.md) importado.</p><p>El elemento referido y el elemento que hace referencia a él deben considerarse iguales en cuanto a su especificación de datos.</p> <p>Si el nodo referido (elemento [&lt;context&gt;](context.md) o [&lt;body&gt;](body.md)) está definido dentro de un documento D importado, el valor del atributo *refer* debe tener el formato "alias#id", donde "alias" es el valor del atributo *alias* asociado con el documento D importado.</p> |
