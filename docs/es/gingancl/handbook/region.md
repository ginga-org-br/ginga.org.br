---
title: "Elemento &lt;region&gt;"
---

### Definición y uso { data-search-exclude }

El elemento [&lt;region&gt;](region.md) define los valores iniciales para los lados izquierdo, derecho,
Propiedades superior, inferior, altura, ancho y zIndex de un elemento [&lt;media&gt;](media.md)
que indirectamente se refiere a él mediante el uso de un elemento [&lt;descriptor&gt;](descriptor.md).

La posición de una región, según lo especificado por su *arriba*, *abajo*,
Los atributos *left* y *right* siempre son relativos al padre.
geometría, que está definida por el elemento principal [&lt;region&gt;](region.md), o el total
área del dispositivo en el caso de regiones del primer nivel de anidación.

Los atributos *arriba* y *izquierda* son la región principal
atributos de posicionamiento.  Colocan la esquina superior izquierda de la región en el
distancia especificada desde el borde superior izquierdo de la región principal (o el
borde superior izquierdo del dispositivo en el caso de la región más externa).  A veces,
establecer explícitamente los atributos *inferior* y *derecha* es
útil.  Sus valores indican la distancia entre el extremo derecho de la región
esquina y la esquina inferior derecha de la región principal (o el dispositivo
borde inferior derecho en el caso de la región más externa).

![](/assets/region.png)

Las regiones secundarias no pueden permanecer fuera del área establecida por sus padres
regiones.

El atributo *zIndex* especifica la precedencia de superposición de regiones,
donde las regiones con mayores valores *zIndex* se apilan encima de
regiones con valores *zIndex* más pequeños.

### Sintaxis { data-search-exclude }

| Elemento | Atributos | Contenido | Padre |
| --- | --- | --- | --- |
| [&lt;region&gt;](region.md) | <u>*id*</u>, *título*, *izquierda*, *derecha*, *arriba*, *abajo*, *alto*, *ancho*, *zIndex* | ([&lt;region&gt;](region.md))* | [&lt;regionBase&gt;](regionbase.md) o [&lt;region&gt;](region.md) |

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
