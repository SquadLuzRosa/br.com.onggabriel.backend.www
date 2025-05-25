# Projeto Site Intitucional Ong Gabriel - BackEnd

### Introdução

Este repositório contém o código-fonte e a documentação para o desenvolvimento do **back-end** do site institucional da **ONG Gabriel**. O objetivo principal da **ONG Gabriel** é **prevenir o suicídio e promover o bem-estar mental de jovens em situação de vulnerabilidade social**. Através de ações voltadas para o apoio psicológico, educação em saúde mental e criação de espaços seguros de acolhimento, a ONG busca impactar positivamente a vida dos jovens e suas comunidades, garantindo acesso a recursos e suporte emocional para aqueles que mais precisam.

### Sobre o Projeto

Este projeto é fruto de uma parceria voluntária entre o **Pipoca Ágil** e a **ONG Gabriel**, com o objetivo de desenvolver uma **plataforma moderna e personalizada** que facilite o acesso a uma rede de apoio emocional para jovens em situação de vulnerabilidade. A plataforma permitirá que as pessoas encontrem ajuda, compartilhem suas experiências, esclareçam dúvidas sobre saúde mental e participem de um ambiente de suporte emocional.

Nosso foco é **criar um sistema intuitivo e acessível**, onde os usuários possam obter informações relevantes, interagir com a comunidade e acessar recursos voltados para o bem-estar mental, tudo com o objetivo de **prevenir o suicídio e promover a saúde mental**.

### Proposta do MVP (Produto Mínimo Viável)

O MVP da plataforma terá as seguintes funcionalidades essenciais:

1. **Cadastro e Autenticação de Usuários**: Permitir que os usuários se registrem e façam login de forma segura para acessar suas informações e interagir com a plataforma.
2. **Blog com Publicação de Posts**: Uma seção de blog onde serão publicados conteúdos sobre saúde mental, bem-estar, prevenção ao suicídio e eventos da ONG, visando fornecer informações e promover discussões construtivas.
3. **Seção de Comentários e Avaliações**: Uma funcionalidade para que os voluntários e participantes do projeto possam compartilhar suas experiências e feedback sobre os conteúdos do blog e as atividades da ONG.
4. **Sistema de Moderação de Conteúdo**: Garantir que os posts do blog e os comentários sejam moderados antes de serem publicados para manter um ambiente seguro e respeitoso.
5. **API de Gestão de Conteúdo**: Gerenciamento de conteúdos relacionados à saúde mental, atividades, eventos e recursos de apoio psicológico.

### Funcionalidades Principais

#### Cadastro de Usuários e Autenticação

A API permitirá o **cadastro de usuários** e **autenticação** segura utilizando **tokens JWT**. O sistema de login será robusto e garantirá que as informações dos usuários sejam mantidas protegidas, criando uma experiência de acesso personalizada e segura.

#### Blog com Publicação de Posts

A API permitirá a **criação, leitura, atualização e exclusão (CRUD)** de posts do blog. Esses posts serão publicados com temas relacionados ao **bem-estar mental**, **prevenção ao suicídio**, **experiências de superação**, **eventos da ONG** e **dicas de apoio psicológico**. O blog será uma ferramenta de educação, apoio e disseminação de informações úteis para os jovens e suas famílias.

#### Seção de Comentários e Avaliações com Moderação

A API incluirá um **endpoint dedicado** para a gestão de **comentários e avaliações**, onde os voluntários, participantes e usuários poderão compartilhar suas experiências sobre os posts do blog, eventos e atividades da ONG. Todos os comentários serão moderados antes de serem publicados.

#### Área de Administração para Moderação de Conteúdo

Será implementada uma **área de administração** onde os administradores poderão revisar, aprovar ou excluir posts e comentários. Esse sistema de moderação ajudará a garantir que o conteúdo publicado seja sempre respeitoso, relevante e alinhado com os valores da ONG.

### Objetivo do MVP

O objetivo principal deste MVP é construir uma **plataforma de apoio emocional** que ajude os usuários a encontrarem recursos, compartilhem experiências de superação e participem de um ambiente seguro e acolhedor. As funcionalidades principais incluem:

- **Cadastro de usuários** com autenticação segura.
- **Blog com funcionalidade CRUD de posts** para disseminação de conteúdos sobre saúde mental.
- **Sistema de comentários e avaliações** para promover a troca de experiências.
- **Moderação de conteúdo** para garantir que apenas conteúdo adequado seja publicado.
- **API de gestão de conteúdo** e de interações entre usuários, voluntários e administradores.

### Proposta Incrementada e Pontos de Destaque

#### Endpoint de Autenticação Segura

Usaremos **JWT (JSON Web Tokens)** para garantir a autenticação segura dos usuários, protegendo suas informações e sessões de acesso. Esse método de autenticação será implementado de forma robusta para garantir a integridade e privacidade dos dados.

#### Paginação Eficiente de Posts e Comentários

A listagem de **posts do blog** e **comentários** será paginada, permitindo que o conteúdo seja carregado de maneira eficiente sem comprometer o desempenho da API, mesmo com um grande número de dados.

#### Sistema de Comentários e Avaliações com Moderação

Implementaremos um sistema interativo de **comentários e avaliações** para que os usuários compartilhem suas experiências e sugestões sobre os posts do blog e as atividades da ONG. Todos os comentários passarão por um processo de **moderação prévia** para manter o ambiente saudável e seguro.

#### Expansão de Funcionalidades Futuras

Em versões futuras, a API poderá ser expandida para incluir:

- **Criação e gestão de eventos** como rodas de conversa, workshops e atividades voltadas à promoção do bem-estar mental.
- **Sistema de categorias e tags** para organizar os posts de forma mais eficiente.
- **Integração com sistemas externos** para disponibilizar conteúdos multimídia, como vídeos e podcasts sobre saúde mental.

#### Suporte e Manutenção Contínuos

Contamos com uma equipe dedicada para manutenção contínua da API, assegurando que a plataforma esteja sempre atualizada e segura, com o objetivo de oferecer a melhor experiência aos usuários e garantir a eficácia das ações da ONG Gabriel.

- **Linguagem de Programação:**
  - [Pyton](https://www.python.org/)
- **Frameworks e Bibliotecas:**
  - [Django](https://www.djangoproject.com/)
  - [Django Rest Framework](https://www.django-rest-framework.org/)
  - [Django Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
  - [DRF Espectacular](https://drf-spectacular.readthedocs.io/en/latest/)
  - [Celery](https://docs.celeryq.dev/en/stable/)
  - [Rabbitmq](https://pypi.org/project/pillow/)
- **Banco de Dados:**
  - [PostgreSQL](https://www.postgresql.org/)
- **Controle de Versão:**
  - [Git](https://git-scm.com/)
  - Repositório hospedado no [GitHub](https://github.com/)

Essa combinação de tecnologias foi escolhida para garantir eficiência, escalabilidade e facilidade de manutenção do projeto.

## Equipe

<div align="center">
  <table>
    <tr>
      <td align="center">
        <img src="https://avatars.githubusercontent.com/u/108550945?v=4" width="100" ><br>
        <a href="https://github.com/thiagoferreirapy" ><b>Thiago Ferreira</b></a><br>
        <i>BackEnd</i>
      </td>
      <td align="center">
        <img src="https://avatars.githubusercontent.com/u/67665085?v=4" width="100" ><br>
        <a href="https://github.com/Sabrinadelpache" ><b>Sabrina Delpache</b></a><br>
        <i>BackEnd</i>
      </td>
      <td align="center">
        <img src="https://avatars.githubusercontent.com/u/109382838?v=4" width="100" ><br>
        <a href="https://github.com/danielerick-dev" ><b>Daniel Erick</b></a><br>
        <i>BackEnd</i>
      </td>
      <td align="center">
        <img src="https://avatars.githubusercontent.com/u/151978350?v=4" width="100" ><br>
        <a href="https://github.com/juhffelix" ><b>Juliana Felix</b></a><br>
        <i>BackEnd</i>
      </td>
    </tr>
  </table>
</div>
