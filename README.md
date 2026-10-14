# Sistema de Gestão de Tarefas

Sistema desenvolvido em Django para gerenciamento de tarefas e categorias, utilizando persistência de dados com SQLite e relacionamento entre entidades através de ForeignKey.

## Funcionalidades

- Cadastro de categorias
- Cadastro de tarefas
- Associação de tarefas a categorias
- Gerenciamento através do Django Admin
- Persistência dos dados em banco SQLite
- Consultas utilizando Django ORM

## Tecnologias Utilizadas

- Python 3
- Django
- SQLite3
- Git/GitHub

---

## Como executar o projeto

### 1. Criar o ambiente virtual

Windows:

```bash
python -m venv venv
```

---

### 2. Ativar o ambiente virtual

Windows PowerShell:

```bash
venv\Scripts\Activate.ps1
```

Windows CMD:

```bash
venv\Scripts\activate
```

---

### 3. Instalar as dependências

```bash
pip install django
```

---

### 4. Aplicar as migrações

Como o banco de dados não é enviado para o repositório, é necessário recriá-lo executando:

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

---

### 6. Criar um usuário administrador

```bash
python manage.py createsuperuser
```

Preencha:

```text
Username
Email
Password
```

---

### 7. Executar o servidor

```bash
python manage.py runserver
```

O sistema estará disponível em:

```text
http://127.0.0.1:8000/
```

Painel administrativo:

```text
http://127.0.0.1:8000/admin/
```

---

## Estrutura do Projeto

```text
gestao_tarefas/
│
├── manage.py
├── gestao_tarefas/
├── tarefas/
├── templates/
└── README.md
```

---

## Evidência de Consulta ORM

Exemplo de consulta filtrando tarefas pendentes:

```python
from tarefas.models import Tarefa

Tarefa.objects.filter(situacao='PENDENTE')
```

---

## Evidência de Atualização de Dados

Exemplo de alteração de situação de uma tarefa:

```python
tarefa = Tarefa.objects.filter(
    situacao='PENDENTE'
).first()

tarefa.situacao = 'CONCLUIDA'
tarefa.save()
```

---

# Registro da Atividade

## Dificuldade Encontrada

Durante o desenvolvimento houve dificuldade na criação do usuário administrador pelo comando `createsuperuser`, pois o terminal não exibe os caracteres digitados durante a inserção da senha.

## Solução Aplicada

Foi verificado que esse comportamento é padrão do Django por motivos de segurança. A senha foi digitada normalmente e confirmada, permitindo a criação do superusuário sem problemas.

## Resultado

O sistema foi desenvolvido com sucesso utilizando Django ORM. As categorias e tarefas foram persistidas em banco de dados SQLite, permitindo consultas, atualizações e manutenção dos dados através do Django Admin.
