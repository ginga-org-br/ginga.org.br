---
title: "Elemento &lt;ncl&gt;"
---

### Definição e uso { data-search-exclude }

A tag [&lt;ncl&gt;](ncl.md) representa a raiz de um documento NCL.

A tag [&lt;ncl&gt;](ncl.md) é o contêiner para todos os outros elementos NCL (exceto para
a tag <?xml>).

### Sintaxe { data-search-exclude }

| Elemento | Atributos | Conteúdo | Pai |
| --- | --- | --- | --- |
| [&lt;ncl&gt;](ncl.md) | <u>*id*</u>, *título*, *xmlns* | ([&lt;head&gt;](head.md)?, [&lt;body&gt;](body.md)?) | -- |

### Atributos { data-search-exclude }

| Nome | Valor | Descrição |
| --- | --- | --- |
| *id* | Pode receber qualquer valor de string que comece com uma letra ou sublinhado e que contenha apenas letras, dígitos, <"."> e <"_">. | O atributo *id* identifica exclusivamente o elemento dentro de um documento. |
| *título* | Corda. | O atributo *title* contém informações consultivas.  Os valores do atributo *title* podem ser renderizados por agentes de usuário de diversas maneiras. |
| *xmlns* | "http://www.ncl.org.br/NCL3.0/EDTVProfile" ou "http://www.ncl.org.br/NCL3.0/BDTVProfile" | O atributo xmlns declara um namespace XML – em outras palavras, ele declara a coleção primária de construções definidas em XML que o documento usa. O valor do atributo é a URL que identifica onde o namespace está oficialmente definido. Dois valores são permitidos para o atributo *xmlns*: "http://www.ncl.org.br/NCL3.0/EDTVProfile" e "http://www.ncl.org.br/NCL3.0/BDTVProfile", para os perfis DTV Enhanced e Basic, respectivamente. Um player NCL deverá saber que o schemaLocation para esses namespaces é, respectivamente: "http://www.ncl.org.br/NCL3.0/profiles/NCL30EDTV.xsd" e "http://www.ncl.org.br/NCL3.0/profiles/NCL30BDTV.xsd". |