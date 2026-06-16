---
title: "Elemento &lt;defaultComponent&gt;"
---

### Definición y uso { data-search-exclude }

El elemento [&lt;defaultComponent&gt;](defaultcomponent.md) identifica el componente secundario predeterminado
del elemento [&lt;switch&gt;](switch.md) que debe seleccionarse si todas las reglas vinculadas a
componentes mapeados del elemento [&lt;switchPort&gt;](switchport.md), a través del cual el
[&lt;switch&gt;](switch.md) elemento fue activado, se evalúan como falso.

### Sintaxis { data-search-exclude }

| Elemento | Atributos | Contenido | Padre |
| --- | --- | --- | --- |
| [&lt;defaultComponent&gt;](defaultcomponent.md) | <u>*componente*</u> | -- | [&lt;switch&gt;](switch.md) o [&lt;descriptorSwitch&gt;](descriptorswitch.md) |

### Atributos { data-search-exclude }

| Nombre | Valor | Descripción |
| --- | --- | --- |
| *componente* | IDREF. | El atributo *defaultComponent* identifica de forma única un elemento secundario del elemento [&lt;switch&gt;](switch.md). |