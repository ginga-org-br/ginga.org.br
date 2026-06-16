---
title: "Elemento &lt;bindParam&gt;"
---

### Definición y uso { data-search-exclude }

El elemento [&lt;bindParam&gt;](../bindparam/) se utiliza para atribuir un valor a un parámetro
definido por el elemento [&lt;connectorParam&gt;](../connectorparam/) de [&lt;causalConnector&gt;](../causalconnector/)
elemento referido por el elemento padre [&lt;link&gt;](../link/).  El alcance de la
El valor atribuido se limita al elemento principal [&lt;bind&gt;](../bind/).

En un elemento [&lt;bindParam&gt;](../bindparam/) el atributo *name* hace referencia al nombre
de un parámetro de conector, mientras que el atributo *valor* define un valor
que se asignará al parámetro respectivo.

### Sintaxis { data-search-exclude }

| Elemento | Atributos | Contenido | Padre |
| --- | --- | --- | --- |
| [&lt;bindParam&gt;](../bindparam/) | <u>*nombre*</u>, <u>*valor*</u> | -- | [&lt;bind&gt;](../bind/) |

### Atributos { data-search-exclude }

| Nombre | Valor | Descripción |
| --- | --- | --- |
| *nombre* | Puede recibir cualquier valor de cadena que comience con una letra o un guión bajo y que solo contenga letras, dígitos, <"."> y <"_">. | El atributo *name* identifica de forma única el parámetro dentro del elemento [&lt;causalConnector&gt;](../causalconnector/) al que se hace referencia. |
| *valor* | Depende del parámetro definido por el elemento [&lt;connectorParam&gt;](../connectorparam/). | El atributo *valor* identifica de forma única el parámetro dentro del elemento [&lt;causalConnector&gt;](../causalconnector/) referido. |