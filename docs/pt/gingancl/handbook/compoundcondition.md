---
title: "Elemento &lt;compoundCondition&gt;"
---

### Definição e uso { data-search-exclude }

O elemento [&lt;compoundCondition&gt;](compoundcondition.md) define uma expressão lógica entre seus
elementos filhos por meio de seu atributo booleano *operador*.

Um atributo *delay* também pode ser definido especificando que o composto
condição é verdadeira após um atraso de tempo a partir da expressão relativa ao seu filho
elementos é verdade.

Quando uma condição composta "e" relaciona mais de uma condição de gatilho
(isto é, uma condição que é satisfeita em um tempo infinitesimal
instantâneo – como por exemplo, o final da apresentação de um objeto), o composto
condição será considerada verdadeira no instante imediatamente após todas as
as condições de disparo são satisfeitas.

### Sintaxe { data-search-exclude }

| Elemento | Atributos | Conteúdo | Pai |  |  |
| --- | --- | --- | --- | --- | --- |
| [&lt;compoundCondition&gt;](compoundcondition.md) | <u>*operador*</u>, *atraso* | (([&lt;simpleCondition&gt;](simplecondition.md) | [&lt;compoundCondition&gt;](compoundcondition.md))+,([&lt;assessmentStatement&gt;](assessmentstatement.md) | [&lt;compoundStatement&gt;](compoundstatement.md))*) | [&lt;causalConnector&gt;](causalconnector.md) ou [&lt;compoundCondition&gt;](compoundcondition.md) |

### Atributos { data-search-exclude }

| Nome | Valor | Descrição |
| --- | --- | --- |
| *operador* | "e" ou "ou". | O atributo *operator* define uma expressão lógica entre os elementos filhos [&lt;compoundCondition&gt;](compoundcondition.md). |
| *atraso* | <p>O atributo *delay* deve ser especificado de acordo com um dos seguintes sintaxe:</p><ol><li class="level1"><div class="li"><"<nowiki>Horas:Minutos:Segundos.Fraction</nowiki>">, onde "Horas" é um número inteiro em \[0,23\] intervalo, "Minutos" é um número inteiro no intervalo \[0,59\], "Segundos" é um número inteiro no intervalo 0,59 e "Fração" é um valor positivo inteiro,</div></li><li class="level1"><div class="li">Seconds<"s">, onde "Segundos" é um real positivo number.</div></li></ol><p>O valor padrão é "0s".</p> | O atributo *delay* define que [&lt;compoundCondition&gt;](compoundcondition.md) é verdadeiro após um atraso de tempo da expressão relativa a seus elementos filhos ser verdadeira.
