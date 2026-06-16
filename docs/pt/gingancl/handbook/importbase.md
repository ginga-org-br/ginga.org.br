---
title: "Elemento &lt;importBase&gt;"
---

### Definição e uso { data-search-exclude }

O elemento [&lt;importBase&gt;](../importbase/) permite incorporar uma base de entidade
(representado por [&lt;connectorBase&gt;](../connectorbase/), [&lt;regionBase&gt;](../regionbase/),
[&lt;descriptorBase&gt;](../descriptorbase/), [&lt;ruleBase&gt;](../rulebase/) ou [&lt;transitionBase&gt;](../transitionbase/)
elementos definidos em um documento externo) para outro já definido
básico. ItsdocumentURIattribute refere-se a um URI correspondente ao NCL
documento contendo a base a ser importada. O atributo alias especifica um
nome a ser usado como prefixo quando se referir a elementos deste importado
básico. A referência deve ter o formato: <nowiki>alias#element_id</nowiki>.

A operação de importação é transitiva, ou seja, se a baseA importa a baseB que
importa baseC, então baseA importa baseC. No entanto, o alias definido para
baseC dentro de baseB não é considerada por baseA.

As seguintes restrições devem ser satisfeitas:

* o elemento [&lt;descriptorBase&gt;](../descriptorbase/) pode ter um filho [&lt;importBase&gt;](../importbase/)
    elemento referente a um URI correspondente a outro documento NCL
    contendo a base do descritor a ser importada e aninhada. Quando um
    base de descritores é importada, a base de região, a base de transição e
    a base de regras, quando presentes no documento importado, também são
    importado automaticamente para a região correspondente e bases de regras do
    documento de importação;
  * o elemento [&lt;connectorBase&gt;](../connectorbase/) pode ter um filho [&lt;importBase&gt;](../importbase/)
    elemento referente a uma URI correspondente a outra base de conector a ser
    importado e aninhado;
  * o elemento [&lt;transitionBase&gt;](../transitionbase/) pode ter um filho [&lt;importBase&gt;](../importbase/)
    elemento referente a um URI correspondente a outra base de transição para
    ser importado e aninhado;
  * o elemento [&lt;ruleBase&gt;](../rulebase/) pode ter um elemento filho [&lt;importBase&gt;](../importbase/)
    referindo-se a um URI correspondente a outro documento NCL contendo o
    base de regras a ser importada e aninhada;
  * o elemento [&lt;regionBase&gt;](../regionbase/) pode ter um elemento filho [&lt;importBase&gt;](../importbase/)
    referindo-se a um URI correspondente a outro documento NCL contendo o
    base de região a ser importada e aninhada. Como o referido URI do documento pode
    possuir mais de uma base regional, a base a ser importada deverá ser
    identificado atribuindo seu idvalue ao atributo baseId do
    [&lt;importBase&gt;](../importbase/) elemento. Ao importar um [&lt;regionBase&gt;](../regionbase/), um
    o atributo denominado região pode ser especificado em [&lt;importBase&gt;](../importbase/)
    elemento. Quando presente, este atributo identifica o id de um
    Elemento [&lt;region&gt;](../region/) declarado em um elemento [&lt;regionBase&gt;](../regionbase/) do
    documento host (o documento que faz a operação de importação). Como um
    consequência, todos os elementos filhos [&lt;region&gt;](../region/) do importado
    [&lt;regionBase&gt;](../regionbase/) será considerado como elemento filho [&lt;region&gt;](../region/) de
    a região referida pelo atributo de região de [&lt;importBase&gt;](../importbase/). Se não
    especificado, os elementos filhos [&lt;region&gt;](../region/) do importado
    [&lt;regionBase&gt;](../regionbase/) serão considerados filhos diretos do anfitrião
    elemento do documento [&lt;regionBase&gt;](../regionbase/).

### Sintaxe { data-search-exclude }

| Elemento | Atributos | Conteúdo | Pai |
| --- | --- | --- | --- |
| [&lt;importBase&gt;](../importbase/) | <u>*alias*</u>, <u>*documentURI*</u>, *região*, *baseId* | -- | [&lt;ruleBase&gt;](../rulebase/) ou [&lt;transitionBase&gt;](../transitionbase/) ou [&lt;regionBase&gt;](../regionbase/) ou [&lt;descriptorBase&gt;](../descriptorbase/) ou [&lt;connectorBase&gt;](../connectorbase/) |

### Atributos { data-search-exclude }

| Nome | Valor | Descrição |
| --- | --- | --- |
| *alias* | Pode receber qualquer valor de string que comece com uma letra ou sublinhado e que contenha apenas letras, dígitos, <"."> e <"_">. | O atributo *alias* especifica um nome a ser utilizado como prefixo quando se referir a elementos da base importada.  O valor *alias* deve ser exclusivo em um documento e seu escopo é restrito ao documento que definiu o atributo alias. |
| *documentURI* | URI. | O atributo *documentURI* é o localizador do documento NCL de onde a base ou documento será importado. |
| *região* | IDREF. | O atributo *region* pode ser usado ao importar um [&lt;regionBase&gt;](../regionbase/).  Ele identifica um elemento [&lt;region&gt;](../region/) do documento de importação que aninhará (será a região pai) todos os elementos [&lt;region&gt;](../region/) importados. |
| *baseId* | IDREF. | O atributo *baseId* pode ser usado ao importar um [&lt;regionBase&gt;](../regionbase/).  Define o elemento [&lt;regionBase&gt;](../regionbase/) a ser importado através do seu valor *id*. |