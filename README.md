# 🐄 Sistema de Gestão da Fazenda 🌾

Bem-vindo ao **Sistema de Gestão da Fazenda**, um projeto desenvolvido para gerenciar atividades em uma fazenda, incluindo o cadastro de animais, funcionários e manejos. Este sistema utiliza **Python**, **MySQL**, e é totalmente containerizado com **Docker Compose**.

---

## 📋 Funcionalidades

O sistema oferece as seguintes operações CRUD:

1. **Animais**:
   - Inserir novo animal.
   - Atualizar dados de um animal existente.
   - Excluir animal.
   - Consultar IDs e nomes dos animais cadastrados.

2. **Funcionários**:
   - Inserir novo funcionário.
   - Excluir (demitir) funcionário.
   - Consultar IDs e nomes dos funcionários cadastrados.

3. **Manejo**:
   - Inserir novo manejo (atividade realizada com um animal por um funcionário).
   - Excluir manejo.
   - Consultar manejos realizados, incluindo informações sobre o animal e o funcionário.

---

## 🚀 Tecnologias Utilizadas

- **Linguagem de Programação**: Python
- **Banco de Dados**: MySQL
- **Containerização**: Docker e Docker Compose

---

## 🛠️ Como Configurar e Executar

### Pré-requisitos

- Docker e Docker Compose instalados em sua máquina.

### Passo a Passo

1. **Clone o Repositório**:
   ```bash
   git clone https://github.com/seu-usuario/APMOD02_Fazenda.git
   cd APMOD02_Fazenda
   ```

2. **Inicie os Contêineres com o Docker Compose**:
   ```bash
   docker-compose up --build
   ```

   Este comando irá:
   - Construir os contêineres do MySQL e da aplicação Python.
   - Inicializar o banco de dados com as tabelas e dados pré-definidos no arquivo `init.sql`.

3. **Acesse a Aplicação**:
   - No terminal, execute:
     ```bash
     docker-compose run app python main.py
     ```
   - Navegue pelo menu interativo para realizar operações.

4. **Acesse o Banco de Dados Diretamente (Opcional)**:
   Para acessar o banco de dados diretamente pelo terminal MySQL, use:
   ```bash
   docker exec -it apmod02_fazenda_db_1 mysql -u root -p
   ```
   Insira a senha configurada (`romero13`).

---

## 🗂️ Estrutura do Projeto

```plaintext
APMOD02_Fazenda/
├── app/
│   ├── main.py            # Código principal da aplicação Python.
│   ├── requirements.txt   # Dependências do projeto.
│   ├── Dockerfile         # Dockerfile para a aplicação Python.
├── db/
│   ├── init.sql           # Script para inicializar o banco de dados.
│   ├── Dockerfile         # Dockerfile para o contêiner MySQL.
├── docker-compose.yml     # Arquivo Docker Compose para orquestração dos serviços.
└── README.md              # Documentação do projeto.
```

---

## 🐾 Exemplos de Uso

### Inserir um Novo Animal
- Escolha a opção `1` no menu.
- Insira os dados solicitados (nome, espécie e idade).
- Receba a confirmação: `✅ Animal '<nome>' inserido com sucesso!`

### Consultar Manejo por Funcionário
- Escolha a opção `3`.
- Veja um relatório detalhado com:
  - Nome do funcionário.
  - Nome do animal.
  - Atividade realizada.
  - Data do manejo.

---

## 📜 Licença

Este projeto é licenciado sob a **MIT License**. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 👨‍💻 Autor

Desenvolvido por **Thiago von Sohsten** durante o módulo de Infraestrutura de Software. 💻

---

## 🌟 Contribuições

Contribuições são bem-vindas! Siga os passos abaixo para contribuir:

1. Faça um fork do projeto.
2. Crie uma branch para a sua feature:
   ```bash
   git checkout -b minha-feature
   ```
3. Faça o commit das suas alterações:
   ```bash
   git commit -m "Adicionei uma nova feature"
   ```
4. Envie as alterações para a sua branch:
   ```bash
   git push origin minha-feature
   ```
5. Abra um Pull Request.

---

## 🛡️ Observações

- Este projeto foi desenvolvido para fins acadêmicos e serve como exemplo de aplicação CRUD com Docker.
- Certifique-se de que a porta `3306` não está em uso para evitar conflitos ao executar o contêiner do MySQL.

---

**🌻 Obrigado por explorar o Sistema de Gestão da Fazenda!**
