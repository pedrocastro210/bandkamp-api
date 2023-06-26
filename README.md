# BandKamp - API

<br>

### A API de Cadastro de Usuários, Álbuns e Músicas é um projeto desenvolvido em Python utilizando o framework Django e o Django Rest Framework. O objetivo dessa API é fornecer funcionalidades para cadastro e gerenciamento de usuários, álbuns e músicas.

<br>

#

## Funcionalidades Principais

<br>

#### A API oferece as seguintes funcionalidades principais:

<br>

- Cadastro de usuários
- Autenticação de usuários
- Cadastro de álbuns
- Cadastro de músicas

#

## Endpoints

<br>

#### A API disponibiliza os seguintes endpoints:

<br>

### Autenticação

<br>

#### A API oferece recursos de autenticação de usuários, permitindo o registro de novos usuários e o login de usuários existentes. Além disso, os usuários autenticados têm a capacidade de criar, visualizar, atualizar e excluir álbuns e músicas.

<br>

- POST /api/users/login/: Realiza o login de um usuário..

  Parâmetros obrigatórios: username, password.

<br>

#### Através dos diversos endpoints disponibilizados pela API, os desenvolvedores podem realizar operações como criar novos usuários, cadastrar álbuns e músicas, obter informações detalhadas sobre esses objetos e atualizá-los conforme necessário. Isso permite a construção de aplicativos e serviços que dependem dessas funcionalidades, como plataformas de streaming de música ou comunidades de compartilhamento de álbuns.

<br>

### Usuários

- POST /api/users/: Registra um novo usuário.

  Parâmetros obrigatórios: username, email, password, artistic_name.

- GET /api/users/{id}/: Retorna os detalhes de um usuário específico.

- PUT /api/users/{id}/: Atualiza os dados de um usuário específico.

- DELETE /api/users/{id}/: Exclui um usuário específico.

<br>

### Álbuns

- GET /api/albums/: Retorna a lista de álbuns cadastrados.

- POST /api/albums/: Cria um novo álbum.

  Parâmetros obrigatórios: name, year e TOKEN.

<br>

### Músicas

- GET /api/albums/albums_id/songs/: Retorna os detalhes de uma música específica.

- POST /api/albums/albums_id/songs/: Cria uma nova música.

  Parâmetros obrigatórios: title, duration e TOKEN.

#

## Modelos de Dados

#### A API utiliza os seguintes modelos de dados:

<br>

### Usuário

- username (string): nome de usuário (único).
- email (string): endereço de e-mail (único).
- password (string): senha do usuário.
- artistic_name (string): nome artístico.

<br>

### Álbum

- name (string): nome do álbum.
- year (integer): ano do álbum.

<br>

### Música

- title (string): título da música.
- duration (string): duração da música.

#

## Licença

### Este projeto está licenciado sob a MIT License.

<br>

#### O projeto é distribuído sob a licença MIT, o que significa que os desenvolvedores têm liberdade para utilizar, modificar e distribuir o código-fonte conforme suas necessidades. Além disso, o projeto é de código aberto, o que incentiva a contribuição da comunidade e o aprimoramento contínuo da API.

<br>

#### Este README oferece uma visão geral da API de cadastro de usuários, álbuns e músicas desenvolvida com Django e Django Rest Framework. Sinta-se à vontade para personalizar e adicionar informações adicionais relevantes ao seu projeto.
