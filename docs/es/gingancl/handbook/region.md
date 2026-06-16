---
title: "Elemento &lt;region&gt;"
---

# &lt;region&gt;

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

| Nombre | Valor | Descripción |
| --- | --- | --- |
| *id* | Puede recibir cualquier valor de cadena que comience con una letra o un guión bajo y que solo contenga letras, dígitos, <"."> y <"_">. | El atributo *id* identifica de forma única al elemento dentro de un documento. |
| *title* | Cadena. | El atributo *title* contiene información consultiva. Los valores del atributo *title* pueden ser representados por los agentes de usuario de diversas maneras. |
| *left* | <p>Un número real en el rango \[0,100\] que termina con el carácter <"%"> (por ejemplo, "30%"), o un entero positivo que especifica el valor del atributo en píxeles. Para valores en píxeles, el calificador de unidad "px" puede omitirse.</p><p>El valor predeterminado es "0%", si el valor del atributo no puede calcularse a partir de los atributos *width* y *right*.</p> | Posición izquierda del contenido en relación con su región padre (o el dispositivo en el caso de la región más externa), expresada como un porcentaje de la dimensión *width* de la región padre (o el ancho del dispositivo en el caso de la región más externa), o como un valor absoluto. Coloca la posición izquierda de la región a la distancia especificada desde el borde izquierdo de la región padre (o el borde izquierdo del dispositivo en el caso de la región más externa). |
| *right* | <p>Un número real en el rango \[0,100\] que termina con el carácter <"%"> (por ejemplo, "30%"), o un entero positivo que especifica el valor del atributo en píxeles. Para valores en píxeles, el calificador de unidad "px" puede omitirse.</p><p>El valor predeterminado es "0%", si el valor del atributo no puede calcularse a partir de los atributos *width* y *left*.</p> | Posición derecha del contenido en relación con su región padre (o el dispositivo en el caso de la región más externa), expresada como un porcentaje de la dimensión *width* de la región padre (o el ancho del dispositivo en el caso de la región más externa), o como un valor absoluto. Coloca la posición derecha de la región a la distancia especificada desde el borde derecho de la región padre (o el borde derecho del dispositivo en el caso de la región más externa). |
| *top* | <p>Un número real en el rango \[0,100\] que termina con el carácter <"%"> (por ejemplo, "30%"), o un entero positivo que especifica el valor del atributo en píxeles. Para valores en píxeles, el calificador de unidad "px" puede omitirse.</p><p>El valor predeterminado es "0%", si el valor del atributo no puede calcularse a partir de los atributos *height* y *bottom*.</p> | Posición superior del contenido en relación con su región padre (o el dispositivo en el caso de la región más externa), expresada como un porcentaje de la dimensión *height* de la región padre (o la altura del dispositivo en el caso de la región más externa), o como un valor absoluto. Coloca la posición superior de la región a la distancia especificada desde el borde superior de la región padre (o el borde superior del dispositivo en el caso de la región más externa). |
| *bottom* | <p>Un número real en el rango \[0,100\] que termina con el carácter <"%"> (por ejemplo, "30%"), o un entero positivo que especifica el valor del atributo en píxeles. Para valores en píxeles, el calificador de unidad "px" puede omitirse.</p><p>El valor predeterminado es "0%", si el valor del atributo no puede calcularse a partir de los atributos *height* y *top*.</p> | Posición inferior del contenido en relación con su región padre (o el dispositivo en el caso de la región más externa), expresada como un porcentaje de la dimensión *height* de la región padre (o la altura del dispositivo en el caso de la región más externa), o como un valor absoluto. Coloca la posición inferior de la región a la distancia especificada desde el borde inferior de la región padre (o el borde inferior del dispositivo en el caso de la región más externa). |
| *height* | <p>Un número real en el rango \[0,100\] que termina con el carácter <"%"> (por ejemplo, "30%"), o un entero positivo que especifica el valor del atributo en píxeles. Para valores en píxeles, el calificador de unidad "px" puede omitirse.</p><p>El valor predeterminado es "100%" de la dimensión *height* de la región padre (o la altura del dispositivo en el caso de la región más externa).</p> | Altura del contenido a exhibir, expresada como un porcentaje de la dimensión *height* de la región padre (o la altura del dispositivo en el caso de la región más externa), o como un valor absoluto. |
| *width* | <p>Un número real en el rango \[0,100\] que termina con el carácter <"%"> (por ejemplo, "30%"), o un entero positivo que especifica el valor del atributo en píxeles. Para valores en píxeles, el calificador de unidad "px" puede omitirse.</p><p>El valor predeterminado es "100%" de la dimensión *width* de la región padre (o el ancho del dispositivo en el caso de la región más externa).</p> | Ancho del contenido a exhibir, expresado como un porcentaje de la dimensión *width* de la región padre (o el ancho del dispositivo en el caso de la región más externa), o como un valor absoluto. |
| *zIndex* | <p>Un número entero en el rango \[0,255\].</p><p>El valor predeterminado es 0.</p> | El atributo *zIndex* especifica la precedencia de superposición, donde los objetos con mayores valores de *zIndex* se apilan encima de los objetos con menores valores de *zIndex*. |
