---
title: "Elemento &lt;compoundCondition&gt;"
---

### Definición y uso { data-search-exclude }

El elemento [&lt;compoundCondition&gt;](compoundcondition.md) define una expresión lógica entre sus
elementos secundarios mediante su atributo booleano *operador*.

También se puede definir un atributo *delay* especificando que el compuesto
la condición es verdadera después de un retraso de tiempo desde la expresión que relaciona a su hijo
elementos es cierto.

Cuando una condición compuesta "y" relaciona más de una condición desencadenante
(es decir, una condición que se cumple en un tiempo infinitesimal
instante –--como por ejemplo, el final de la presentación de un objeto), el compuesto
condición se considerará verdadera en el instante inmediato posterior a todas las
se cumplen las condiciones de activación.

### Sintaxis { data-search-exclude }

| Elemento | Atributos | Contenido | Padre |  |  |
| --- | --- | --- | --- | --- | --- |
| [&lt;compoundCondition&gt;](compoundcondition.md) | <u>*operador*</u>, *retraso* | (([&lt;simpleCondition&gt;](simplecondition.md) | [&lt;compoundCondition&gt;](compoundcondition.md))+,([&lt;assessmentStatement&gt;](assessmentstatement.md) | [&lt;compoundStatement&gt;](compoundstatement.md))*) | [&lt;causalConnector&gt;](causalconnector.md) o [&lt;compoundCondition&gt;](compoundcondition.md) |

### Atributos { data-search-exclude }

| Nombre | Valor | Descripción |
| --- | --- | --- |
| *operador* | "y" o "o". | El atributo *operador* define una expresión lógica entre los [&lt;compoundCondition&gt;](compoundcondition.md) elementos secundarios. |
| *retraso* | <p>El atributo *retraso* se especificará de acuerdo con uno de los siguientes sintaxis:</p><ol><li class="level1"><div class="li"><"<nowiki>Horas:Minutos:Segundos.Fracción</nowiki>">, donde "Horas" es un número entero en el intervalo \[0,23\], "Minutos" es un número entero en el intervalo \[0,59\], "Segundos" es un número entero en el intervalo 0,59 y "Fracción" es un intervalo positivo entero,</div></li><li class="level1"><div class="li">Seconds<"s">, donde "Segundos" es un real positivo número.</div></li></ol><p>El valor predeterminado es "0s".</p> | El atributo *delay* define que [&lt;compoundCondition&gt;](compoundcondition.md) es verdadero después de un retraso de tiempo desde que la expresión que relaciona sus elementos secundarios es verdadera.
