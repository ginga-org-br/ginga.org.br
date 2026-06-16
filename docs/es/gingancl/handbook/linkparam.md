---
title: "Elemento &lt;linkParam&gt;"
---

### Definición y uso { data-search-exclude }

El elemento [&lt;linkParam&gt;](linkparam.md) se utiliza para atribuir un valor a un parámetro
definido por el elemento [&lt;connectorParam&gt;](connectorparam.md) de [&lt;causalConnector&gt;](causalconnector.md)
elemento referido por el elemento padre [&lt;link&gt;](link.md).  El alcance de la
El valor atribuido es todo el elemento principal [&lt;link&gt;](link.md).

En un elemento [&lt;linkParam&gt;](linkparam.md), el atributo *name* hace referencia al nombre
de un parámetro de conector mientras que el atributo *valor* define un valor
asignado a este parámetro.

### Sintaxis { data-search-exclude }

| Elemento | Atributos | Contenido | Padre |
| --- | --- | --- | --- |
| [&lt;linkParam&gt;](linkparam.md) | <u>*nombre*</u>, <u>*valor*</u> | -- | [&lt;link&gt;](link.md) |

### Atributos { data-search-exclude }

| Nombre | Valor | Descripción |
| --- | --- | --- |
| *nombre* | Puede recibir cualquier valor de cadena que comience con una letra o un guión bajo y que solo contenga letras, dígitos, <"."> y <"_">. | El atributo *name* identifica de forma única el parámetro dentro del elemento [&lt;causalConnector&gt;](causalconnector.md) al que se hace referencia. |
| *valor* | Depende del parámetro definido por el elemento [&lt;connectorParam&gt;](connectorparam.md). | El atributo *valor* define un valor para el parámetro.  Por tanto, el valor es válido para toda la definición [&lt;link&gt;](link.md). |