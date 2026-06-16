---
title: "Elemento &lt;rule&gt;"
---

### Definición y uso { data-search-exclude }

El elemento [&lt;rule&gt;](rule.md) define reglas simples para definir cualquiera de las alternativas
componentes o descriptores alternativos.

El atributo *id* es el identificador de la regla.  Una regla se establece por
comparar (atributo *comparador*) una variable (atributo *var*)
valor con un valor absoluto.  La variable será una propiedad del
nodo de configuración ([&lt;media&gt;](media.md) elemento de aplicación/tipo de configuración x-ncl),
es decir, el atributo *var* debe tener como valor un nombre de propiedad de
el elemento [&lt;media&gt;](media.md) del tipo "aplicación/x-ncl-settings".

### Sintaxis { data-search-exclude }

| Elemento | Atributos | Contenido | Padre |
| --- | --- | --- | --- |
| [&lt;rule&gt;](rule.md) | *id*, <u>*var*</u>, <u>*comparador*</u>, <u>*valor*</u> | -- | [&lt;ruleBase&gt;](rulebase.md) o [&lt;compositeRule&gt;](compositerule.md) |

### Atributos { data-search-exclude }

| Nombre | Valor | Descripción |
| --- | --- | --- |
| *identificación* | Puede recibir cualquier valor de cadena que comience con una letra o un guión bajo y que solo contenga letras, dígitos, <"."> y <"_">. | El atributo *id* identifica de forma única el elemento dentro de un documento. |
| *var* | Puede recibir cualquier valor de cadena que comience con una letra o un guión bajo y que solo contenga letras, dígitos, <"."> y <"_">. | El atributo *var* identifica de forma única un nombre de propiedad del nodo de configuración (elemento [&lt;media&gt;](media.md) de tipo "application/x-ncl-settings"). |
| *comparador* | "eq", "ne", "gt", "lt", "gte" o "lte". | El atributo *comparator* compara el valor de la propiedad especificada por el atributo *var* con el valor absoluto especificado en el atributo *value*. |
| *valor* | Cadena. | El atributo *value* define un valor que se comparará con el valor de propiedad al que hace referencia el atributo *var*. |