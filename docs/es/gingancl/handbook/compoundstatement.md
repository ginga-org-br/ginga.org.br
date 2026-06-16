---
title: "Elemento &lt;compoundStatement&gt;"
---

### Definición y uso { data-search-exclude }

El elemento [&lt;compoundStatement&gt;](compoundstatement.md) define una expresión lógica entre sus
elementos secundarios ([&lt;assessmentStatement&gt;](assessmentstatement.md) y [&lt;compoundStatement&gt;](compoundstatement.md)) por
mediante un atributo booleano *operador*.

El atributo *isNegated* puede definirse para especificar que un
[&lt;compoundStatement&gt;](compoundstatement.md) elemento secundario debe negarse antes del booleano
Se evalúa la operación.

### Sintaxis { data-search-exclude }

| Elemento | Atributos | Contenido | Padre |  |
| --- | --- | --- | --- | --- |
| [&lt;compoundStatement&gt;](compoundstatement.md) | <u>*operador*</u>, *estáNegado* | ([&lt;assessmentStatement&gt;](assessmentstatement.md) | [&lt;compoundStatement&gt;](compoundstatement.md))+ | [&lt;compoundCondition&gt;](compoundcondition.md) o [&lt;compoundStatement&gt;](compoundstatement.md) |

### Atributos { data-search-exclude }

| Nombre | Valor | Descripción |
| --- | --- | --- |
| *operador* | "y" o "o". | El atributo *operador* define la expresión lógica entre los [&lt;compoundStatement&gt;](compoundstatement.md) elementos secundarios. |
| *está negado* | <p>"verdadero" o "falso".</p><p>El valor predeterminado es "falso".</p> | El atributo *isNegated* define si los [&lt;compoundStatement&gt;](compoundstatement.md) elementos secundarios deben negarse antes de evaluar la declaración. |
