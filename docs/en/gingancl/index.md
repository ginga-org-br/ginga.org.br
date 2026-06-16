---
title: About
---

Ginga-NCL is the Ginga subsystem in charge of the presentation of NCL documents and was developed at PUC-Rio (Pontifical Catholic University of Rio de Janeiro). It defines a presentation environment for declarative applications written in NCL. NCL is an XML application language that provides support for specifying spatio-temporal synchronization among media objects, media content and presentation alternatives, exhibition on multiple devices, and live producing of interactive non-linear programs

## What is NCL?

NCL is the acronym for *Nested Context Language*.

NCL is a declarative language, indeed an XML application, which has been
specified in a modular way, aiming at combining its modules into language
profiles.

Among the NCL profiles are those targeting DTV domain.  The NCL flexibility,
its reuse facility, multi-device support, application content and
presentation adaptability, and mainly, its intrinsic support for easily
defining spatio-temporal synchronization among media assets, including those
coming from viewer interactions, make NCL an outstanding solution for all
kinds of interactive DTV systems.

NCL is the declarative language of the Japanese-Brazilian DTV middleware
ISDB-T<sub>B</sub>[^1]
[^2], and also ITU-T Recommendation for IPTV services[^3].

NCL has a stricter separation between application content and structure.
NCL does not define any media content itself.  Instead, it defines the glue
that holds media together in multimedia presentations.  Thus, an NCL
document only defines how media objects are structured and related in time
and space.

As a *glue* language, NCL does not restrict or prescribe any
media-object content type.  Which media objects are supported depends on the
media players embedded in the NCL formatter (the NCL player).

Therefore, we can have perceptual content, like videos, images, audios, and
texts, as NCL media objects.  We can also have media objects with imperative
code content, like Lua code, ECMAScript code, Java code, etc.  In addition,
we can have media objects with declarative code content, like HTML-based
code, SVG code, X3D code, SMIL code, NCL code (yes, NCL applications embed
other NCL applications), etc.  Therefore, NCL does not substitute but embeds
other language's applications, relating all objects in time and space in a
multiple device distributed presentation.

## PUC-Rio Seminal Reports

These are seminal texts written by Luiz Fernando about the NCL and NCM.

- Luiz Fernando Gomes Soares.  
    **[Introduction to DTV and to Ginga-NCL](/assets/pdf/Introduction%20to%20DTV%20and%20to%20Ginga-NCL.pdf)** (PDF).  
    Monografias em Ciência da Computação, Departamento de Informática, PUC-Rio.

- Luiz Fernando Gomes Soares.  
    **[Part 11 – Declarative Hypermedia Objects in NCL: Nesting Objects with NCL Code in NCL Documents](/assets/pdf/Part%2011%20-%20NCL3.0-DO.pdf)** (PDF).  
    Monografias em Ciência da Computação, Departamento de Informática, PUC-Rio, 2009.

- Luiz Fernando Gomes Soares.  
    **[Part 12 – Support to Multiple Exhibition Devices](/assets/pdf/Part%2012%20-%20NCL3.0-MD.pdf)** (PDF).  
    Monografias em Ciência da Computação, Departamento de Informática, PUC-Rio, 2009.

- Luiz Fernando Gomes Soares.  
    **[Part 13 - Ginga-NCL Implementors Guide v1.0](https://bib-di.inf.puc-rio.br/techreports/)** (PDF).  
    Monografias em Ciência da Computação, Departamento de Informática, PUC-Rio, 2009.

- Luiz Fernando Gomes Soares, Francisco Sant'Anna, Renato Cerqueira.  
    **[Part 10 – Imperative Objects in NCL: The NCLua Scripting Language](/assets/pdf/Part%2010%20-%20NCL3.0-IO.pdf)** (PDF).  
    Monografias em Ciência da Computação, Departamento de Informática, PUC-Rio, 2008.

- Luiz Fernando Gomes Soares, Rogério Ferreira Rodrigues.  
    **[Part 8 – NCL (Nested Context Language) Digital TV Profiles](/assets/pdf/Part%208%20-%20NCL3.0-DTV_0.pdf)** (PDF).  
    Monografias em Ciência da Computação, Departamento de Informática, PUC-Rio, 2006.

- Luiz Fernando Gomes Soares, Rogério Ferreira Rodrigues, Romualdo Monteiro Resende Costa, Marcio Ferreira Moreno.  
    **[Part 9 – NCL Live Editing Commands](/assets/pdf/Part%209%20-%20NCL3.0-EC.pdf)** (PDF).  
    Monografias em Ciência da Computação, Departamento de Informática, PUC-Rio, 2006.

- Luiz Fernando Gomes Soares, Rogério Ferreira Rodrigues.  
    **[Nested Context Model 3.0. Part 1 – NCM Core](/assets/pdf/Part1%20-%20NCM%203.0.pdf)** (PDF).  
    Monografias em Ciência da Computação, Departamento de Informática, PUC-Rio, 2005.

[^1]: Associação Brasileira de Normas Técnicas.  NBR 15606-2.  Digital terrestrial television -- Data coding and transmission specification for digital broadcasting -- Part 2: Ginga-NCL for fixed and mobile receivers -- XML application language for application coding. 2<sup>nd</sup> Edition. May, 2011. Available at https://forumsbtvd.org.br/legislacao-e-normas-tecnicas/normas-tecnicas-da-tv-digital/english/
[^2]: Associação Brasileira de Normas Técnicas. NBR 15606-5.  Digital terrestrial television -- Data coding and transmission specification for digital broadcasting -- Part 5: Ginga-NCL for portable receivers -- XML application language for application coding. 2<sup>nd</sup> Edition. May, 2011. Available at https://forumsbtvd.org.br/legislacao-e-normas-tecnicas/normas-tecnicas-da-tv-digital/english/
[^3]: ITU-T Recommendation H.761. Nested Context Language (NCL) and Ginga-NCL for IPTV Services.  Geneva, April, 2009.  Available at http://www.itu.int/rec/T-REC-H.761
