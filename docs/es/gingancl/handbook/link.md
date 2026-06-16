---
title: "Elemento &lt;link&gt;"
---

### Definición y uso { data-search-exclude }

El elemento [&lt;link&gt;](link.md) define una relación entre medios y compuestos.
objetos.

Un elemento [&lt;link&gt;](link.md) puede tener un atributo *id*, que de forma única
Identifica el elemento dentro de un documento y debe tener un
Atributo *xconnector*, que hace referencia a un URI de conector.

El elemento [&lt;causalConnector&gt;](causalconnector.md) referido define la relación sin
especificando quién desempeña los roles de relación.  Quién juega se define usando
[&lt;bind&gt;](bind.md) elementos, hijos del elemento [&lt;link&gt;](link.md).

### Sintaxis { data-search-exclude }

| Elemento | Atributos | Contenido | Padre |
| --- | --- | --- | --- |
| [&lt;link&gt;](link.md) | *id*, <u>*xconector*</u> | ([&lt;linkParam&gt;](linkparam.md)*, [&lt;bind&gt;](bind.md)+) | [&lt;body&gt;](body.md) o [&lt;context&gt;](context.md) o [&lt;switch&gt;](switch.md) |

### Atributos { data-search-exclude }

| Nombre | Valor | Descripción |
| --- | --- | --- |
| *identificación* | Puede recibir cualquier valor de cadena que comience con una letra o un guión bajo y que solo contenga letras, dígitos, <"."> y <"_">. | El atributo *id* identifica de forma única el elemento dentro de un documento. |
| *xconector* | <p>String.</p><p>El valor debe tener el formato:</p><ol><li class="level1"><div class="li">"alias#connector_id", o "documentURI_value#connector_id", para conectores definidos en un documento externo importado, o</div></li><li class="level1"><div class="li">"connector_id", el conector *id* para conectores definidos en el documento sí mismo.</div></li> | El atributo *xconnector* hace referencia a un conector definido como elemento descendiente de [&lt;connectorBase&gt;](connectorbase.md) en un documento externo importado. |