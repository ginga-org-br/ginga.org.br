---
title: "Elemento &lt;regionBase&gt;"
---

### Definición y uso { data-search-exclude }

El elemento [&lt;regionBase&gt;](regionbase.md) agrupa un conjunto de elementos [&lt;region&gt;](region.md), cada uno
de los cuales puede contener otro conjunto de elementos [&lt;region&gt;](region.md) anidados, y así
adelante, recursivamente.

Cada elemento [&lt;regionBase&gt;](regionbase.md) está asociado con una clase de dispositivos donde
se realizará la presentación.  Para identificar la asociación, el
El elemento [&lt;regionBase&gt;](regionbase.md) define el atributo *dispositivo*.  cuando el
El atributo no está especificado, la presentación se realiza en el mismo dispositivo.
que ejecuta el reproductor NCL.

Hay dos tipos diferentes de clases de dispositivos: activos y pasivos.  en un
clase activa, un dispositivo puede ejecutar algunos reproductores multimedia durante [&lt;media&gt;](media.md)
presentaciones de elementos.  En una clase pasiva, no se requiere que un dispositivo se ejecute
Reproductores multimedia, solo para exhibir un mapa de bits o una secuencia de muestras de audio.
recibido de otro dispositivo.

La propiedad "deviceClass" de un elemento [&lt;media&gt;](media.md) se inicializa con el
*valor del dispositivo*, si el elemento [&lt;media&gt;](media.md) se refiere indirectamente a un
elemento [&lt;region&gt;](region.md) dentro de un [&lt;regionBase&gt;](regionbase.md), utilizando un
[&lt;descriptor&gt;](descriptor.md) elemento.

La clase elegida también define las variables de entorno global (propiedades
del objeto de configuración ---[&lt;media&gt;](media.md) elemento de
Tipo "aplicación/x-ncl-settings": "system.screenSize(i)",
"system.screenGraphicSize(i)" y "system.audioType(i)".

"systemScreen(1)" y "systemAudio(1)" están reservados para clases pasivas,
y "systemScreen(2)" y "systemAudio(2)" están reservados para clases activas.

El elemento [&lt;regionBase&gt;](regionbase.md) que define una clase pasiva también puede tener un
atributo de región.  Este atributo se utiliza para identificar un [&lt;region&gt;](region.md)
elemento en otro [&lt;regionBase&gt;](regionbase.md) asociado con el dispositivo principal que
crea el mapa de bits enviado a la clase pasiva; en la región especificada el
También se debe exhibir el mapa de bits.  La propiedad "system.parentDeviceRegion(i)"
del objeto de configuración ([&lt;media&gt;](media.md) elemento de "application/x-ncl-settings"
tipo) se inicializa con el valor del atributo *región*.

### Sintaxis { data-search-exclude }

| Elemento | Atributos | Contenido | Padre |  |
| --- | --- | --- | --- | --- |
| [&lt;regionBase&gt;](regionbase.md) | *id*, *dispositivo*, *región* | ([&lt;importBase&gt;](importbase.md) | [&lt;region&gt;](region.md))+ | [&lt;head&gt;](head.md) |

### Atributos { data-search-exclude }

| Nombre | Valor | Descripción |
| --- | --- | --- |
| *identificación* | Puede recibir cualquier valor de cadena que comience con una letra o un guión bajo y que solo contenga letras, dígitos, <"."> y <"_">. | El atributo *id* identifica de forma única el elemento dentro de un documento. |
| *dispositivo* | "systemScreen(i)" o "systemAudio(i)".  Cuando no se especifica el atributo, la presentación se realizará en la misma clase de dispositivo que ejecuta el reproductor NCL. | El atributo *dispositivo* identifica la clase de dispositivos donde se realizará la presentación. |
| *región* | IDREF. | El atributo *region* identifica un elemento [&lt;region&gt;](region.md) en otro [&lt;regionBase&gt;](regionbase.md) asociado con el dispositivo principal que crea el mapa de bits enviado a la clase pasiva; en la región especificada también se debe exhibir el mapa de bits. |
