---
title: "Elemento &lt;descriptorSwitch&gt;"
---

### Definição e uso { data-search-exclude }

O elemento [&lt;descriptorSwitch&gt;](../descriptorswitch/) contém um conjunto de alternativas
descritores a serem associados a um objeto.  A escolha é feita durante
horário de apresentação.

As regras de teste usadas para escolher o elemento [&lt;descriptor&gt;](../descriptor/) são definidas por
Elementos [&lt;rule&gt;](../rule/) e [&lt;compositeRule&gt;](../compositerule/); [&lt;bindRule&gt;](../bindrule/) filho
elementos associam essas regras aos elementos filhos [&lt;descriptor&gt;](../descriptor/) do
[&lt;descriptorSwitch&gt;](../descriptorswitch/) elemento.

As regras são avaliadas na ordem em que são definidas.  A primeira regra
avaliado como verdadeiro determina o elemento [&lt;descriptor&gt;](../descriptor/) escolhido.  Se tudo
regras são avaliadas como falsas, um elemento [&lt;descriptor&gt;](../descriptor/) padrão, definido
pelo elemento [&lt;defaultDescriptor&gt;](../defaultdescriptor/), é escolhido; se o
O elemento [&lt;defaultDescriptor&gt;](../defaultdescriptor/) não está definido, nenhum descritor está selecionado
e o player NCL se comporta como se o elemento não existisse.

### Sintaxe { data-search-exclude }

| Elemento | Atributos | Conteúdo | Pai |  |
| --- | --- | --- | --- | --- |
| [&lt;descriptorSwitch&gt;](../descriptorswitch/) | <u>*id*</u> | ([&lt;defaultDescriptor&gt;](../defaultdescriptor/)?, ([&lt;bindRule&gt;](../bindrule/) | [&lt;descriptor&gt;](../descriptor/))*) | [&lt;descriptorBase&gt;](../descriptorbase/) |

### Atributos { data-search-exclude }

| Nome | Valor | Descrição |
| --- | --- | --- |
| *id* | Pode receber qualquer valor de string que comece com uma letra ou sublinhado e que contenha apenas letras, dígitos, <"."> e <"_">. | O atributo *id* identifica exclusivamente o elemento dentro de um documento. |
