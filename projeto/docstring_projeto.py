from cores import (Reset, Azul, AmareloClaro, Magenta, Verde)

print(f"""\n\n{Azul}🤖 Projeto — Automação de Cadastro de Produtos com Python
{Reset}

{AmareloClaro}🎯 Objetivo:
Automatizar o processo de cadastro de produtos em um sistema web
utilizando Python, lendo os dados de um arquivo CSV e inserindo
automaticamente cada produto nos campos do formulário.
{Reset}

{Magenta}📚 Bibliotecas utilizadas e suas funções:

- 🐍 Python: Linguagem principal do projeto.
- 🐼 Pandas: Leitura e manipulação da base de dados (Produtos.csv).
- 🧭 PyAutoGUI: Simula ações humanas no computador (cliques, digitação, navegação).
- 📎 PyperClip: Permite copiar e colar textos com mais estabilidade que o .write().
- ⏰ from time import sleep: Controla pausas entre as ações automatizadas.
- 💻 OS: Abre o navegador e interage com o sistema operacional.
- 📊 OpenPyXL: Suporte para leitura e escrita de arquivos Excel quando necessário.
{Reset}

{AmareloClaro}📝 Passo a passo da automação:

1️⃣ Acessar o sistema da empresa:
- 🌐 Abrir o navegador Google Chrome;
- 🔗 Digitar o link do sistema;
- ⌛ Aguardar o carregamento da página.

2️⃣ Realizar o login:
- 📧 Preencher o campo de e-mail;
- 🔐 Preencher a senha;
- 🖱️ Enviar o formulário de login.

3️⃣ Importar a base de dados:
- 📂 Localizar o arquivo Produtos.csv;
- 📄 Ler os dados com Pandas;
- 📋 Armazenar os produtos na variável tabela_dados.

4️⃣ Cadastrar os produtos automaticamente:
- 🔁 Percorrer cada linha do CSV;
- 🏷️ Preencher código, marca, tipo, categoria, preço e custo;
- 📝 Inserir observações quando existirem;
- 📤 Enviar o formulário para cadastrar o produto.

5️⃣ Repetir o processo:
- 🔄 Após cada cadastro, o sistema volta ao topo;
- 🧭 O script reposiciona o foco corretamente;
- 🚀 O loop continua até todos os produtos serem cadastrados.
{Reset}

{Verde}✅ Automação finalizada com sucesso!
Todos os produtos do arquivo CSV foram inseridos no sistema.
{Reset}
""")
