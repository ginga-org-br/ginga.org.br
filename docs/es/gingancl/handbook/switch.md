---
title: "Elemento &lt;switch&gt;"
---

### Definición y uso { data-search-exclude }

El elemento [&lt;switch&gt;](switch.md) permite definir objetos alternativos
(representado por [&lt;media&gt;](media.md), [&lt;context&gt;](context.md) u otro [&lt;switch&gt;](switch.md)
elementos) a presentar.  La elección se realiza durante el tiempo de presentación.

Las reglas de prueba utilizadas para elegir el componente secundario del conmutador que se presentará son
definido por elementos [&lt;rule&gt;](rule.md) y [&lt;compositeRule&gt;](compositerule.md); [&lt;bindRule&gt;](bindrule.md)
Los elementos secundarios asocian estas reglas a los objetos del componente secundario del
[&lt;switch&gt;](switch.md) elemento.

Un elemento secundario [&lt;switchPort&gt;](switchport.md) puede definir una asignación a un subconjunto del
componentes secundarios del conmutador.  Cuando un enlace está vinculado a un [&lt;switchPort&gt;](switchport.md)
elemento, las reglas vinculadas a los componentes asignados se evalúan en el orden en que
están definidos.  La primera regla evaluada como verdadera determina el objeto elegido.
Si todas las reglas vinculadas a componentes asignados se evalúan como falsas, se aplicará un valor predeterminado.
se elige el componente, definido por el elemento secundario [&lt;defaultComponent&gt;](defaultcomponent.md); si
el elemento [&lt;defaultComponent&gt;](defaultcomponent.md) no está definido, no hay ningún componente seleccionado
para la presentación y el reproductor NCL se comporta como si el componente seleccionado
no existe.

Todas las referencias al componente secundario de un conmutador se realizan a través de
[&lt;switchPort&gt;](switchport.md) elementos o, de forma predeterminada, al elemento [&lt;switch&gt;](switch.md)
sin especificar ningún [&lt;switchPort&gt;](switchport.md).  En este caso se considera como
si la referencia se hace a un [&lt;switchPort&gt;](switchport.md) predeterminado que contiene
mapear elementos a cada objeto hijo del interruptor y hacer referencia a su
ancla de contenido completo.

Desde el momento en que se evalúa un [&lt;switch&gt;](switch.md) se considera resuelto
hasta el final de la presentación del interruptor actual.

El elemento [&lt;switch&gt;](switch.md) puede hacer referencia a otro elemento [&lt;switch&gt;](switch.md).  en
en este caso tiene la misma especificación del elemento referido.

### Sintaxis { data-search-exclude }

| Elemento | Atributos | Contenido | Padre |
| --- | --- | --- | --- |
| [&lt;switch&gt;](switch.md) | <u>*id*</u>, *referir* | ([&lt;defaultComponent&gt;](defaultcomponent.md)?, ([&lt;switchPort&gt;](switchport.md) &#124; [&lt;bindRule&gt;](bindrule.md) &#124; [&lt;media&gt;](media.md) &#124; [&lt;context&gt;](context.md) &#124; [&lt;switch&gt;](switch.md))*) | [&lt;body&gt;](body.md), [&lt;context&gt;](context.md) o [&lt;switch&gt;](switch.md) |

### Atributos { data-search-exclude }

| Nombre | Valor | Descripción |
| --- | --- | --- |
| *identificación* | Puede recibir cualquier valor de cadena que comience con una letra o un guión bajo y que solo contenga letras, dígitos, <"."> y <"_">. | El atributo *id* identifica de forma única el elemento dentro de un documento. |
| *referir* | IDREF o la cadena "alias#id" donde "id" es un valor IDREF. | <p>El atributo *refer* hace referencia a un elemento *id* que será reutilizado.  Un elemento que hace referencia a otro elemento no se puede reutilizar; es decir, su *id* no se puede reutilizar; es decir, su *id* no puede ser el valor de ningún atributo *refer*.  El elemento referido será un elemento [&lt;switch&gt;](switch.md).</p><p>El elemento referido y el elemento que hace referencia a él se considerarán iguales solo con respecto a su especificación de datos.</p><p>Si el nodo referido se define dentro de un documento importado D, el valor del atributo *refer* tendrá el formato "alias#id", donde "alias" es el valor del atributo *alias* asociado con el componente importado D.</p> |
