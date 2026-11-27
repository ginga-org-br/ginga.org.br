---
title: "Elemento &lt;switchPort&gt;"
---

# &lt;switchPort&gt;

Explore el ejemplo de `<switchPort>` a continuación:

<div class="ginga-playground-container">

<nav class="ginga-playground-tabs" role="tablist" aria-label="Ejemplos de Ginga Playground">
  <button type="button" class="ginga-playground-tab" role="tab" aria-selected="true" data-playground-src="https://ginga.org.br/gingaf/playground/?app=https://raw.githubusercontent.com/ginga-org-br/gingaf/refs/heads/main/examples/ginga.org.br/switchPort.ncl">switchPort.ncl</button>
</nav>

<iframe
  class="ginga-playground"
  src="https://ginga.org.br/gingaf/playground/?app=https://raw.githubusercontent.com/ginga-org-br/gingaf/refs/heads/main/examples/ginga.org.br/switchPort.ncl"
  loading="lazy"
  allow="autoplay; fullscreen">
</iframe>

</div>

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