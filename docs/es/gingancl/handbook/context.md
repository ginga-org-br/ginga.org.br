---
title: "Elemento &lt;context&gt;"
---

### Definición y uso { data-search-exclude }

El elemento [&lt;context&gt;](../context/) permite estructurar una aplicación NCL. el
El elemento puede contener elementos con contenido multimedia ([&lt;media&gt;](../media/) elementos),
llamados objetos multimedia, otros elementos [&lt;context&gt;](../context/) anidados, elementos
agrupación de alternativas de contenido (elementos [&lt;switch&gt;](../switch/)) y relaciones
([&lt;link&gt;](../link/) elementos) entre todos los objetos representados por el
elementos antes mencionados.

Cabe destacar que el elemento [&lt;body&gt;](../body/) se considera un elemento especial
tipo de contexto, el que representa toda la aplicación.

El elemento [&lt;context&gt;](../context/) puede hacer referencia a otro [&lt;context&gt;](../context/) o un
elemento [&lt;body&gt;](../body/) importado. En este caso, hereda la especificación de
el elemento referido.

### Sintaxis { data-search-exclude }

| Elemento | Atributos | Contenido | Padre |
| --- | --- | --- | --- |
| [&lt;context&gt;](../context/) | <u>*id*</u>, *referir* | ([&lt;port&gt;](../port/)  &#124; [&lt;property&gt;](../property/)  &#124; [&lt;media&gt;](../media/)  &#124; [&lt;context&gt;](../context/)  &#124; [&lt;link&gt;](../link/)  &#124; [&lt;switch&gt;](../switch/)  &#124; [&lt;meta&gt;](../meta/)  &#124; [&lt;metadata&gt;](../metadata/))* | [&lt;body&gt;](../body/), [&lt;context&gt;](../context/) o [&lt;switch&gt;](../switch/) |

### Atributos { data-search-exclude }

| Nombre | Valor | Descripción |
| --- | --- | --- |
| *identificación* | Puede recibir cualquier valor de cadena que comience con una letra o un guión bajo y que solo contenga letras, dígitos, <"."> y <"_">. | El atributo *id* identifica de forma única el elemento dentro de un documento. |
| *referir* | IDREF o la cadena "alias#id" donde "id" es un valor IDREF. | <p>El atributo *refer* hace referencia a un elemento *id* que será reutilizado.  Un elemento que hace referencia a otro elemento no se puede reutilizar; es decir, su valor *id* no puede ser el valor de ningún atributo *refer*.  El elemento referido debe ser un [&lt;context&gt;](../context/) o un elemento [&lt;body&gt;](../body/) importado.</p><p>El elemento referido y el elemento que hace referencia a él deben considerarse iguales en cuanto a su especificación de datos.</p> <p>Si el nodo referido (elemento [&lt;context&gt;](../context/) o [&lt;body&gt;](../body/)) está definido dentro de un documento D importado, el valor del atributo *refer* debe tener el formato "alias#id", donde "alias" es el valor del atributo *alias* asociado con el documento D importado.</p> |
