---
title: "Elemento &lt;media&gt;"
---

### Definição e uso { data-search-exclude }

O elemento [&lt;media&gt;](media.md) define um objeto de mídia contendo: mídia perceptual
conteúdo; conteúdo de código imperativo; conteúdo de código declarativo; Conteúdo UTC; ou
variáveis globais para o aplicativo. O tipo de objeto é definido pelo
*type* ou é inferido pela extensão de arquivo usada no
*src* atributo.

Quatro tipos especiais são definidos:

- O tipo "application/x-ncl-NCL" (ou "application/x-ginga-NCL") é
    aplicado a elementos [&lt;media&gt;](media.md) com conteúdo de código NCL (observe assim que
    uma aplicação NCL pode incorporar outra aplicação NCL).

- O tipo "application/x-ncl-NCLua" (ou "application/x-ginga-NCLua") é
    aplicado a elementos [&lt;media&gt;](media.md) com conteúdo de código imperativo Lua.

- O "application/x-ncl-settings" (ou "application/x-ginga-settings") é
    aplicado a um elemento [&lt;media&gt;](media.md) especial (pode haver apenas um em um
    documento NCL, mas pode ser reutilizado como elemento filho de outro
    [&lt;context&gt;](context.md) elementos) cujas propriedades são variáveis globais
    (propriedades definidas pelo autor do documento ou ambiente reservado
    propriedades gerenciadas pelo sistema) que podem ser manipuladas pelo NCL
    processador de documentos. O objeto de mídia do tipo "application/x-ncl-settings"
    não possui conteúdo para ser exibido. Uma vez que uma aplicação NCL é
    iniciado, as propriedades deste objeto de mídia estão disponíveis para regra
    avaliações definidas por elementos [&lt;rule&gt;](rule.md). Para usar estes
    propriedades nas definições de elemento [&lt;link&gt;](link.md), elas devem ser explicitamente
    declarado.

- O tipo application/x-ncl-time (ou application/x-ginga-time) deve ser
    aplicado a um elemento [&lt;media&gt;](media.md) especial (pode haver apenas um em um
    documento NCL, mas pode ser reutilizado como elemento filho de outro
    [&lt;context&gt;](context.md) elementos), cujo conteúdo é o UTC. Quando for iniciado,
    o conteúdo UTC não é exibido; no entanto, pode ser usado para definir
    âncoras de conteúdo usando elementos [&lt;area&gt;](area.md). Observe que qualquer contínuo
    O elemento [&lt;media&gt;](media.md) sem fonte especificada pode ser usado para definir um
    relógio relativo à hora de início do elemento [&lt;media&gt;](media.md).

#### Reutilização de objetos de mídia { data-search-exclude }

Exceto os elementos [&lt;media&gt;](media.md) de "application/x-ncl-NCL" e
tipos "application/x-ncl-NCLua", um elemento [&lt;media&gt;](media.md) pode se referir a outro
[&lt;media&gt;](media.md) elemento do mesmo documento ou para um [&lt;media&gt;](media.md) importado
elemento. Todos os atributos e elementos filhos definidos pelo elemento referido
são herdados pelo elemento de referência, exceto o *focusIndex*
atributo. Todos os atributos e elementos filhos definidos pelo referente
elemento deve ser ignorado pelo player NCL, exceto os seguintes atributos
e elementos filhos:

- *id* atributo, que deve ser definido.

- *instance* atributo, que pode ser definido, caso contrário tem "new" como
    seu valor de string padrão;

  - Elementos filhos [&lt;area&gt;](area.md) podem ser adicionados. Se o novo adicionado [&lt;area&gt;](area.md)
    elemento tem o mesmo atributo *id* de um já existente
    Elemento [&lt;area&gt;](area.md) (definido no elemento [&lt;media&gt;](media.md) reutilizado), o
    novo adicionado [&lt;area&gt;](area.md) é ignorado pelo player NCL.

  - Elementos filhos [&lt;property&gt;](property.md) podem ser adicionados. Se o novo adicionado
    O elemento [&lt;property&gt;](property.md) tem o mesmo atributo de nome de um elemento já
    elemento [&lt;property&gt;](property.md) existente (definido no [&lt;media&gt;](media.md) reutilizado
    elemento), o novo [&lt;property&gt;](property.md) adicionado é ignorado pelo player NCL.

O referido elemento e o elemento a ele referente serão considerados
o mesmo, quanto à especificação dos dados. Também serão considerados
o mesmo em relação à sua apresentação, se o atributo da instância receber
os valores "instSame" ou "gradSame".

A semântica a seguir deve ser respeitada ao reutilizar um [&lt;media&gt;](media.md)
elemento. Suponha que o conjunto de [&lt;media&gt;](media.md) elementos composto pelos referidos
Elemento [&lt;media&gt;](media.md) e todos os elementos [&lt;media&gt;](media.md) referentes.

- Se algum elemento do subconjunto formado pelo referido elemento [&lt;media&gt;](media.md)
    e todos os outros elementos [&lt;media&gt;](media.md) tendo o atributo de instância igual
    para "instSame" ou "gradSame" está programado para ser apresentado, todos os outros
    elementos neste subconjunto, que não são descendentes de um [&lt;switch&gt;](switch.md)
    elemento, também são assumidos como programados para apresentação, e mais de
    que, quando apresentados, sejam representados pelo mesmo
    instância de apresentação. Elementos descendentes de um elemento [&lt;switch&gt;](switch.md)
    têm o mesmo comportamento se as regras necessárias para apresentá-los forem
    satisfeitos, caso contrário não serão agendados para apresentação.
  - Se o atributo da instância for igual a "instSame", todos os nós agendados
      do subconjunto são imediatamente apresentados através de uma instância única
      (instrução de início aplicada a todos eles) se uma instrução de início for
      aplicado em qualquer um deles.
  - Se o atributo da instância for igual a "gradSame", todos os nós agendados
      do subconjunto são apresentados através de uma instância única, mas agora
      gradativamente, assim que as instruções de início forem aplicadas a eles, chegando
      de um link, etc.
  - À medida que cada elemento [&lt;media&gt;](media.md) inicia sua apresentação, o comum
      instância na apresentação deve notificar os eventos associados
      seus elementos [&lt;area&gt;](area.md) e [&lt;property&gt;](property.md).

- Os elementos [&lt;media&gt;](media.md) no conjunto que possuem valores de atributos de instância
    iguais a "novo" não estão programados para apresentação caso algum outro elemento
    o conjunto está programado para ser apresentado. Quando eles são individualmente
    programado para apresentação, nenhum outro elemento do conjunto é
    afetado. Além disso, novas instâncias de apresentação independentes serão
    criado no início de cada apresentação individual.

### Sintaxe { data-search-exclude }

| Elemento | Atributos | Conteúdo | Pai |
| --- | --- | --- | --- |
| [&lt;media&gt;](media.md) | <u>*id*</u>, *src*, *type*, *refer*, *instance*, *descriptor* | ([&lt;area&gt;](area.md) &#124; [&lt;property&gt;](property.md))* | [&lt;body&gt;](body.md), [&lt;context&gt;](context.md) ou [&lt;switch&gt;](switch.md) |

### Atributos { data-search-exclude }

| Name | Value | Description |
| --- | --- | --- |
| *id* | It may receive any string value that begins with a letter or an underscore and that only contains letters, digits, <".">, and <"_">. | The *id* attribute uniquely identifies the element within a document. |
| *src* | <p>The following are valid values:</p><ul><li class="level1"><div class="li"><"<nowiki>file:/*file_path/#fragment_identifier</nowiki>"> -- for local files,</div></li><li class="level1"><div class="li"><"<nowiki>http:*server_identifier/file_path/#fragment_identifier</nowiki>"> -- for remote files downloaded using the HTTP protocol,</div></li><li class="level1"><div class="li"><"<nowiki>https://server_identifier/file_path/#fragment_identifier</nowiki>"> -- for remote files downloaded using the HTTPS protocol,</div></li><li class="level1"><div class="li"><"<nowiki>rtsp://server_identifier/file_path/#fragment_identifier</nowiki>"> -- for streams downloaded using the RTSP protocol,</div></li><li class="level1"><div class="li"><"<nowiki>rtp://server_identifier/file_path/#fragment_identifier</nowiki>"> -- for streams downloaded using the RTP protocol,</div></li><li class="level1"><div class="li"><"<nowiki>ncl-mirror://media_element_identifier</nowiki>"> -- for a content flow identical to the one in presentation by another [&lt;media&gt;](media.md) element,</div></li><li class="level1"><div class="li"><"<nowiki>sbtvd-ts:</nowiki>"> or <"<nowiki>isdb-ts:</nowiki>"> or <"<nowiki>ts://program_number.component_tag</nowiki>"> -- for elementary streams received from the transport stream.</div></li></ul><p>For *src* attribute whose value identifies the <"sbtvd-ts">, <"isdb-ts">, or <"ts"> scheme, the "program_number.component_tag", can be substituted by the following reserved words:</p><ul><li class="level1"><div class="li">"video" -- corresponding to the primary video ES being presented on the video plan,</div></li><li class="level1"><div class="li">"audio" -- corresponding to the primary audio ES,</div></li><li class="level1"><div class="li">"text" -- corresponding to the primary text ES,</div></li><li class="level1"><div class="li">"video(i)" -- corresponding to the *i*-th smaller video ES "component_tag" listed in the PMT of the tuned services,</div></li><li class="level1"><div class="li">"audio(i)" -- corresponding to the *i*-th smaller audio ES "component_tag" listed in the PMT of the tuned services, or</div></li><li class="level1"><div class="li">"text(i)" -- corresponding to the *i*-th smaller text ES "component_tag" listed in the PMT of the tuned services.</div></li></ul> | The *src* attribute is the locator for the media object content. |
| *type* | <p>String.</p><p>It shall follow MIME Media Types format.  Four special types are defined: "application/x-ncl-NCL" (or "application/x-ginga-NCL"), "application/x-ncl-NCLua" (or "application/x-ginga-NCLua"), "application/x-ncl-settings" (or "application/x-ginga-settings"), and "application/x-ncl-time" (or "application/x-ginga-time").</p> | The *type* attribute shall follow MIME Media Types format (or, more simply, mimetypes). A mimetype is a string that defines the class of media (audio, video, image, text, application) and a media encoding type (such as jpeg, mpeg, etc.). Mimetypes may be registered or informal. Registered mimetypes are controlled by the IANA. Informal mimetypes are not registered with IANA, but are defined by common agreement; they usually have an "x-" before the media type name. |
| *refer* | IDREF or the string "alias#id" where "id" is an IDREF value. | <p>The *refer* attribute refers to a [&lt;media&gt;](media.md) element *id* that will be reused. An element that refers to another element cannot be reused; that is, its *id* cannot be the value of any *refer* attribute. The referred element must be a [&lt;media&gt;](media.md) element.</p><p>The referred element and the element that refers to it is considered the same regarding their data specification.</p><p>If the referred media object is defined within an imported document D, the refer attribute value must have the format "alias#id", where "alias" is the value of the alias attribute associated with the imported D document.</p> |
| *instance* | "new", "instSame", or "gradSame". | Specifies the reuse type.  The "new" value defines a new presentation instance but inheriting the specification of the referred [&lt;media&gt;](media.md) element.  The "instSame" value defines a same presentation instance that is immediately started as soon as the referred [&lt;media&gt;](media.md) element or any other [&lt;media&gt;](media.md) elements referring to it with instance attribute equal to "instSame" is started, or if a start instruction is applied on it.  The "gradSame" value defines a same presentation instance that is started as soon an start instruction is applied on it, coming from a link, etc. |
| *descriptor* | IDREF. | The *descriptor* attribute refers to a [&lt;descriptor&gt;](descriptor.md) element. |
