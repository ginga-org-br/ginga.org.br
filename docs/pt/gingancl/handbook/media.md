---
title: "Elemento &lt;media&gt;"
---

# &lt;media&gt;

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

| Nome | Valor | Descrição |
| --- | --- | --- |
| *id* | Pode receber qualquer valor de string que comece com uma letra ou um sublinhado e que contenha apenas letras, dígitos, <"."> e <"_">. | O atributo *id* identifica exclusivamente o elemento dentro de um documento. |
| *src* | <p>Os seguintes valores são válidos:</p><ul><li class="level1"><div class="li"><code>file:///file_path/#fragment_identifier</code> -- para arquivos locais,</div></li><li class="level1"><div class="li"><code>http://server_identifier/file_path/#fragment_identifier</code> -- para arquivos remotos baixados usando o protocolo HTTP,</div></li><li class="level1"><div class="li"><code>https://server_identifier/file_path/#fragment_identifier</code> -- para arquivos remotos baixados usando o protocolo HTTPS,</div></li><li class="level1"><div class="li"><code>rtsp://server_identifier/file_path/#fragment_identifier</code> -- para fluxos baixados usando o protocolo RTSP,</div></li><li class="level1"><div class="li"><code>rtp://server_identifier/file_path/#fragment_identifier</code> -- para fluxos baixados usando o protocolo RTP,</div></li><li class="level1"><div class="li"><code>ncl-mirror://media_element_identifier</code> -- para um fluxo de conteúdo idêntico ao que está em apresentação por outro elemento [&lt;media&gt;](media.md),</div></li><li class="level1"><div class="li"><code>sbtvd-ts:</code> ou <code>isdb-ts:</code> ou <code>ts://program_number.component_tag</code> -- para fluxos elementares recebidos do fluxo de transporte.</div></li></ul><p>Para o atributo *src* cujo valor identifica o esquema "sbtvd-ts", "isdb-ts" ou "ts", o "program_number.component_tag" pode ser substituído pelas seguintes palavras reservadas:</p><ul><li class="level1"><div class="li">"video" -- correspondente ao ES de vídeo primário sendo apresentado no plano de vídeo,</div></li><li class="level1"><div class="li">"audio" -- correspondente ao ES de áudio primário,</div></li><li class="level1"><div class="li">"text" -- correspondente ao ES de texto primário,</div></li><li class="level1"><div class="li">"video(i)" -- correspondente ao *i*-ésimo menor "component_tag" de ES de vídeo listado na PMT dos serviços sintonizados,</div></li><li class="level1"><div class="li">"audio(i)" -- correspondente ao *i*-ésimo menor "component_tag" de ES de áudio listado na PMT dos serviços sintonizados, ou</div></li><li class="level1"><div class="li">"text(i)" -- correspondente ao *i*-ésimo menor "component_tag" de ES de texto listado na PMT dos serviços sintonizados.</div></li></ul> | O atributo *src* é o localizador para o conteúdo do objeto de mídia. |
| *type* | <p>String.</p><p>Deve seguir o formato MIME Media Types. Quatro tipos especiais são definidos: "application/x-ncl-NCL" (ou "application/x-ginga-NCL"), "application/x-ncl-NCLua" (ou "application/x-ginga-NCLua"), "application/x-ncl-settings" (ou "application/x-ginga-settings") e "application/x-ncl-time" (ou "application/x-ginga-time").</p> | O atributo *type* deve seguir o formato MIME Media Types (ou, mais simplesmente, mimetypes). Um mimetype é uma string que define a classe de mídia (áudio, vídeo, imagem, texto, aplicação) e um tipo de codificação de mídia (como jpeg, mpeg, etc.). Os mimetypes podem ser registrados ou informais. Os mimetypes registrados são controlados pela IANA. Os mimetypes informais não são registrados na IANA, mas são definidos por acordo comum; geralmente têm um "x-" antes do nome do tipo de mídia. |
| *refer* | IDREF ou a string "alias#id", onde "id" é um valor IDREF. | <p>O atributo *refer* faz referência a um *id* de elemento [&lt;media&gt;](media.md) que será reutilizado. Um elemento que faz referência a outro elemento não pode ser reutilizado; ou seja, seu *id* não pode ser o valor de nenhum atributo *refer*. O elemento referenciado deve ser um elemento [&lt;media&gt;](media.md).</p><p>O elemento referenciado e o elemento que faz referência a ele são considerados o mesmo em relação à sua especificação de dados.</p><p>Se o objeto de mídia referenciado estiver definido dentro de um documento importado D, o valor do atributo *refer* deverá ter o formato "alias#id", onde "alias" é o valor do atributo *alias* associado ao documento D importado.</p> |
| *instance* | "new", "instSame" ou "gradSame". | Especifica o tipo de reutilização. O valor "new" define uma nova instância de apresentação, mas herdando a especificação do elemento [&lt;media&gt;](media.md) referenciado. O valor "instSame" define uma mesma instância de apresentação que é iniciada imediatamente assim que o elemento [&lt;media&gt;](media.md) referenciado ou quaisquer outros elementos [&lt;media&gt;](media.md) que façam referência a ele com o atributo *instance* igual a "instSame" forem iniciados, ou se uma instrução de início for aplicada a ele. O valor "gradSame" define uma mesma instância de apresentação que é iniciada assim que uma instrução de início é aplicada a ela, vinda de um elo, etc. |
| *descriptor* | IDREF. | O atributo *descriptor* faz referência a um elemento [&lt;descriptor&gt;](descriptor.md). |
