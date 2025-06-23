
### **1. Verificar se o Python está instalado**

  ```bash
  python --version
  ```
  Ou, em alguns sistemas, pode ser:

  ```bash
  python3 --version
  ```

### **2. Executar um script Python no terminal**

  ```bash
  python script.py
  ```
  Ou, para versões específicas:

  ```bash
  python3 script.py
  ```

### **3. Abrir o interpretador Python (REPL)**

  ```bash
  python
  ```
  Ou:

  ```bash
  python3
  ```

### **4. Instalar pacotes com pip**

  Para instalar um pacote específico:

  ```bash
  pip install nome_do_pacote
  ```
  Para instalar pacotes listados em um arquivo `requirements.txt`:

  ```bash
  pip install -r requirements.txt
  ```

### **5. Atualizar um pacote com pip**

  ```bash
  pip install --upgrade nome_do_pacote
  ```

### **6. Criar um ambiente virtual**

  Para criar um ambiente virtual (importante para isolar dependências):

  ```bash
  python -m venv nome_do_ambiente
  ```

  Ativar o ambiente:

  * **Windows:**

    ```bash
    nome_do_ambiente\Scripts\activate
    ```
  * **Linux/MacOS:**

    ```bash
    source nome_do_ambiente/bin/activate
    ```

### **7. Desativar o ambiente virtual**

  ```bash
  deactivate
  ```

### **8. Verificar quais pacotes estão instalados**

  ```bash
  pip list
  ```

### **9. Instalar uma versão específica de um pacote**

  ```bash
  pip install nome_do_pacote==versao
  ```

### **10. Gerar um arquivo `requirements.txt`**

  Para gerar um arquivo `requirements.txt` com todos os pacotes instalados no ambiente:

  ```bash
  pip freeze > requirements.txt
  ```

### **11. Atualizar o Python**

* **Comando (Linux, usando o apt-get):**

  ```bash
  sudo apt update
  sudo apt upgrade python3
  ```

### **12. Verificar dependências de pacotes**

  Para verificar as dependências de um pacote:

  ```bash
  pip show nome_do_pacote
  ```

### **13. Executar um script diretamente no terminal (sem criar um arquivo)**

  ```bash
  python -c "print('Hello, World!')"
  ```

### **14. Rodar um servidor local (para desenvolvimento web, por exemplo)**

* **Comando (para um servidor básico com o Python):**

  ```bash
  python -m http.server
  ```

### **15. Verificar a ajuda de um comando ou módulo**

  Para obter ajuda sobre um módulo:

  ```bash
  python -m pydoc nome_do_modulo
  ```

### **16. Comando para sair do Python REPL**

  ```bash
  exit()
  ```

  Ou:

  ```bash
  quit()
  ```