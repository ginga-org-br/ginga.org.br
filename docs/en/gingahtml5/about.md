---
title: About Ginga-HTML5
---

This Standard standardizes a common profile of HTML5, CSS, and JavaScript APIs to be supported by interactive digital television receiver devices. The purpose of this standard is to define a profile that interactive application developers can use, as well as the necessary requirements for implementers of the Ginga middleware. This standard does not specify extensions to the mentioned technologies, but only a subset of interest for the development of applications for interactive television.

This Standard is primarily intended for entities that are specifying receivers and/or standards based on Ginga-HTML5. It is also intended for application developers who use the features of Ginga-HTML5 and its APIs. The specification of the HTML5 profile for the Ginga middleware aims to ensure the interoperability of applications across different implementations of platforms that support it.

This Standard does not specify how the Ginga-HTML5 application environment must be implemented in a compliant receiver. A receiver manufacturer can implement its Ginga-HTML5 presentation engine using any implementations, as long as they comply with the specified requirements.

For the complete technical specification, refer to the document [ABNT NBR 15606-10](/assets/pdf/NBR15606-10.pdf).

## Technical Specifications

The Ginga-HTML5 environment supports the following main features:

### HTML5 and CSS3 Profile

- **HTML5 Markup**: Support for standard HTML5 markup elements (excluding specific desktop or heavy-weight elements not suitable for DTV) and global attributes.
- **CSS3 Styling**: Layout control via Flexbox, basic graphics (backgrounds, borders), advanced graphics (transforms, transitions, multi-column layouts), and device-specific styling (media queries for screen resolution adaptation).
- **Text & Fonts**: Font styling, alignment, and formatting suited for TV screens (including WOFF file format).

### Scripting and Browser APIs

- **ECMAScript**: JavaScript support compliant with the ECMAScript 5.1 specification.
- **DOM & Events**: Support for DOM4 and UI events, including mapping remote control keys to standard virtual keycodes.
- **Asynchronous Communication**: Support for `XMLHttpRequest`, WebSockets (`WebSocket`), Server-Sent Events (`EventSource`), and Web Messaging (`postMessage`).
- **High Resolution Support**: Support for `devicePixelRatio` to handle high-density screens.
- **Offline Storage**: Persistent and session-based data storage through Web Storage (`localStorage` and `sessionStorage`).
- **Multithreading**: Execution of background scripts via Web Workers.

### Multimedia and Advanced API Support

- **Canvas 2D**: Dynamic 2D rendering using `HTMLCanvasElement`, `CanvasRenderingContext2D`, and helper interfaces like `TextMetrics` and `CanvasGradient`.
- **Web Audio API**: Synthetic audio generation and advanced audio processing.
- **Encrypted Media Extensions (EME)**: Support for digital rights management and encrypted media playback in compliance with W3C recommendations.
- **Media Support**: Integration of standard media element interfaces and playback event handling.
