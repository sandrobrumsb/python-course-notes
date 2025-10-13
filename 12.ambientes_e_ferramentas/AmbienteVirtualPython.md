# Ambiente Virtual Python

Ambientes virtuais permitem criar espaços isolados para cada projeto Python, facilitando o gerenciamento de dependências e evitando conflitos entre projetos.

## Vantagens do ambiente virtual

- Isolamento de pacotes e dependências
- Permite diferentes versões de pacotes em projetos distintos
- Mantém a instalação global do Python limpa
- Facilita testes e portabilidade

---

## 1. Criando um ambiente virtual

O Python possui o módulo integrado `venv` para criar ambientes virtuais.

**Windows:**

```powershell
python -m venv meu_projeto
```

**macOS/Linux:**

```bash
python3 -m venv meu_projeto
```

Isso criará uma pasta chamada `meu_projeto` com a estrutura do ambiente virtual.

**Estrutura de pastas:**

```
meu_projeto/
├── Include/
├── Lib/
├── Scripts/ (Windows) ou bin/ (Linux/Mac)
├── pyvenv.cfg
```

---

## 2. Ativando o ambiente virtual

**Windows:**

```powershell
meu_projeto\Scripts\activate
```

**macOS/Linux:**

```bash
source meu_projeto/bin/activate
```

Após ativar, o prompt indicará que você está no ambiente virtual.

---

## 3. Instalando pacotes

Com o ambiente ativado, instale pacotes usando o `pip`:

```powershell
pip install cowsay
```

---

## 4. Usando pacotes instalados

Crie um arquivo chamado `teste.py` e adicione:

```python
import cowsay
cowsay.cow("Bom dia, Pythonista!")
```

Execute o arquivo dentro do ambiente virtual:

```powershell
python teste.py
```

**Saída esperada:**

```
  _______________________
< Bom dia, Pythonista! >
  ======================
                 \
                  \
                    ^__^
                    (oo)\_______
                    (__)\       )\/\
                        ||----w |
                        ||     ||
```

---

## 5. Desativando e excluindo o ambiente virtual

**Desativar:**

```powershell
deactivate
```

**Excluir:**

```powershell
rmdir /s /q meu_projeto
```

# 1. Criando um ambiente virtual.

# O Python tem o módulo integrado venvpara criar ambientes virtuais.

# Para criar um ambiente virtual no seu computador, abra o prompt de comando, navegue até a pasta onde deseja criar seu projeto e digite este comando:

windows: C:\Users\Your Name> python -m venv myfirstproject
macOS/Linux:

# Isso configurará um ambiente virtual e criará uma pasta chamada "myfirstproject" com subpastas e arquivos, como este:

# Resultado:

A estrutura do arquivo/pasta ficará assim:

myfirstproject
Include
Lib
Scripts
.gitignore
pyvenv.cfg

# Ativar ambiente virtual

Para usar o ambiente virtual, você deve ativá-lo com este comando:

Windows: C:\Users\Your Name> myfirstproject\Scripts\activate
macOS/Linux

Após a ativação, seu prompt mudará para mostrar que agora você está trabalhando no ambiente ativo

# Instalar pacotes:

## Depois que seu ambiente virtual estiver ativado, você poderá instalar pacotes nele usando pip.

# exemplo: Instalaremos um pacote chamado 'cowsay':

(myfirstproject) C:\Users\Your Name> pip install cowsay

# Resultado:

--
Collecting cowsay
Downloading cowsay-6.1-py3-none-any.whl.metadata (5.6 kB)
Downloading cowsay-6.1-py3-none-any.whl (25 kB)
Installing collected packages: cowsay
Successfully installed cowsay-6.1

[notice] A new release of pip is available: 25.0.1 -> 25.1.1
[notice] To update, run: python.exe -m pip install --upgrade pip
--

# Usando o pacote

Agora que o módulo 'cowsay' está instalado no seu ambiente virtual, vamos usá-lo para exibir uma vaca falante.

Crie um arquivo chamado test.pyno seu computador. Você pode colocá-lo onde quiser, mas eu o colocarei no mesmo local da myfirstprojectpasta — não na pasta, mas no mesmo local.

Abra o arquivo e insira estas três linhas nele:

import cowsay

cowsay.cow("Good Mooooorning!")

Em seguida, tente executar o arquivo enquanto estiver no ambiente virtual:

(myfirstproject) C:\Users\Your Name> python test.py

Resultado:

--

---

  _________________
| Good Mooooorning! |
  =================
                 \
                  \
                    ^__^
                    (oo)\_______
                    (__)\       )\/\
                        ||----w |
                        ||     ||
--

Desativar ambiente virtual : (myfirstproject) C:\Users\Your Name> deactivate

Excluir ambiente virtual: rmdir /s /q myfirstproject
