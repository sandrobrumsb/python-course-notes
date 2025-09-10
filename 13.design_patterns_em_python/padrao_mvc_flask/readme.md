# Padrão MVC em Flask

**Passo 1:** Criar a estrutura de diretórios do padrão MVC:

```
padrao_mvc_flask/
├── app.py
│   config.py
│   readme.md
├── controllers/
│     └── user_controller.py
├── models/
│     └── user.py
└── view/
	└── template/
		├── contact.html
		└── index.html

```

**Descrição das Pastas:**

- `controllers/`: Lógica de controle e rotas da aplicação.
- `models/`: Definição das classes e manipulação dos dados.
- `view/template/`: Templates HTML para renderização das páginas.
- `app.py`: Arquivo principal para inicialização da aplicação Flask.
- `config.py`: Configurações da aplicação.

**Passo 2:** Implementar o modulo principal da aplicação: `app.py`
**Passo 3:** criar rota para da aplicação: `em controllers`
**Passo 4:** construir a parte do models: `responsavel pelos dados da aplicação`

---
