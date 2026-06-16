---
title: "Elemento &lt;media&gt;"
---

### Definición y uso { data-search-exclude }

El elemento [&lt;media&gt;](media.md) define un objeto multimedia que contiene: medios perceptivos
contenido; contenido del código imperativo; contenido del código declarativo; contenido UTC; o
variables globales para la aplicación. El tipo de objeto está definido por el
*tipo* atributo o se infiere por la extensión de archivo utilizada en el
*src* atributo.

Se definen cuatro tipos especiales:

- El tipo "application/x-ncl-NCL" (o "application/x-ginga-NCL") es
    aplicado a [&lt;media&gt;](media.md) elementos con contenido de código NCL (tenga en cuenta que
    una aplicación NCL puede incorporar otra aplicación NCL).

- El tipo "application/x-ncl-NCLua" (o "application/x-ginga-NCLua") es
    aplicado a [&lt;media&gt;](media.md) elementos con contenido de código imperativo Lua.

- La "aplicación/x-ncl-settings" (o "aplicación/x-ginga-settings") es
    aplicado a un elemento [&lt;media&gt;](media.md) especial (puede haber solo uno en un
    documento NCL, pero puede reutilizarse como elemento secundario de otros
    [&lt;context&gt;](context.md) elementos) cuyas propiedades son variables globales
    (propiedades definidas por el autor del documento o entorno reservado
    propiedades gestionadas por el sistema) que pueden ser manipuladas por la NCL
    procesador de documentos. El objeto multimedia del tipo "application/x-ncl-settings"
    no tiene contenido para ser exhibido. Una vez que se presenta una solicitud NCL
    iniciado, las propiedades de este objeto multimedia están disponibles para la regla
    evaluaciones definidas por [&lt;rule&gt;](rule.md) elementos. Para poder utilizar estos
    propiedades en [&lt;link&gt;](link.md) definiciones de elementos, deben ser explícitamente
    declarado.

- El tipo application/x-ncl-time (o application/x-ginga-time) será
    aplicado a un elemento [&lt;media&gt;](media.md) especial (puede haber solo uno en un
    documento NCL, pero puede reutilizarse como elemento secundario de otros
    [&lt;context&gt;](context.md) elementos), cuyo contenido es el UTC. Cuando se inicia,
    el contenido UTC no se exhibe; sin embargo, se puede utilizar para definir
    anclajes de contenido mediante el uso de elementos [&lt;area&gt;](area.md). Tenga en cuenta que cualquier continuo
    El elemento [&lt;media&gt;](media.md) sin fuente especificada se puede utilizar para definir un
    reloj relativo a la hora de inicio del elemento [&lt;media&gt;](media.md).

#### Reutilización de objetos multimedia { data-search-exclude }

Excepto [&lt;media&gt;](media.md) elementos de "application/x-ncl-NCL" y
Tipos "application/x-ncl-NCLua", un elemento [&lt;media&gt;](media.md) puede hacer referencia a otro
[&lt;media&gt;](media.md) elemento del mismo documento o a un [&lt;media&gt;](media.md) importado
elemento. Todos los atributos y elementos secundarios definidos por el elemento referido
son heredados por el elemento de referencia, excepto *focusIndex*
atributo. Todos los atributos y elementos secundarios definidos por el referente
El jugador NCL debe ignorar el elemento, excepto los siguientes atributos.
y elementos secundarios:

- Atributo *id*, que será definido.

- Atributo *instancia*, que puede definirse; de lo contrario, tiene "nuevo" como
    su valor de cadena predeterminado;

  - Se pueden agregar elementos secundarios [&lt;area&gt;](area.md). Si el nuevo agregado [&lt;area&gt;](area.md)
    El elemento tiene el mismo atributo *id* de un elemento ya existente.
    elemento [&lt;area&gt;](area.md) (definido en el elemento [&lt;media&gt;](media.md) reutilizado), el
    El reproductor NCL ignora el nuevo [&lt;area&gt;](area.md) agregado.

  - Se pueden agregar elementos secundarios [&lt;property&gt;](property.md). Si el nuevo agregado
    El elemento [&lt;property&gt;](property.md) tiene el mismo atributo de nombre que un elemento ya
    elemento [&lt;property&gt;](property.md) existente (definido en el [&lt;media&gt;](media.md) reutilizado
    elemento), el reproductor NCL ignora el nuevo [&lt;property&gt;](property.md) agregado.

El elemento referido y el elemento que se refiere a él se considerarán
lo mismo, en cuanto a su especificación de datos. También serán considerados
lo mismo en cuanto a su presentación, si el atributo de instancia recibe
los valores "instSame" o "gradSame".

Se debe respetar la siguiente semántica al reutilizar un [&lt;media&gt;](media.md)
elemento. Supongamos el conjunto de [&lt;media&gt;](media.md) elementos compuestos por el referido
[&lt;media&gt;](media.md) elemento y todos los elementos [&lt;media&gt;](media.md) de referencia.

- Si algún elemento del subconjunto formado por el referido elemento [&lt;media&gt;](media.md)
    y todos los demás elementos [&lt;media&gt;](media.md) que tengan el atributo de instancia igual
    a "instSame" o "gradSame" está programado para ser presentado, todos los demás
    elementos de este subconjunto, que no son descendientes de un [&lt;switch&gt;](switch.md)
    elemento, también se asumen como programados para su presentación, y más de
    que, al ser presentados, estén representados por el mismo
    instancia de presentación. Elementos descendientes de un elemento [&lt;switch&gt;](switch.md)
    tienen el mismo comportamiento si las reglas necesarias para presentarlos son
    satisfechos, de lo contrario no están programados para su presentación.
  - Si el atributo de instancia es igual a "instSame", todos los nodos programados
      del subconjunto se presentan inmediatamente a través de una instancia única
      (Instrucción de inicio aplicada en todos ellos) si una instrucción de inicio es
      aplicado en cualquiera de ellos.
  - Si el atributo de instancia es igual a "gradSame", todos los nodos programados
      del subconjunto se presentan a través de una instancia única, pero ahora
      gradualmente, tan pronto como se les apliquen las instrucciones de inicio,
      desde un enlace, etc.
  - A medida que cada elemento [&lt;media&gt;](media.md) comienza su presentación, el común
      instancia en la presentación debe notificar los eventos asociados con
      sus elementos [&lt;area&gt;](area.md) y [&lt;property&gt;](property.md).

- Los [&lt;media&gt;](media.md) elementos del conjunto que tienen valores de atributos de instancia
    iguales a "nuevo" no están programados para su presentación si cualquier otro elemento en
    El conjunto está programado para ser presentado. Cuando son individualmente
    programado para su presentación, ningún otro elemento del conjunto está
    afectado. Además, se abrirán nuevas instancias de presentación independiente.
    creado en cada presentación individual que comienza.

### Sintaxis { data-search-exclude }

| Elemento | Atributos | Contenido | Padre |
| --- | --- | --- | --- |
| [&lt;media&gt;](media.md) | <u>*id*</u>, *src*, *tipo*, *referencia*, *instancia*, *descriptor* | ([&lt;area&gt;](area.md) &#124; [&lt;property&gt;](property.md))* | [&lt;body&gt;](body.md), [&lt;context&gt;](context.md) o [&lt;switch&gt;](switch.md) |

### Atributos { data-search-exclude }

| Name | Value | Description |
| --- | --- | --- |
| *id* | It may receive any string value that begins with a letter or an underscore and that only contains letters, digits, <".">, and <"_">. | The *id* attribute uniquely identifies the element within a document. |
| *src* | <p>The following are valid values:</p><ul><li class="level1"><div class="li"><"<nowiki>file:/*file_path/#fragment_identifier</nowiki>"> -- for local files,</div></li><li class="level1"><div class="li"><"<nowiki>http:*server_identifier/file_path/#fragment_identifier</nowiki>"> -- for remote files downloaded using the HTTP protocol,</div></li><li class="level1"><div class="li"><"<nowiki>https://server_identifier/file_path/#fragment_identifier</nowiki>"> -- for remote files downloaded using the HTTPS protocol,</div></li><li class="level1"><div class="li"><"<nowiki>rtsp://server_identifier/file_path/#fragment_identifier</nowiki>"> -- for streams downloaded using the RTSP protocol,</div></li><li class="level1"><div class="li"><"<nowiki>rtp://server_identifier/file_path/#fragment_identifier</nowiki>"> -- for streams downloaded using the RTP protocol,</div></li><li class="level1"><div class="li"><"<nowiki>ncl-mirror://media_element_identifier</nowiki>"> -- for a content flow identical to the one in presentation by another [&lt;media&gt;](media.md) element,</div></li><li class="level1"><div class="li"><"<nowiki>sbtvd-ts:</nowiki>"> or <"<nowiki>isdb-ts:</nowiki>"> or <"<nowiki>ts://program_number.component_tag</nowiki>"> -- for elementary streams received from the transport stream.</div></li></ul><p>For *src* attribute whose value identifies the <"sbtvd-ts">, <"isdb-ts">, or <"ts"> scheme, the "program_number.component_tag", can be substituted by the following reserved words:</p><ul><li class="level1"><div class="li">"video" -- corresponding to the primary video ES being presented on the video plan,</div></li><li class="level1"><div class="li">"audio" -- corresponding to the primary audio ES,</div></li><li class="level1"><div class="li">"text" -- corresponding to the primary text ES,</div></li><li class="level1"><div class="li">"video(i)" -- corresponding to the *i*-th smaller video ES "component_tag" listed in the PMT of the tuned services,</div></li><li class="level1"><div class="li">"audio(i)" -- corresponding to the *i*-th smaller audio ES "component_tag" listed in the PMT of the tuned services, or</div></li><li class="level1"><div class="li">"text(i)" -- corresponding to the *i*-th smaller text ES "component_tag" listed in the PMT of the tuned services.</div></li></ul> | The *src* attribute is the locator for the media object content. |
| *type* | <p>String.</p><p>It shall follow MIME Media Types format.  Four special types are defined: "application/x-ncl-NCL" (or "application/x-ginga-NCL"), "application/x-ncl-NCLua" (or "application/x-ginga-NCLua"), "application/x-ncl-settings" (or "application/x-ginga-settings"), and "application/x-ncl-time" (or "application/x-ginga-time").</p> | The *type* attribute shall follow MIME Media Types format (or, more simply, mimetypes). A mimetype is a string that defines the class of media (audio, video, image, text, application) and a media encoding type (such as jpeg, mpeg, etc.). Mimetypes may be registered or informal. Registered mimetypes are controlled by the IANA. Informal mimetypes are not registered with IANA, but are defined by common agreement; they usually have an "x-" before the media type name. |
| *refer* | IDREF or the string "alias#id" where "id" is an IDREF value. | <p>The *refer* attribute refers to a [&lt;media&gt;](media.md) element *id* that will be reused. An element that refers to another element cannot be reused; that is, its *id* cannot be the value of any *refer* attribute. The referred element must be a [&lt;media&gt;](media.md) element.</p><p>The referred element and the element that refers to it is considered the same regarding their data specification.</p><p>If the referred media object is defined within an imported document D, the refer attribute value must have the format "alias#id", where "alias" is the value of the alias attribute associated with the imported D document.</p> |
| *instance* | "new", "instSame", or "gradSame". | Specifies the reuse type.  The "new" value defines a new presentation instance but inheriting the specification of the referred [&lt;media&gt;](media.md) element.  The "instSame" value defines a same presentation instance that is immediately started as soon as the referred [&lt;media&gt;](media.md) element or any other [&lt;media&gt;](media.md) elements referring to it with instance attribute equal to "instSame" is started, or if a start instruction is applied on it.  The "gradSame" value defines a same presentation instance that is started as soon an start instruction is applied on it, coming from a link, etc. |
| *descriptor* | IDREF. | The *descriptor* attribute refers to a [&lt;descriptor&gt;](descriptor.md) element. |
