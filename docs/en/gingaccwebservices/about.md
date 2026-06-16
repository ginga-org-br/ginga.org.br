---
title: Ginga-CC-WebServices
---

Ginga-CC-WebServices is the Ginga Common Core Web Services integration subsystem, enabling web services and remote service invocation capabilities in SBTVD (Brazilian Digital Terrestrial Television System) middleware.

This Standard establishes a common set of WebServices supported by Ginga Common Core implementations in digital interactive television receiver devices. It defines services for application developers and the necessary requirements for Ginga middleware implementers to ensure interoperability across different hardware platforms.

For the complete technical specification, refer to the document [ABNT NBR 15606-11](/assets/pdf/NBR15606-11.pdf).

## Architecture & Communication APIs

The WebServices API enables communication between the Ginga execution environment and external or local clients. The services are divided into several functional APIs:

### Security, Pairing, and Client Authorization

- **Client Authentication**: Identifies and authorizes local or external application clients, managing user consent history and session access tokens.
- **Client Pairing**: Supports pairing external devices (e.g., smartphones or tablets) to the receiver using QR Codes or PINs via a key-establishment protocol.
- **Security Contexts**: Allows broadcasters to register, access, and revoke tokens for service contexts to secure interaction.

### DTV Context and Service Access

- **Service Retrieval**: Allows queries to find the current active digital television service and the list of all available services.
- **Service Selection**: Supports changing the tuner service (channel zapping) via remote invocations.
- **Component Access**: Retrieves detailed information and performs operations on specific elementary components (audio, video, data) of the current service.

### Execution Environment Communication

- **Interactive Application Control**: Lists, queries details, starts, stops, or controls interactive applications running on the receiver.
- **Node & Document Control**: Allows querying and controlling the execution nodes of a running Ginga-NCL application, including dynamically sending NCL editing commands.
- **Remote Control Key Registration**: Manages the list of keys reserved for specific applications, allowing remote clients to reserve or release remote control keys.
- **Data Persistence**: Provides read and write access to the dedicated application persistence area.
- **DSM-CC Access**: Facilitates reading files from DSM-CC Object Carousels and registering listeners for broadcast DSM-CC Stream Events.

### Broadcast Metadata and SI/PSI Tables

- **Time Retrieval**: Returns the current official broadcast time and date.
- **SI/PSI Tables**: Provides read access to standard MPEG-2 and ISDB-T system information tables, including NIT, SDT, PAT, BAT, PMT, and BIT.
- **EPG Program Guide**: Accesses Electronic Program Guide data and broadcast schedules.

### Multimedia Content and Platform Integration

- **Stream Access & Media Players**: Handles direct stream resource allocation and allows querying, controlling, or releasing dedicated multimedia players.
- **Platform Capability Queries**: Inquires about receiver characteristics, hardware capabilities, and supported digital rights management (DRM) systems.
- **Target Application Execution**: Discovers and runs native, pre-installed target applications using deep links.
