---
title: "Elemento &lt;area&gt;"
---

# &lt;area&gt;

O elemento [&lt;area&gt;](area.md) permite definir uma âncora de conteúdo (um subconjunto de
unidades de informação do conteúdo de um elemento [&lt;media&gt;](media.md)) que podem ser usadas em
relacionamentos com outros objetos em uma aplicação NCL.

As âncoras de conteúdo podem representar:

- porções espaciais de imagens: através do atributo *coords*;
- porções temporais de conteúdo de mídia contínua (áudio, vídeo, etc.):
  através dos atributos *begin* e *end*, ou com base no
  número de amostras de áudio ou quadros de vídeo, através do *primeiro* e
  *últimos* atributos, que indicam o início e o final
  amostra/quadro;
- porções temporais e espaciais dos vídeos: através das *coordenadas*,
  atributos *begin* e *end*; ou através do
  atributos *coords*, *primeiro* e *último*;
- segmentos textuais: através de *beginText*, *beginPosition*,
  Atributos *endText* e *endPosition*, que definem o
  strings de início e fim e sua ocorrência no texto
  respectivamente;
- uma string usada pelo media player para identificar uma região de conteúdo
  (por exemplo, uma função ou método em um objeto de mídia imperativo, um
  interface em um objeto de mídia declarativo, como uma âncora HTML, uma porta em
  um objeto de mídia com uma aplicação NCL como conteúdo, etc.): através do
  atributo *rótulo*;
- um clipe no conteúdo de um objeto hipermídia declarativo: usando o
  *clipe* atributo.

Cada elemento [&lt;media&gt;](media.md), [&lt;context&gt;](context.md), [&lt;body&gt;](body.md) e [&lt;switch&gt;](switch.md)
tem uma âncora de conteúdo com uma região que representa todo o conteúdo do
nó definido por padrão.  Essa âncora é chamada de "âncora de todo o conteúdo".
Exceto para objetos de mídia com conteúdo de código imperativo (por exemplo, aqueles
cujo tipo MIME é "application/x-ncl-NCLua"), toda vez que um componente NCL
é referido sem especificar uma de suas âncoras, toda a âncora de conteúdo
é assumido.

### Sintaxe { data-search-exclude }

| Elemento | Atributos | Conteúdo | Pai |
| --- | --- | --- | --- |
| [&lt;area&gt;](area.md) | <u>*id*</u>, *coords*, *begin*, *end*, *beginText*, *endText*, *beginPosition*, *endPosition*, *first*, *last*, *label*, *clip* | -- | [&lt;media&gt;](media.md) |

### Atributos { data-search-exclude }

| Nome | Valor | Descrição |
| --- | --- | --- |
| *id* | Pode receber qualquer valor de string que comece com uma letra ou um sublinhado e que contenha apenas letras, dígitos, "." e "_". | O atributo *id* identifica exclusivamente o elemento dentro de um documento. |
| *coords* | <p>Uma lista de valores da forma "left-x, top-y, right-x, bottom-y" onde cada valor é:</p><ol><li>um número real no intervalo \[0,100\] terminando com o caractere "%" (por exemplo, "30%"), ou</li><li>um inteiro positivo especificando o valor em pixels. Para valores em pixels, o qualificador de unidade "px" pode ser omitido.</li></ol> | <p>O atributo *coords* especifica a posição de uma área retangular na tela.</p><p>As coordenadas são relativas ao canto superior esquerdo do conteúdo do objeto.</p><p>Os valores são separados por vírgulas.</p><p>A ordem dos valores é "left-x", "top-y", "right-x" e "bottom-y".</p><p>Quando "left-x" e "right-x" são expressos como uma porcentagem, o valor é relativo à propriedade de largura (*width*) do objeto de mídia.</p><p>Quando "top-y" e "bottom-y" são expressos como uma porcentagem, o valor é relativo à propriedade de altura (*height*) do objeto de mídia.</p> |
| *begin* | <p>Exceto para o elemento [&lt;media&gt;](media.md) do tipo "application/x-ncl-time", o atributo *begin* deve ser especificado de acordo com uma das seguintes sintaxes:</p><ol><li>"Hours:Minutes:Seconds.Fraction", onde "Hours" é um inteiro no intervalo \[0,23\], "Minutes" é um inteiro no intervalo \[0,59\], "Seconds" é um inteiro no intervalo \[0,59\] e "Fraction" é um inteiro positivo,</li><li>Seconds"s", onde "Seconds" é um número real positivo.</li></ol><p>Para o elemento [&lt;media&gt;](media.md) do tipo "application/x-ncl-time", o atributo *begin* deve ser especificado de acordo com a seguinte sintaxe: "Year:Month:Day:Hours:Minutes:Seconds.Fraction", conforme o fuso horário do país. O agente de usuário NCL é responsável por traduzir o valor do fuso horário do país para o correspondente ao UTC.</p><p>Se o atributo *end* for definido, mas sem uma definição explícita para o atributo *begin*, o início da apresentação de todo o conteúdo de mídia será considerado como o início da âncora.</p><p>No caso de um elemento de mídia do tipo "application/x-ncl-time", o atributo *begin* deve sempre ser definido e assume um valor UTC absoluto.</p> | O atributo *begin* especifica o início da âncora temporal. |
| *end* | Igual ao atributo *begin*. | O atributo *end* especifica o fim da âncora temporal. |
| *beginText* | <p>String.</p><p>Se o início da região da âncora de conteúdo não for definido, o início do conteúdo de texto é assumido.</p> | Os atributos *beginText* e *beginPosition* especificam o início da âncora de texto. O *beginText* define uma string no texto. |
| *endText* | String. | Os atributos *endText* e *endPosition* especificam o fim da âncora de texto. O *endText* define uma string no texto. |
| *beginPosition* | Inteiro positivo. O valor padrão é 1. | Os atributos *beginText* e *beginPosition* especificam o início da âncora de texto. O *beginPosition* define a ocorrência da string no texto. |
| *endPosition* | Inteiro positivo. O valor padrão é a posição do último caractere na string. | Os atributos *endText* e *endPosition* especificam o fim da âncora de texto. O *endPosition* define a ocorrência da string no texto. |
| *first* | <p>O atributo *first* deve ser especificado de acordo com uma das seguintes sintaxes:</p><ol><li>Samples"s", onde Samples é um inteiro positivo,</li><li>Frames"f", onde Frames é um inteiro positivo, ou</li><li>NPT"npt", onde NPT é o valor de Normal Play Time.</li></ol><p>Se o atributo *last* for definido, mas sem uma definição explícita para o atributo *first*, o início da apresentação de todo o conteúdo de mídia será considerado como o início da âncora.</p> | -- |
| *last* | <p>O atributo *last* deve ser especificado de acordo com uma das seguintes sintaxes:</p><ol><li>Samples"s", onde Samples é um inteiro positivo,</li><li>Frames"f", onde Frames é um inteiro positivo, ou</li><li>NPT"npt", onde NPT é o valor de Normal Play Time.</li></ol><p>Se o atributo *first* for definido, mas o atributo *last* não for especificado, o fim da apresentação de todo o conteúdo de mídia será assumido como o fim da âncora.</p> | -- |
| *label* | String. | O atributo *label* identifica uma região de conteúdo, por exemplo, uma função em um objeto de mídia imperativo, uma interface em um objeto de mídia declarativo, como uma âncora HTML, ou uma porta em um objeto de mídia com uma aplicação NCL como conteúdo, etc. |
| *clip* | <p>String.</p><p>O valor depende do tipo de objeto hipermídia declarativo. Para objetos de mídia NCL, o valor de *clip* é uma tripla "(chainId,beginOffset,endOffset)" usada pelo reprodutor de mídia NCL para identificar um elemento [&lt;port&gt;](port.md) de aplicação NCL através do qual uma cadeia temporal começa, e o tempo de início e fim nessa cadeia temporal.</p><p>Para elementos [&lt;media&gt;](media.md) com conteúdo de código NCL, os seguintes padrões são definidos:</p><ol><li>"chainId" é a âncora de todo o conteúdo do elemento [&lt;body&gt;](body.md),</li><li>"beginOffset" é "0s", e</li><li>"endOffset" é o tempo final da cadeia temporal.</li></ol> | O atributo *clip* identifica um clipe de fluxo no conteúdo de um objeto hipermídia declarativo. |
