---
title: "Elemento &lt;bindRule&gt;"
---

### Definición y uso { data-search-exclude }

El elemento [&lt;bindRule&gt;](bindrule.md) asocia una regla con un componente de un
elemento [&lt;switch&gt;](switch.md) o [&lt;descriptorSwitch&gt;](descriptorswitch.md), a través de su regla y
atributos constituyentes, respectivamente.

### Sintaxis { data-search-exclude }

| Elemento | Atributos | Contenido | Padre |
| --- | --- | --- | --- |
| [&lt;bindRule&gt;](bindrule.md) | <u>*constituyente*</u>, <u>*regla*</u> | -- | [&lt;switch&gt;](switch.md) o [&lt;descriptorSwitch&gt;](descriptorswitch.md) |

### Atributos { data-search-exclude }

| Nombre | Valor | Descripción |
| --- | --- | --- |
| *constituyente* | IDREF. | El atributo *constituent* identifica de forma única un elemento secundario del elemento [&lt;switch&gt;](switch.md) o [&lt;descriptorSwitch&gt;](descriptorswitch.md), a través de su valor *id*. |
| *regla* | IDREF. | El atributo *rule* identifica de forma única una regla definida por un elemento [&lt;rule&gt;](rule.md) o *compositeRule*, a través de su valor *id*. |