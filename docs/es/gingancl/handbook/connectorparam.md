---
title: "Elemento &lt;connectorParam&gt;"
---

### Definición y uso { data-search-exclude }

El elemento [&lt;connectorParam&gt;](connectorparam.md) se utiliza para parametrizar el conector.
valores de atributos.  Cualquier atributo definido por un elemento [&lt;causalConnector&gt;](causalconnector.md)
o por sus elementos descendientes puede tener su valor especificado como parámetro
cuyo valor está definido por la relación que hace referencia al conector,
utilizando elementos [&lt;linkParam&gt;](linkparam.md) o [&lt;bindParam&gt;](bindparam.md).

En un elemento [&lt;connectorParam&gt;](connectorparam.md) el atributo *nombre* define el
nombre del parámetro y el atributo *type* el tipo de parámetro.

Para especificar que un atributo definido por [&lt;causalConnector&gt;](causalconnector.md)
elemento o por sus elementos descendientes recibe el valor del parámetro, es
suficiente para definir el valor del atributo como el nombre del parámetro precedido por
el símbolo "$".  Por ejemplo, para parametrizar el atributo de retraso
de un elemento [&lt;simpleAction&gt;](simpleaction.md), un parámetro llamado *actionDelay* es
definido y el valor "$actionDelay" se utiliza en el atributo
(*retraso*="$acciónRetraso").

### Sintaxis { data-search-exclude }

| Elemento | Atributos | Contenido | Padre |
| --- | --- | --- | --- |
| [&lt;connectorParam&gt;](connectorparam.md) | <u>*nombre*</u>, *tipo* | -- | [&lt;causalConnector&gt;](causalconnector.md) |

### Atributos { data-search-exclude }

| Nombre | Valor | Descripción |
| --- | --- | --- |
| *nombre* | Puede recibir cualquier valor de cadena que comience con una letra o un guión bajo y que solo contenga letras, dígitos, <"."> y <"_">. | El atributo *name* identifica de forma única el parámetro dentro de un elemento [&lt;causalConnector&gt;](causalconnector.md). |
| *tipo* | Cadena. | El *tipo* define un tipo para el parámetro. |