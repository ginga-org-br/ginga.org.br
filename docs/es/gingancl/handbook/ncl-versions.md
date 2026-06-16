---
title: "Versiones NCL"
---

Las siguientes instrucciones de procesamiento deben estar escritas en un documento NCL. Identifican las solicitudes NCL y la versión NCL a la que se envía el documento. se ajusta.

```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
<ncl id="any string" xmlns="http://www.ncl.org.br/NCL3.0/profileName">
```

Se especifica una versión específica en la ruta URI, donde el número de versión "x.y" se escribe inmediatamente después de "/NCL".

El número de versión de una especificación de documento NCL consta de una número y un número menor, separados por un punto.  Los números están representados como cadenas de caracteres decimales con ceros a la izquierda suprimidos.  la inicial El número de versión estándar es 3.0.

Las nuevas versiones de NCL se publicarán de acuerdo con las siguientes versiones política.  Si los jugadores de NCL que cumplen con versiones anteriores aún pueden recibir una documento basado en la especificación revisada, debido a correcciones de errores, razones operativas, o la adición de una nueva notación de sintaxis concisa ("azúcar de sintaxis") que se puede traducir en tiempo de compilación al antiguo, el se lanzará una nueva versión de NCL con el número menor actualizado.  Si NCL Los reproductores que cumplen con versiones anteriores no pueden recibir un documento basado en las especificaciones revisadas, el número mayor debe actualizarse.

### Perfiles NCL { data-search-exclude }

NCL permite la combinación de sus módulos en perfiles lingüísticos.

Cualquier documento conforme a los perfiles NCL deberá tener el [&lt;ncl&gt;](ncl.md) elemento como su elemento raíz.

```xml
<ncl id="any string" xmlns="http://www.ncl.org.br/NCLx.y/profileName">
```

La cadena "profileName" en la ruta URI identifica el perfil de idioma se utiliza para especificar el documento.  Actualmente, se han elaborado siete perfiles lingüísticos. definido:

  * El *Perfil completo de NCL 3.0*, también llamado //lenguaje NCL 3.0 Perfil//, es el perfil completo del lenguaje NCL 3.0.  eso comprende todos los módulos NCL y proporciona todas las facilidades para la Autoría declarativa de documentos NCL.

  * El *NCL 3.1 Language Profile* extiende la versión 3.0 con un "azúcar sintáctico" para definir relaciones y relaciones.

  * El *NCL 3.0 Raw Profile* tiene la misma expresividad del NCL 3.0 Language Profile, pero sin facilidades de reutilización y con un número mínimo de "azúcares sintácticos".  Tiene el minimo posible número de elementos y atributos aunque manteniendo los mismos expresividad del Perfil Completo.

  * El *Perfil DTV mejorado NCL 3.0 (Perfil EDTV)* apunta a la DTV dominio.  Es el lenguaje declarativo estándar de la Middleware DTV japonés-brasileño ISDB-T<sub>B</sub> para fijo y móvil receptores, y también la Recomendación UIT-T para servicios de IPTV.

  * El *Perfil DTV Básico NCL 3.0 (Perfil BDTV)* es una simplificación del perfil EDTV en el que se incluyen efectos de transición y metadatos. Las funcionalidades son opcionales.  Es el lenguaje declarativo estándar del middleware DTV japonés-brasileño ISDB-T<sub>B</sub> para portátiles receptores.

  * El *Perfil de conector NCL 3.0* permite la creación de conexiones causales y relaciones de restricción que pueden ser importadas por cualquiera de los perfiles listados, excepto el perfil NCL 3.0 Raw.

  * El *NCL 3.0 CausalConnector Profile* es una versión simplificada del Perfil del conector NCL 3.0, que solo permite definir causas relaciones.