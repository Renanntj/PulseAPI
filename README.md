# DevSpace — API de Rede Social

API REST para uma rede social minimalista voltada para desenvolvedores, construída com **FastAPI** e **SQLAlchemy**. Permite criação de usuários, autenticação com JWT e publicação de posts com imagens.

---

## 🚀 Tecnologias

- **Python 3.11+**
- **FastAPI** — framework web assíncrono
- **SQLAlchemy** — ORM para banco de dados
- **JWT (JSON Web Tokens)** — autenticação stateless com access token e refresh token
- **Bcrypt** — hash seguro de senhas
- **Uvicorn** — servidor ASGI

---

## 📦 Funcionalidades

- ✅ Cadastro de usuário com validação de username (letras minúsculas, números, `_`, `-`, `.`)
- ✅ Login com e-mail e senha, retornando access token e refresh token
- ✅ Autenticação via Bearer Token
- ✅ Visualização de perfil público
- ✅ Edição de perfil autenticado
- ✅ Criação de posts com título, descrição e imagem (upload binário)
- ✅ Edição de post (somente pelo autor)
- ✅ Listagem pública de posts
- ✅ Endpoint de imagem por post
- ✅ Frontend simples em HTML/CSS/JS para demonstração

---

## 🗂️ Estrutura do Projeto

```
├── main.py
├── models/
│   ├── models.py
│   ├── models_user.py
│   └── models_post.py
├── schemas/
│   ├── usuario.py
│   └── posts.py
├── routers/
│   ├── router_user.py
│   └── router_posts.py
├── services/
│   ├── crypt_services.py
│   ├── criar_token.py
│   └── verificar_nome.py
├── dependecies/
│   └── dependecies.py
└── frontend/
    └── index.html
```

---

## ⚙️ Como rodar localmente

### 1. Clone o repositório

```bash
git clone (link a ser modificado) att em breve

cd NOME DO REP
```

### 2. Crie e ative o ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Rode a API

```bash
uvicorn main:app --reload
```

A API estará disponível em `http://127.0.0.1:8000`.

A documentação interativa (Swagger) estará em `http://127.0.0.1:8000/docs`.

---

## 🔐 Autenticação

A API utiliza **JWT Bearer Token**. Após o login, inclua o token no header das requisições protegidas:

```
Authorization: Bearer <seu_token>
```

O login retorna dois tokens:

| Token | Validade |
|---|---|
| `access_token` | Curta duração |
| `refresh_token` | 7 dias |

Use o endpoint `/user/refresh` com o refresh token para obter um novo access token sem precisar fazer login novamente.

---

## 📡 Principais Endpoints

### Usuários

| Método | Rota | Descrição | Auth |
|---|---|---|---|
| `POST` | `/user/criar-usuario` | Cadastro de novo usuário | ❌ |
| `POST` | `/user/login` | Login, retorna tokens | ❌ |
| `GET` | `/user/ver-perfil/{username}` | Perfil público | ❌ |
| `GET` | `/user/refresh` | Renova access token | ✅ |
| `PATCH` | `/user/editar-perfil` | Edita perfil | ✅ |

### Posts

| Método | Rota | Descrição | Auth |
|---|---|---|---|
| `GET` | `/principal/publicacoes` | Lista todos os posts | ❌ |
| `GET` | `/principal/imagem/{id}` | Retorna imagem de um post | ❌ |
| `POST` | `/posts/criar-post` | Cria novo post | ✅ |
| `PATCH` | `/posts/editar-post/{id}` | Edita post (só o autor) | ✅ |

---

## 🖥️ Frontend

Inclui um frontend estático em HTML/CSS/JS para demonstração visual da API.

- Feed público de posts visível sem login
- Login e cadastro via modal
- Criação de posts com upload de imagem
- Edição de posts do próprio usuário

> A API roda localmente por enquanto. Deploy em breve.

---

## 👤 Autor

Desenvolvido por **Renan Alves**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/renanalves433/)
