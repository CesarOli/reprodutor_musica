import mysql.connector
import requests
from time import sleep

config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'SENHA_DESEJADA',
    'database': 'reprodutor-musica'
}

while True:
    print("========== Reprodutor de Música ==========")
    print("1. Adicionar Música")
    print("2. Pesquisar Música")
    print("3. Listar Todas as Músicas")
    print("0. Sair")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        print("Adicionar Música")

        titulo = input("Digite o título da música: ")
        artista = input("Digite o nome do artista: ")

        escolha = input("Voltar para o menu? (S/N): ")
        if escolha.lower() != "s":
            break
    else:
        print("Opção inválida. Digite novamente.")

print("Fim do programa.")


        