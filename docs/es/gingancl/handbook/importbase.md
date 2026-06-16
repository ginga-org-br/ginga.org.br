---
title: "Elemento &lt;importBase&gt;"
---

### Definición y uso { data-search-exclude }

El elemento [&lt;importBase&gt;](../importbase/) permite incorporar una base de entidad
(representado por [&lt;connectorBase&gt;](../connectorbase/), [&lt;regionBase&gt;](../regionbase/),
[&lt;descriptorBase&gt;](../descriptorbase/), [&lt;ruleBase&gt;](../rulebase/) o [&lt;transitionBase&gt;](../transitionbase/)
elementos definidos en un documento externo) a otro ya definido
base. Su atributodocumentURI se refiere a un URI correspondiente a la NCL
documento que contiene la base a importar. El atributo alias especifica un
nombre que se utilizará como prefijo cuando se haga referencia a elementos de este importado
base. La referencia debe tener el formato: <nowiki>alias#element_id</nowiki>.

La operación de importación es transitiva, es decir, si baseA importa baseB que
importa baseC, luego baseA importa baseC. Sin embargo, el alias definido para
baseC dentro de baseB no es considerada por baseA.

Se deben cumplir las siguientes restricciones:

* el elemento [&lt;descriptorBase&gt;](../descriptorbase/) puede tener un elemento secundario [&lt;importBase&gt;](../importbase/)
    elemento que hace referencia a un URI correspondiente a otro documento NCL
    que contiene la base del descriptor que se importará y anidará. cuando un
    Se importa la base de descriptores, la base de región, la base de transición y
    la base de reglas, cuando está presente en el documento importado, también
    importado automáticamente a la región correspondiente y a las bases de reglas del
    documento de importación;
  * el elemento [&lt;connectorBase&gt;](../connectorbase/) puede tener un elemento secundario [&lt;importBase&gt;](../importbase/)
    elemento que hace referencia a un URI correspondiente a otra base de conector a ser
    importado y anidado;
  * el elemento [&lt;transitionBase&gt;](../transitionbase/) puede tener un elemento secundario [&lt;importBase&gt;](../importbase/)
    elemento que hace referencia a un URI correspondiente a otra base de transición a
    ser importado y anidado;
  * el elemento [&lt;ruleBase&gt;](../rulebase/) puede tener un elemento secundario [&lt;importBase&gt;](../importbase/)
    haciendo referencia a un URI correspondiente a otro documento NCL que contiene el
    base de reglas para importar y anidar;
  * el elemento [&lt;regionBase&gt;](../regionbase/) puede tener un elemento secundario [&lt;importBase&gt;](../importbase/)
    haciendo referencia a un URI correspondiente a otro documento NCL que contiene el
    base de región que se importará y anidará. Como el URI del documento referido puede
    tener más de una base de región, la base a importar debe ser
    identificado asignando su valor de identificación al atributo baseId del
    [&lt;importBase&gt;](../importbase/) elemento. Al importar un [&lt;regionBase&gt;](../regionbase/), un
    El atributo denominado región se puede especificar dentro de [&lt;importBase&gt;](../importbase/)
    elemento. Cuando está presente, este atributo identifica la identificación de un
    [&lt;region&gt;](../region/) elemento declarado en un elemento [&lt;regionBase&gt;](../regionbase/) del
    documento anfitrión (el documento que realiza la operación de importación). como un
    En consecuencia, todos los elementos secundarios [&lt;region&gt;](../region/) del importado
    [&lt;regionBase&gt;](../regionbase/) se considerarán elementos secundarios [&lt;region&gt;](../region/) de
    la región a la que hace referencia el atributo de región de [&lt;importBase&gt;](../importbase/). Si no
    especificado, los [&lt;region&gt;](../region/) elementos secundarios del archivo importado
    [&lt;regionBase&gt;](../regionbase/) se considerarán hijos directos del anfitrión.
    documento [&lt;regionBase&gt;](../regionbase/) elemento.

### Sintaxis { data-search-exclude }

| Elemento | Atributos | Contenido | Padre |
| --- | --- | --- | --- |
| [&lt;importBase&gt;](../importbase/) | <u>*alias*</u>, <u>*documentURI*</u>, *región*, *baseId* | -- | [&lt;ruleBase&gt;](../rulebase/) o [&lt;transitionBase&gt;](../transitionbase/) o [&lt;regionBase&gt;](../regionbase/) o [&lt;descriptorBase&gt;](../descriptorbase/) o [&lt;connectorBase&gt;](../connectorbase/) |

### Atributos { data-search-exclude }

| Nombre | Valor | Descripción |
| --- | --- | --- |
| *alias* | Puede recibir cualquier valor de cadena que comience con una letra o un guión bajo y que solo contenga letras, dígitos, <"."> y <"_">. | El atributo *alias* especifica un nombre que se utilizará como prefijo cuando se haga referencia a elementos de la base importada.  El valor *alias* debe ser único en un documento y su alcance está restringido al documento que ha definido el atributo alias. |
| *documentURI* | URI. | El atributo *documentURI* es el localizador del documento NCL desde donde se importará la base o el documento. |
| *región* | IDREF. | El atributo *región* se puede utilizar al importar un [&lt;regionBase&gt;](../regionbase/).  Identifica un elemento [&lt;region&gt;](../region/) del documento de importación que anidará (será la región principal) todos los elementos [&lt;region&gt;](../region/) importados. |
| *ID base* | IDREF. | El atributo *baseId* se puede utilizar al importar un [&lt;regionBase&gt;](../regionbase/).  Define el elemento [&lt;regionBase&gt;](../regionbase/) que se importará a través de su valor *id*. |