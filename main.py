from dados import transacoes, fila_pendentes, pilha_pagamentos, TIPOS, STATUS, CATEGORIAS
from tarefas import cadastra_transacao, listar_trasacoes, pagar_despesa, exibir_historico, exibir_saldo
from utils import titulo
def mostrar_menu():
    print("1. Registrar nova transação")
    print("2. Pagar despesa")
    print("3. Ver todas as transações")
    print("4. Exibir histórico")
    print("5. Consultar saldo")
    print("6. Sair")

while True:
    mostrar_menu()
    opcao= input("Escolha uma opção: ")
    if opcao == "1":
        cadastra_transacao()
    elif opcao == "2":
        pagar_despesa()
    elif opcao == "3":
        listar_trasacoes()
    elif opcao == "4":
        exibir_historico()
    elif opcao == "5":
        exibir_saldo()
    elif opcao == "6":
        print("Saindo do Programa...")
        break
    else:
        print("Opção Inválida. Tente Novamente")
