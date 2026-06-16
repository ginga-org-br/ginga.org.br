---
title: "Elemento &lt;ncl&gt;"
---

### Definición y uso { data-search-exclude }

El elemento [&lt;ncl&gt;](ncl.md) representa la raíz de un documento NCL.

El elemento [&lt;ncl&gt;](ncl.md) es el contenedor de todos los demás elementos NCL (excepto
la declaración <?xml>).

### Sintaxis { data-search-exclude }

| Elemento | Atributos | Contenido | Padre |
| --- | --- | --- | --- |
| [&lt;ncl&gt;](ncl.md) | <u>*id*</u>, *título*, *xmlns* | ([&lt;head&gt;](head.md)?, [&lt;body&gt;](body.md)?) | -- |

### Atributos { data-search-exclude }

| Nombre | Valor | Descripción |
| --- | --- | --- |
| *identificación* | Puede recibir cualquier valor de cadena que comience con una letra o un guión bajo y que solo contenga letras, dígitos, <"."> y <"_">. | El atributo *id* identifica de forma única el elemento dentro de un documento. |
| *título* | Cadena. | El atributo *title* contiene información de asesoramiento.  Los valores del atributo *title* pueden ser representados por agentes de usuario de diversas formas. |
| *xmlns* | "http://www.ncl.org.br/NCL3.0/EDTVProfile" o "http://www.ncl.org.br/NCL3.0/BDTVProfile" | El atributo xmlns declara un espacio de nombres XML; en otras palabras, declara la colección principal de construcciones definidas por XML que utiliza el documento. El valor del atributo es la URL que identifica dónde se define oficialmente el espacio de nombres. Se permiten dos valores para el atributo *xmlns*: "http://www.ncl.org.br/NCL3.0/EDTVProfile" y "http://www.ncl.org.br/NCL3.0/BDTVProfile", para los perfiles DTV Mejorado y Básico, respectivamente. Un jugador NCL deberá saber que la ubicación del esquema para estos espacios de nombres es, respectivamente: "http://www.ncl.org.br/NCL3.0/profiles/NCL30EDTV.xsd" y "http://www.ncl.org.br/NCL3.0/profiles/NCL30BDTV.xsd". |