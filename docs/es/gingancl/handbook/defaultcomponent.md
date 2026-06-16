---
title: "Elemento &lt;defaultComponent&gt;"
---

### Definición y uso { data-search-exclude }

El elemento [&lt;defaultComponent&gt;](../defaultcomponent/) identifica el componente secundario predeterminado
del elemento [&lt;switch&gt;](../switch/) que debe seleccionarse si todas las reglas vinculadas a
componentes mapeados del elemento [&lt;switchPort&gt;](../switchport/), a través del cual el
[&lt;switch&gt;](../switch/) elemento fue activado, se evalúan como falso.

### Sintaxis { data-search-exclude }

| Elemento | Atributos | Contenido | Padre |
| --- | --- | --- | --- |
| [&lt;defaultComponent&gt;](../defaultcomponent/) | <u>*componente*</u> | -- | [&lt;switch&gt;](../switch/) o [&lt;descriptorSwitch&gt;](../descriptorswitch/) |

### Atributos { data-search-exclude }

| Nombre | Valor | Descripción |
| --- | --- | --- |
| *componente* | IDREF. | El atributo *defaultComponent* identifica de forma única un elemento secundario del elemento [&lt;switch&gt;](../switch/). |