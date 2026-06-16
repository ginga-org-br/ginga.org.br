---
title: "Elemento &lt;simpleCondition&gt;"
---

### Definição e uso { data-search-exclude }

O elemento [&lt;simpleCondition&gt;](simplecondition.md) define uma condição simples para acionar
ações em uma relação causal.

O elemento [&lt;simpleCondition&gt;](simplecondition.md) possui um role *attribute*, cujo valor
deve ser exclusivo no conjunto de funções do conector.  O papel é um conector
ponto de interface, que está associado às interfaces dos nós por um link que
refere-se ao conector.

Um [&lt;simpleCondition&gt;](simplecondition.md) também define um tipo de evento (*eventType*
atributo) e a qual transição na máquina de estado de evento ela se refere
(atributo *transição*).  O *eventType* e
*transição* pode ser inferida pelo valor do papel, se palavras reservadas forem
usado.  Caso contrário, os atributos *eventType* e *transition*
são necessários.

Valores de função de condição reservada associados a máquinas de estado de evento:

| Valor da função | Valor de transição | Tipo de Evento |
| --- | --- | --- |
| onBegin | começa | apresentação |
| no fim | paragens | apresentação |
| onAbortar | abortos | apresentação |
| emPausa | pausas | apresentação |
| onRetomar | currículos | apresentação |
| onSelection | paragens | seleção |
| onBeginSelection | começa | seleção |
| onEndSelection | paragens | seleção |
| onAbortSelection | pagamentos | seleção |
| onPauseSelection | pausas | seleção |
| onResumeSelection | currículos | seleção |
| onBeginAttribution | começa | atribuição |
| onEndAttribution | paragens | atribuição |
| onPauseAttribution | pausas | atribuição |
| onResumeAttribution | currículos | atribuição |
| onAbortAttribution | abortos | atribuição |

Se um valor *eventType* for "selection", a função também poderá definir
qual aparelho de seleção (por exemplo, teclas do teclado ou controle remoto
chaves) a que se refere, através do seu atributo chave.  Se este atributo não for
especificado, a seleção através de um dispositivo apontador (mouse, tela sensível ao toque,
teclas de navegação) é assumido.

A cardinalidade da função especifica o mínimo (atributo min) e o máximo (max
atributo) número de participantes que podem desempenhar o papel (ou seja, o
número de ligações) quando o [&lt;causalConnector&gt;](causalconnector.md) é usado para criar um
[&lt;link&gt;](link.md).  Se o valor máximo for maior que um, um qualificador
atributos devem ser especificados informando o relacionamento lógico entre os
condição simples vincula: "ou" ou "e".  Se o qualificador estabelecer o
operador lógico "ou", a ação do link será disparada sempre que qualquer condição
ocorre.  Se o qualificador estabelecer o operador lógico "e", o link
a ação será disparada após todas as ocorrências de condições simples.

Um atributo de atraso também pode ser definido para um [&lt;simpleCondition&gt;](simplecondition.md),
especificando que a condição é verdadeira após um atraso de tempo a partir do momento em que
ocorre a transição.

### Sintaxe { data-search-exclude }

| Elemento | Atributos | Conteúdo | Pai |
| --- | --- | --- | --- |
| [&lt;simpleCondition&gt;](simplecondition.md) | <u>*papel*</u>, *atraso*, *eventType*, *chave*, *transição*, *min*, *máx*, *qualificador* | -- | [&lt;causalConnector&gt;](causalconnector.md) ou [&lt;compoundCondition&gt;](compoundcondition.md) |

### Atributos { data-search-exclude }

| Nome | Valor | Descrição |
| --- | --- | --- |
| *papel* | Corda. | O atributo *role* define um ponto de interface do conector, que está associado às interfaces dos nós por um link que se refere ao conector.  O valor *role* deve ser exclusivo dentro do conjunto de funções do conector. |
| *atraso* | <p>O atributo *delay* deve ser especificado de acordo com um dos seguintes sintaxe:</p><ol><li class="level1"><div class="li"><"<nowiki>Horas:Minutos:Segundos.Fraction</nowiki>">, onde "Horas" é um número inteiro em \[0,23\] intervalo, "Minutos" é um número inteiro no intervalo \[0,59\], "Segundos" é um número inteiro no intervalo 0,59 e "Fração" é um valor positivo inteiro,</div></li><li class="level1"><div class="li">Seconds<"s">, onde "Segundos" é um real positivo number.</div></li></ol><p>O valor padrão é "0s".</p> | O atributo *delay* define um atraso de tempo, a partir do momento em que ocorre a transição, a partir do qual o [&lt;simpleCondition&gt;](simplecondition.md) deve ser considerado satisfeito.
| *tipodeevento* | "apresentação", "seleção" ou "atribuição". | O atributo *eventType* identifica o tipo de evento para a ação ou condição. |
| *chave* | Pelo menos os seguintes valores (sensível a maiúsculas e minúsculas) devem ser aceitos para o atributo chave: "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "*", "#", "MENU", "INFO", "GUIDE", "CURSOR_DOWN", "CURSOR_LEFT", "CURSOR_RIGHT", "CURSOR_UP", "CHANNEL_DOWN", "CHANNEL_UP", "VOLUME_DOWN", "VOLUME_UP", "ENTER", "RED", "GREEN", "YELLOW", "BLUE", "BACK", "EXIT", "POWER", "REWIND", "STOP", "EJECT", "PLAY", "RECORD" e "PAUSE". | O atributo *key* identifica a chave de seleção usada para a seleção. |
| *transição* | "inicia", "para", "aborta", "pausa" ou "retoma". | O atributo *transition* especifica uma transição na máquina de estados do evento usada para definir a condição. |
| *min* | <p>Inteiro positivo menor ou igual ao valor *max*.</p><p>O valor padrão é 1.</p> | O atributo *min* define o número mínimo de participantes que podem desempenhar a função. |
| *máx* | <p>Inteiro positivo maior ou igual ao valor *min* ou ao valor "ilimitado".</p><p>O valor padrão é 1.</p> | O atributo *max* define o número máximo de participantes que podem desempenhar a função. |
| *qualificatória* | "e" ou "ou". | O atributo *qualifier* define o relacionamento lógico entre as vinculações de condição. |