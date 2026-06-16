---
title: "Elemento &lt;transition&gt;"
---

### Definição e uso { data-search-exclude }

O elemento [&lt;transition&gt;](transition.md) permite definir um modelo de transição.

### Sintaxe { data-search-exclude }

| Elemento | Atributos | Conteúdo | Pai |
| --- | --- | --- | --- |
| [&lt;transition&gt;](transition.md) | <u>*id*</u>, <u>*tipo*</u>, *subtipo*, *dur*, *startProgress*, *endProgress*, *direção*, *fadeColor*, *horzRepeat*, *vertRepeat*, *borderWidth*, *borderColor* | -- | [&lt;transitionBase&gt;](transitionbase.md) |

### Atributos { data-search-exclude }

| Nome | Valor | Descrição |
| --- | --- | --- |
| *id* | Pode receber qualquer valor de string que comece com uma letra ou sublinhado e que contenha apenas letras, dígitos, <"."> e <"_">. | O atributo *id* identifica exclusivamente o elemento dentro de um documento. |
| *tipo* | "barWipe", "irisWipe", "clockWipe", "snakeWipe" ou "fade".  Estes são os valores necessários.  Para obter a lista completa de tipos de transição predefinidos, consulte: http://www.w3.org/TR/SMIL2/smil-transitions.html#TransitionEffects-Appendix. | Os atributos *type* e *subtype* definem a transição. |
| *subtipo* | Os valores de subtipo necessários dependem do valor do tipo.  Para "barWipe" o subtipo necessário é "leftToRight", para "irisWipe" é "rectangle", para "clockWipe" é "clockwiseTwelve", para "snakeWipe" é "topLeftHorizontal" e para "fade" é "crossfade".  A lista completa pode ser encontrada em http://www.w3.org/TR/SMIL2/smil-transitions.html#TransitionEffects-Appendix.  Os valores de subtipo necessários também são os valores padrão. | Os atributos *type* e *subtype* definem a transição. |
| *dur* | O atributo *dur* é especificado de acordo com uma das seguintes sintaxes: (i) "Horas:Minutos:Segundos.Fração", onde "Horas" é um número inteiro no intervalo \[0,23\], "Minutos" é um número inteiro no intervalo \[0,59\], "Minutos" é um número inteiro no intervalo \[0,59\] e "Fração" é um número inteiro positivo; (ii) Segundos<"s">, onde "Segundos" é um número real positivo.  O valor padrão é "1s". | O atributo *dur* especifica a duração da transição. |
| *startProgress* | Um número real no intervalo \[0,1\].  O valor padrão é 0. | O atributo *startProgress* especifica a quantidade de progresso através da transição na qual iniciar a execução. Por exemplo, podemos querer iniciar um crossfade com a imagem de destino já com 30% de fade in. Para este caso, *startProgress* seria 0,3. |
| *fimProgresso* | Um número real no intervalo \[0,1\].  O valor padrão é 0. | O atributo *endProgress* especifica a quantidade de progresso através da transição em que a execução será finalizada.  O valor deste atributo deve ser maior ou igual ao valor do atributo *startProgress*. Se *endProgress* for igual a *startProgress*, a transição permanecerá em um progresso fixo durante a transição. |
| *direção* | "para frente" ou "para trás".  O valor padrão é "encaminhar". | Especifica a direção em que a transição será executada.  Observe que nem todas as transições terão interpretações reversas significativas.  Por exemplo, um crossfade não é uma transição geométrica e, portanto, não tem interpretação de direção reversa. Transições que não possuem interpretação reversa têm seu atributo de direção ignorado e o valor padrão de "forward" é assumido. |
| *cor desbotada* | "branco", "preto", "prata", "cinza", "vermelho", "marrom", "fúcsia", "roxo", "limão", "verde", "amarelo", "oliva", "azul", "marinho", "água" ou "verde-azulado".  O valor padrão é "preto". | Se o valor do atributo *type* for "fade" e o valor do atributo *subtype* for "fadeToColor" ou "fadeFromColor", então o atributo *fadeColor* especifica a cor final ou inicial do fade. Se o valor do atributo *type* não for "fade", ou o valor do atributo *subtype* não for "fadeToColor" ou "fadeFromColor", então o atributo *fadeColor* deverá ser ignorado. |
| *horzRepetir* | Inteiro positivo.  O valor padrão é 1. | Este atributo é válido somente se o valor do atributo *type* não for "fade".  Especifica quantas vezes executar o padrão de transição ao longo do eixo horizontal. |
| *vertRepeat* | Inteiro positivo.  O valor padrão é 1. | Este atributo é válido somente se o valor do atributo *type* não for "fade".  Especifica quantas vezes executar o padrão de transição ao longo do eixo vertical. |
| *larguradaborda* | Inteiro positivo.  O valor padrão é 0. | Este atributo é válido somente se o valor do atributo *type* não for "fade".  Ele especifica a largura de uma borda gerada ao longo de uma borda apagada. |
| *borderColor* | "branco", "preto", "prata", "cinza", "vermelho", "marrom", "fúcsia", "roxo", "limão", "verde", "amarelo", "oliva", "azul", "marinho", "água" ou "verde-azulado".  O valor padrão é "preto". | Este atributo é válido somente se o valor do atributo type não for "fade".  Ele especifica o conteúdo da borda gerada ao longo de uma borda apagada. Se o valor deste atributo for uma cor, então a borda gerada ao longo da borda apagada ou distorcida será preenchida com esta cor. Se o valor deste atributo for "mescla", então a borda gerada ao longo da mistura de apagamento será uma mistura aditiva (ou desfoque) das fontes de mídia. |
