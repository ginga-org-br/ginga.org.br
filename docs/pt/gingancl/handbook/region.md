---
title: "Elemento &lt;region&gt;"
---

### Definição e uso { data-search-exclude }

O elemento [&lt;region&gt;](region.md) define os valores iniciais para a esquerda, direita,
Propriedades superior, inferior, altura, largura e zIndex de um elemento [&lt;media&gt;](media.md)
que indiretamente se refere a ele usando um elemento [&lt;descriptor&gt;](descriptor.md).

A posição de uma região, conforme especificado por seu *top*, *bottom*,
Os atributos *left* e *right* são sempre relativos ao pai
geometria, que é definida pelo elemento pai [&lt;region&gt;](region.md) ou pelo total
área do dispositivo no caso de regiões de primeiro nível de aninhamento.

Os atributos *top* e *left* são a região primária
atributos de posicionamento.  Eles colocam o canto superior esquerdo da região no
distância especificada da borda superior esquerda da região pai (ou do
borda superior esquerda do dispositivo no caso da região mais externa).  Às vezes,
definir explicitamente os atributos *bottom* e *right* é
útil.  Seus valores indicam a distância entre o canto inferior direito da região
canto e o canto inferior direito da região pai (ou o dispositivo
borda inferior direita no caso da região ultraperiférica).

![](/assets/region.png)

As regiões filhas não podem ficar fora da área estabelecida pelos seus pais
regiões.

O atributo *zIndex* especifica a precedência da superposição da região,
onde regiões com valores maiores de *zIndex* são empilhadas em cima de
regiões com valores menores de *zIndex*.

### Sintaxe { data-search-exclude }

| Elemento | Atributos | Conteúdo | Pai |
| --- | --- | --- | --- |
| [&lt;region&gt;](region.md) | <u>*id*</u>, *título*, *esquerda*, *direita*, *superior*, *inferior*, *altura*, *largura*, *zIndex* | ([&lt;region&gt;](region.md))* | [&lt;regionBase&gt;](regionbase.md) ou [&lt;region&gt;](region.md) |

### Atributos { data-search-exclude }

| Name | Value | Description |
| --- | --- | --- |
| *id* | It may receive any string value that begins with a letter or an underscore and that only contains letters, digits, <".">, and <"_">. | The *id* attribute uniquely identifies the element within a document. |
| *title* | String. | The *title* attribute contains advisory information.  Values of the *title* attribute may be rendered by user agents in a variety of ways. |
| *left* | <p>A real number in the range \[0,100\] ending with the character <"%"> (e.g. "30%"), or a positive integer specifying the attribute value in pixels.  For pixel values, the "px" unit qualifier may be omitted.</p><p>The default value is "0%", if the attribute value cannot be computed from the *width* and *right* attributes.</p> | Left position of the content relative to its parent region (or the device in the case of the outermost region), expressed as a percentage of the parent region *width* dimension (or the device width in the case of the outermost region), or as an absolute value.It places the left position of the region in the specified distance away from the left edge of the parent region (or the device left edge in the case of the outermost region). |
| *right* | <p>A real number in the range \[0,100\] ending with the character <"%"> (e.g. "30%"), or a positive integer specifying the attribute value in pixels.  For pixel values, the "px" unit qualifier may be omitted.</p><p>The default value is "0%", if the attribute value cannot be computed from the *width* and *left* attributes.</p> | Right position of the content relative to its parent region (or the device in the case of the outermost region), expressed as a percentage of the parent region *width* dimension (or the device width in the case of the outermost region), or as an absolute value.It places the right position of the region in the specified distance away from the right edge of the parent region (or the device right edge in the case of the outermost region). |
| *top* | <p>A real number in the range \[0,100\] ending with the character <"%"> (e.g. "30%"), or a positive integer specifying the attribute value in pixels.  For pixel values, the "px" unit qualifier may be omitted.</p><p>The default value is "0%", if the attribute value cannot be computed from the *height* and *bottom* attributes.</p> | Top position of the content relative to its parent region (or the device in the case of the outermost region), expressed as a percentage of the parent region *height* dimension (or the device height in the case of the outermost region), or as an absolute value.It places the top position of the region in the specified distance away from the top edge of the parent region (or the device top edge in the case of the outermost region). |
| *bottom* | <p>A real number in the range \[0,100\] ending with the character <"%"> (e.g. "30%"), or a positive integer specifying the attribute value in pixels.  For pixel values, the "px" unit qualifier may be omitted.</p><p>The default value is "0%", if the attribute value cannot be computed from the *height* and *top* attributes.</p> | Bottom position of the content relative to its parent region (or the device in the case of the outermost region), expressed as a percentage of the parent region *height* dimension (or the device height in the case of the outermost region), or as an absolute value.It places the bottom position of the region in the specified distance away from the bottom edge of the parent region (or the device bottom edge in the case of the outermost region). |
| *height* | <p>A real number in the range \[0,100\] ending with the character <"%"> (e.g. "30%"), or a positive integer specifying the attribute value in pixels.  For pixel values, the "px" unit qualifier may be omitted.</p><p>The default value is "100%" of the parent region *height* dimension (or the device height in the case of the outermost region).</p> | Height of the content to be exhibited, expressed as a percentage of the parent region *height* dimension (or the device height in the case of the outermost region), or as an absolute value. |
| *width* | <p>A real number in the range \[0,100\] ending with the character <"%"> (e.g. "30%"), or a positive integer specifying the attribute value in pixels.  For pixel values, the "px" unit qualifier may be omitted.</p><p>The default value is "100%" of the parent region *width* dimension (or the device width in the case of the outermost region).</p> | Width of the content to be exhibited, expressed as a percentage of the parent region *width* dimension (or the device width in the case of the outermost region), or as an absolute value. |
| *zIndex* | <p>An integer number in the range \[0,255\].</p><p>The default value is 0.</p> | The *zIndex* attribute specifies the superposition precedence, where objects with greater *zIndex* values are stacked on top of objects with smaller *zIndex* values. |
