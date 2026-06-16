---
title: "Elemento &lt;regionBase&gt;"
---

### Definição e uso { data-search-exclude }

O elemento [&lt;regionBase&gt;](regionbase.md) agrupa um conjunto de elementos [&lt;region&gt;](region.md), cada um
dos quais podem conter outro conjunto de elementos [&lt;region&gt;](region.md) aninhados, e assim
ligado, recursivamente.

Cada elemento [&lt;regionBase&gt;](regionbase.md) está associado a uma classe de dispositivos onde
ocorrerá a apresentação.  Para identificar a associação, o
O elemento [&lt;regionBase&gt;](regionbase.md) define o atributo *device*.  Quando o
atributo não for especificado, a apresentação ocorre no mesmo dispositivo
que executa o reprodutor NCL.

Existem dois tipos diferentes de classes de dispositivos: ativo e passivo.  Em um
classe ativa, um dispositivo é capaz de executar alguns reprodutores de mídia para [&lt;media&gt;](media.md)
apresentações de elementos.  Em uma classe passiva, não é necessário um dispositivo para executar
reprodutores de mídia, apenas para exibir um mapa de bits ou uma sequência de amostras de áudio
recebido de outro dispositivo.

A propriedade "deviceClass" de um elemento [&lt;media&gt;](media.md) é inicializada com o
*valor do dispositivo*, se o elemento [&lt;media&gt;](media.md) se referir indiretamente a um
Elemento [&lt;region&gt;](region.md) dentro de um [&lt;regionBase&gt;](regionbase.md), usando um
[&lt;descriptor&gt;](descriptor.md) elemento.

A classe escolhida também define as variáveis de ambiente globais (propriedades
do objeto de configurações ---[&lt;media&gt;](media.md) elemento de
Tipo "aplicativo/x-ncl-settings"): "system.screenSize(i)",
"system.screenGraphicSize(i)" e "system.audioType(i)".

O "systemScreen(1)" e o "systemAudio(1)" são reservados para classes passivas,
e "systemScreen(2)" e "systemAudio(2)" são reservados para classes ativas.

O elemento [&lt;regionBase&gt;](regionbase.md) que define uma classe passiva também pode ter um
atributo de região.  Este atributo é usado para identificar um [&lt;region&gt;](region.md)
elemento em outro [&lt;regionBase&gt;](regionbase.md) associado ao dispositivo pai que
cria o mapa de bits enviado para a classe passiva; na região especificada o
o mapa de bits também deve ser exibido.  A propriedade "system.parentDeviceRegion(i)"
do objeto de configurações (elemento [&lt;media&gt;](media.md) de "application/x-ncl-settings"
type) é inicializado com o valor do atributo *region*.

### Sintaxe { data-search-exclude }

| Elemento | Atributos | Conteúdo | Pai |  |
| --- | --- | --- | --- | --- |
| [&lt;regionBase&gt;](regionbase.md) | *id*, *dispositivo*, *região* | ([&lt;importBase&gt;](importbase.md) | [&lt;region&gt;](region.md))+ | [&lt;head&gt;](head.md) |

### Atributos { data-search-exclude }

| Nome | Valor | Descrição |
| --- | --- | --- |
| *id* | Pode receber qualquer valor de string que comece com uma letra ou sublinhado e que contenha apenas letras, dígitos, <"."> e <"_">. | O atributo *id* identifica exclusivamente o elemento dentro de um documento. |
| *dispositivo* | "systemScreen(i)" ou "systemAudio(i)".  Onde o atributo não for especificado, a apresentação deverá ocorrer na mesma classe de dispositivo que executa o reprodutor NCL. | O atributo *device* identifica a classe de dispositivos onde ocorrerá a apresentação. |
| *região* | IDREF. | O atributo *region* identifica um elemento [&lt;region&gt;](region.md) em outro [&lt;regionBase&gt;](regionbase.md) associado ao dispositivo pai que cria o mapa de bits enviado para a classe passiva; na região especificada o bitmap também deve ser exibido. |
