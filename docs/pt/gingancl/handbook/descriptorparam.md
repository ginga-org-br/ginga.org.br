---
title: "Elemento &lt;descriptorParam&gt;"
---

### Definição e uso { data-search-exclude }

Os elementos [&lt;descriptorParam&gt;](descriptorparam.md) definem valores iniciais para propriedades de
um elemento [&lt;media&gt;](media.md). A propriedade é identificada no *nome*
atributo do elemento [&lt;descriptorParam&gt;](descriptorparam.md) e o valor é definido em
o atributo *valor*.

### Sintaxe { data-search-exclude }

| Elemento | Atributos | Conteúdo | Pai |
| --- | --- | --- | --- |
| [&lt;descriptorParam&gt;](descriptorparam.md) | <u>*nome*</u>, <u>*valor*</u> | -- | [&lt;descriptor&gt;](descriptor.md) |

### Atributos { data-search-exclude }

| Nome | Valor | Descrição |
| --- | --- | --- |
| *nome* | Pode receber qualquer valor de string que comece com uma letra ou sublinhado e que contenha apenas letras, dígitos, <"."> e <"_">. | O atributo *name* identifica a propriedade do elemento [&lt;media&gt;](media.md) que se refere ao elemento [&lt;descriptor&gt;](descriptor.md) pai do elemento [&lt;descriptorParam&gt;](descriptorparam.md). |
| *valor* | Depende do valor *nome*. | O atributo *value* define um valor inicial para a propriedade identificada no atributo *name*. |