---
title: About Ginga-HTML5
---

# Ginga-HTML5

Explore the Ginga-HTML5 examples below:

<div class="ginga-playground-container">

<nav class="ginga-playground-tabs" role="tablist" aria-label="Ginga Playground examples">
  <button type="button" class="ginga-playground-tab" role="tab" aria-selected="true" data-playground-src="https://ginga.org.br/gingaf/playground/?app=https://raw.githubusercontent.com/ginga-org-br/gingaf/refs/heads/main/examples/image.html">image.html</button>
  <button type="button" class="ginga-playground-tab" role="tab" aria-selected="false" data-playground-src="https://ginga.org.br/gingaf/playground/?app=https://raw.githubusercontent.com/ginga-org-br/gingaf/refs/heads/main/examples/current_service.html">current_service.html</button>
</nav>

<iframe
  class="ginga-playground"
  src="https://ginga.org.br/gingaf/playground/?app=https://raw.githubusercontent.com/ginga-org-br/gingaf/refs/heads/main/examples/image.html"
  loading="lazy"
  allow="autoplay; fullscreen">
</iframe>

</div>

This Standard standardizes a common profile of HTML5, CSS, and JavaScript APIs to be supported by interactive digital television receiver devices. The purpose of this standard is to define a profile that interactive application developers can use, as well as the necessary requirements for implementers of the Ginga middleware. This standard does not specify extensions to the mentioned technologies, but only a subset of interest for the development of applications for interactive television.

This Standard is primarily intended for entities that are specifying receivers and/or standards based on Ginga-HTML5. It is also intended for application developers who use the features of Ginga-HTML5 and its APIs. The specification of the HTML5 profile for the Ginga middleware aims to ensure the interoperability of applications across different implementations of platforms that support it.

This Standard does not specify how the Ginga-HTML5 application environment must be implemented in a compliant receiver. A receiver manufacturer can implement its Ginga-HTML5 presentation engine using any implementations, as long as they comply with the specified requirements.

## Ginga-CC WebServices Integration

HTML5 applications running on Ginga interact with broadcast resources, receiver settings, media players, and companion devices through **Ginga-CC-WebServices** (ABNT NBR 15606-11), which standardizes the Common Core REST and WebSocket APIs exposed to interactive TV applications. HTML5 applications can also be embedded directly inside NCL presentations via the [&lt;media&gt;](../gingancl/handbook/media.md) element.
