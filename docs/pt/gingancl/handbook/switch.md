---
title: "Elemento &lt;switch&gt;"
---

### Definição e uso { data-search-exclude }

O elemento [&lt;switch&gt;](switch.md) permite definir objetos alternativos
(representado por [&lt;media&gt;](media.md), [&lt;context&gt;](context.md) ou outro [&lt;switch&gt;](switch.md)
elementos) a serem apresentados.  A escolha é feita no momento da apresentação.

As regras de teste utilizadas para escolher o componente filho do switch a ser apresentado são
definido pelos elementos [&lt;rule&gt;](rule.md) e [&lt;compositeRule&gt;](compositerule.md); [&lt;bindRule&gt;](bindrule.md)
elementos filhos associam essas regras a objetos componentes filhos do
[&lt;switch&gt;](switch.md) elemento.

Um elemento filho [&lt;switchPort&gt;](switchport.md) pode definir um mapeamento para um subconjunto do
componentes filhos do switch.  Quando um link está vinculado a um [&lt;switchPort&gt;](switchport.md)
elemento, as regras vinculadas aos componentes mapeados são avaliadas na ordem em que
são definidos.  A primeira regra avaliada como verdadeira determina o objeto escolhido.
Se todas as regras vinculadas aos componentes mapeados forem avaliadas como falsas, um padrão
o componente, definido pelo elemento filho [&lt;defaultComponent&gt;](defaultcomponent.md), é escolhido; se
o elemento [&lt;defaultComponent&gt;](defaultcomponent.md) não está definido, nenhum componente está selecionado
para apresentação e o player NCL se comporta como se o componente selecionado
não existe.

Todas as referências ao componente filho de um switch são feitas através
[&lt;switchPort&gt;](switchport.md) elementos ou, por padrão, para o elemento [&lt;switch&gt;](switch.md)
sem especificar nenhum [&lt;switchPort&gt;](switchport.md).  Neste caso, é considerado como
se a referência for feita a um [&lt;switchPort&gt;](switchport.md) padrão que contém
mapeando elementos para cada objeto filho do switch e referindo-se ao seu
âncora de todo o conteúdo.

A partir do momento em que um [&lt;switch&gt;](switch.md) é avaliado, ele é considerado resolvido
até o final da apresentação do switch atual.

O elemento [&lt;switch&gt;](switch.md) pode referir-se a outro elemento [&lt;switch&gt;](switch.md).  Em
neste caso, possui a mesma especificação do referido elemento.

### Sintaxe { data-search-exclude }

| Elemento | Atributos | Conteúdo | Pai |
| --- | --- | --- | --- |
| [&lt;switch&gt;](switch.md) | <u>*id*</u>, *consulte* | ([&lt;defaultComponent&gt;](defaultcomponent.md)?, ([&lt;switchPort&gt;](switchport.md) &#124; [&lt;bindRule&gt;](bindrule.md) &#124; [&lt;media&gt;](media.md) &#124; [&lt;context&gt;](context.md) &#124; [&lt;switch&gt;](switch.md))*) | [&lt;body&gt;](body.md), [&lt;context&gt;](context.md) ou [&lt;switch&gt;](switch.md) |

### Atributos { data-search-exclude }

| Nome | Valor | Descrição |
| --- | --- | --- |
| *id* | Pode receber qualquer valor de string que comece com uma letra ou sublinhado e que contenha apenas letras, dígitos, <"."> e <"_">. | O atributo *id* identifica exclusivamente o elemento dentro de um documento. |
| *consulte* | IDREF ou a string "alias#id" onde "id" é um valor IDREF. | <p>O atributo *refer* refere-se a um elemento *id* que será reutilizado.  Um elemento que se refere a outro elemento não pode ser reutilizado; isto é, seu *id* não pode ser reutilizado; isto é, seu *id* não pode ser o valor de nenhum atributo *refer*.  O elemento referido deve ser um elemento [&lt;switch&gt;](switch.md).</p><p>O elemento referido e o elemento que se refere a ele devem ser considerados iguais apenas em relação à especificação de seus dados.</p><p>Se o nó referido for definido em um documento D importado, o valor do atributo *refer* deverá ter o formato "alias#id", onde "alias" é o valor do atributo *alias* associado ao componente importado D.</p> |
