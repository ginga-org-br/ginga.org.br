---
title: "Elemento &lt;rule&gt;"
---

### Definição e uso { data-search-exclude }

O elemento [&lt;rule&gt;](rule.md) define regras simples para definir qualquer alternativa
componentes ou descritores alternativos.

O atributo *id* é o identificador da regra.  Uma regra é estabelecida por
comparando (atributo *comparator*) uma variável (atributo *var*)
valor com um valor absoluto.  A variável deve ser uma propriedade do
nó de configurações (elemento [&lt;media&gt;](media.md) do tipo application/x-ncl-settings),
isto é, o atributo *var* deve ter como valor um nome de propriedade de
o elemento [&lt;media&gt;](media.md) do tipo "application/x-ncl-settings".

### Sintaxe { data-search-exclude }

| Elemento | Atributos | Conteúdo | Pai |
| --- | --- | --- | --- |
| [&lt;rule&gt;](rule.md) | *id*, <u>*var*</u>, <u>*comparador*</u>, <u>*valor*</u> | -- | [&lt;ruleBase&gt;](rulebase.md) ou [&lt;compositeRule&gt;](compositerule.md) |

### Atributos { data-search-exclude }

| Nome | Valor | Descrição |
| --- | --- | --- |
| *id* | Pode receber qualquer valor de string que comece com uma letra ou sublinhado e que contenha apenas letras, dígitos, <"."> e <"_">. | O atributo *id* identifica exclusivamente o elemento dentro de um documento. |
| *var* | Pode receber qualquer valor de string que comece com uma letra ou sublinhado e que contenha apenas letras, dígitos, <"."> e <"_">. | O atributo *var* identifica exclusivamente um nome de propriedade do nó de configurações (elemento [&lt;media&gt;](media.md) do tipo "application/x-ncl-settings"). |
| *comparador* | "eq", "ne", "gt", "lt", "gte" ou "lte". | O atributo *comparator* compara o valor da propriedade especificada pelo atributo *var* com o valor absoluto especificado no atributo *value*. |
| *valor* | Corda. | O atributo *value* define um valor a ser comparado com o valor da propriedade referido pelo atributo *var*. |