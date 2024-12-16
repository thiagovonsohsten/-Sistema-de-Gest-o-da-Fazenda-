import mysql.connector
from mysql.connector import Error
import time

# Configurações do banco de dados
config = {
    "user": "root",
    "password": "romero13",
    "host": "db",
    "database": "fazenda_db",
}


# Função para conectar ao banco de dados
def conectar():
    try:
        time.sleep(3)  # Pausa para garantir que o banco de dados esteja pronto
        conexao = mysql.connector.connect(**config)
        if conexao.is_connected():
            print("🌐 Conexão ao banco de dados bem-sucedida!")
        return conexao
    except Error as e:
        print("❌ Erro ao conectar ao banco de dados:", e)
        return None


# Função para inserir um novo animal
def inserir_animal():
    print("\n=== Inserir Novo Animal ===")
    try:
        conexao = conectar()
        if conexao is None:
            print("❌ Falha na conexão com o banco de dados.")
            return
        cursor = conexao.cursor()
        nome = input("Digite o nome do animal: ")
        especie = input("Digite a espécie do animal: ")
        idade = int(input("Digite a idade do animal: "))

        query = "INSERT INTO Animais (nome, especie, idade) VALUES (%s, %s, %s)"
        cursor.execute(query, (nome, especie, idade))
        conexao.commit()

        if cursor.rowcount == 1:
            print(f"✅ Animal '{nome}' inserido com sucesso!")
        else:
            print("⚠️ Ocorreu um problema ao inserir o animal.")
    except Error as e:
        print("Erro ao inserir o animal:", e)
    finally:
        if "cursor" in locals():
            cursor.close()
        if "conexao" in locals() and conexao.is_connected():
            conexao.close()


def atualizar_animal():
    print("\n=== Atualizar Dados do Animal ===")
    try:
        conexao = conectar()
        if conexao is None:
            print("❌ Falha na conexão com o banco de dados.")
            return
        cursor = conexao.cursor()

        # Exibir todos os IDs e nomes dos animais
        cursor.execute("SELECT id, nome FROM Animais")
        animais = cursor.fetchall()
        print("\n🐾 Animais Disponíveis para Atualização:")
        for animal in animais:
            print(f"ID: {animal[0]}, Nome: {animal[1]}")

        id_animal = int(input("Digite o ID do animal a ser atualizado: "))
        novo_nome = input("Digite o novo nome do animal: ")
        nova_especie = input("Digite a nova espécie do animal: ")
        nova_idade = int(input("Digite a nova idade do animal: "))

        query = "UPDATE Animais SET nome = %s, especie = %s, idade = %s WHERE id = %s"
        cursor.execute(query, (novo_nome, nova_especie, nova_idade, id_animal))
        conexao.commit()

        if cursor.rowcount == 1:
            print(f"✅ Dados do animal com ID {id_animal} atualizados com sucesso!")
        else:
            print("⚠️ Animal com ID especificado não encontrado.")
    except Error as e:
        print("Erro ao atualizar o animal:", e)
    finally:
        if "cursor" in locals():
            cursor.close()
        if "conexao" in locals() and conexao.is_connected():
            conexao.close()


# Função para inserir um novo funcionário
def inserir_funcionario():
    print("\n=== Inserir Novo Funcionário ===")
    try:
        conexao = conectar()
        if conexao is None:
            print("❌ Falha na conexão com o banco de dados.")
            return
        cursor = conexao.cursor()
        nome = input("Digite o nome do funcionário: ")
        cargo = input("Digite o cargo do funcionário: ")

        query = "INSERT INTO Funcionarios (nome, cargo) VALUES (%s, %s)"
        cursor.execute(query, (nome, cargo))
        conexao.commit()

        if cursor.rowcount == 1:
            print(f"✅ Funcionário '{nome}' inserido com sucesso!")
        else:
            print("⚠️ Ocorreu um problema ao inserir o funcionário.")
    except Error as e:
        print("Erro ao inserir o funcionário:", e)
    finally:
        if "cursor" in locals():
            cursor.close()
        if "conexao" in locals() and conexao.is_connected():
            conexao.close()


# Função para inserir um novo manejo
def inserir_manejo():
    print("\n=== Inserir Novo Manejo ===")
    try:
        conexao = conectar()
        if conexao is None:
            print("❌ Falha na conexão com o banco de dados.")
            return
        cursor = conexao.cursor()
        consultar_ids()
        animal_id = int(input("Digite o ID do animal para o manejo: "))
        funcionario_id = int(input("Digite o ID do funcionário responsável: "))
        atividade = input("Digite a atividade de manejo: ")
        data = input("Digite a data (AAAA-MM-DD): ")

        query = "INSERT INTO Manejo (animal_id, funcionario_id, atividade, data) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (animal_id, funcionario_id, atividade, data))
        conexao.commit()

        if cursor.rowcount == 1:
            print("✅ Manejo inserido com sucesso!")
        else:
            print("⚠️ Ocorreu um problema ao inserir o manejo.")
    except Error as e:
        print("Erro ao inserir o manejo:", e)
    finally:
        if "cursor" in locals():
            cursor.close()
        if "conexao" in locals() and conexao.is_connected():
            conexao.close()


# Função para consultar IDs e nomes de animais e funcionários
def consultar_ids():
    print("\n=== IDs e Nomes dos Animais e Funcionários ===")
    try:
        conexao = conectar()
        if conexao is None:
            print("❌ Falha na conexão com o banco de dados.")
            return
        cursor = conexao.cursor()

        # Consultar IDs e nomes dos Animais
        print("\n🐾 Animais:")
        cursor.execute("SELECT id, nome FROM Animais")
        animais = cursor.fetchall()
        for animal in animais:
            print(f"ID: {animal[0]}, Nome: {animal[1]}")

        # Consultar IDs e nomes dos Funcionários
        print("\n👷 Funcionários:")
        cursor.execute("SELECT id, nome FROM Funcionarios")
        funcionarios = cursor.fetchall()
        for funcionario in funcionarios:
            print(f"ID: {funcionario[0]}, Nome: {funcionario[1]}")

    except Error as e:
        print("Erro ao consultar IDs:", e)
    finally:
        if "cursor" in locals():
            cursor.close()
        if "conexao" in locals() and conexao.is_connected():
            conexao.close()


def consultar_manejo_funcionario():
    print("\n=== Consultar Manejo por Funcionário ===")
    try:
        conexao = conectar()
        if conexao is None:
            print("❌ Falha na conexão com o banco de dados.")
            return
        cursor = conexao.cursor()
        query = """
            SELECT f.nome AS Funcionario, a.nome AS Animal, m.atividade, m.data
            FROM Manejo m
            JOIN Funcionarios f ON m.funcionario_id = f.id
            JOIN Animais a ON m.animal_id = a.id
            ORDER BY m.data DESC
        """
        cursor.execute(query)
        resultados = cursor.fetchall()

        if resultados:
            print("📝 Relatório de Manejo por Funcionário:")
            for linha in resultados:
                print(
                    f"Funcionario: {linha[0]}, Animal: {linha[1]}, Atividade: {linha[2]}, Data: {linha[3]}"
                )
        else:
            print("⚠️ Nenhum registro de manejo encontrado.")
    except Error as e:
        print("Erro ao consultar manejo:", e)
    finally:
        if "cursor" in locals():
            cursor.close()
        if "conexao" in locals() and conexao.is_connected():
            conexao.close()


def excluir_animal():
    print("\n=== Excluir Animal ===")
    try:
        conexao = conectar()
        if conexao is None:
            print("❌ Falha na conexão com o banco de dados.")
            return
        cursor = conexao.cursor()

        # Exibir todos os IDs e nomes dos animais
        cursor.execute("SELECT id, nome FROM Animais")
        animais = cursor.fetchall()
        print("\n🐾 Animais Disponíveis para Exclusão:")
        for animal in animais:
            print(f"ID: {animal[0]}, Nome: {animal[1]}")

        id_animal = int(input("Digite o ID do animal a ser excluído: "))

        query = "DELETE FROM Animais WHERE id = %s"
        cursor.execute(query, (id_animal,))
        conexao.commit()

        if cursor.rowcount == 1:
            print(f"🗑️ Animal com ID {id_animal} excluído com sucesso!")
        else:
            print("⚠️ Animal com ID especificado não encontrado.")
    except Error as e:
        print("Erro ao excluir o animal:", e)
    finally:
        if "cursor" in locals():
            cursor.close()
        if "conexao" in locals() and conexao.is_connected():
            conexao.close()


# Função para excluir um funcionário
def excluir_funcionario():
    print("\n=== Demitir Funcionário ===")
    try:
        conexao = conectar()
        if conexao is None:
            print("❌ Falha na conexão com o banco de dados.")
            return
        cursor = conexao.cursor()
        consultar_ids()  # Mostrar IDs dos funcionários para ajudar na seleção
        id_funcionario = int(input("Digite o ID do funcionário a ser demitido: "))

        query = "DELETE FROM Funcionarios WHERE id = %s"
        cursor.execute(query, (id_funcionario,))
        conexao.commit()

        if cursor.rowcount == 1:
            print(f"👋 Funcionário com ID {id_funcionario} demitido com sucesso!")
        else:
            print("⚠️ Funcionário com ID especificado não encontrado.")
    except Error as e:
        print("Erro ao demitir o funcionário:", e)
    finally:
        if "cursor" in locals():
            cursor.close()
        if "conexao" in locals() and conexao.is_connected():
            conexao.close()


def excluir_manejo():
    print("\n=== Excluir Manejo ===")
    try:
        conexao = conectar()
        if conexao is None:
            print("❌ Falha na conexão com o banco de dados.")
            return
        cursor = conexao.cursor()

        # Consulta para obter detalhes do manejo com o nome do animal e do funcionário
        cursor.execute(
            """
            SELECT m.id, m.atividade, m.data, a.nome AS animal_nome, f.nome AS funcionario_nome
            FROM Manejo m
            JOIN Animais a ON m.animal_id = a.id
            JOIN Funcionarios f ON m.funcionario_id = f.id
        """
        )
        manejos = cursor.fetchall()

        print("\n🌱 Manejos:")
        for manejo in manejos:
            print(
                f"ID: {manejo[0]}, Atividade: {manejo[1]}, Data: {manejo[2]}, Animal: {manejo[3]}, Funcionário: {manejo[4]}"
            )

        id_manejo = int(input("Digite o ID do manejo a ser excluído: "))

        query = "DELETE FROM Manejo WHERE id = %s"
        cursor.execute(query, (id_manejo,))
        conexao.commit()

        if cursor.rowcount == 1:
            print(f"🗑️ Manejo com ID {id_manejo} excluído com sucesso!")
        else:
            print("⚠️ Manejo com ID especificado não encontrado.")
    except Error as e:
        print("Erro ao excluir o manejo:", e)
    finally:
        if "cursor" in locals():
            cursor.close()
        if "conexao" in locals() and conexao.is_connected():
            conexao.close()


# Função para exibir o menu interativo e temático
def menu():
    while True:
        print("\n===============================")
        print("🌾 Bem-vindo ao Sistema de Gestão da Fazenda 🌾")
        print("===============================")
        print("1. 🐄 Inserir Novo Animal")
        print("2. 📝 Atualizar Dados de um Animal")
        print("3. 🔍 Consultar Manejo por Funcionário")
        print("4. 🗑️ Excluir Animal")
        print("5. 👷 Inserir Novo Funcionário")
        print("6. 🌱 Inserir Novo Manejo")
        print("7. 📋 Consultar IDs de Animais e Funcionários")
        print("8. 👋 Demitir Funcionário")  # Nova opção para excluir funcionário
        print("9. 🗑️ Excluir Manejo")  # Nova opção para excluir manejo
        print("0. ❌ Sair")
        print("===============================")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            inserir_animal()
        elif opcao == "2":
            atualizar_animal()
        elif opcao == "3":
            consultar_manejo_funcionario()
        elif opcao == "4":
            excluir_animal()
        elif opcao == "5":
            inserir_funcionario()
        elif opcao == "6":
            inserir_manejo()
        elif opcao == "7":
            consultar_ids()
        elif opcao == "8":
            excluir_funcionario()  # Chama a nova função de excluir funcionário
        elif opcao == "9":
            excluir_manejo()  # Chama a nova função de excluir manejo
        elif opcao == "0":
            print("Encerrando o sistema... Até logo! 🌻")
            break
        else:
            print("🚫 Opção inválida! Tente novamente.")


if __name__ == "__main__":
    menu()
