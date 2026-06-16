---
title: "Elemento &lt;switchPort&gt;"
---

### Definición y uso { data-search-exclude }

El elemento [&lt;switchPort&gt;](switchport.md) define una asignación a un subconjunto del
[&lt;switch&gt;](switch.md) componentes del elemento.  Todas las referencias a un interruptor interno.
El componente debe realizarse a través de un elemento [&lt;switchPort&gt;](switchport.md) o, por defecto,
al elemento [&lt;switch&gt;](switch.md) sin especificar ningún [&lt;switchPort&gt;](switchport.md). en
En este último caso, se considera como si se hiciera referencia a un incumplimiento.
[&lt;switchPort&gt;](switchport.md) que contiene elementos de mapeo para cada objeto secundario del
cambiar y hacer referencia a todos sus anclajes de contenido.

### Sintaxis { data-search-exclude }

| Elemento | Atributos | Contenido | Padre |
| --- | --- | --- | --- |
| [&lt;switchPort&gt;](switchport.md) | <u>*id*</u> | [&lt;mapping&gt;](mapping.md)+ | [&lt;switch&gt;](switch.md) |

### Atributos { data-search-exclude }

| Nombre | Valor | Descripción |
| --- | --- | --- |
| *identificación* | Puede recibir cualquier valor de cadena que comience con una letra o un guión bajo y que solo contenga letras, dígitos, <"."> y <"_">. | El atributo *id* identifica de forma única el elemento dentro de un documento. |