---
title: "Versões NCL"
---

As seguintes instruções de processamento devem ser escritas em um documento NCL. Eles identificam as aplicações NCL e a versão NCL para a qual o documento está em conformidade.

```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
<ncl id="any string" xmlns="http://www.ncl.org.br/NCL3.0/profileName">
```

Uma versão específica é especificada no caminho URI, onde o número da versão "x.y" é escrito imediatamente após "/NCL".

O número de versão de uma especificação de documento NCL consiste em um código principal número e um número menor, separados por um ponto.  Os números são representados como cadeias de caracteres decimais com zeros à esquerda suprimidos.  A inicial o número da versão padrão é 3.0.

Novas versões NCL devem ser lançadas de acordo com o seguinte versionamento política.  Se os reprodutores NCL compatíveis com versões mais antigas ainda puderem receber um documento baseado na especificação revisada, devido a correções de erros, razões operacionais, ou a adição de uma nova notação de sintaxe concisa ("açúcar de sintaxe") que pode ser traduzido em tempo de compilação para o antigo, o nova versão do NCL deverá ser lançada com o número menor atualizado.  Se NCL jogadores que estão em conformidade com versões mais antigas não podem receber um documento baseado em especificações revisadas, o número principal deve ser atualizado.

### Perfis NCL { data-search-exclude }

NCL permite a combinação de seus módulos em perfis de linguagem.

Qualquer documento em conformidade com os perfis NCL deverá ter o [&lt;ncl&gt;](ncl.md) elemento como seu elemento raiz.

```xml
<ncl id="any string" xmlns="http://www.ncl.org.br/NCLx.y/profileName">
```

A string "profileName" no caminho URI identifica o perfil de idioma usado para especificar o documento.  Atualmente, sete perfis linguísticos foram definido:

  * O *NCL 3.0 Full Profile*, também chamado de //NCL 3.0 Language Profile//, é o perfil completo da linguagem NCL 3.0.  Isso compreende todos os módulos NCL e fornece todas as facilidades para o autoria declarativa de documentos NCL.

  * O *NCL 3.1 Language Profile* estende a versão 3.0 com um "açúcar sintático" para definir relações e relacionamentos.

  * O *NCL 3.0 Raw Profile* tem a mesma expressiveness do NCL 3.0, mas sem quaisquer facilidades de reutilização e com um número mínimo de "açúcares sintáticos".  Tem o mínimo possível número de elementos e atributos, embora mantendo o mesmo expressividade do Perfil Completo.

  * O *NCL 3.0 Enhanced DTV Profile (EDTV Profile)* visa o DTV domínio.  É a linguagem declarativa padrão do Middleware de TV digital nipo-brasileiro ISDB-T<sub>B</sub> para fixo e móvel receptores, e também Recomendação ITU-T para serviços de IPTV.

  * O *Perfil Básico DTV NCL 3.0 (Perfil BDTV)* é uma simplificação do perfil EDTV em que efeitos de transição e metadados funcionalidades são opcionais.  É a linguagem declarativa padrão do middleware de TV digital nipo-brasileiro ISDB-T<sub>B</sub> para dispositivos portáteis receptores.

  * O *NCL 3.0 Connector Profile* permite a criação de conexões causais e relações de restrição que podem ser importadas por qualquer um dos anteriormente perfis listados, exceto o perfil NCL 3.0 Raw.

  * O *NCL 3.0 CausalConnector Profile* é uma versão simplificada do Perfil do conector NCL 3.0, que permite apenas definir causas relações.