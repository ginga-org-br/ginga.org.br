---
title: "Elemento &lt;importNCL&gt;"
---

### Definición y uso { data-search-exclude }

El elemento [&lt;importNCL&gt;](../importncl/) permite incorporar otro documento NCL
especificación.  Como consecuencia, todas las bases definidas dentro de la NCL importada
documento, así como el elemento documento [&lt;body&gt;](../body/), se importan, todo en
una vez.  Las bases serán tratadas como si cada una hubiera sido importada por [&lt;importBase&gt;](../importbase/)
elementos.  El elemento [&lt;body&gt;](../body/) importado se tratará como un [&lt;context&gt;](../context/)
elemento.  Cabe destacar que el elemento [&lt;importNCL&gt;](../importncl/) no
"incluir" el documento NCL referido pero solo hace que el documento referido
visible para que sus componentes sean reutilizados por el documento que ha definido el
[&lt;importNCL&gt;](../importncl/) elemento.  Así, el [&lt;body&gt;](../body/) importado, así como cualquiera de sus
nodos contenidos, se pueden reutilizar dentro del elemento [&lt;body&gt;](../body/) de la importación
Documento NCL.

El atributo *documentURI* del elemento [&lt;importNCL&gt;](../importncl/) hace referencia a un URI
correspondiente al documento NCL a importar.   El atributo *alias*
especifica un nombre que se utilizará como prefijo cuando se haga referencia a elementos de este
documento importado.  La referencia debe tener el formato: alias#element_id.  eso
Es importante tener en cuenta que se debe utilizar el mismo alias cuando se hace referencia a
elementos definidos en las bases de documentos importadas indirectamente ([&lt;regionBase&gt;](../regionbase/),
[&lt;connectorBase&gt;](../connectorbase/), [&lt;descriptorBase&gt;](../descriptorbase/), etc.).

La operación de importación es transitiva, es decir, si baseA importa baseB que
importa baseC, luego baseA importa baseC.  Sin embargo, el alias definido para
baseC dentro de baseBi no es considerada por baseA.

### Sintaxis { data-search-exclude }

| Elemento | Atributos | Contenido | Padre |
| --- | --- | --- | --- |
| [&lt;importNCL&gt;](../importncl/) | <u>*alias*</u>, <u>*documentURI*</u> | -- | [&lt;importedDocumentBase&gt;](../importeddocumentbase/) |

### Atributos { data-search-exclude }

| Nombre | Valor | Descripción |
| --- | --- | --- |
| *alias* | Puede recibir cualquier valor de cadena que comience con una letra o un guión bajo y que solo contenga letras, dígitos, <"."> y <"_">. | El atributo *alias* especifica un nombre que se utilizará como prefijo cuando se haga referencia a elementos de la base importada.  El valor *alias* debe ser único en un documento y su alcance está restringido al documento que ha definido el atributo alias. |
| *documentURI* | URI. | El atributo *documentURI* es el localizador del documento NCL desde donde se importará la base o el documento. |