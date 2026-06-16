---
title: "Elemento &lt;valueAssessment&gt;"
---

### Definición y uso { data-search-exclude }

El elemento [&lt;valueAssessment&gt;](valueassessment.md) se utiliza para definir un valor a comparar
contra otros valores de variables especificados por [&lt;attributeAssessment&gt;](attributeassessment.md)
elementos.

El elemento [&lt;valueAssessment&gt;](valueassessment.md) tiene un atributo de valor que puede asumir un
valor del estado del evento ("ocurriendo", "pausado" o "inactivo"), o cualquier valor que se deba
comparado con una propiedad de nodo o atributo de evento ("ocurrencias" o
"repetición").

### Sintaxis { data-search-exclude }

| Elemento | Atributos | Contenido | Padre |
| --- | --- | --- | --- |
| [&lt;valueAssessment&gt;](valueassessment.md) | <u>*valor*</u> | -- | [&lt;assessmentStatement&gt;](assessmentstatement.md) |

### Atributos { data-search-exclude }

| Nombre | Valor | Descripción |
| --- | --- | --- |
| *valor* | <p>String.</p><p>Puede ser un valor de estado de evento ("ocurriendo", "en pausa" o "inactivo"), o cualquier valor que se compare con una propiedad de nodo o atributo de evento ("ocurrencias" o "repeticiones").</p> | El atributo *valor* define un valor que se comparará en [&lt;assessmentStatement&gt;](assessmentstatement.md) elementos. |