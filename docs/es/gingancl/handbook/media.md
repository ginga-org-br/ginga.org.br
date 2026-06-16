---
title: "Elemento &lt;media&gt;"
---

# &lt;media&gt;

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

| Nombre | Valor | Descripción |
| --- | --- | --- |
| *id* | Puede recibir cualquier valor de cadena que comience con una letra o un guión bajo y que solo contenga letras, dígitos, <"."> y <"_">. | El atributo *id* identifica de forma única al elemento dentro de un documento. |
| *src* | <p>Los siguientes son valores válidos:</p><ul><li class="level1"><div class="li"><code>file:///file_path/#fragment_identifier</code> -- para archivos locales,</div></li><li class="level1"><div class="li"><code>http://server_identifier/file_path/#fragment_identifier</code> -- para archivos remotos descargados mediante el protocolo HTTP,</div></li><li class="level1"><div class="li"><code>https://server_identifier/file_path/#fragment_identifier</code> -- para archivos remotos descargados mediante el protocolo HTTPS,</div></li><li class="level1"><div class="li"><code>rtsp://server_identifier/file_path/#fragment_identifier</code> -- para flujos descargados mediante el protocolo RTSP,</div></li><li class="level1"><div class="li"><code>rtp://server_identifier/file_path/#fragment_identifier</code> -- para flujos descargados mediante el protocolo RTP,</div></li><li class="level1"><div class="li"><code>ncl-mirror://media_element_identifier</code> -- para un flujo de contenido idéntico al que está en presentación por otro elemento [&lt;media&gt;](media.md),</div></li><li class="level1"><div class="li"><code>sbtvd-ts:</code> o <code>isdb-ts:</code> o <code>ts://program_number.component_tag</code> -- para flujos elementales recibidos del flujo de transporte.</div></li></ul><p>Para el atributo *src* cuyo valor identifica el esquema "sbtvd-ts", "isdb-ts" o "ts", el "program_number.component_tag" puede sustituirse por las siguientes palabras reservadas:</p><ul><li class="level1"><div class="li">"video" -- correspondiente al ES de video primario presentado en el plano de video,</div></li><li class="level1"><div class="li">"audio" -- correspondiente al ES de audio primario,</div></li><li class="level1"><div class="li">"text" -- correspondiente al ES de texto primario,</div></li><li class="level1"><div class="li">"video(i)" -- correspondiente al *i*-ésimo menor "component_tag" de ES de video listado en la PMT de los servicios sintonizados,</div></li><li class="level1"><div class="li">"audio(i)" -- correspondiente al *i*-ésimo menor "component_tag" de ES de audio listado en la PMT de los servicios sintonizados, o</div></li><li class="level1"><div class="li">"text(i)" -- correspondiente al *i*-ésimo menor "component_tag" de ES de texto listado en la PMT de los servicios sintonizados.</div></li></ul> | El atributo *src* es el localizador del contenido del objeto multimedia. |
| *type* | <p>Cadena.</p><p>Debe seguir el formato MIME Media Types. Se definen cuatro tipos especiales: "application/x-ncl-NCL" (o "application/x-ginga-NCL"), "application/x-ncl-NCLua" (o "application/x-ginga-NCLua"), "application/x-ncl-settings" (o "application/x-ginga-settings") y "application/x-ncl-time" (o "application/x-ginga-time").</p> | El atributo *type* debe seguir el formato MIME Media Types (o, más simplemente, mimetypes). Un mimetype es una cadena que define la clase de medio (audio, video, imagen, texto, aplicación) y un tipo de codificación de medio (como jpeg, mpeg, etc.). Los mimetypes pueden ser registrados o informales. Los mimetypes registrados están controlados por la IANA. Los mimetypes informales no están registrados en la IANA, sino que se definen por acuerdo común; suelen llevar un prefijo "x-" antes del nombre del tipo de medio. |
| *refer* | IDREF o la cadena "alias#id", donde "id" es un valor IDREF. | <p>El atributo *refer* hace referencia al *id* de un elemento [&lt;media&gt;](media.md) que será reutilizado. Un elemento que hace referencia a otro elemento no puede ser reutilizado; es decir, su *id* no puede ser el valor de ningún atributo *refer*. El elemento referenciado debe ser un elemento [&lt;media&gt;](media.md).</p><p>El elemento referenciado y el elemento que hace referencia a él se consideran el mismo en cuanto a su especificación de datos.</p><p>Si el objeto multimedia referenciado está definido dentro de un documento importado D, el valor del atributo *refer* debe tener el formato "alias#id", donde "alias" es el valor del atributo *alias* asociado con el documento D importado.</p> |
| *instance* | "new", "instSame" o "gradSame". | Especifica el tipo de reutilización. El valor "new" define una nueva instancia de presentación pero heredando la especificación del elemento [&lt;media&gt;](media.md) referenciado. El valor "instSame" define una misma instancia de presentación que se inicia inmediatamente tan pronto como se inicia el elemento [&lt;media&gt;](media.md) referenciado o cualquier otro elemento [&lt;media&gt;](media.md) que haga referencia a él con el atributo *instance* igual a "instSame", o si se le aplica una instrucción de inicio. El valor "gradSame" define una misma instancia de presentación que se inicia tan pronto como se le aplica una instrucción de inicio, proveniente de un enlace, etc. |
| *descriptor* | IDREF. | El atributo *descriptor* hace referencia a un elemento [&lt;descriptor&gt;](descriptor.md). |
