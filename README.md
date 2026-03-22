# README.md - Sistema de Apoio ao Foco em Objetivos Pessoais

🎯 Um sistema completo de aplicação web para gerenciar seus objetivos pessoais, inspirar-se com personagens, rastrear habilidades necessárias e acompanhar atividades diárias.

## 🚀 Stack Técnica

- **Backend**: FastAPI (Python 3.11) + SQLAlchemy + MySQL 8.0 + JWT Authentication
- **Frontend**: React 18 + TypeScript + Axios + React Router + Tailwind CSS + Zustand
- **Infra**: Docker + Docker Compose + VS Code Dev Containers
- **Arquitetura**: API-first (backend e frontend separados)

## ⚡ Quick Start

```bash
# Clone o repositório
git clone https://github.com/danielexpe/desenvolvimento-pessoal-001.git
cd desenvolvimento-pessoal-001

# Inicie todos os serviços
docker-compose up -d

# Aguarde ~30 segundos para inicialização

# Acesse:
# Frontend: http://localhost:3000
# Backend: http://localhost:8000
# API Docs: http://localhost:8000/docs
```

## 📁 Estrutura do Projeto

```
projeto-foco-objetivos/
├��─ backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── core/
│   │   │   ├── __init__.py
│   │   │   ├── config.py
│   │   │   └── security.py
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── base.py
│   │   │   ├── user.py
│   │   │   ├── objetivo.py
│   │   │   ├── personagem.py
│   │   │   ├── ponto_forte.py
│   │   │   ├── habilidade.py
│   │   │   └── atividade.py
│   │   ├── schemas/
│   │   │   ├── __init__.py
│   │   │   ├── user.py
│   │   │   ├── objetivo.py
│   │   │   ├── personagem.py
│   │   │   ├── ponto_forte.py
│   │   │   ├── habilidade.py
│   │   │   └── atividade.py
│   │   ├── routers/
│   │   │   ├── __init__.py
│   │   │   ├── auth.py
│   │   │   ├── objetivos.py
│   │   │   ├── personagens.py
│   │   │   ├── pontos_fortes.py
│   │   │   ├── habilidades.py
│   │   │   └── atividades.py
│   │   └── database/
│   │       ├── __init__.py
│   │       └── session.py
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── hooks/
│   │   ├── store/
│   │   └── utils/
│   ├── package.json
│   └── Dockerfile
├── docker-compose.yml
├── .devcontainer/
│   └── devcontainer.json
└── README.md
```

## 🔐 Autenticação

- JWT local com email/senha
- Registro de novo usuário
- Middleware de autenticação para rotas protegidas
- Refresh tokens com validade estendida

## 📋 Endpoints Disponíveis

### Autenticação
```
POST   /auth/register          # Registrar novo usuário
POST   /auth/login             # Login com email/senha
GET    /auth/me                # Obter dados do usuário autenticado
```

### Objetivos
```
POST   /objetivos/             # Criar novo objetivo
GET    /objetivos/             # Listar objetivos do usuário
GET    /objetivos/{id}         # Obter detalhes de um objetivo
PUT    /objetivos/{id}         # Atualizar objetivo
DELETE /objetivos/{id}         # Deletar objetivo
```

## 🛠️ Comandos Úteis

```bash
# Ver logs
docker-compose logs -f backend

# Parar todos os serviços
docker-compose down

# Remover volumes (limpar banco de dados)
docker-compose down -v

# Reconstruir imagens
docker-compose up -d --build
```

## 📊 Dados Iniciais

Usuário admin pré-configurado:
- Email: admin@example.com
- Senha: admin123

## 📖 Documentação da API

Acesse em: http://localhost:8000/docs (Swagger UI)

---
**Última atualização**: 2026-03-22