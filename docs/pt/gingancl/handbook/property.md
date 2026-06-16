---
title: "Elemento &lt;property&gt;"
---

# &lt;property&gt;

O elemento [&lt;property&gt;](property.md) define uma propriedade ou um grupo de propriedades para
seu pai [&lt;media&gt;](media.md), [&lt;context&gt;](context.md), [&lt;body&gt;](body.md) ou [&lt;switch&gt;](switch.md)
elementos. Essas propriedades podem ser usadas em relacionamentos com outros objetos
de uma aplicação NCL, se o atributo externo do [&lt;property&gt;](property.md)
elemento tem "true" como valor.

O elemento [&lt;property&gt;](property.md) define o atributo name, que indica o
nome da propriedade ou grupo de propriedades e o atributo de valor.  O pai
elemento não pode ter mais de um elemento [&lt;property&gt;](property.md) com o mesmo
valor do atributo nome.

O atributo *value* é opcional e define um valor inicial para o
propriedade declarada no atributo *nome*. Quando o valor não é
especificado, a propriedade é inicializada com o valor definido no homônimo
atributos dos elementos [&lt;descriptor&gt;](descriptor.md) ou [&lt;region&gt;](region.md) associados
com o elemento pai que define [&lt;property&gt;](property.md), ou então com um
valor padrão (que depende do valor do atributo name). Quando o
valor é especificado no elemento [&lt;property&gt;](property.md), ele tem precedência sobre
o valor definido nos atributos homônimos de [&lt;descriptor&gt;](descriptor.md) ou
[&lt;region&gt;](region.md) elementos associados ao elemento pai que define o
[&lt;property&gt;](property.md).

### Sintaxe { data-search-exclude }

| Elemento | Atributos | Conteúdo | Pai |
| --- | --- | --- | --- |
| [&lt;property&gt;](property.md) | *nome*, *valor*, *externável* | -- | [&lt;media&gt;](media.md) ou [&lt;context&gt;](context.md) ou [&lt;body&gt;](body.md) |

### Atributos { data-search-exclude }

| Nome | Valor | Descrição |
| --- | --- | --- |
| *nome* | Pode receber qualquer valor de string que comece com uma letra ou sublinhado e que contenha apenas letras, dígitos, "." e "_". | O atributo *name* identifica exclusivamente a propriedade dentro de seu elemento pai. |
| *valor* | Depende do valor do nome. | O atributo *value* define um valor inicial para o atributo *name*. |
| *externável* | "falso" ou "verdadeiro".  O valor padrão é: "true" se a propriedade estiver definida em um elemento [&lt;property&gt;](property.md) ou "false" se a propriedade estiver definida em um elemento [&lt;descriptor&gt;](descriptor.md). | O atributo *externable* determina se uma propriedade pode (externable="true") ou não (externable="false") ser usada em relacionamentos. |

### Propriedades predefinidas { data-search-exclude }

Várias palavras reservadas são usadas para especificar propriedades com valores pré-definidos
semântica conhecida pelos jogadores NCL. Essas propriedades, sua semântica, sua
os valores possíveis e seus valores padrão são apresentados abaixo.

#### Propriedades predefinidas para todas as &lt;media&gt; elementos { data-search-exclude }

| Nome | Valor | Descrição |
| --- | --- | --- |
| style | URI. | O localizador de um arquivo de folha de estilo que especifica outras propriedades para o objeto. |
| player | String. | <p>Identifica a ferramenta de apresentação a ser usada.</p>  <p>Se não for especificado, o reprodutor é determinado pelo tipo de objeto, definido pelo atributo *type* do elemento [&lt;media&gt;](media.md), ou inferido pela extensão de arquivo do valor do atributo *src* do elemento [&lt;media&gt;](media.md).</p> |
| reusePlayer | <p>"true" ou "false".</p><p>O valor padrão é "false".</p> | Especifica se um novo reprodutor deve ser instanciado ("false") ou se um reprodutor já instanciado deve ser reutilizado ("true"). |
| playerLife | <p>"close" ou "keep".</p>  <p>O valor padrão é "close".</p> | Especifica o que acontecerá com a instância do reprodutor ao final da apresentação do objeto. |
| deviceClass | <p>"systemScreen(i)" ou "systemAudio(i)", onde *i* é um inteiro não negativo.</p><p>O valor padrão é a mesma classe de dispositivo que executa o reprodutor NCL.</p> | <p>Especifica a classe de dispositivo onde o objeto de mídia será apresentado.</p>   <p>Existem dois tipos diferentes de classes de dispositivos: ativa e passiva. Em uma classe ativa, um dispositivo é capaz de executar alguns reprodutores de mídia para apresentações de elementos [&lt;media&gt;](media.md). Em uma classe passiva, um dispositivo não precisa executar reprodutores de mídia, apenas exibir um mapa de bits ou uma sequência de amostras de áudio recebidas de outro dispositivo.</p>   <p>Os valores "systemScreen(1)" e "systemAudio(1)" são reservados para classes passivas, e "systemScreen(2)" e "systemAudio(2)" são reservados para classes ativas.</p> |
| explicitDur | <p>A propriedade "explicitDur" é especificada de acordo com uma das seguintes sintaxes:</p>   <ol>  <li>"Hours:Minutes:Seconds.Fraction", onde "Hours" é um inteiro no intervalo \[0,23\], "Minutes" é um inteiro no intervalo \[0,59\], "Seconds" é um inteiro no intervalo \[0,59\] e "Fraction" é um inteiro positivo.</li>  <li>Seconds"s", onde Seconds é um número real positivo.</li>  </ol>   <p>Para mídia contínua, o valor padrão é definido como a duração do conteúdo; caso contrário, deve ser definido como nulo (*nil*).</p> | Define a duração explícita de um objeto. |
| focusIndex | <p>Inteiro positivo.</p>  <p>Quando esta propriedade não está definida, o objeto é considerado como se nenhum foco pudesse ser aplicado a ele.</p> | <p>Especifica um índice para o elemento [&lt;media&gt;](media.md) ao qual o foco pode ser aplicado.</p>   <p>Nota: Quando um elemento em foco é selecionado pressionando a tecla de ativação ("SELECT" ou "ENTER"), o controle de foco deve ser passado para o renderizador (reprodutor) do elemento [&lt;media&gt;](media.md). O reprodutor pode então seguir suas próprias regras de navegação. O controle de foco deve ser devolvido ao reprodutor NCL quando a tecla "VOLTAR" (*back*) for pressionada. Neste caso, o foco vai para o elemento identificado pela propriedade "service.currentFocus" do nó de configurações (elemento [&lt;media&gt;](media.md) do tipo "application/x-ncl-settings").</p> |
| moveLeft | Inteiro positivo. | Especifica um valor igual ao valor *focusIndex* associado ao elemento ao qual o foco deve ser aplicado quando a tecla de seta para a esquerda for pressionada. Quando o foco é aplicado a um elemento com a propriedade *visible* definida como "false", ou a um elemento que não está sendo apresentado, o foco atual não se move. |
| moveRight | Inteiro positivo. | Especifica um valor igual ao valor *focusIndex* associado ao elemento ao qual o foco deve ser aplicado quando a tecla de seta para a direita for pressionada. Quando o foco é aplicado a um elemento com a propriedade *visible* definida como "false", ou a um elemento que não está sendo apresentado, o foco atual não se move. |
| moveUp | Inteiro positivo. | Especifica um valor igual ao valor *focusIndex* associado ao elemento ao qual o foco deve ser aplicado quando a tecla de seta para cima for pressionada. Quando o foco é aplicado a um elemento com a propriedade *visible* definida como "false", ou a um elemento que não está sendo apresentado, o foco atual não se move. |
| moveDown | Inteiro positivo. | Especifica um valor igual ao valor *focusIndex* associado a um elemento ao qual o foco deve ser aplicado quando a tecla de seta para baixo for pressionada. Quando o foco é aplicado a um elemento com a propriedade *visible* definida como "false", ou a um elemento que não está sendo apresentado, o foco atual não se move. |

#### Propriedades predefinidas para &lt;media&gt; elementos com conteúdo visual { data-search-exclude }

| Nome | Valor | Descrição |
| --- | --- | --- |
| top | <p>Um número real no intervalo \[0,100\] terminando com o caractere "%" (por exemplo, 30%), ou um valor inteiro não negativo especificando o atributo em pixels. Para valores em pixels, o qualificador de unidade "px" pode ser omitido.</p>   <p>O valor padrão é "0%", se o valor de *bottom* não for especificado.</p> | Posição superior do conteúdo, expressa como uma porcentagem da dimensão de altura do dispositivo de exibição, ou como um valor absoluto. Posiciona o topo do conteúdo a ser exibido na distância especificada a partir da borda superior do dispositivo de exibição. |
| bottom | <p>Se os valores de "top" e "height" forem especificados, deve ser calculado com base nesses valores. Caso contrário, deve ser um número real no intervalo \[0,100\] terminando com o caractere "%" (por exemplo, 30%), ou um valor inteiro não negativo especificando o atributo em pixels. Para valores em pixels, o qualificador de unidade "px" pode ser omitido.</p>   <p>O valor padrão é "0%", se o valor do atributo não puder ser calculado a partir dos atributos *height* e *top*.</p> | Posição inferior do conteúdo, expressa como uma porcentagem da dimensão de altura do dispositivo de exibição, ou como um valor absoluto. Posiciona a base do conteúdo a ser exibido na distância especificada a partir da borda inferior do dispositivo de exibição. |
| left | <p>Um número real no intervalo \[0,100\] terminando com o caractere "%" (por exemplo, 30%), ou um valor inteiro não negativo especificando o atributo em pixels. Para valores em pixels, o qualificador de unidade "px" pode ser omitido.</p>   <p>O valor padrão é "0%", se o valor de *right* não for especificado.</p> | Posição esquerda do conteúdo, expressa como uma porcentagem da dimensão de largura do dispositivo de exibição, ou como um valor absoluto. Posiciona o lado esquerdo do conteúdo a ser exibido na distância especificada a partir da borda esquerda do dispositivo de exibição. |
| right | <p>Se os valores de *left* e *width* forem especificados, deve ser calculado com base nesses valores. Caso contrário, deve ser um número real no intervalo \[0,100\] terminando com o caractere "%" (por exemplo, 30%), ou um valor inteiro não negativo especificando o atributo em pixels. Para valores em pixels, o qualificador de unidade "px" pode ser omitido.</p>   <p>O valor padrão é "0%", se o valor do atributo não puder ser calculado a partir dos atributos *width* e *left*.</p> | Posição direita do conteúdo, expressa como uma porcentagem da dimensão de largura do dispositivo de exibição, ou como um valor absoluto. Posiciona o lado direito do conteúdo a ser exibido na distância especificada a partir da borda direita do dispositivo de exibição. |
| width | <p>Um número real no intervalo \[0,100\] terminando com o caractere "%" (por exemplo, 30%), ou um valor inteiro não negativo especificando o atributo em pixels. Para valores em pixels, o qualificador de unidade "px" pode ser omitido.</p>   <p>O valor padrão é "0%".</p> | Largura do conteúdo a ser exibido, expressa como uma porcentagem da dimensão de largura do dispositivo de exibição, ou como um valor absoluto. |
| height | <p>Um número real no intervalo \[0,100\] terminando com o caractere "%" (por exemplo, 30%), ou um valor inteiro não negativo especificando o atributo em pixels. Para valores em pixels, o qualificador de unidade "px" pode ser omitido.</p>   <p>O valor padrão é "0%".</p> | Altura do conteúdo a ser exibido, expressa como uma porcentagem da dimensão de altura do dispositivo de exibição, ou como um valor absoluto. |
| location | Consulte as propriedades "left" e "top". | Dois números separados por vírgula, cada um seguindo a regra especificada para as propriedades "left" e "top", respectivamente. |
| size | Consulte as propriedades "width" e "height". | Dois números separados por vírgula, cada um seguindo a regra especificada para as propriedades "width" e "height", respectivamente. |
| bounds | Consulte as propriedades "left", "top", "width" e "height". | Quatro números separados por vírgula, cada um seguindo a regra especificada para as propriedades "left", "top", "width" e "height", respectivamente. |
| background | <p>"white", "black", "silver", "gray", "red", "maroon", "fuchsia", "purple", "lime", "green", "yellow", "olive", "blue", "navy", "aqua" ou "teal". Também pode ser o valor reservado "transparent".</p>   <p>O valor padrão é "transparent".</p> | A cor de fundo usada para preencher a área de uma região para exibição do conteúdo de mídia que não é preenchida pelo próprio conteúdo. |
| rgbChromakey | <p>Cor RGB definida usando uma notação hexadecimal (hex) para a combinação de valores de cores Vermelho, Verde e Azul (RGB). O menor valor que pode ser atribuído a uma das fontes de luz é 0 (hex 00). O maior valor é 255 (hex FF).</p>   <p>Também pode ser definida pelas palavras reservadas: "white", "black", "silver", "gray", "red", "maroon", "fuchsia", "purple", "lime", "green", "yellow", "olive", "blue", "navy", "aqua" ou "teal".</p> | A cor RGB a ser definida como transparente. |
| visible | <p>"true" ou "false".</p><p>O valor padrão é "false".</p> | <p>Permite que a apresentação do objeto seja vista ou ocultada.</p>   <p>Quando a propriedade *visible* associada a um elemento [&lt;context&gt;](context.md) ou [&lt;body&gt;](body.md) é igual a "true", a propriedade *visible* de cada elemento filho da composição é levada em consideração para definir como cada um desses elementos filhos será exibido.</p>   <p>Quando a propriedade *visible* associada a um elemento [&lt;context&gt;](context.md) ou [&lt;body&gt;](body.md) é igual a "false", todos os elementos filhos da composição são exibidos como ocultos.</p>   <p>Deve-se notar que um objeto com uma propriedade *visible* igual a "false", ou seja, um objeto exibido como oculto, não pode ter nenhuma de suas âncoras de conteúdo selecionada enquanto o valor da propriedade *visible* persistir como "false".</p>   <p>Quando um documento tem seu elemento [&lt;body&gt;](body.md) com sua propriedade *visible* definida como "false" e seu evento de apresentação está no estado pausado, diz-se que o documento está em espera (*stand-by*). No padrão ISDB-T, quando há apenas uma aplicação em execução e esta aplicação está em *stand-by*, o vídeo principal do serviço é dimensionado para 100% da tela e o áudio principal é definido para 100% de seu volume.</p> |
| transparency | <p>Um número real no intervalo \[0,1\] ou um número real no intervalo \[0,100\] terminando com o caractere "%" (por exemplo, "30%").</p>   <p>O valor padrão é "0%".</p> | Indica o grau de transparência da apresentação de um objeto: "1" ou "100%" significa transparência total e "0" ou "0%" significa opaco. |
| fit | <p>"fill", "hidden", "meet", "meetBest" ou "slice".</p>  <p>O valor padrão é "fill".</p> | <p>Indica como um objeto será apresentado.</p>   <p>"fill": redimensiona o conteúdo de mídia do objeto para que toque todas as bordas da caixa definida pelas propriedades "width" e "height" do objeto.</p>   <p>"hidden": se a "height" ("width") intrínseca do conteúdo de mídia for menor que a propriedade "height" ("width"), o objeto deve ser renderizado a partir da borda "top" ("left") e ter o restante da "height" ("width") preenchido com a cor de fundo; se a "height" ("width") intrínseca do conteúdo de mídia for maior que a propriedade "height" ("width"), o objeto deve ser renderizado a partir da borda superior (esquerda) até que a altura (largura) definida na propriedade seja alcançada; a parte do conteúdo de mídia abaixo (à direita) da altura (largura) é recortada.</p>   <p>"meet": redimensiona o objeto de mídia visual preservando sua proporção até que sua altura ou largura seja igual ao valor especificado pelas propriedades "height" ou "width". O canto superior esquerdo do conteúdo de mídia é posicionado nas coordenadas superiores esquerdas da caixa; o espaço vazio à direita ou na parte inferior deve ser preenchido com a cor de fundo.</p>   <p>"meetBest": a semântica é idêntica a "meet", exceto que a imagem não é ampliada além de 100% em nenhuma dimensão. "slice": redimensiona o conteúdo de mídia visual preservando sua proporção até que sua altura ou largura sejam iguais ao valor especificado nas propriedades "height" e "width" e a caixa de apresentação definida seja completamente preenchida. Algumas partes do conteúdo podem ser recortadas. O excesso de largura é recortado à direita do objeto de mídia. O excesso de altura é recortado na parte inferior do objeto de mídia.</p> |
| scroll | <p>"none", "horizontal", "vertical", "both" ou "automatic".</p>  <p>O valor padrão é 0.</p> | Permite especificar como a rolagem é configurada em uma região de exibição. |
| zIndex | <p>Um número inteiro no intervalo \[0,255\].</p>  <p>O valor padrão é 0.</p> | O atributo *zIndex* especifica a precedência de superposição, onde objetos com maiores valores de *zIndex* são empilhados sobre objetos com menores valores de *zIndex*. |
| plan | <p>"video", "graphic" ou "background".</p>   <p>O padrão é "video" para mídia com atributo *src* referindo-se a um PES de um fluxo de transporte, ou "graphic" para todos os outros casos.</p> | Define em qual plano de uma tela estruturada um objeto será posicionado. |
| focusBorderColor | <p>"white", "black", "silver", "gray", "red", "maroon", "fuchsia", "purple", "lime", "green", "yellow", "olive", "blue", "navy", "aqua" ou "teal".</p>   <p>O valor padrão é definido pela propriedade "default.focusBorderColor" do objeto *settings*.</p> | Define a cor para decorar a região da tela onde o objeto em foco está sendo apresentado, antes de ser selecionado. |
| selBorderColor | <p>"white", "black", "silver", "gray", "red", "maroon", "fuchsia", "purple", "lime", "green", "yellow", "olive", "blue", "navy", "aqua" ou "teal".</p>   <p>O valor padrão é definido pela propriedade "default.selBorderColor" do objeto *settings*.</p> | Define a cor para decorar a região da tela onde o objeto em foco está sendo apresentado, após ser selecionado. |
| focusBorderWidth | <p>Inteiro.</p>  <p>O valor padrão é definido pela propriedade "default.focusBorderWidth" do objeto *settings*.</p> | Largura (em pixels) aplicada à borda de um elemento em foco (0 significa que nenhuma borda aparecerá, valores positivos significam que a borda está fora do conteúdo do objeto e valores negativos significam que a borda é desenhada sobre o conteúdo do objeto). |
| focusBorderTransparency | <p>Um valor real entre 0 e 1, ou um valor real no intervalo \[0,100\] terminando com o caractere "%" (por exemplo, "30%").</p>   <p>O valor padrão é definido pela propriedade "default.focusBorderTransparency" do objeto *settings*.</p> | Transparência aplicada à borda de um elemento em foco, com "1" ou "100%" significando transparência total e "0" ou "0%" significando nenhuma transparência. |
| focusSrc | <p>Os seguintes valores são válidos:</p><ul><li><code>file:///file_path/#fragment_identifier</code>  -- para arquivos locais,</li><li><code>http://server_identifier/file_path/#fragment_identifier</code>  -- para arquivos remotos baixados usando o protocolo HTTP,</li><li><code>https://server_identifier/file_path/#fragment_identifier</code>  -- para arquivos remotos baixados usando o protocolo HTTPS,</li><li><code>rtsp://server_identifier/file_path/#fragment_identifier</code>  -- para fluxos baixados usando o protocolo RTSP,</li><li><code>rtp://server_identifier/file_path/#fragment_identifier</code>  -- para fluxos baixados usando o protocolo RTP,</li><li><code>ncl-mirror://media_element_identifier</code> -- para um fluxo de conteúdo idêntico ao que está em apresentação por outro elemento [&lt;media&gt;](media.md),</li><li><code>sbtvd-ts:</code> ou <code>isdb-ts:</code>  ou <code>ts://program_number.component_tag</code> -- para fluxos elementares recebidos do fluxo de transporte.</li></ul><p>Para o atributo *focusSrc* cujo valor identifica o esquema "sbtvd-ts", "isdb-ts" ou "ts", o "program_number.component_tag" pode ser substituído pelas seguintes palavras reservadas:</p><ul><li>"video" -- correspondente ao ES de vídeo primário sendo apresentado no plano de vídeo,</li><li>"audio"  -- correspondente ao ES de áudio primário,</li><li>"text" -- correspondente ao ES de texto primário,</li><li>"video(i)" -- correspondente ao *i*-ésimo menor "component_tag" de ES de vídeo listado na PMT dos serviços sintonizados,</li><li>"audio(i)" -- correspondente ao *i*-ésimo menor "component_tag" de ES de áudio listado na PMT dos serviços sintonizados, ou</li><li>"text(i)" -- correspondente ao *i*-ésimo menor "component_tag" de ES de texto listado na PMT dos serviços sintonizados.</li></ul> | Especifica uma fonte de mídia alternativa a ser apresentada, em vez da apresentação atual, se um elemento receber o foco. Este atributo segue as mesmas regras do atributo *src* do elemento [&lt;media&gt;](media.md). |
| focusSelSrc | Igual ao atributo *focusSrc*. | Especifica uma fonte de mídia alternativa a ser apresentada, em vez da apresentação atual, quando um elemento em foco é selecionado pressionando a tecla de ativação ("SELECT" ou "ENTER"). Este atributo segue as mesmas regras do atributo *src* do elemento [&lt;media&gt;](media.md). |
| freeze | "true" ou "false". O valor padrão é "false". | Define o que acontecerá com um objeto ao final de sua apresentação, se o conteúdo final será congelado ("true") ou não ("false"). O padrão é "false". |
| transIn, transOut | <p>Lista de (type, subtype, dur, startProgress, endProgress, direction, fadeColor, horzRepeat, vertRepeat, borderWidth, borderColor) separados por ponto e vírgula onde:</p>  <ul>  <li> O *type* obrigatório pode ser: "barWipe", "irisWipe", "clockWipe", "snakeWipe" ou "fade". Para a lista completa dos tipos de transição predefinidos, consulte: http://www.w3.org/TR/SMIL2/smil-transitions.html#TransitionEffects-Appendix.</li>  <li>Os valores obrigatórios de *subtype* dependem dos valores de *type*, conforme definido: "leftToRight" para "barWipe", "rectangle" para "irisWipe", "clockwiseTwelve" para "clockWipe", "topLeftHorizontal" para "snakeWipe" e "crossfade" para "fade". Para a lista completa dos subtipos de transição predefinidos, consulte: http://www.w3.org/TR/SMIL2/smil-transitions.html#TransitionEffects-Appendix.</li>  <li>O atributo *dur* é especificado de acordo com uma das seguintes sintaxes: (i) "Hours:Minutes:Seconds.Fraction", onde "Hours" é um inteiro no intervalo \[0,23\], "Minutes" é um inteiro no intervalo \[0,59\], "Seconds" é um inteiro no intervalo \[0,59\] e "Fraction" é um inteiro positivo; (ii) Seconds"s", onde "Seconds" é um número real positivo. O valor padrão é "0s".</li>  <li>*startProgress* e *endProgress* são números reais no intervalo \[0,1\].</li>  <li>Os valores de *direction* são "forward" e "reverse".</li>  <li>*fadeColor* é "white", "black", "silver", "gray", "red", "maroon", "fuchsia", "purple", "lime", "green", "yellow", "olive", "blue", "navy", "aqua" ou "teal".</li>  <li>*horzRepeat* e *vertRepeat* são inteiros positivos.</li>  <li>*borderWidth* é um inteiro não negativo.</li>  <li>*borderColor* é "white", "black", "silver", "gray", "red", "maroon", "fuchsia", "purple", "lime", "green", "yellow", "olive", "blue", "navy", "aqua" ou "teal".</li>  </ul>   <p>O valor padrão da propriedade é a string vazia. Se um tipo de transição for especificado, então:</p>  <ul>  <li>a duração padrão de "dur" é "1s",</li>  <li>o valor padrão de "startProgress" é 0,</li>  <li>el valor padrão de "endProgress" é 1,</li>  <li>o valor padrão de "direction" é "forward",</li>  <li>o valor padrão de "fadeColor" é "black",</li>  <li>o valor padrão de "horzRepeat" é 1,</li>  <li>o valor padrão de "vertRepeat" é 1,</li>  <li>o valor padrão de "borderWidth" é 0,</li>  <li>o valor padrão de "borderColor" é "black".</li>  </ul> | <p>O valor de *transIn* e *transOut* é uma lista de transições separadas por ponto e vírgula.</p>   <p>O objetivo da lista separada por ponto e vírgula é permitir que os autores especifiquem um conjunto de transições alternativas caso a transição preferida não esteja disponível. A primeira transição da lista deve ser executada se o agente de usuário tiver implementado essa transição. Se não estiver disponível, a segunda transição da lista deve ser executada, e assim por diante.</p>   <p>Os atributos *type* e *subtype* definem a transição. O atributo *dur* especifica a duração da transição.</p>   <p>O atributo *startProgress* especifica a quantidade de progresso na transição a partir da qual iniciar a execução. Por exemplo, podemos querer iniciar um *crossfade* com a imagem de destino já 30% visível. Nesse caso, *startProgress* seria 0.3.</p>   <p>O atributo *endProgress* especifica a quantidade de progresso na transição na qual encerrar a execução. O valor deste atributo deve ser maior ou igual ao valor do atributo *startProgress*. Se *endProgress* for igual a *startProgress*, a transição permanecerá em um progresso fixo durante toda a sua duração.</p>   <p>O atributo *direction* especifica a direção em que a transição será executada. Observe que nem todas as transições terão interpretações reversas significativas. Por exemplo, um *crossfade* não é uma transição geométrica e, portanto, não possui interpretação de direção reversa. Transições sem interpretação reversa devem ter o atributo *direction* ignorado e o valor padrão "forward" assumido.</p>   <p>Se o valor do atributo *type* for "fade" e o valor do atributo *subtype* for "fadeToColor" ou "fadeFromColor", o atributo *fadeColor* especifica a cor final ou inicial do *fade*. Se o valor do atributo *type* não for "fade", ou o valor do atributo *subtype* não for "fadeToColor" ou "fadeFromColor", o atributo *fadeColor* será ignorado.</p>   <p>Se o valor do atributo *type* não for "fade", os seguintes atributos podem ser especificados:</p>   <p>O atributo *horzRepeat* especifica quantas vezes repetir o padrão de transição ao longo do eixo horizontal.</p>   <p>O atributo *vertRepeat* especifica quantas vezes repetir o padrão de transição ao longo do eixo vertical.</p>   <p>O atributo *borderWidth* especifica a largura de uma borda gerada ao longo de uma borda de varredura (*wipe*).</p>   <p>O atributo *borderColor* especifica o conteúdo da borda gerada ao longo de uma borda de varredura (*wipe*). Se o valor deste atributo for uma cor, a borda gerada será preenchida com essa cor. Se o valor deste atributo for "blend", a borda gerada será uma mistura aditiva (ou desfoque) das fontes de mídia.</p> |

#### Propriedades predefinidas para &lt;media&gt; elementos com conteúdo de mídia contínua (somente leitura) { data-search-exclude }

| Nome | Valor | Descrição |
| --- | --- | --- |
| ID do conteúdo | <p>String.</p><p>(Definido apenas pelo player NCL.)</p> <p>O valor padrão é nulo.</p> | A propriedade "contentId" está associada a objetos de mídia contínua cujo conteúdo é definido referente a um fluxo elementar. Possui *null* como valor inicial e é definido como o valor do identificador transportado no descritor de referência NPT (em um campo de mesmo nome: contentId), assim que o objeto de mídia contínua associado é iniciado. |
| espera | <p>"true" ou "false".</p> <p>(Definido apenas pelo player NCL.)</p> <p>O valor padrão é "false".</p> | A propriedade "standby" é definida como "true" enquanto um conteúdo de objeto de mídia contínua já iniciado referente a um fluxo elementar é temporariamente interrompido por outro conteúdo intercalado, no mesmo fluxo elementar. |

#### Propriedades predefinidas para &lt;media&gt;  elementos com conteúdo audível { data-search-exclude }

| Nome | Valor | Descrição |
| --- | --- | --- |
| nível de som | Um número real no intervalo \[0,1\] ou um número real no intervalo \[0,100\] terminando com o caractere "%" (por exemplo, "30%").  <p>O valor padrão é 1.</p> | Volume de áudio relativo ao áudio gravado. |
| nível de equilíbrio | Um número real no intervalo \[-1,1\] ou um número real no intervalo \[-100,100\] terminando com o caractere "%" (por exemplo, "30%").  <p>O valor padrão é 0.</p> | Nível de equilíbrio do áudio (-1 à esquerda e +1 à direita). |
| nível agudo | Um número real no intervalo \[0,1\] ou um número real no intervalo \[0,100\] terminando com o caractere "%" (por exemplo, "30%").  <p>O valor padrão é 1.</p> | Configuração de agudos, relativa ao áudio gravado. |
| nível de graves | Um número real no intervalo \[0,1\] ou um número real no intervalo \[0,100\] terminando com o caractere "%" (por exemplo, "30%").  <p>O valor padrão é 1.</p> | Configuração de graves, relativa ao áudio gravado. |
| congelar | <p>"verdadeiro" ou "falso".</p><p>O valor padrão é "falso".</p> | Esta propriedade define o que acontecerá com um objeto ao final de sua apresentação, se o conteúdo final estiver congelado ("true") ou não ("false"). |
| transIn, transOut | Uma lista no formato "(type,subtype,dur,startProgress,endProgress)" onde: <ul> <li> "type" é "fade" por padrão, </li> <li> "subtipo" é "fade" por padrão,</li> <li>A propriedade "explicitDur" é especificada de acordo com um dos seguintes sintaxe: <ol> <li>"Horas:Minutos:Segundos.Fração", onde "Horas" é um número inteiro no intervalo \[0,23\], "Minutos" é um número inteiro no intervalo \[0,59\], "Segundos" é um número inteiro no intervalo \[0,59\] e "Fração" é um número inteiro positivo.</li> <li>Seconds"s", onde Segundos é um real positivo number.</li> </ol></li> <li>"startProgress" é um número real no intervalo \[0,1\], e "endProgress" é um número real no intervalo \[0,1\].</li> </ul> <p>O valor padrão da propriedade é a string vazia. Se uma transição for especificada, então:</p> <ul> <li> A duração padrão de "dur" é "1s",</li> <li> O valor padrão de "startProgress" é 0,</li> <li> O valor padrão de "endProgress" é 1.</li> </ul> | <p>O tipo de *transIn* e *transOut* é sempre "fade" e o *subtype* é sempre "fade" e é definido por padrão.</p> <p>O atributo *dur* especifica a duração da transição.</p> <p>O atributo *startProgress* especifica a quantidade de progresso durante a transição em que a execução deve ser iniciada.</p> <p>O atributo *endProgress* especifica a quantidade de progresso em que a transição deve ser finalizada. O valor deste atributo deve ser maior ou igual ao valor do atributo *startProgress*. Se *endProgress* for igual a *startProgress*, então a transição permanecerá em um progresso fixo durante a transição.</p> |

#### Propriedades predefinidas para &lt;media&gt;  elementos com conteúdo textual { data-search-exclude }

| Nome | Valor | Descrição |
| --- | --- | --- |
| fontColor | <p>"white", "black", "silver", "gray", "red", "maroon", "fuchsia", "purple", "lime", "green", "yellow", "olive", "blue", "navy", "aqua" ou "teal".</p>  <p>O valor padrão é "white".</p> | Define a cor da fonte. |
| fontFamily | <p>Uma lista priorizada de nomes de famílias de fontes e/ou nomes de famílias genéricas.</p>   <p>Existem dois tipos de nomes de famílias de fontes:</p>  <ul>  <li>"family-name": o nome de uma família de fontes de preferência, ou</li>  <li>"generic-family": as seguintes famílias genéricas são definidas: "serif", "sans-serif", "cursive", "fantasy" ou "monospace".</li>  </ul>   <p>O valor padrão desta propriedade depende do sistema.</p> | Os valores da lista são separados por vírgula para indicar que são alternativas. |
| textAlign | <p>"left", "right", "center" ou "justify".</p>  <p>O valor padrão é "left".</p> | Esta propriedade descreve como o conteúdo textual é alinhado. |
| fontStyle | <p>"normal" ou "italic".</p><p>O valor padrão é "normal".</p> | Define o estilo da fonte. |
| fontSize | <p>Inteiro positivo terminando com os caracteres "px" ou "pt", para tamanho relativo da fonte expresso em pixels, ou tamanho absoluto da fonte expresso em pontos, respectivamente.</p>  <p>O valor padrão desta propriedade depende do sistema.</p> | Define o tamanho da fonte para um tamanho fixo em pixels ou em pontos. |
| fontVariant | <p>"small-caps" ou "normal".</p><p>O valor padrão é "normal".</p> | Define um tipo de variação dentro de uma família de fontes. |
| fontWeight | <p>"normal" ou "bold".</p><p>O valor padrão é "normal".</p> | Esta propriedade seleciona o peso (espessura) da fonte. |
| freeze | <p>"true" ou "false".</p><p>O valor padrão é "false".</p> | Esta propriedade define o que acontecerá com um objeto ao final de sua apresentação, se o conteúdo final será congelado ("true") ou não ("false"). |
| transIn, transOut | <p>Lista de (type, subtype, dur, startProgress, endProgress, direction, fadeColor, horzRepeat, vertRepeat, borderWidth, borderColor) separados por ponto e vírgula onde:</p>  <ul>  <li> O *type* obrigatório pode ser: "barWipe", "irisWipe", "clockWipe", "snakeWipe" ou "fade". Para a lista completa dos tipos de transição predefinidos, consulte: http://www.w3.org/TR/SMIL2/smil-transitions.html#TransitionEffects-Appendix.</li>  <li>Os valores obrigatórios de *subtype* dependem dos valores de *type*, conforme definido: "leftToRight" para "barWipe", "rectangle" para "irisWipe", "clockwiseTwelve" para "clockWipe", "topLeftHorizontal" para "snakeWipe" e "crossfade" para "fade". Para a lista completa dos subtipos de transição predefinidos, consulte: http://www.w3.org/TR/SMIL2/smil-transitions.html#TransitionEffects-Appendix.</li>  <li>El atributo *dur* é especificado de acordo com uma das seguintes sintaxes: (i) "Hours:Minutes:Seconds.Fraction", onde "Hours" é um inteiro no intervalo \[0,23\], "Minutes" é um inteiro no intervalo \[0,59\], "Seconds" é um inteiro no intervalo \[0,59\] e "Fraction" é um inteiro positivo; (ii) Seconds"s", onde "Seconds" é um número real positivo. O valor padrão é "0s".</li>  <li>*startProgress* e *endProgress* são números reais no intervalo \[0,1\].</li>  <li>Os valores de *direction* são "forward" e "reverse".</li>  <li>*fadeColor* é "white", "black", "silver", "gray", "red", "maroon", "fuchsia", "purple", "lime", "green", "yellow", "olive", "blue", "navy", "aqua" ou "teal".</li>  <li>*horzRepeat* e *vertRepeat* são inteiros positivos.</li>  <li>*borderWidth* é um inteiro não negativo.</li>  <li>*borderColor* é "white", "black", "silver", "gray", "red", "maroon", "fuchsia", "purple", "lime", "green", "yellow", "olive", "blue", "navy", "aqua" ou "teal".</li>  </ul>   <p>O valor padrão da propriedade é a string vazia. Se um tipo de transição for especificado, então:</p>  <ul>  <li>a duração padrão de "dur" é "1s",</li>  <li>o valor padrão de "startProgress" é 0,</li>  <li>o valor padrão de "endProgress" é 1,</li>  <li>o valor padrão de "direction" é "forward",</li>  <li>o valor padrão de "fadeColor" é "black",</li>  <li>o valor padrão de "horzRepeat" é 1,</li>  <li>o valor padrão de "vertRepeat" é 1,</li>  <li>o valor padrão de "borderWidth" é 0,</li>  <li>o valor padrão de "borderColor" é "black".</li>  </ul> | <p>O valor de *transIn* e *transOut* é uma lista de transições separadas por ponto e vírgula.</p>   <p>O objetivo da lista separada por ponto e vírgula é permitir que os autores especifiquem um conjunto de transições alternativas caso a transição preferida não esteja disponível. A primeira transição da lista deve ser executada se o agente de usuário tiver implementado essa transição. Se não estiver disponível, a segunda transição da lista deve ser executada, e assim por diante.</p>   <p>Os atributos *type* e *subtype* definem a transição. O atributo *dur* especifica a duração da transição.</p>   <p>O atributo *startProgress* especifica a quantidade de progresso na transição a partir da qual iniciar a execução. Por exemplo, podemos querer iniciar um *crossfade* com a imagem de destino já 30% visível. Nesse caso, *startProgress* seria 0.3.</p>   <p>O atributo *endProgress* especifica a quantidade de progresso na transição na qual encerrar a execução. O valor deste atributo deve ser maior ou igual ao valor do atributo *startProgress*. Se *endProgress* for igual a *startProgress*, a transição permanecerá em um progresso fixo durante toda a sua duração.</p>   <p>O atributo *direction* especifica a direção em que a transição será executada. Observe que nem todas as transições terão interpretações reversas significativas. Por exemplo, um *crossfade* não é uma transição geométrica e, portanto, não possui interpretação de direção reversa. Transições sem interpretação reversa devem ter o atributo *direction* ignorado e o valor padrão "forward" assumido.</p>   <p>Se o valor do atributo *type* for "fade" e o valor do atributo *subtype* for "fadeToColor" ou "fadeFromColor", o atributo *fadeColor* especifica a cor final ou inicial do *fade*. Se o valor do atributo *type* não for "fade", ou o valor do atributo *subtype* não for "fadeToColor" ou "fadeFromColor", o atributo *fadeColor* será ignorado.</p>   <p>Se o valor do atributo *type* não for "fade", os seguintes atributos podem ser especificados:</p>   <p>O atributo *horzRepeat* especifica quantas vezes repetir o padrão de transição ao longo do eixo horizontal.</p>   <p>O atributo *vertRepeat* especifica quantas vezes repetir o padrão de transição ao longo do eixo vertical.</p>   <p>O atributo *borderWidth* especifica a largura de uma borda gerada ao longo de uma borda de varredura (*wipe*).</p>   <p>O atributo *borderColor* especifica o conteúdo da borda gerada ao longo de uma borda de varredura (*wipe*). Se o valor deste atributo for uma cor, a borda gerada será preenchida com essa cor. Se o valor deste atributo for "blend", a borda gerada será uma mistura aditiva (ou desfoque) das fontes de mídia.</p> |

#### Propriedades predefinidas para &lt;media&gt;  elementos do tipo "application/x-ncl-settings" { data-search-exclude }

O grupo *sistema*.  Conjunto de propriedades gerenciadas pelo sistema receptor.
Eles podem ser lidos, mas não podem ter seus valores alterados por uma NCL
aplicação, um procedimento Lua ou qualquer outro código imperativo ou declarativo
procedimento.  Os aplicativos nativos do receptor podem alterar essas propriedades'
valores.  Eles devem persistir durante todo o ciclo de vida do receptor.

| Nome | Valor | Descrição |
| --- | --- | --- |
| idioma do sistema | Código ISO 639-1. | Linguagem de áudio. |
| sistema.caption | Código ISO 639-1. | Idioma da legenda. |
| sistema.subtitle | Código ISO 639-1. | Idioma da legenda. |
| sistema.returnBitRate(i) | Número real. | A taxa de bits total do canal interativo (i) em quilobytes por segundo. |
| sistema.screenSize | (Inteiro, Inteiro). | Tamanho da tela do dispositivo, em (linhas, pixels/linha), quando uma classe não está definida. |
| system.screenGraphicSize | (Inteiro, Inteiro). | Resolução definida para o plano gráfico da tela do dispositivo, em (linhas, pixels/linha), quando não há classe definida. |
| sistema.audioType | "mono", "estéreo" ou "5.1". | Tipo de áudio do dispositivo, quando uma classe não está definida. |
| sistema.screenSize(i) | (Inteiro, Inteiro). | Tamanho da tela da classe (i) de dispositivos, em (linhas, pixels/linha). |
| system.screenGraphicSize(i) | (Inteiro, Inteiro). | Resolução definida para o plano gráfico da tela da classe (i) de dispositivos, em (linhas, pixels/linha). |
| sistema.audioType(i) | "mono", "estéreo" ou "5.1". | Tipo de áudio da classe (i) de dispositivos. |
| sistema.devNumber(i) | Inteiro. | Número de dispositivos de exposição cadastrados na classe (i). |
| sistema.classType(i) | "passivo" ou "ativo". | Tipo da classe (i). |
| system.parentDeviceRegion(i) | Cinco números separados por vírgula; cada um seguindo a regra de valor especificada para as propriedades "left", "top", "width", "height" e "zIndex", respectivamente. | Identifica um elemento [&lt;region&gt;](region.md) em outro [&lt;regionBase&gt;](regionbase.md) associado ao dispositivo pai que cria o mapa de bits enviado aos dispositivos de classe passiva (i); na região especificada o mapa de bits enviado também deverá ser exibido. |
| sistema.info(i) | Corda. | Lista dos reprodutores de mídia da classe (i). |
| sistema.classNumber | Inteiro. | Número de classes que foram definidas. |
| sistema.CPU | Número real. | Desempenho da CPU no MIPS, quanto à sua capacidade de executar aplicações. |
| memória do sistema | Inteiro. | Espaço mínimo de memória em megabytes fornecido aos aplicativos. |
| sistema.sistema operacional | String (a ser definida). | Tipo do sistema operacional. |
| system.luaVersion | String (a ser definida). | Versão do mecanismo Lua suportada pelo receptor. |
| sistema.ncl.versão | String (a ser definida). | Versão da linguagem NCL. |
| sistema.GingaNCL.versão | String (a ser definida). | Versão do ambiente Ginga-NCL. |
| sistema.xyz | Corda. | Qualquer propriedade com o prefixo "sistema" é reservada para uso futuro. |

O grupo *usuário*.  Conjunto de propriedades gerenciadas pelo sistema receptor.
Eles podem ser lidos, mas não podem ter seus valores alterados por uma NCL
aplicação, um procedimento Lua ou qualquer outro código imperativo ou declarativo
procedimento.  Os aplicativos nativos do receptor podem alterar as propriedades
valores.  Eles devem persistir durante todo o ciclo de vida do receptor.

| Nome | Valor | Descrição |
| --- | --- | --- |
| usuário.idade | Inteiro. | Idade do usuário. |
| usuário.localização | Corda. | Localização do usuário. |
| usuário.gênero | "m" (masculino) ou "f" (feminino). | Gênero do usuário. |
| usuário.xyz | Corda. | Qualquer propriedade com o prefixo "usuário" é reservada para uso futuro. |

O grupo *padrão*.  Conjunto de propriedades gerenciadas pelo receptor
sistema.  Eles podem ser lidos e ter seus valores alterados por um NCL
aplicação, um procedimento Lua ou qualquer outro código imperativo ou declarativo
procedimento.  Os aplicativos nativos do receptor podem alterar as propriedades
valores.  Eles devem persistir durante todo o ciclo de vida do receptor, no entanto, são
ajustados para seus valores iniciais quando um novo canal é sintonizado.

| Nome | Valor | Descrição |
| --- | --- | --- |
| padrão.focusBorderColor | "branco", "preto", "prata", "cinza", "vermelho", "marrom", "fúcsia", "roxo", "limão", "verde", "amarelo", "oliva", "azul", "marinho", "água" ou "verde-azulado". | Cor padrão aplicada à borda de um elemento em foco. |
| padrão.selBorderColor | "branco", "preto", "prata", "cinza", "vermelho", "marrom", "fúcsia", "roxo", "limão", "verde", "amarelo", "oliva", "azul", "marinho", "água" ou "verde-azulado". | Cor padrão aplicada à borda de um elemento em foco quando ativado. |
| padrão.focusBorderWidth | Inteiro. | Largura padrão (em pixels) aplicada à borda de um elemento em foco. |
| default.focusBorderTransparency | Número no intervalo \[0,1\] ou \[0,100\], terminando com o caractere "%" (por exemplo, "30%"), com "1" ou "100%" significando transparência total e "0" ou "0%" significando nenhuma transparência. | Transparência padrão aplicada à borda de um elemento em foco. |
| padrão.xyz | Corda. | Qualquer propriedade com o prefixo "default" é reservada para uso futuro. |

O grupo *serviço*.  Conjunto de propriedades gerenciadas pelo formatador NCL.
Eles podem ser lidos e ter seus valores alterados por uma aplicação NCL do
mesmo serviço.  Eles podem ser lidos, mas não podem ter seus valores alterados
por um procedimento Lua ou qualquer outro procedimento de código imperativo ou declarativo.
As alterações de variáveis ​​devem ser feitas usando comandos NCL.  Eles devem persistir em
pelo menos durante o ciclo de vida do serviço.

| Nome | Valor | Descrição |
| --- | --- | --- |
| serviço.currentFocus | Inteiro. | O valor *focusIndex* do elemento [&lt;media&gt;](media.md) em foco. |
| serviço.currentKeyMaster | Corda. | Identificador *id* do elemento [&lt;media&gt;](media.md) que controla as chaves de navegação; se o elemento [&lt;media&gt;](media.md) não estiver sendo apresentado ou não estiver pausado, o controle da chave de navegação pertence ao formatador NCL. |
| serviço.xyz | Corda. | Qualquer propriedade com o prefixo "serviço" segue as regras especificadas para o grupo. |

O grupo *si*.  Conjunto de propriedades gerenciadas pelo middleware.  Eles
podem ser lidos, mas não podem ter seus valores alterados por um NCL
aplicação, um procedimento Lua ou qualquer outro código imperativo ou declarativo
procedimento.  Eles devem persistir pelo menos até a próxima sintonia de canal.

| Nome | Valor | Descrição |
| --- | --- | --- |
| si.numberOfServices | Inteiro. | Número de serviços disponíveis no país para o canal sintonizado. Nota: O valor desta variável deve ser obtido a partir do número de tabelas PMT especificadas na tabela PAT do fluxo de transporte recebido no canal de sintonia (ver ISO/IEC 13818-1:2007). O valor da variável deve levar em consideração apenas as tabelas PMT cujos campos country_code, especificados no descritor country_availability_descriptor (ver Seção 8.3.6 da ABNT NBR 15603-2:2007) relacionados à tabela, são equivalentes ao valor da variável "user.location" do nó *settings*. |
| si.numberOfPartialServices | Inteiro | Número de serviços de 1 segmento disponíveis no país para o canal sintonizado. Nota: O valor desta variável deve ser obtido a partir do número de tabelas PMT especificadas na tabela PAT do fluxo de transporte recebido no canal de sintonia (ver ISO/IEC 13818-1:2007). O valor da variável deve levar em consideração apenas as tabelas PMT cujos campos country_code, especificados no country_availability_descriptor (ver Seção 8.3.6 da ABNT NBR 15603-2:2007) relacionado à tabela, sejam iguais ao valor da variável "user.location" do nó *settings*, e cujos campos program_number sejam equivalentes aos campos service_id do parcial_reception_descriptor relacionado às tabelas NIT. |
| si.canalNumber | Inteiro | Número do canal sintonizado. Nota: O valor desta variável deve ser obtido no campo remote_control_key_id do descritor ts_information_descriptor (ver Seção 8.3.42 da ABNT NBR 15603-2:2007) da tabela NIT (ver Seção 7.2.4 da ABNT NBR 15603-2:2007) que descreve o serviço atual. |
| si.xyz | Corda | Qualquer propriedade com o prefixo "si" segue as regras especificadas para o grupo. |

O grupo *canal*.  Conjunto de propriedades gerenciadas pelo formatador NCL.
Eles podem ser lidos e ter seus valores alterados por uma aplicação NCL do
mesmo canal.  Eles podem ser lidos, mas não podem ter seus valores alterados
por um procedimento Lua ou qualquer outro procedimento de código imperativo ou declarativo de
o mesmo canal; alterações de variáveis ​​devem ser feitas usando comandos NCL.  Eles
deve persistir pelo menos até a próxima sintonia de canal.

| Nome | Valor | Descrição |
| --- | --- | --- |
| canal.keyCapture | Corda | Solicitação de chaves alfanuméricas para aplicações NCL. |
| canal.virtualTeclado | "verdadeiro" ou "falso" | Solicitação de teclado virtual para aplicações NCL. |
| canal.keyboardBounds | (Inteiro, Inteiro, Inteiro, Inteiro) | Região do teclado virtual (esquerda, superior, largura, altura). |
| canal.xyz | Corda | Qualquer variável com o prefixo "canal" segue as regras especificadas para o grupo. |

O *compartilhado*.  Conjunto de propriedades gerenciadas pelo formatador NCL.  Eles
podem ser lidos e ter seus valores alterados por uma aplicação NCL.  Eles podem
ser lidos, mas não podem ter seus valores alterados por um procedimento Lua ou qualquer
outro procedimento de código imperativo ou declarativo; mudanças de variáveis devem ser
feito usando comandos NCL.  Eles devem persistir pelo menos durante o ciclo de vida
do serviço que os definiu.

| Nome | Valor | Descrição |
| --- | --- | --- |
| compartilhado.xyz | Corda | Qualquer propriedade com o prefixo "compartilhado" segue as regras especificadas para o grupo. |

#### Nomes reservados para definição de cores { data-search-exclude }

<table class="inline">
<tbody>
<tr class="row0">
  <th>Cor</th>
  <th>Nome</th>
  <th>Hexadecimal</th>
  <th>(R,G,B)</th>
  <th>Matiz</th>
  <th>(Saturação, Luz)</th>
  <th>(Saturação, Valor)</th>
</tr>
<tr>
<td bgcolor="#ffffff"/>
<td>Branco</td>
<td>#ffffff</td>
<td>(100%, 100%, 100%)</td>
<td>0°;</td>
<td>(0%, 100%)</td>
<td>(0%, 100%)</td>
</tr>

<tr>
<td bgcolor="#c0c0c0"/>
<td>Prata</td>
<td>#c0c0c0</td>
<td>(75%, 75%, 75%)</td>
<td>0°;</td>
<td>(0%, 75%)</td>
<td>(0%, 75%)</td>
</tr>

<tr>
<td bgcolor="#808080"/>
<td>Cinza</td>
<td>#808080</td>
<td>(50%, 50%, 50%)</td>
<td>0°;</td>
<td>(0%, 50%)</td>
<td>(0%, 50%)</td>
</tr>

<tr>
<td bgcolor="#000000"/>
<td>Preto</td>
<td>#000000</td>
<td>(0%, 0%, 0%)</td>
<td>0°;</td>
<td>(0%, 0%)</td>
<td>(0%, 0%)</td>
</tr>

<tr>
<td bgcolor="#ff0000"/>
<td>Vermelho</td>
<td>#ff0000</td>
<td>(100%, 0%, 0%)</td>
<td>0°;</td>
<td>(100%, 50%)</td>
<td>(100%, 100%)</td>
</tr>

<tr>
<td bgcolor="#800000"/>
<td>Marrom</td>
<td>#800000</td>
<td>(50%, 0%, 0%)</td>
<td>0°;</td>
<td>(100%, 25%)</td>
<td>(100%, 50%)</td>
</tr>

<tr>
<td bgcolor="#ffff00"/>
<td>Amarelo</td>
<td>#ffff00</td>
<td>(100%, 100%, 0%)</td>
<td>60°;</td>
<td>(100%, 50%)</td>
<td>(100%, 100%)</td>
</tr>

<tr>
<td bgcolor="#808000"/>
<td>Olive</td>
<td>#808000</td>
<td>(50%, 50%, 0%)</td>
<td>60°;</td>
<td>(100%, 25%)</td>
<td>(100%, 50%)</td>
</tr>

<tr>
<td bgcolor="#00ff00"/>
<td>Lime</td>
<td>#00ff00</td>
<td>(0%, 100%, 0%)</td>
<td>120°;</td>
<td>(100%, 50%)</td>
<td>(100%, 100%)</td>
</tr>

<tr>
<td bgcolor="#008000"/>
<td>Verde</td>
<td>#008000</td>
<td>(0%, 50%, 0%)</td>
<td>120°;</td>
<td>(100%, 25%)</td>
<td>(100%, 50%)</td>
</tr>

<tr>
<td bgcolor="#00ffff"/>
<td>Aqua</td>
<td>#00ffff</td>
<td>(0%, 100%, 100%)</td>
<td>180°;</td>
<td>(100%, 50%)</td>
<td>(100%, 100%)</td>
</tr>

<tr>
<td bgcolor="#008080"/>
<td>Teal</td>
<td>#008080</td>
<td>(0%, 50%, 50%)</td>
<td>180°;</td>
<td>(100%, 25%)</td>
<td>(100%, 50%)</td>
</tr>

<tr>
<td bgcolor="#0000ff"/>
<td>Azul</td>
<td>#0000ff</td>
<td>(0%, 0%, 100%)</td>
<td>240°;</td>
<td>(100%, 50%)</td>
<td>(100%, 100%)</td>
</tr>

<tr>
<td bgcolor="#000080"/>
<td>Marinha</td>
<td>#000080</td>
<td>(0%, 0%, 50%)</td>
<td>240°;</td>
<td>(100%, 25%)</td>
<td>(100%, 50%)</td>
</tr>

<tr>
<td bgcolor="#ff00ff"/>
<td>Fúcsia</td>
<td>#ff00ff</td>
<td>(100%, 0%, 100%)</td>
<td>300°;</td>
<td>(100%, 50%)</td>
<td>(100%, 100%)</td>
</tr>

<tr>
<td bgcolor="#800080"/>
<td>Roxo</td>
<td>#800080</td>
<td>(50%, 0%, 50%)</td>
<td>300°;</td>
<td>(100%, 25%)</td>
<td>(100%, 50%)</td>
</tr>

</tbody>
</table>
