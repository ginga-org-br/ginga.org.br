---
title: Sobre o Ginga-J
---

O Ginga-J é o ambiente de execução procedural do middleware Ginga, baseado na plataforma Java. Ele permite a execução de aplicações de televisão interativa codificadas em Java.

Esta Norma especifica os requisitos para a parte procedural do middleware para o Sistema Brasileiro de Televisão Digital Terrestre (SBTVD). Ela garante que as aplicações possam ser executadas de forma consistente em diferentes implementações de plataformas de receptores.

Para a especificação técnica completa, consulte o documento [ABNT NBR 15606-4](/assets/pdf/NBR15606-4.pdf).

## Arquitetura e Modelo de Aplicação

O Ginga-J define um modelo de execução e ciclo de vida para aplicações procedurais (denominadas Xlets):

### Modelo de Aplicação e Ciclo de Vida

- **Gerenciamento do Ciclo de Vida**: Define os estados de inicialização, início, pausa e finalização para as aplicações. Suporta a execução de múltiplas aplicações simultâneas e o compartilhamento de recursos entre elas.
- **Controle de Aplicação**: Utiliza códigos de controle específicos para iniciar, parar ou consultar serviços interativos.
- **Armazenamento e Caching**: Suporta diferentes modelos de armazenamento e mecanismos de cache pró-ativo para otimizar a inicialização das aplicações.
- **Transmissão e Sinalização**: Define regras de sinalização, empacotamento (utilizando arquivos JAR), autenticação de aplicações e download de aplicações por canais de transmissão (broadcast) e de interatividade (banda larga).

### Plataforma de Execução Procedural

A plataforma Ginga-J é construída sobre perfis e bibliotecas padrão Java:

- **Bases Java ME**: Construída sobre as especificações Connected Device Configuration 1.1 (CDC 1.1 / JSR 218), Foundation Profile 1.1 (FP 1.1 / JSR 219) e Personal Basis Profile 1.1 (PBP 1.1 / JSR 217).
- **APIs Padrão para TV**: Inclui Java TV 1.1 (JSR 927) e JavaDTV 1.3 (provendo pacotes sob o namespace com.sun.dtv.* para radiodifusão, eventos de UI, sintonia, cartões inteligentes, etc.).
- **Extensões de Segurança**: Emprega Java Cryptography Extension (JCE 1.0.1), Java Secure Socket Extension (JSSE 1.0.1) e Security and Trust Services API (SATSA 1.0.1 / JSR 177).
- **Kit de Ferramentas de Interface Gráfica**: Padroniza o uso do LightWeight User Interface Toolkit (LWUIT 1.1) para construir interfaces gráficas e tratar eventos do usuário em telas de TV.

### APIs Específicas do Ginga-J

Além das APIs padrão Java, o Ginga-J introduz pacotes específicos para o SBTVD:

- **br.org.sbtvd.net.tuning**: Fornece APIs de sintonia (como as classes ChannelManager e Channel) para seleção de serviços de transmissão.
- **br.org.sbtvd.net e br.org.sbtvd.si**: Especifica APIs de informações de serviço (SI/PSI) dependentes do protocolo.
- **Ponte NCL (br.org.sbtvd.bridge)**: Integra o ambiente procedural com a máquina declarativa NCL, viabilizando a comunicação e sincronização entre aplicações Java e NCL.
- **Acesso Avançado a Dados**: Padroniza o acesso a dados via arquivos, protocolos de transporte por radiodifusão (DSM-CC), armazenamento persistente, propriedades do sistema e filtragem de seções MPEG-2.
