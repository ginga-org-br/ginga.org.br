---
title: "Elemento &lt;descriptorSwitch&gt;"
---

### Definição e uso { data-search-exclude }

O elemento [&lt;descriptorSwitch&gt;](descriptorswitch.md) contém um conjunto de alternativas
descritores a serem associados a um objeto.  A escolha é feita durante
horário de apresentação.

As regras de teste usadas para escolher o elemento [&lt;descriptor&gt;](descriptor.md) são definidas por
Elementos [&lt;rule&gt;](rule.md) e [&lt;compositeRule&gt;](compositerule.md); [&lt;bindRule&gt;](bindrule.md) filho
elementos associam essas regras aos elementos filhos [&lt;descriptor&gt;](descriptor.md) do
[&lt;descriptorSwitch&gt;](descriptorswitch.md) elemento.

As regras são avaliadas na ordem em que são definidas.  A primeira regra
avaliado como verdadeiro determina o elemento [&lt;descriptor&gt;](descriptor.md) escolhido.  Se tudo
regras são avaliadas como falsas, um elemento [&lt;descriptor&gt;](descriptor.md) padrão, definido
pelo elemento [&lt;defaultDescriptor&gt;](defaultdescriptor.md), é escolhido; se o
O elemento [&lt;defaultDescriptor&gt;](defaultdescriptor.md) não está definido, nenhum descritor está selecionado
e o player NCL se comporta como se o elemento não existisse.

### Sintaxe { data-search-exclude }

| Elemento | Atributos | Conteúdo | Pai |  |
| --- | --- | --- | --- | --- |
| [&lt;descriptorSwitch&gt;](descriptorswitch.md) | <u>*id*</u> | ([&lt;defaultDescriptor&gt;](defaultdescriptor.md)?, ([&lt;bindRule&gt;](bindrule.md) | [&lt;descriptor&gt;](descriptor.md))*) | [&lt;descriptorBase&gt;](descriptorbase.md) |

### Atributos { data-search-exclude }

| Nome | Valor | Descrição |
| --- | --- | --- |
| *id* | Pode receber qualquer valor de string que comece com uma letra ou sublinhado e que contenha apenas letras, dígitos, <"."> e <"_">. | O atributo *id* identifica exclusivamente o elemento dentro de um documento. |
