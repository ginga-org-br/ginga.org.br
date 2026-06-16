---
title: About Ginga-J
---

Ginga-J is the procedural execution environment of the Ginga middleware, based on the Java platform. It allows the execution of interactive television applications coded in Java.

This Standard specifies the requirements for the procedural part of the middleware for the Brazilian Digital Terrestrial Television System (SBTVD). It guarantees that applications can run seamlessly across different implementations of receiver platforms.

For the complete technical specification, refer to the document [ABNT NBR 15606-4](/assets/pdf/NBR15606-4.pdf).

## Architecture & Application Model

Ginga-J defines an execution model and lifecycle for procedural applications (called Xlets):

### Application Model and Lifecycle

- **Lifecycle Management**: Defines initialization, start, pause, and finalization states for applications. It supports running multiple concurrent applications and sharing resources between them.
- **Application Control**: Uses specific control codes to start, stop, or query interactive services.
- **Storage & Caching**: Supports different storage models and proactive caching mechanisms to optimize application startup.
- **Transmission and Signaling**: Defines signaling rules, packaging (using JAR files), application authentication, and downloading applications over both broadcast and broadband interaction channels.

### Procedural Execution Platform

The Ginga-J platform is built on standard Java profiles and libraries:

- **Java ME Foundations**: Built on Connected Device Configuration 1.1 (CDC 1.1 / JSR 218), Foundation Profile 1.1 (FP 1.1 / JSR 219), and Personal Basis Profile 1.1 (PBP 1.1 / JSR 217).
- **Television Standard APIs**: Includes Java TV 1.1 (JSR 927) and JavaDTV 1.3 (providing com.sun.dtv.* packages for broadcast, UI events, tuning, smartcards, etc.).
- **Security Extensions**: Employs Java Cryptography Extension (JCE 1.0.1), Java Secure Socket Extension (JSSE 1.0.1), and Security and Trust Services API (SATSA 1.0.1 / JSR 177).
- **User Interface Toolkit**: Standardizes on the LightWeight User Interface Toolkit (LWUIT 1.1) to build user interfaces and handle user events on TV screens.

### Specific Ginga-J APIs

In addition to standard Java APIs, Ginga-J introduces specific packages for SBTVD:

- **br.org.sbtvd.net.tuning**: Provides tuning APIs (such as ChannelManager and Channel) for broadcast service selection.
- **br.org.sbtvd.net and br.org.sbtvd.si**: Specifies protocol-dependent service information (SI/PSI) APIs.
- **NCL Bridge (br.org.sbtvd.bridge)**: Integrates the procedural environment with the declarative NCL engine, enabling communication and synchronization between Java and NCL applications.
- **Advanced Data Access**: Standardizes data access via files, broadcast transport protocols (DSM-CC), persistent storage, system properties, and MPEG-2 section filtering.
