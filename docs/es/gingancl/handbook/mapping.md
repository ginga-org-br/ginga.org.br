---
title: "Elemento &lt;mapping&gt;"
---

# &lt;mapping&gt;

Explore el ejemplo de `<mapping>` a continuación:

<div class="ginga-playground-container">

<nav class="ginga-playground-tabs" role="tablist" aria-label="Ejemplos de Ginga Playground">
  <button type="button" class="ginga-playground-tab" role="tab" aria-selected="true" data-playground-src="https://ginga.org.br/gingaf/playground/?app=https://raw.githubusercontent.com/ginga-org-br/gingaf/refs/heads/main/examples/ginga.org.br/mapping.ncl">mapping.ncl</button>
</nav>

<iframe
  class="ginga-playground"
  src="https://ginga.org.br/gingaf/playground/?app=https://raw.githubusercontent.com/ginga-org-br/gingaf/refs/heads/main/examples/ginga.org.br/mapping.ncl"
  loading="lazy"
  allow="autoplay; fullscreen">
</iframe>

</div>

Un elemento de mapeo define una ruta desde [&lt;switchPort&gt;](switchport.md) a una interfaz
(atributo de interfaz) de uno de los componentes del conmutador (especificado por su
atributo del componente).

### Sintaxis { data-search-exclude }

| Elemento | Atributos | Contenido | Padre |
| --- | --- | --- | --- |
| [&lt;mapping&gt;](mapping.md) | <u>*componente*</u>, *interfaz* | -- | [&lt;switchPort&gt;](switchport.md) |

### Atributos { data-search-exclude }

| Nombre | Valor | Descripción |
| --- | --- | --- |
| *componente* | IDREF. | El atributo *component* identifica de forma única un elemento secundario del conmutador, a través de su valor *id*. |
| *interfaz* | <p>String.</p><p>El valor predeterminado es el ancla de contenido completo.</p> | El atributo *interface* identifica de forma única una interfaz ([&lt;area&gt;](area.md), [&lt;property&gt;](property.md), [&lt;port&gt;](port.md) o [&lt;switchPort&gt;](switchport.md)) de un elemento secundario de [&lt;switch&gt;](switch.md), a través de su *id* o valor de nombre. |