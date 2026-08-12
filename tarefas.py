from dados import transacoes, fila_pendentes, pilha_pagamentos, STATUS, TIPOS, CATEGORIAS
from utils import titulo, ler_valor

# Cadastra uma nova transação e adiciona na lista principal
# Se for despesa, adiciona também na fila de pendentes (FIFO)
def cadastra_transacao():
    descricao = input("Escreva a descrição: ")
    valor = ler_valor()
    print(TIPOS)
    tipo = input("Digite o tipo: ")
    print(CATEGORIAS)
    categoria = input("Digite a catrgoria: ")
    print("Transação Cadastrada com sucesso!")

    # Cria um dicionário com todos os atributos da transação
    dict_transacao = {
        "id": len(transacoes) + 1,
        "status": STATUS[0],
        "descricao": descricao,
        "valor": valor,
        "tipo": tipo,
        "categoria": categoria,
    }

    # Adiciona na lista principal
    transacoes.append(dict_transacao)

    # Se for despesa, entra no final da fila (FIFO)
    if tipo == 'despesa':
        fila_pendentes.append(dict_transacao)

# Lista todas as transações cadastradas no sistema
def listar_trasacoes():
    titulo("Listar Transação")
    for transacao in transacoes:
        print(f"Id: {transacao['id']}")
        print(f"Descrição: {transacao['descricao']}")
        print(f"Valor: {transacao['valor']}")
        print(f"Tipo: {transacao['tipo']}")
        print(f"Categoria: {transacao['categoria']}")
        print(f"Status: {transacao['status']}")
        print()

# Paga a despesa mais antiga da fila (FIFO)
# Atualiza o status e empilha no histórico (LIFO)
def pagar_despesa():
    if not fila_pendentes:
        print("Nenhuma despesa pendente")
    else:
        # Remove o primeiro da fila — FIFO
        transacao = fila_pendentes.pop(0)
        transacao['status'] = STATUS[1]
        # Empilha no histórico — LIFO
        pilha_pagamentos.append(transacao)
        print(f"Despesa '{transacao['descricao']}' paga com sucesso")

# Exibe o histórico de pagamentos do mais recente ao mais antigo (LIFO)
def exibir_historico():
    if not pilha_pagamentos:
        print("Nenhum pagamento efetuado")
    else:
        # reversed() lê a pilha do topo para baixo
        for transacao in reversed(pilha_pagamentos):
            print(f"Descrição: {transacao['descricao']}")
            print(f"Valor: {transacao['valor']}")
            print(f"Status: {transacao['status']}")

# Calcula e exibe o saldo atual (receitas - despesas pagas)
def exibir_saldo():
    receitas = 0
    despesas = 0
    for transacao in transacoes:
        if transacao['tipo'] == 'receita':
            receitas += transacao['valor']
        elif transacao['tipo'] == 'despesa' and transacao['status'] == STATUS[1]:
            despesas += transacao['valor']
    print(f"O seu saldo atual é R${receitas - despesas}")
