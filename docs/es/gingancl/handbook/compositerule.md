---
title: "Elemento &lt;compositeRule&gt;"
---

### Definición y uso { data-search-exclude }

El elemento [&lt;compositeRule&gt;](../compositerule/) define una expresión lógica entre sus
elementos secundarios ([&lt;rule&gt;](../rule/) y [&lt;compositeRule&gt;](../compositerule/)) mediante un valor booleano
atributo del operador.

### Sintaxis { data-search-exclude }

| Elemento | Atributos | Contenido | Padre |  |
| --- | --- | --- | --- | --- |
| [&lt;compositeRule&gt;](../compositerule/) | <u>*id*</u>, <u>*operador*</u> | ([&lt;compositeRule&gt;](../compositerule/) | [&lt;rule&gt;](../rule/))+ | [&lt;ruleBase&gt;](../rulebase/) o [&lt;compositeRule&gt;](../compositerule/) |

### Atributos { data-search-exclude }

| Nombre | Valor | Descripción |
| --- | --- | --- |
| *identificación* | Puede recibir cualquier valor de cadena que comience con una letra o un guión bajo y que solo contenga letras, dígitos, <"."> y <"_">. | El atributo *id* identifica de forma única el elemento dentro de un documento. |
| *operador* | "y" o "o". | El atributo *operador* define una expresión lógica entre los elementos secundarios del elemento [&lt;compositeRule&gt;](../compositerule/). |
