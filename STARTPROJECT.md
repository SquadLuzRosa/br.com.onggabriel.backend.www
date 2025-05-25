# 💻 BACKEND ONG GABRIEL

<p align="left">
  Esta API foi desenvolvida para gerenciar os dados relacionados aos posts, comentários, avaliações de voluntários e participantes do projeto, promovendo o bem-estar mental e prevenção ao suicídio. 
  O framework Django foi utilizado para garantir uma estrutura robusta, escalável e segura para interação entre jovens e voluntários.
</p>

---

## 🚀 Tecnologias Utilizadas

<div align="left">
  <img src="https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white"/>
  <img src="https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray"/>
  <img src="https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white"/>
</div>

---

## ✅ Pré-requisitos

Antes de iniciar, verifique se você possui os seguintes programas instalados:

- [Git](https://git-scm.com)
- [Docker Desktop](https://www.docker.com/products/docker-desktop) (caso esteja usando Windows ou Mac)
- [Docker Compose](https://docs.docker.com/compose/install/) (Linux)
- Terminal/Bash

---

## ⚙️ Como Rodar o Projeto

### 1. Clonar o Repositório

Abra seu terminal e digite:

```bash
git clone https://github.com/SquadLuzRosa/br.com.onggabriel.backend.www.git
cd br.com.onggabriel.backend.www
```

### 2. Criar o arquivo .env

No projeto existe um arquivo .env.example que contém as variavéis de configuração, você pode renomear .env.example para .env:

```bash
Abra o arquivo .env e configure os seguintes dados:

POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=postgres
POSTGRES_PORT=5432
POSTGRES_HOST=data_base

RABBITMQ_MANAGEMENT_PORT=15672
RABBITMQ_AMQP_PORT=5672
RABBITMQ_DEFAULT_USER=admin
RABBITMQ_DEFAULT_PASS=mypassword

DJANGO_PORT=8000
DJANGO_SECRET_KEY="django-insecure-)mg&)dwik1@c=$i6t6m4y92l9gocmc2wvpn1@rtoen54^%7y"
DEBUG=True
```

### 3. Subir os Containers com Docker Compose

No diretório raiz do projeto, execute:

```bash
docker-compose up --build
```

Esse comando irá:
Criar e iniciar os containers: Django, PostgreSQL e RabbitMQ e instalar as dependências automaticamente.

### 💡Para verificar se os containers estão rodando:

```bash
docker ps
```

### 4. Acessar a Aplicação no Navegador

Após a inicialização, acesse:

```bash
API Principal: http://localhost:8000

Admin Django: http://localhost:8000/admin

```

### 5. Acessar o Painel do RabbitMQ

Gerencie filas e mensagens em:

```bash
http://localhost:15672

Credenciais (do .env):

Usuário: admin
Senha: mypassword
```

### 6. Acessar a Documentação da API

Acesse a documentação interativa nos links abaixo:

```bash
Swagger UI: http://localhost:8000/api/v1/swagger/

Redoc: http://localhost:8000/api/v1/redoc/

Schema JSON: http://localhost:8000/api/v1/schema/
```

7. Rotas de Autenticação
   Você pode usar as rotas abaixo para lidar com autenticação JWT:

```bash
Obter Token: POST http://localhost:8000/api/v1/auth/token/

Atualizar Token: POST http://localhost:8000/api/v1/auth/token/refresh/

Verificar Token: POST http://localhost:8000/api/v1/auth/token/verify/
```

### 🛠️ Problemas Comuns

#### Docker travado?

Reinicie o Docker Desktop.

```bash
Execute docker system prune -a com cuidado (isso remove containers e imagens antigas).
```

#### Porta em uso?

```bash
Verifique se as portas 8000, 5432 e 15672 estão livres.
```

#### Erro de banco não encontrado?

Verifique se POSTGRES_HOST=data_base no .env bate com o nome do serviço no docker-compose.yml.
