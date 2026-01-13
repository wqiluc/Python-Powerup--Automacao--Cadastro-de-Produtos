<h1 align="center">
  <span style="color:#FFD43B;">Jornada Python (Hashtag Treinamentos) — Projeto 1</span> <br>
  <span style="color:#306998;">Automação de Cadastro de Produtos</span> <br>
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" width="36" style="vertical-align:middle;"/>🛒🛍️
</h1>

<p align="center">
  <img src="img/Jornada Python_logo1.jpeg" alt="Logo centro" height="350">
</p>


<p align="center">
Aplicação real em Python para <strong>automatizar o cadastro de produtos em um sistema web</strong>,
integrando planilhas CSV e simulando ações humanas no navegador com PyAutoGUI e outras funcionalidades. <br>
🤖✅📦💻  
<br><br>
<img src="https://img.shields.io/badge/-Python-3776AB?style=for-the-badge&logo=python&logoColor=black" width="75"/>
</p>

<h2 align="center">👨🏻‍💻 Autor deste Repositório: </h2>
<div align="center">
<strong>Lucas Paguetti Pereira</strong> 🧙‍♂️<br>
🏫 <strong>Instituição:</strong> Cesar School 🎓🧡<br>
📍 Recife, Pernambuco — <strong>Brazil</strong> 🇧🇷  
<br><br>

<a href="https://www.instagram.com/lucpaguetti/">
  <img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white" height="32">
</a>
<a href="https://github.com/wqiluc">
  <img src="https://img.shields.io/badge/GitHub-000000?style=for-the-badge&logo=github&logoColor=white" height="32">
</a>
<a href="https://www.linkedin.com/in/lucas-paguetti-pereira-70267339b/">
  <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" height="32">
</a>
<a href="mailto:lpp2@cesar.school">
  <img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=black" height="32">
</a>
<a href="https://discord.com/users/lucaspaguettipereira">
  <img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=black" height="32">
</a>
</div>


<h2 align="center">🌐 Hashtag Treinamentos: </h2>

<div align="center">
<a href="https://www.hashtagtreinamentos.com">
  <img src="img/Hashtag_logo.jpeg" height="32" alt="Hashtag Treinamentos">
</a>
<a href="https://www.youtube.com/@HashtagProgramacao">
  <img src="https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=black" height="32">
</a>
<a href="https://www.instagram.com/hashtagtreinamentos/">
  <img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white" height="32">
</a>
<a href="https://www.linkedin.com/company/hashtag-treinamentos/">
  <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" height="32">
</a>
</div>


<h2 align="center">🎯 Objetivo do Projeto: </h2>

<p align="center">
Automatizar completamente o processo de <strong>cadastro de produtos</strong> em um sistema web, lendo os dados de um
arquivo <strong>Produtos.csv</strong> e preenchendo automaticamente todos os campos do formulário utilizando: Python,
Pandas e PyAutoGUI. ✅🧭🤖
</p>

<h2 align="center">📁 Estrutura do Projeto: </h2>

<pre>
Python Powerup - Automação Cadastro de Produtos/
├── img/
│   ├── Hashtag_logo.jpeg
│   ├── Jornada Python_logo1.jpeg
├── projeto/
│   ├── __pycache__/
│   ├── automação.py
│   ├── apoio.py
│   ├── docstring_projeto.py
│   ├── docstring_projeto.ipynb
│   ├── cores.py
├── Produtos.csv   
├── readme.md
└── license (MIT)
<img src="https://img.shields.io/badge/-Arquitetura-111827?style=flat-square&logo=databricks&logoColor=white"
style="vertical-align:middle; margin-left:5px;"/>
</pre>

<h2 align="center">⛏️💻 Ferramentas Utilizadas: </h2>

<div align="center">
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/vscode/vscode-original.svg" width="28"/>
<img src="https://img.shields.io/badge/-Python-3776AB?style=for-the-badge&logo=python&logoColor=black" height="28"/>
<img src="https://img.shields.io/badge/-Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" height="28"/>
<img src="https://img.shields.io/badge/-PyAutoGUI-FF4500?style=for-the-badge&logo=python&logoColor=white" height="28"/>
<img src="https://img.shields.io/badge/-Pyperclip-4B0082?style=for-the-badge&logo=python&logoColor=white" height="28"/>
<img src="https://img.shields.io/badge/-OpenPyXL-32CD32?style=for-the-badge&logo=python&logoColor=white" height="28"/>
<img src="https://img.shields.io/badge/Automação%20de%20captação%20de%20dados%20em%20listas%20CSV-FFD43B?style=for-the-badge&logo=python&logoColor=black" height="28"/> <br>
<img src="https://img.shields.io/badge/-Git-F05032?style=for-the-badge&logo=git&logoColor=black" height="28"/>
<img src="https://img.shields.io/badge/-GitHub-000000?style=for-the-badge&logo=github&logoColor=white" height="28"/>
</div>

<br>


<h2 align="center">⚙️🤖 Como a automação funciona e como rodar o projeto: </h2>

Este projeto simula um **usuário humano operando um sistema web**, preenchendo automaticamente o formulário de cadastro de produtos a partir de um arquivo CSV.

O fluxo executado pelo robô é o seguinte🧭:

1. O Python abre o navegador Google Chrome automaticamente✅
2. Acessa o sistema da empresa em: `https://dlp.hashtagtreinamentos.com/python/intensivao/login`  
3. Preenche o e-mail e a senha nos campos de login `(open source, apenas pra testes)` 
4. Acessa o formulário de cadastro de produtos  
5. Lê o arquivo `Produtos.csv` com Pandas 🐼  
6. Para cada linha do CSV, preenche: `código, marca, tipo, categoria, preço, custo e observações`  
7. Envia o formulário 🔄
8. O processo se repete até todos os produtos serem cadastrados  

Ao final, todos os produtos do CSV estarão registrados no sistema automaticamente. ✅🌐


<h2 align="center">🫵 Como rodar na sua máquina: </h2>

```bash
"python --version"
"pip install: pandas, pyautogui(pyperclip vem incluso), openpyxl"
Produtos.csv:
    "itens:" codigo, marca, tipo, categoria, preco_unitario, custo, obs
"Salvar o Arquivo em: "
/Users/seu_usuario/Downloads/Produtos.csv
"ou como já está em seu sistema operacional!📲"