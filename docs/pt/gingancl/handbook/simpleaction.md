---
title: "Elemento &lt;simpleAction&gt;"
---

### Definição e uso { data-search-exclude }

O elemento [&lt;simpleAction&gt;](simpleaction.md) define uma ação simples acionada pelo
avaliação de uma condição de relacionamento causal.

O elemento [&lt;simpleAction&gt;](simpleaction.md) possui um atributo *role*, cujo valor
deve ser exclusivo no conjunto de funções do conector. Uma função é uma interface de conector
ponto, que está associado às interfaces dos nós por um link que se refere ao
conector.

Um [&lt;simpleAction&gt;](simpleaction.md) também define um tipo de evento (*eventType*
atributo) e qual ação deve ser aplicada à máquina de estado de evento que ela
refere-se (atributo *actionType*). O *eventType* e
Os valores *actionType* podem ser inferidos pelo valor da função se reservados
palavras são usadas como valores. Caso contrário, *eventType* e
Os atributos *actionType* são obrigatórios.

Valores de função de ação reservada associados a máquinas de estado de evento:
| Valor da função | Tipo de ação | Tipo de Evento |
| --- | --- | --- |
| começar | começar | apresentação |
| parar | parar | apresentação |
| abortar | abortar | apresentação |
| pausa | pausa | apresentação |
| currículo | currículo | apresentação |
| definir | começar | atribuição |

Se um valor *eventType* for "atribuição", o [&lt;simpleAction&gt;](simpleaction.md)deve
defina também o valor a ser atribuído, através do seu *valor*
atributo. Se o *valor* for especificado como "$anyName" (onde "$" é um
símbolo reservado e "anyName" é qualquer string, exceto nomes de funções reservadas),
o valor atribuído é recuperado da propriedade associada ao
*role* "anyName" e definido por um elemento filho [&lt;bind&gt;](bind.md) do
[&lt;link&gt;](link.md) elemento que faz referência ao conector.  Se este valor não puder ser
recuperado, nenhuma atribuição é feita.  Este é o único caso possível de
[&lt;bind&gt;](bind.md) elemento referente a uma função que não está explicitamente declarada em um
conector.

A cardinalidade da função especifica o valor mínimo (atributo *min*) e
número máximo (atributo *max*) de participantes que podem jogar o
função (ou seja, o número de ligações) quando o [&lt;causalConnector&gt;](causalconnector.md) é usado
para criar um [&lt;link&gt;](link.md). Se o valor máximo for maior que um, o
O atributo *qualificador* pode ser especificado informando a lógica
relação entre as ligações de ação simples: "par" ou "seq". Quando o
qualificador sequencial "seq" é usado, as ações devem ser disparadas no especificado
ordem. Entretanto, uma ação não precisa esperar que a anterior seja
terminou para ser demitido. Quando o qualificador paralelo "par" é usado,
as ações podem ser executadas em qualquer ordem.

Um atributo *delay* também pode ser definido para um [&lt;simpleAction&gt;](simpleaction.md),
especificando que a ação deve ser disparada somente após esperar pelo
tempo especificado.

O [&lt;simpleAction&gt;](simpleaction.md) também pode definir um atributo *repeat* para ser
atribuído ao atributo *repetições* do evento, e um
*repeatDelay* a ser esperado antes de repetir a ação.

O elemento [&lt;simpleAction&gt;](simpleaction.md) também pode definir a duração e por
atributos se seu valor *eventType* for "atribuição" e somente se o
propriedade referida define valores numéricos ou cores. Ao definir um novo
valor para uma propriedade a mudança é instantânea por padrão (*duração*
é 0), mas a mudança também pode ser realizada durante um período explicitamente declarado
duração, especificada pelo atributo *duration*. A mudança do
valor antigo para o novo pode ser linear por padrão (*by* é
"indefinido"), ou realizado passo a passo, no ritmo especificado pelo
*por* atributo.

### Sintaxe { data-search-exclude }

| Elemento | Atributos | Conteúdo | Pai |
| --- | --- | --- | --- |
| [&lt;simpleAction&gt;](simpleaction.md) | <u>*role*</u>, *atraso*, *eventType*, *actionType*, *valor*, *min*, *max*, *qualificador*, *repeat*, *repeatDelay*, *duração*, *por* | -- | [&lt;causalConnector&gt;](causalconnector.md) ou [&lt;compoundAction&gt;](compoundaction.md) |

### Atributos { data-search-exclude }

| Nome | Valor | Descrição |
| --- | --- | --- |
| *papel* | Corda. | O atributo *role* define um ponto de interface do conector, que está associado às interfaces dos nós por um link que se refere ao conector.  O valor *role* deve ser exclusivo dentro do conjunto de funções do conector. |
| *atraso* | <p>O atributo *delay* deve ser especificado de acordo com um dos seguintes sintaxe:</p><ol><li class="level1"><div class="li"><"<nowiki>Horas:Minutos:Segundos.Fraction</nowiki>">, onde "Horas" é um número inteiro em \[0,23\] intervalo, "Minutos" é um número inteiro no intervalo \[0,59\], "Segundos" é um número inteiro no intervalo 0,59 e "Fração" é um valor positivo inteiro,</div></li><li class="level1"><div class="li">Seconds<"s">, onde "Segundos" é um real positivo number.</div></li></ol><p>O valor padrão é "0s".</p> | O atributo *delay* define um atraso de tempo a ser aguardado antes de acionar a ação |
| *tipodeevento* | "apresentação", "seleção" ou "atribuição". | O atributo *eventType* identifica o tipo de evento para a ação ou condição. |
| *actionType* | "iniciar", "parar", "abortar", "pausar" ou "continuar". | O atributo *actionType* especifica a ação para acionar a transição correspondente na máquina de estado do evento referido. |
| *valor* | Corda | O atributo *value* define um valor a ser definido para a propriedade vinculada à ação simples de atribuição. |
| *min* | <p>Inteiro positivo menor ou igual ao valor *max*.</p><p>O valor padrão é 1.</p> | O atributo *min* define o número mínimo de participantes que podem desempenhar a função. |
| *máx* | <p>Inteiro positivo maior ou igual ao valor *min* ou ao valor "ilimitado".</p><p>O valor padrão é 1.</p> | O atributo *max* define o número máximo de participantes que podem desempenhar a função. |
| *qualificatória* | "seq" ou "par".  O valor padrão é "par". | O atributo *qualifier* define a ordem em que as ações devem ser aplicadas nos vínculos de ação simples. |
| *repetir* | Inteiro positivo.  O valor padrão é 0 | O atributo *repeat* define um valor a ser atribuído ao atributo de repetições do evento definido no elemento [&lt;simpleAction&gt;](simpleaction.md). |
| *repetirAtraso* | O mesmo que para *atraso*. | O atributo *repeatDelay* especifica um intervalo de tempo a ser esperado antes de repetir a ação. |
| *duração* | O atributo *duration* é especificado como Seconds<"s">, onde "Seconds" é um número real positivo. | O atributo *duration* estabelece o tempo que uma atribuição deve durar ao passar do valor antigo para o novo. |
| *por* | <p>Um número real ou "indefinido".</p><p>O valor padrão é "indefinido".</p> | O atributo *by* estabelece como ocorre a mudança feita por uma ação de atribuição de um valor antigo para o novo: se de forma linear (by é "indefinido") ou realizada passo a passo, com o ritmo especificado pelo atributo *by*. |
