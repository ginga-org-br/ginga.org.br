---
title: Sobre o Ginga-HTML5
---

# Ginga-HTML5

Explore os exemplos de Ginga-HTML5 abaixo:

<div class="ginga-playground-container">

<nav class="ginga-playground-tabs" role="tablist" aria-label="Exemplos do Ginga Playground">
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

Esta Norma padroniza um perfil comum de HTML5, CSS e APIs JavaScript a serem suportadas por dispositivos receptores de televisão digital interativa. O objetivo desta norma é definir um perfil que os desenvolvedores de aplicações interativas possam utilizar, assim como os requisitos necessários para os implementadores do middleware Ginga. Esta norma não especifica extensões às tecnologias mencionadas, mas somente um subconjunto de interesse para o desenvolvimento de aplicações para televisão interativa.

Esta Norma é primordialmente destinada às entidades que estão especificando receptores e/ou padrões baseados no Ginga-HTML5. Também é destinada aos desenvolvedores de aplicações que utilizam as funcionalidades do Ginga-HTML5 e de suas APIs. A especificação do perfil HTML5 para o middleware Ginga tem como objetivo assegurar a interoperabilidade das aplicações em diferentes implementações de plataformas que o suportam.

Esta Norma não especifica a forma como o ambiente de aplicação Ginga-HTML5 deve ser implementado em um receptor em conformidade. Um fabricante de receptores pode implementar sua máquina de apresentação Ginga-HTML5 utilizando quaisquer implementações, desde que conforme com os requisitos especificados.

## Integração com Ginga-CC WebServices

Aplicações HTML5 executadas no Ginga interagem com recursos de radiodifusão, configurações do receptor, reprodutores de mídia e dispositivos secundários por meio do **Ginga-CC-WebServices** (ABNT NBR 15606-11), que padroniza as APIs REST e WebSocket expostas pelo Ginga Common Core. Aplicações HTML5 também podem ser incorporadas diretamente em apresentações NCL por meio do elemento [&lt;media&gt;](../gingancl/handbook/media.md).
