---
title: "Elemento &lt;causalConnector&gt;"
---

### Definição e uso { data-search-exclude }

O elemento [&lt;causalConnector&gt;](causalconnector.md) representa uma relação causal que pode ser
usado para criar relacionamentos (elementos [&lt;link&gt;](link.md)) em documentos NCL.  Em
uma relação causal, uma condição deve ser satisfeita para desencadear uma
ação.

Um [&lt;causalConnector&gt;](causalconnector.md) especifica uma relação independentemente de
relacionamentos, ou seja, não especifica quais nós (representados por
[&lt;media&gt;](media.md), [&lt;context&gt;](context.md), [&lt;body&gt;](body.md) e [&lt;switch&gt;](switch.md) elementos) irão
interagir através da relação.  Um elemento [&lt;link&gt;](link.md), por sua vez,
representa um relacionamento do tipo definido pelo seu referido conector,
interconectando diferentes nós.  Links que representam o mesmo tipo de
relação, mas interconectando nós diferentes, pode reutilizar o mesmo conector,
reutilizando todas as suas especificações anteriores.

Um [&lt;causalConnector&gt;](causalconnector.md) define, através de seus elementos filhos, um conjunto de
pontos de interface, chamados de funções.  Um elemento [&lt;link&gt;](link.md) refere-se a um
[&lt;causalConnector&gt;](causalconnector.md) e define um conjunto de vínculos ([&lt;bind&gt;](bind.md) filho
elementos do elemento [&lt;link&gt;](link.md)), que associam cada ponto final do link
(interface do nó) para uma função do referido conector.

As relações na NCL são baseadas em eventos.  Um evento NCL é uma ocorrência no tempo
que pode ser instantâneo ou ter uma duração mensurável.  Cada evento define
uma máquina de estado mantida pelo player NCL (veja a Figura 1).
Além disso, todo evento possui um atributo associado, denominado
*ocorrências*, que conta quantas vezes o evento transita de
ocorrendo ao estado de hibernação durante a apresentação de um documento.  Eventos de
tipos de apresentação e atribuição também têm um atributo chamado
*repetições*, que conta quantas vezes o evento será
reiniciado automaticamente (passado do estado de suspensão para o estado de ocorrência) pelo
Jogador NCL.  Este atributo pode conter o valor "indefinido", levando a
um loop infinito de ocorrências de eventos até alguma interrupção externa.

![Figure 1: Event state machine.](/assets/state-machine.png)

O perfil NCL 3.0 EDTV define os seguintes tipos de eventos:

- evento de apresentação: definido pela apresentação de um subconjunto de
    unidades de informação do conteúdo de um objeto de mídia.  Os eventos de apresentação são
    especificado em NCL em elementos [&lt;area&gt;](area.md) ou nos próprios nós de mídia
    (em todas as âncoras de conteúdo).  Eventos de apresentação também podem ser
    definido em nós compostos (representados por [&lt;body&gt;](body.md), [&lt;context&gt;](context.md),
    ou [&lt;switch&gt;](switch.md) elementos), representando a apresentação de informações
    unidades de qualquer nó dentro do nó composto);

- evento de seleção: definido pela seleção de um subconjunto de informações
    unidades do conteúdo de um objeto de mídia sendo apresentadas.  Os eventos de seleção são
    especificado em NCL em elementos [&lt;area&gt;](area.md) ou nos próprios nós de mídia
    (em todas as âncoras de conteúdo);

- evento de atribuição: definido pela atribuição de um valor a um imóvel
    de um nó (representado por [&lt;media&gt;](media.md), [&lt;body&gt;](body.md) ou [&lt;context&gt;](context.md)
    elemento), que deve ser declarado em um elemento filho [&lt;property&gt;](property.md) de
    o nó; e

  - evento de composição: definido pela apresentação da estrutura de um
    nó composto (representado por um [&lt;body&gt;](body.md), [&lt;context&gt;](context.md) ou
    [&lt;switch&gt;](switch.md) element).  Composition events are used to present the
    composite map (composite organization).  This functionality is optional
    em perfis EDTV/BDTV.

### Syntax { data-search-exclude }

| Elemento | Atributos | Conteúdo | Pai |  |  |
| --- | --- | --- | --- | --- | --- |
| [&lt;causalConnector&gt;](causalconnector.md) | <u>*id*</u> | ([&lt;connectorParam&gt;](connectorparam.md)*, ([&lt;simpleCondition&gt;](simplecondition.md) | [&lt;compoundCondition&gt;](compoundcondition.md)), ([&lt;simpleAction&gt;](simpleaction.md) | [&lt;compoundAction&gt;](compoundaction.md))) | [&lt;connectorBase&gt;](connectorbase.md) |

### Attributes { data-search-exclude }

| Nome | Valor | Descrição |
| --- | --- | --- |
| *id* | Pode receber qualquer valor de string que comece com uma letra ou sublinhado e que contenha apenas letras, dígitos, <"."> e <"_">. | O atributo *id* identifica exclusivamente o elemento dentro de um documento. |
