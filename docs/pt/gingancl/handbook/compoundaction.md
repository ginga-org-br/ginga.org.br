---
title: "Elemento &lt;compoundAction&gt;"
---

### Definição e uso { data-search-exclude }

O elemento [&lt;compoundAction&gt;](compoundaction.md) define uma expressão lógica entre seus
elementos filhos ([&lt;simpleAction&gt;](simpleaction.md), [&lt;compoundAction&gt;](compoundaction.md)) por meio de um
atributo do operador que pode receber o valor "par" ou "seq".

Ações compostas paralelas ("par") e sequenciais ("seq") especificam que o
a execução das ações será realizada em qualquer ordem ou em uma ordem específica,
respectivamente.  Quando o operador sequencial é utilizado, as ações devem ser disparadas
na ordem especificada.  Entretanto, uma ação não precisa esperar o
anterior para ser concluído.

Um atributo *delay* também pode ser definido especificando que o composto
a ação deve ser aplicada após o atraso especificado.

### Sintaxe { data-search-exclude }

| Elemento | Atributos | Conteúdo | Pai |  |
| --- | --- | --- | --- | --- |
| [&lt;compoundAction&gt;](compoundaction.md) | <u>*operador*</u>, *atraso* | ([&lt;simpleAction&gt;](simpleaction.md) | [&lt;compoundAction&gt;](compoundaction.md))+ | [&lt;causalConnector&gt;](causalconnector.md) ou [&lt;compoundAction&gt;](compoundaction.md) |

### Atributos { data-search-exclude }

| Nome | Valor | Descrição |
| --- | --- | --- |
| *operador* | "seq" ou "par". O valor padrão é "par". | O *operador* define a ordem em que as ações devem ser aplicadas nos elementos filhos [&lt;compoundAction&gt;](compoundaction.md). |
| *atraso* | <p>O atributo *delay* deve ser especificado de acordo com um dos seguintes sintaxe:</p><ol><li class="level1"><div class="li"><"<nowiki>Horas:Minutos:Segundos.Fraction</nowiki>">, onde "Horas" é um número inteiro em \[0,23\] intervalo, "Minutos" é um número inteiro no intervalo \[0,59\], "Segundos" é um número inteiro no intervalo 0,59 e "Fração" é um valor positivo inteiro,</div></li><li class="level1"><div class="li">Seconds<"s">, onde "Segundos" é um real positivo number.</div></li></ol><p>O valor padrão é "0s".</p> | O atributo *delay* define um atraso de tempo a ser esperado antes de acionar o [&lt;compoundAction&gt;](compoundaction.md) |
