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
    sleep(0.8)
    print("Aguarde, abrindo menu de opções")
    sleep(1.5)
    print("1. Adicionar Música")
    sleep(0.3)
    print("2. Pesquisar Música")
    sleep(0.3)
    print("3. Listar Todas as Músicas")
    sleep(0.3)
    print("0. Sair")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        print("Adicionar Música")

        titulo = input("Digite o título da música: ")
        artista = input("Digite o nome do artista: ")

        escolha = input("Voltar para o menu? (S/N): ")
        if escolha.lower() != "s":
            break

    elif opcao == "0":
        break
    else:
        print("Opção inválida. Digite novamente.")
print("Encerrando o programa...")
sleep(1)
print("Obrigado!!")
sleep(1.5)
print("Fim do programa.")


        