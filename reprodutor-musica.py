import mysql.connector
from time import sleep

config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'SENHA_DESEJADA',
    'database': 'reprodutor-musica'
}
conexao = mysql.connector.connect(**config)
cursor = conexao.cursor()

cursor.execute("SHOW TABLES")
tabelas = cursor.fetchall()

tabela_musica_existe = False
for tabela in tabelas:
    if tabela[0] == 'musicas':
        tabela_musica_existe = True
        break

if not tabela_musica_existe:
    cursor.execute("CREATE TABLE IF NOT EXISTS Musicas (id INT AUTO_INCREMENT PRIMARY KEY, titulo VARCHAR(255), artista VARCHAR(255))")

print("=" * 50)
print("Bem Vindo ao seu 'Reprodutor de Música'!")
print("=" * 50)
print()

while True:
    sleep(0.8)
    print("Aguarde, abrindo menu de opções...")
    print()
    print("=" * 50)
    print()
    sleep(1.5)
    print("1. Adicionar Música")
    print()
    sleep(0.3)
    print("2. Pesquisar Música")
    print()
    sleep(0.3)
    print("3. Listar Todas as Músicas")
    print()
    sleep(0.3)
    print("0. Sair")
    print()
    opcao = input("Digite o número da opção desejada: ")

    if opcao.isdigit():
        opcao = int(opcao)

        if opcao == 1:
            print("Adicionar Música")

            titulo = input("Digite o título da música: ")
            artista = input("Digite o nome do artista: ")

            sql = "INSERT INTO Musicas (titulo, artista) VALUES (%s, %s)"
            valores = (titulo, artista)
            cursor.execute(sql, valores)
            conexao.commit()

            print("Música adicionada com Sucesso!!")

            escolha = input("Voltar para o menu? (S/N): ")
            if escolha.lower() != "s":
                break

        elif opcao == 2:
            print("Pesquisar Música")

            titulo = input("Digite o título da música: ")

            sql = "SELECT * FROM Musicas WHERE titulo = %s"
            valores = (titulo,)
            cursor.execute(sql, valores)
            resultado = cursor.fetchall()

            if resultado:
                for musica in resultado:
                     if resultado:
                        for musica in resultado:
                            print("Título:", musica[1])
                            print("Artista:", musica[2])
            else:
                print("Nenhuma música cadastrada.")

        elif opcao == 3:
            print("Listar Todas as Músicas")

            cursor.execute("SELECT * FROM Musicas")
            resultado = cursor.fetchall()

            if resultado:
                for musica in resultado:
                    print("Título:", musica[1])
                    sleep(0.5)
                    print("Artista:", musica[2])
            else:
                print("Nenhuma música cadastrada.")

        elif opcao == 0:
            break

    else:
        print("Opção inválida. Digite novamente.")

print("Encerrando o programa...")
sleep(1)
print("Obrigado!!")
sleep(1.5)
print("Fim do programa.")
