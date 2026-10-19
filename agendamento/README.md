# 📅 Sistema de Agendamento Automatizado (Consultas e Reuniões)

Um sistema completo de agendamento desenvolvido em **Python** e **Flask**, voltado para a marcação flexível de consultas ou reuniões. O projeto conta com autenticação segura via **JWT (JSON Web Tokens)**, separação de níveis de acesso (Clientes e Funcionários/Admin), notificações automáticas na véspera do compromisso via **WhatsApp, SMS e E-mail**, além de gestão completa de cancelamentos e reagendamentos.

## 🚀 Funcionalidades Principais

* **Autenticação Segura (JWT) e Perfis de Acesso:**

  * Autenticação via **JWT (Flask-JWT-Extended)** com controle de expiração e rotas protegidas.

  * Área exclusiva para **Clientes** (agendamento e gestão das suas marcações).

  * Painel exclusivo para **Funcionários e Administração** (gestão de horários, visão interna da empresa).

* **CRUD Completo de Agendamentos:**

  * Criação, visualização, atualização e cancelamento de marcações.

* **Notificações Automáticas (24h antes):**

  * Automação via **APScheduler** para verificação diária de agendamentos próximos.

  * Envio de alertas de lembrete via **WhatsApp** e **SMS** (Twilio API).

  * Envio de lembretes por **E-mail** (Yagmail).

* **Gestão e Reengajamento de Cancelamentos:**

  * Tabela dedicada para agendamentos cancelados com script voltado para entrar em contato e realizar o reagendamento.

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python

* **Framework Web:** Flask

* **Autenticação:** Flask-JWT-Extended & Flask-Bcrypt (criptografia de senhas)

* **Banco de Dados:** SQL (SQLAlchemy / SQLite / PostgreSQL)

* **Agendamento de Tarefas:** APScheduler

* **Integrações de Comunicação:**

  * Twilio API (WhatsApp e SMS)

  * Yagmail (Notificações por E-mail)

## 🗄️ Estrutura do Banco de Dados

O banco de dados é estruturado em **4 tabelas principais**:

1. `clientes`: Cadastro dos usuários finais/clientes que utilizam o sistema.

2. `funcionarios`: Cadastro de funcionários e administradores internos da empresa.

3. `agendamentos_confirmados`: Registros dos agendamentos e reuniões/consultas ativas.

4. `agendamentos_cancelados`: Histórico de agendamentos cancelados, utilizado pelo script de pós-atendimento para contato de reagendamento.

## 📁 Estrutura de Pastas do Projeto

```
meu-projeto/
│
├── .gitignore
├── README.md
├── requirements.txt
├── main.py (ou app.py)
│
├── config/             # Configurações gerais e parâmetros
├── database/           # Conexão e modelos do banco de dados (Models)
├── routes/             # Rotas/Endpoints da aplicação (Views protegidas por JWT)
├── services/           # Lógica de automação (APScheduler, Twilio, Yagmail)
└── static/             # Arquivos estáticos (CSS, JS, Imagens)
```

## ⚙️ Como Executar o Projeto Localmente

### 1. Pré-requisitos

* Python 3.8+ instalado.

### 2. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 3. Criar e ativar o ambiente virtual

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux / macOS
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 5. Configurar as Variáveis de Ambiente (`.env`)

Crie um arquivo `.env` na raiz do projeto com as suas credenciais:

```env
SECRET_KEY=sua_chave_secreta_flask
JWT_SECRET_KEY=sua_chave_secreta_jwt
DATABASE_URL=sqlite:///database.db

# Configurações Twilio (WhatsApp / SMS)
TWILIO_ACCOUNT_SID=seu_account_sid
TWILIO_AUTH_TOKEN=seu_auth_token
TWILIO_PHONE_NUMBER=seu_numero_twilio
TWILIO_WHATSAPP_NUMBER=whatsapp:+14155238886

# Configurações E-mail (Yagmail)
EMAIL_USER=seu_email@gmail.com
EMAIL_PASSWORD=sua_senha_de_app
```

### 6. Executar a aplicação

```bash
python main.py
```

Acesse a aplicação no seu navegador em: `http://127.0.0.1:5000`

---

### 🔒 Autenticação via API (JWT)

Nas requisições para rotas protegidas, envie o token de acesso no cabeçalho (Header):

```http
Authorization: Bearer <seu_jwt_token>
```

## 📝 Licença

Este projeto está sob a licença MIT. Sinta-se à vontade para colaborar ou utilizar para aprendizado.