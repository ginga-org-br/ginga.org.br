---
title: "Elemento &lt;descriptorParam&gt;"
---

### Definición y uso { data-search-exclude }

Los elementos [&lt;descriptorParam&gt;](descriptorparam.md) definen valores iniciales para las propiedades de
un elemento [&lt;media&gt;](media.md). La propiedad se identifica en el *nombre*
atributo del elemento [&lt;descriptorParam&gt;](descriptorparam.md) y el valor está definido en
el atributo *valor*.

### Sintaxis { data-search-exclude }

| Elemento | Atributos | Contenido | Padre |
| --- | --- | --- | --- |
| [&lt;descriptorParam&gt;](descriptorparam.md) | <u>*nombre*</u>, <u>*valor*</u> | -- | [&lt;descriptor&gt;](descriptor.md) |

### Atributos { data-search-exclude }

| Nombre | Valor | Descripción |
| --- | --- | --- |
| *nombre* | Puede recibir cualquier valor de cadena que comience con una letra o un guión bajo y que solo contenga letras, dígitos, <"."> y <"_">. | El atributo *name* identifica la propiedad del elemento [&lt;media&gt;](media.md) que hace referencia al elemento [&lt;descriptor&gt;](descriptor.md) padre del elemento [&lt;descriptorParam&gt;](descriptorparam.md). |
| *valor* | Depende del valor *nombre*. | El atributo *valor* define un valor inicial para la propiedad identificada en el atributo *nombre*. |