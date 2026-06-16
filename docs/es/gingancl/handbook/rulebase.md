---
title: "Elemento &lt;ruleBase&gt;"
---

### Definición y uso { data-search-exclude }

El elemento [&lt;ruleBase&gt;](rulebase.md) agrupa un conjunto de reglas especificadas en [&lt;rule&gt;](rule.md)
y [&lt;compositeRule&gt;](compositerule.md) elementos.  La especificación de reglas en NCL 3.0
se hizo en un módulo separado, porque son útiles para definir
componentes alternativos o descriptores alternativos.

### Sintaxis { data-search-exclude }

| Elemento | Atributos | Contenido | Padre |  |  |
| --- | --- | --- | --- | --- | --- |
| [&lt;ruleBase&gt;](rulebase.md) | *identificación* | ([&lt;importBase&gt;](importbase.md) | [&lt;compositeRule&gt;](compositerule.md) | [&lt;rule&gt;](rule.md))+ | [&lt;head&gt;](head.md) |

### Atributos { data-search-exclude }

| Nombre | Valor | Descripción |
| --- | --- | --- |
| *identificación* | Puede recibir cualquier valor de cadena que comience con una letra o un guión bajo y que solo contenga letras, dígitos, <"."> y <"_">. | El atributo *id* identifica de forma única el elemento dentro de un documento. |
