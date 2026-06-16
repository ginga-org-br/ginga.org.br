---
title: "Elemento &lt;compoundStatement&gt;"
---

### Definición y uso { data-search-exclude }

El elemento [&lt;compoundStatement&gt;](../compoundstatement/) define una expresión lógica entre sus
elementos secundarios ([&lt;assessmentStatement&gt;](../assessmentstatement/) y [&lt;compoundStatement&gt;](../compoundstatement/)) por
mediante un atributo booleano *operador*.

El atributo *isNegated* puede definirse para especificar que un
[&lt;compoundStatement&gt;](../compoundstatement/) elemento secundario debe negarse antes del booleano
Se evalúa la operación.

### Sintaxis { data-search-exclude }

| Elemento | Atributos | Contenido | Padre |  |
| --- | --- | --- | --- | --- |
| [&lt;compoundStatement&gt;](../compoundstatement/) | <u>*operador*</u>, *estáNegado* | ([&lt;assessmentStatement&gt;](../assessmentstatement/) | [&lt;compoundStatement&gt;](../compoundstatement/))+ | [&lt;compoundCondition&gt;](../compoundcondition/) o [&lt;compoundStatement&gt;](../compoundstatement/) |

### Atributos { data-search-exclude }

| Nombre | Valor | Descripción |
| --- | --- | --- |
| *operador* | "y" o "o". | El atributo *operador* define la expresión lógica entre los [&lt;compoundStatement&gt;](../compoundstatement/) elementos secundarios. |
| *está negado* | <p>"verdadero" o "falso".</p><p>El valor predeterminado es "falso".</p> | El atributo *isNegated* define si los [&lt;compoundStatement&gt;](../compoundstatement/) elementos secundarios deben negarse antes de evaluar la declaración. |
