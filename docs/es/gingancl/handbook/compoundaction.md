---
title: "Elemento &lt;compoundAction&gt;"
---

### Definición y uso { data-search-exclude }

El elemento [&lt;compoundAction&gt;](compoundaction.md) define una expresión lógica entre sus
elementos secundarios ([&lt;simpleAction&gt;](simpleaction.md), [&lt;compoundAction&gt;](compoundaction.md)) mediante un
Atributo del operador que puede recibir el valor "par" o "seq".

Las acciones compuestas paralelas ("par") y secuenciales ("seq") especifican que el
la ejecución de acciones se realizará en cualquier orden o en un orden específico,
respectivamente.  Cuando se utilice el operador secuencial, se dispararán acciones.
en el orden especificado.  Sin embargo, una acción no necesita esperar el
el anterior por terminar.

También se puede definir un atributo *delay* especificando que el compuesto
La acción debe aplicarse después del retraso especificado.

### Sintaxis { data-search-exclude }

| Elemento | Atributos | Contenido | Padre |  |
| --- | --- | --- | --- | --- |
| [&lt;compoundAction&gt;](compoundaction.md) | <u>*operador*</u>, *retraso* | ([&lt;simpleAction&gt;](simpleaction.md) | [&lt;compoundAction&gt;](compoundaction.md))+ | [&lt;causalConnector&gt;](causalconnector.md) o [&lt;compoundAction&gt;](compoundaction.md) |

### Atributos { data-search-exclude }

| Nombre | Valor | Descripción |
| --- | --- | --- |
| *operador* | "seq" o "par". El valor predeterminado es "par". | El *operador* define el orden en que se deben aplicar las acciones en los [&lt;compoundAction&gt;](compoundaction.md) elementos secundarios. |
| *retraso* | <p>El atributo *retraso* se especificará de acuerdo con uno de los siguientes sintaxis:</p><ol><li class="level1"><div class="li"><"<nowiki>Horas:Minutos:Segundos.Fracción</nowiki>">, donde "Horas" es un número entero en el intervalo \[0,23\], "Minutos" es un número entero en el intervalo \[0,59\], "Segundos" es un número entero en el intervalo 0,59 y "Fracción" es un intervalo positivo entero,</div></li><li class="level1"><div class="li">Seconds<"s">, donde "Segundos" es un real positivo número.</div></li></ol><p>El valor predeterminado es "0s".</p> | El atributo *delay* define un retraso de tiempo que se debe esperar antes de activar [&lt;compoundAction&gt;](compoundaction.md).
