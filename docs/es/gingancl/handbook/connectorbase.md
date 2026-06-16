---
title: "Elemento &lt;connectorBase&gt;"
---

### Definición y uso { data-search-exclude }

El elemento [&lt;connectorBase&gt;](connectorbase.md) agrupa relaciones definidas mediante conectores.

Los conectores se pueden definir directamente en el elemento [&lt;connectorBase&gt;](connectorbase.md) que es
hijo del elemento [&lt;head&gt;](head.md) de una aplicación NCL.  Sin embargo, desde el
La definición de conectores puede resultar difícil para usuarios no expertos, la idea es
tener expertos definiendo conectores, almacenándolos en bibliotecas (conector
bases) que puedan ser importados, y ponerlos a disposición de otros para su
creando enlaces.

### Sintaxis { data-search-exclude }

| Elemento | Atributos | Contenido | Padre |  |
| --- | --- | --- | --- | --- |
| [&lt;connectorBase&gt;](connectorbase.md) | *identificación* | ([&lt;importBase&gt;](importbase.md) | [&lt;causalConnector&gt;](causalconnector.md))* | [&lt;head&gt;](head.md) |

### Atributos { data-search-exclude }

| Nombre | Valor | Descripción |
| --- | --- | --- |
| *identificación* | Puede recibir cualquier valor de cadena que comience con una letra o un guión bajo y que solo contenga letras, dígitos, <"."> y <"_">. | El atributo *id* identifica de forma única el elemento dentro de un documento. |
