---
title: "NCL Versions"
---

The following processing instructions must be written in an NCL document. They identify NCL applications and the NCL version to which the document conforms.

```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
<ncl id="any string" xmlns="http://www.ncl.org.br/NCL3.0/profileName">
```

A specific version is specified in the URI path, where the version number "x.y" is written immediately after the "/NCL".

The version number of an NCL document specification consists of a major number and a minor number, separated by a dot.  The numbers are represented as decimal character strings with leading zeros suppressed.  The initial standard version number is 3.0.

New NCL versions shall be released in accordance to the following versioning policy.  If NCL players that conform to older versions can still receive a document based on the revised specification, due to error corrections, operational reasons, or the addition of a new concise syntax notation ("syntax sugar") that can be translated at compile time to the old one, the new version of NCL shall be released with the minor number updated.  If NCL players that conform to older versions cannot receive a document based on the revised specifications, the major number must be updated.

### NCL Profiles { data-search-exclude }

NCL allows for the combination of its modules in language profiles.

Any document in conformance with NCL profiles shall have the [&lt;ncl&gt;](ncl.md) element as its root element.

```xml
<ncl id="any string" xmlns="http://www.ncl.org.br/NCLx.y/profileName">
```

The "profileName" string in the URI path, identifies the language profile used to specify the document.  Currently, seven language profiles have been defined:

  * The *NCL 3.0 Full Profile*, also called //NCL 3.0 Language Profile//, is the complete profile of the NCL 3.0 language.  It comprises all NCL modules and provides all facilities for the declarative authoring of NCL documents.

  * The *NCL 3.1 Language Profile* extends the version 3.0 with a "syntactic sugar" for defining relations and relationships.

  * The *NCL 3.0 Raw Profile* has the same expressiveness of the NCL 3.0 Language Profile, but without any reuse facilities and with a minimum number of "syntactic sugars".  It has the minimum possible number of elements and attributes although maintaining the same expressiveness of the Full Profile.

  * The *NCL 3.0 Enhanced DTV Profile (EDTV Profile)* aims at the DTV domain.  It is the standard declarative language of the Japanese-Brazilian DTV middleware ISDB-T<sub>B</sub> for fixed and mobile receivers, and also ITU-T Recommendation for IPTV services.

  * The *NCL 3.0 Basic DTV Profile (BDTV Profile)* is a simplification of the EDTV profile in which transition effects and metadata functionalities are optional.  It is the standard declarative language of the Japanese-Brazilian DTV middleware ISDB-T<sub>B</sub> for portable receivers.

  * The *NCL 3.0 Connector Profile* allows for the creation of causal and constraint relations that can be imported by any of the previously listed profiles, except the NCL 3.0 Raw profile.

  * The *NCL 3.0 CausalConnector Profile* is simplified version of the NCL 3.0 Connector profile, which only allows for defining causal relations.
