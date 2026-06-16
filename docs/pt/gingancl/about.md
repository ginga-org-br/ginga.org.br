---
title: Sobre
---

Ginga-NCL é o subsistema [Ginga](http://www.ginga.org.br/) desenvolvido pela [PUC-Rio](http://www.puc-rio.br/) que visa prover uma infraestrutura de apresentação para aplicações declarativas escritas na linguagem NCL (Nested Context Language). [NCL](http://www.ncl.org.br/) é uma linguagem de aplicação XML com facilidades para a especificação de aspectos de interatividade, sincronismo espaço-temporal entre objetos de mídia, adaptabilidade, suporte a múltiplos dispositivos e suporte à produção ao vivo de programas interativos não-lineares.

## O que é NCL?

NCL é o acrônimo para *Nested Context Language*.

NCL é uma linguagem declarativa, na verdade uma aplicação XML, que tem sido especificado de forma modular, visando combinar seus módulos em linguagem perfis.

Entre os perfis NCL estão aqueles direcionados ao domínio DTV.  A flexibilidade NCL, sua facilidade de reutilização, suporte a vários dispositivos, conteúdo de aplicativos e adaptabilidade de apresentação e, principalmente, seu suporte intrínseco para facilitar definindo a sincronização espaço-temporal entre ativos de mídia, incluindo aqueles provenientes das interações do espectador, fazem da NCL uma excelente solução para todos tipos de sistemas DTV interativos.

NCL é a linguagem declarativa do middleware nipo-brasileiro de TV digital ISDB-T<sub>B</sub>[^1][^2], e também Recomendação ITU-T para serviços de IPTV[^3].

A NCL tem uma separação mais rígida entre o conteúdo e a estrutura do aplicativo. A NCL não define nenhum conteúdo de mídia por si só.  Em vez disso, define a cola que mantém a mídia unida em apresentações multimídia.  Assim, um NCL documento apenas define como os objetos de mídia são estruturados e relacionados no tempo e espaço.

Como uma linguagem *cola*, a NCL não restringe nem prescreve qualquer tipo de conteúdo do objeto de mídia.  Quais objetos de mídia são suportados depende do reprodutores de mídia incorporados no formatador NCL (o reprodutor NCL).

 Portanto, podemos ter conteúdos perceptivos, como vídeos, imagens, áudios e textos, como objetos de mídia NCL.  Também podemos ter objetos de mídia com imperativo conteúdo de código, como código Lua, código ECMAScript, código Java, etc. Além disso, podemos ter objetos de mídia com conteúdo de código declarativo, como baseado em HTML código, código SVG, código X3D, código SMIL, código NCL (sim, aplicativos NCL incorporados outras aplicações NCL), etc. Portanto, NCL não substitui, mas incorpora aplicações de outras línguas, relacionando todos os objetos no tempo e no espaço em uma apresentação distribuída em vários dispositivos.

## Relatórios PUC-Rio

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

- M.T. Medina, C.C. Ribeiro, Luiz Fernando Gomes Soares.  
    **[Automatic Scheduling of Hypermedia Documents with Elastic Times](https://bib-di.inf.puc-rio.br/techreports/)** (PDF).  
    Monografias em Ciência da Computação, Departamento de Informática, PUC-Rio, 2001.

- Rogério Ferreira Rodrigues, Bruno Bachelet, Philippe Mahey, Luiz Fernando Gomes Soares.  
    **[Elastic Time Computations for Hypermedia Documents](https://bib-di.inf.puc-rio.br/techreports/)** (PDF).  
    Monografias em Ciência da Computação, Departamento de Informática, PUC-Rio, 2001.

- Débora Christina Muchaluat Saade, Sérgio Colcher, Luiz Fernando Gomes Soares.  
    **[Relações de Sincronização Espaço-Temporal Hipermídia Também Merecem Status de Primeira Classe](https://bib-di.inf.puc-rio.br/techreports/)** (PDF).  
    Monografias em Ciência da Computação, Departamento de Informática, PUC-Rio, 2001.

- M.F. Felix, Edward Hermann Haeusler, Luiz Fernando Gomes Soares.  
    **[Validating Hypermedia Documents: a Timed Automata Approach](https://bib-di.inf.puc-rio.br/techreports/)** (PDF).  
    Monografias em Ciência da Computação, Departamento de Informática, PUC-Rio, 2001.

[^1]: Associação Brasileira de Normas Técnicas.  NBR 15606-2.  TV digital terrestre -- Codificação de dados e especificações de transmissão para radiodifusão digital -- Parte 2: Ginga-NCL para receptores fixos e móveis -- Linguagem XML de aplicação para codificação de aplicações. 2ª Edição. Maio, 2011. Disponível em https://forumsbtvd.org.br/legislacao-e-normas-tecnicas/normas-tecnicas-da-tv-digital/portugues/
[^2]: Associação Brasileira de Normas Técnicas. NBR 15606-5.  TV digital terrestre -- Codificação de dados e especificações de transmissão para radiodifusão digital -- Parte 5: Ginga-NCL para receptores portáteis -- Linguagem XML de aplicação para codificação de aplicações. 2ª Edição. Maio, 2011. Disponível em https://forumsbtvd.org.br/legislacao-e-normas-tecnicas/normas-tecnicas-da-tv-digital/portugues/
[^3]: Recomendação ITU-T H.761. Nested Context Language (NCL) e Ginga-NCL para Serviços IPTV.  Genebra, Abril, 2009.  Disponível em http://www.itu.int/rec/T-REC-H.761
