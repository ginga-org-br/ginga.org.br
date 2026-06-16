---
title: "Elemento &lt;attributeAssessment&gt;"
---

### Definition and Usage { data-search-exclude }

O elemento [&lt;attributeAssessment&gt;](attributeassessment.md) é usado para definir uma variável a ser
avaliado, em elementos [&lt;assessmentStatement&gt;](assessmentstatement.md), em relação a outra variável
valores ou um valor absoluto.

A variável pode ser uma propriedade especificada em um elemento [&lt;property&gt;](property.md) ou
pode ser um atributo de evento (apresentação, seleção ou atribuição):
ocorrências, repetição ou estado (que possui os seguintes valores:
"ocorrendo", "pausado" ou "adormecido").

O elemento [&lt;attributeAssessment&gt;](attributeassessment.md) possui um atributo *role*, que
deve ser exclusivo no conjunto de funções do conector.  Este atributo é o conector
ponto de interface, que está associado às interfaces do nó ([&lt;port&gt;](port.md),
[&lt;area&gt;](area.md), [&lt;property&gt;](property.md) ou [&lt;switchPort&gt;](switchport.md) elementos) por [&lt;link&gt;](link.md)
que se refere ao conector.

A variável definida pelo elemento depende do seu *eventType*
atributo e seu atributo *attributeType*:

  * Se o valor eventType for "presentation", o *attributeType*
    o atributo pode especificar como variável: o evento de "ocorrências" ou "repetição"
    atributos ou o estado do evento "estado".

  * Se o eventType for "attribution" o *attributeType* pode ter o
    valores: "nodeProperty" (especificando uma propriedade do nó), "ocorrências",
    "repetição" ou "estado".

  * Se o valor eventType for "selection", o [&lt;attributeAssessment&gt;](attributeassessment.md)pode
    definir também para qual aparelho de seleção (por exemplo, teclas do teclado ou
    teclas de controle remoto) a que se refere, através de seu atributo *key*.  O
    *attributeType* attribute may have the values:  "occurrences"
    (padrão) ou "estado".

Um valor de deslocamento pode ser adicionado a um [&lt;attributeAssessment&gt;](attributeassessment.md) antes de seu
comparação em um elemento [&lt;assessmentStatement&gt;](assessmentstatement.md).  Por exemplo, um deslocamento
pode ser adicionado a um *attributeassessment* para especificar: "a tela
posição vertical mais 50 pixels".

### Sintaxe { data-search-exclude }

| Elemento | Atributos | Conteúdo | Pai |
| --- | --- | --- | --- |
| [&lt;attributeAssessment&gt;](attributeassessment.md) | <u>*role*</u>, <u>*eventType*</u>, *key*, *attributeType*, *offset* | -- | [&lt;assessmentStatement&gt;](assessmentstatement.md) |

### Atributos { data-search-exclude }

| Nome | Valor | Descrição |
| --- | --- | --- |
| *papel* | Corda. | O atributo *role* define um ponto de interface do conector, que está associado às interfaces dos nós por um link que se refere ao conector.  O valor *role* deve ser exclusivo dentro do conjunto de funções do conector. |
| *tipodeevento* | "apresentação", "seleção" ou "atribuição". | O atributo *eventType* identifica o tipo de evento para a ação ou condição. |
| *chave* | Pelo menos os seguintes valores (sensível a maiúsculas e minúsculas) devem ser aceitos para o atributo chave: "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "*", "#", "MENU", "INFO", "GUIDE", "CURSOR_DOWN", "CURSOR_LEFT", "CURSOR_RIGHT", "CURSOR_UP", "CHANNEL_DOWN", "CHANNEL_UP", "VOLUME_DOWN", "VOLUME_UP", "ENTER", "RED", "GREEN", "YELLOW", "BLUE", "BACK", "EXIT", "POWER", "REWIND", "STOP", "EJECT", "PLAY", "RECORD" e "PAUSE". | O atributo *key* identifica a chave de seleção usada para a seleção. |
| *atributoType* | <p>"nodeProperty" (somente no caso de *eventType*="atribuição"), "ocorrências", "repetição" ou "estado".</p><p>Os valores padrão são: "nodeProperty" se *eventType*="atribuição" ou "ocorrências" se *eventType*="seleção".</p> | O atributo *attributeType* identifica a variável a ser avaliada em um elemento [&lt;assessmentStatement&gt;](assessmentstatement.md). |
| *deslocamento* | Corda. | O atributo *offset* especifica um valor a ser adicionado à variável selecionada antes de sua avaliação em um elemento [&lt;assessmentStatement&gt;](assessmentstatement.md). |