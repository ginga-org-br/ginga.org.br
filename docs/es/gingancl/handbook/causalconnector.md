---
title: "Elemento &lt;causalConnector&gt;"
---

### Definición y uso { data-search-exclude }

El elemento [&lt;causalConnector&gt;](causalconnector.md) representa una relación causal que puede ser
Se utiliza para crear relaciones (elementos [&lt;link&gt;](link.md)) en documentos NCL.  en
En una relación causal, se debe cumplir una condición para desencadenar una
acción.

Un [&lt;causalConnector&gt;](causalconnector.md) especifica una relación independientemente de
relaciones, es decir, no especifica qué nodos (representados por
[&lt;media&gt;](media.md), [&lt;context&gt;](context.md), [&lt;body&gt;](body.md) y [&lt;switch&gt;](switch.md) elementos)
interactúan a través de la relación.  Un elemento [&lt;link&gt;](link.md), a su vez,
representa una relación del tipo definido por su conector referido,
interconectando diferentes nodos.  Enlaces que representan el mismo tipo de
relación, pero interconectando diferentes nodos, se puede reutilizar el mismo conector,
reutilizando todas sus especificaciones anteriores.

Un [&lt;causalConnector&gt;](causalconnector.md) define, a través de sus elementos secundarios, un conjunto de
puntos de interfaz, llamados roles.  Un elemento [&lt;link&gt;](link.md) hace referencia a un
[&lt;causalConnector&gt;](causalconnector.md) y define un conjunto de enlaces ([&lt;bind&gt;](bind.md) hijo
elementos del elemento [&lt;link&gt;](link.md)), que asocian cada punto final del enlace
(interfaz de nodo) a un rol del conector referido.

Las relaciones en NCL se basan en eventos.  Un evento NCL es un suceso en el tiempo
que puede ser instantáneo o tener una duración mensurable.  Cada evento define
una máquina de estados mantenida por el reproductor NCL (ver Figura 1).
Además, cada evento tiene un atributo asociado, llamado
*ocurrencias*, que cuenta cuántas veces el evento transita desde
ocurriendo al estado de sueño durante la presentación de un documento.  Eventos de
Los tipos de presentación y atribución también tienen un atributo llamado
*repeticiones*, que cuenta cuantas veces se realizará el evento
reiniciado automáticamente (pasa del estado inactivo al estado en curso) por el
Jugador de la NCL.  Este atributo puede contener el valor "indefinido", lo que lleva a
un bucle sin fin de ocurrencia del evento hasta alguna interrupción externa.

![Figure 1: Event state machine.](/assets/state-machine.png)

El perfil NCL 3.0 EDTV define los siguientes tipos de eventos:

- evento de presentación: definido por la presentación de un subconjunto de
    unidades de información del contenido de un objeto multimedia.  Los eventos de presentación son
    especificado en NCL en [&lt;area&gt;](area.md) elementos, o en los propios nodos de medios
    (en todos sus anclajes de contenido).  Los eventos de presentación también pueden ser
    definido en nodos compuestos (representados por [&lt;body&gt;](body.md), [&lt;context&gt;](context.md),
    o [&lt;switch&gt;](switch.md) elementos), que representan la presentación de información
    unidades de cualquier nodo dentro del nodo compuesto);

- evento de selección: definido por la selección de un subconjunto de información
    unidades del contenido de un objeto multimedia que se presenta.  Los eventos de selección son
    especificado en NCL en [&lt;area&gt;](area.md) elementos, o en los propios nodos de medios
    (en todos sus anclajes de contenido);

- evento de atribución: definido por la atribución de un valor a una propiedad
    de un nodo (representado por [&lt;media&gt;](media.md), [&lt;body&gt;](body.md) o [&lt;context&gt;](context.md)
    elemento), que debe declararse en un elemento secundario [&lt;property&gt;](property.md) de
    el nodo; y

  - evento de composición: definido por la presentación de la estructura de un
    nodo compuesto (representado por [&lt;body&gt;](body.md), [&lt;context&gt;](context.md) o
    [&lt;switch&gt;](switch.md) elemento).  Los eventos de composición se utilizan para presentar la
    mapa compuesto (organización compuesta).  Esta funcionalidad es opcional.
    en perfiles EDTV/BDTV.

### Sintaxis { data-search-exclude }

| Elemento | Atributos | Contenido | Padre |  |  |
| --- | --- | --- | --- | --- | --- |
| [&lt;causalConnector&gt;](causalconnector.md) | <u>*id*</u> | ([&lt;connectorParam&gt;](connectorparam.md)*, ([&lt;simpleCondition&gt;](simplecondition.md) | [&lt;compoundCondition&gt;](compoundcondition.md)), ([&lt;simpleAction&gt;](simpleaction.md) | [&lt;compoundAction&gt;](compoundaction.md))) | [&lt;connectorBase&gt;](connectorbase.md) |

### Atributos { data-search-exclude }

| Nombre | Valor | Descripción |
| --- | --- | --- |
| *identificación* | Puede recibir cualquier valor de cadena que comience con una letra o un guión bajo y que solo contenga letras, dígitos, <"."> y <"_">. | El atributo *id* identifica de forma única el elemento dentro de un documento. |
