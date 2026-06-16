---
title: Sobre Ginga-NCL
---

Ginga-NCL es el subsistema Ginga encargado de la presentación de documentos NCL y fue desarrollado en la PUC-Rio (Pontificia Universidad Católica de Río de Janeiro). Define un entorno de presentación para aplicaciones declarativas escritas en NCL. NCL es un lenguaje de aplicación XML que proporciona soporte para especificar la sincronización espacio-temporal entre objetos de medios, contenido de medios y alternativas de presentación, exhibición en múltiples dispositivos y producción en vivo de programas interactivos no lineales.

## ¿Qué es NCL?

NCL es el acrónimo de *Lenguaje de contexto anidado*.

NCL es un lenguaje declarativo, de hecho una aplicación XML, que ha sido especificado de forma modular, con el objetivo de combinar sus módulos en un lenguaje perfiles.

Entre los perfiles de NCL se encuentran aquellos dirigidos al dominio DTV.  La flexibilidad de NCL, su función de reutilización, soporte multidispositivo, contenido de aplicaciones y adaptabilidad de la presentación y, principalmente, su soporte intrínseco para facilitar definir la sincronización espacio-temporal entre los activos de los medios, incluidos aquellos provenientes de las interacciones de los espectadores, hacen de NCL una solución excepcional para todos tipos de sistemas DTV interactivos.

NCL es el lenguaje declarativo del middleware DTV japonés-brasileño ISDB-T<sub>B</sub>[^1][^2], y también la Recomendación UIT-T para servicios de IPTV[^3].

NCL tiene una separación más estricta entre el contenido y la estructura de la aplicación. NCL no define ningún contenido multimedia por sí mismo.  En cambio, define el pegamento que mantiene unidos a los medios en presentaciones multimedia.  Así, una NCL documento sólo define cómo se estructuran y relacionan los objetos multimedia en el tiempo y espacio.

Como lenguaje *pegamento*, NCL no restringe ni prescribe ningún tipo de contenido de objeto multimedia.  Los objetos multimedia admitidos dependen del reproductores multimedia integrados en el formateador NCL (el reproductor NCL).

Por lo tanto, podemos tener contenido perceptual, como videos, imágenes, audios y textos, como objetos multimedia NCL.  También podemos tener objetos multimedia con imperativo contenido del código, como código Lua, código ECMAScript, código Java, etc. Además, podemos tener objetos multimedia con contenido de código declarativo, como los basados en HTML código, código SVG, código X3D, código SMIL, código NCL (sí, las aplicaciones NCL incorporan otras aplicaciones NCL), etc. Por lo tanto, NCL no sustituye sino que incorpora aplicaciones de otros lenguajes, relacionando todos los objetos en el tiempo y el espacio en una presentación distribuida en múltiples dispositivos.

## Informes de la PUC-Rio

- Luiz Fernando Gomes Soares.  
    **[Introduction to DTV and to Ginga-NCL](/assets/pdf/Introduction%20to%20DTV%20and%20to%20Ginga-NCL.pdf)** (PDF).  
    Monografías en Ciencia de la Computación, Departamento de Informática, PUC-Rio.

- Luiz Fernando Gomes Soares.  
    **[Part 11 – Declarative Hypermedia Objects in NCL: Nesting Objects with NCL Code in NCL Documents](/assets/pdf/Part%2011%20-%20NCL3.0-DO.pdf)** (PDF).  
    Monografías en Ciencia de la Computación, Departamento de Informática, PUC-Rio, 2009.

- Luiz Fernando Gomes Soares.  
    **[Part 12 – Support to Multiple Exhibition Devices](/assets/pdf/Part%2012%20-%20NCL3.0-MD.pdf)** (PDF).  
    Monografías en Ciencia de la Computación, Departamento de Informática, PUC-Rio, 2009.

- Luiz Fernando Gomes Soares.  
    **[Part 13 - Ginga-NCL Implementors Guide v1.0](https://bib-di.inf.puc-rio.br/techreports/)** (PDF).  
    Monografías en Ciencia de la Computación, Departamento de Informática, PUC-Rio, 2009.

- Luiz Fernando Gomes Soares, Francisco Sant'Anna, Renato Cerqueira.  
    **[Part 10 – Imperative Objects in NCL: The NCLua Scripting Language](/assets/pdf/Part%2010%20-%20NCL3.0-IO.pdf)** (PDF).  
    Monografías en Ciencia de la Computación, Departamento de Informática, PUC-Rio, 2008.

- Luiz Fernando Gomes Soares, Rogério Ferreira Rodrigues.  
    **[Part 8 – NCL (Nested Context Language) Digital TV Profiles](/assets/pdf/Part%208%20-%20NCL3.0-DTV_0.pdf)** (PDF).  
    Monografías en Ciencia de la Computación, Departamento de Informática, PUC-Rio, 2006.

- Luiz Fernando Gomes Soares, Rogério Ferreira Rodrigues, Romualdo Monteiro Resende Costa, Marcio Ferreira Moreno.  
    **[Part 9 – NCL Live Editing Commands](/assets/pdf/Part%209%20-%20NCL3.0-EC.pdf)** (PDF).  
    Monografías en Ciencia de la Computación, Departamento de Informática, PUC-Rio, 2006.

- Luiz Fernando Gomes Soares, Rogério Ferreira Rodrigues.  
    **[Nested Context Model 3.0. Part 1 – NCM Core](/assets/pdf/Part1%20-%20NCM%203.0.pdf)** (PDF).  
    Monografías en Ciencia de la Computación, Departamento de Informática, PUC-Rio, 2005.

- M.T. Medina, C.C. Ribeiro, Luiz Fernando Gomes Soares.  
    **[Automatic Scheduling of Hypermedia Documents with Elastic Times](https://bib-di.inf.puc-rio.br/techreports/)** (PDF).  
    Monografías en Ciencia de la Computación, Departamento de Informática, PUC-Rio, 2001.

- Rogério Ferreira Rodrigues, Bruno Bachelet, Philippe Mahey, Luiz Fernando Gomes Soares.  
    **[Elastic Time Computations for Hypermedia Documents](https://bib-di.inf.puc-rio.br/techreports/)** (PDF).  
    Monografías en Ciencia de la Computación, Departamento de Informática, PUC-Rio, 2001.

- Débora Christina Muchaluat Saade, Sérgio Colcher, Luiz Fernando Gomes Soares.  
    **[Relações de Sincronização Espaço-Temporal Hipermídia Também Merecem Status de Primeira Classe](https://bib-di.inf.puc-rio.br/techreports/)** (PDF).  
    Monografías en Ciencia de la Computación, Departamento de Informática, PUC-Rio, 2001.

- M.F. Felix, Edward Hermann Haeusler, Luiz Fernando Gomes Soares.  
    **[Validating Hypermedia Documents: a Timed Automata Approach](https://bib-di.inf.puc-rio.br/techreports/)** (PDF).  
    Monografías en Ciencia de la Computación, Departamento de Informática, PUC-Rio, 2001.

[^1]: Associação Brasileira de Normas Técnicas.  NBR 15606-2.  Televisión digital terrestre -- Especificación de codificación y transmisión de datos para radiodifusión digital -- Parte 2: Ginga-NCL para receptores fijos y móviles -- Lenguaje de aplicación XML para codificación de aplicaciones. Segunda edición. Mayo de 2011. Disponible en https://forumsbtvd.org.br/legislacao-e-normas-tecnicas/normas-tecnicas-da-tv-digital/espanol/
[^2]: Associação Brasileira de Normas Técnicas. NBR 15606-5.  Televisión digital terrestre -- Codificación de datos y especificaciones de transmisión para radiodifusión digital -- Parte 5: Ginga-NCL para receptores portátiles -- Lenguaje XML de aplicación para codificación de aplicaciones. Segunda edición. Mayo de 2011. Disponible en https://forumsbtvd.org.br/legislacao-e-normas-tecnicas/normas-tecnicas-da-tv-digital/espanol/
[^3]: Recomendación UIT-T H.761. Nested Context Language (NCL) y Ginga-NCL para Servicios IPTV. Ginebra, abril de 2009. Disponible en http://www.itu.int/rec/T-REC-H.761
