---
title: "Elemento &lt;descriptorSwitch&gt;"
---

### Definición y uso { data-search-exclude }

El elemento [&lt;descriptorSwitch&gt;](descriptorswitch.md) contiene un conjunto de alternativas
descriptores que se asociarán con un objeto.  La elección se hace durante
tiempo de presentación.

Las reglas de prueba utilizadas para elegir el elemento [&lt;descriptor&gt;](descriptor.md) están definidas por
elementos [&lt;rule&gt;](rule.md) y [&lt;compositeRule&gt;](compositerule.md); [&lt;bindRule&gt;](bindrule.md) niño
Los elementos asocian estas reglas a elementos secundarios [&lt;descriptor&gt;](descriptor.md) del
[&lt;descriptorSwitch&gt;](descriptorswitch.md) elemento.

Las reglas se evalúan en el orden en que se definen.  la primera regla
evaluado como verdadero determina el elemento [&lt;descriptor&gt;](descriptor.md) elegido.  si todo
las reglas se evalúan como falsas, un elemento [&lt;descriptor&gt;](descriptor.md) predeterminado, definido
por el elemento [&lt;defaultDescriptor&gt;](defaultdescriptor.md),se elige; si el
[&lt;defaultDescriptor&gt;](defaultdescriptor.md) elemento no está definido no se ha seleccionado ningún descriptor
y el reproductor NCL se comporta como si el elemento no existiera.

### Sintaxis { data-search-exclude }

| Elemento | Atributos | Contenido | Padre |  |
| --- | --- | --- | --- | --- |
| [&lt;descriptorSwitch&gt;](descriptorswitch.md) | <u>*id*</u> | ([&lt;defaultDescriptor&gt;](defaultdescriptor.md)?, ([&lt;bindRule&gt;](bindrule.md) | [&lt;descriptor&gt;](descriptor.md))*) | [&lt;descriptorBase&gt;](descriptorbase.md) |

### Atributos { data-search-exclude }

| Nombre | Valor | Descripción |
| --- | --- | --- |
| *identificación* | Puede recibir cualquier valor de cadena que comience con una letra o un guión bajo y que solo contenga letras, dígitos, <"."> y <"_">. | El atributo *id* identifica de forma única el elemento dentro de un documento. |
