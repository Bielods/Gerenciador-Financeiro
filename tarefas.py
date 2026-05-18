from dados import transacoes , fila_pendentes , pilha_pagamentos , STATUS , TIPOS, CATEGORIAS
from utils import titulo , ler_valor

def cadastra_transaca():
    descricao= input("Escreva a descrição: ")
    valor= ler_valor()
    print(TIPOS)
    tipo= input("Digite o tipo: ")
    print(CATEGORIAS)
    categoria= input("Digite a catrgoria: ")

    dict_transacao= {
        "id": len(transacoes)+1,
    "status": STATUS[0],
        "descrição": descricao,
        "valor": valor,
        "tipo": tipo ,
        "categoria": categoria ,
    }
    transacoes.append(dict_transacao)
    if tipo == 'despesa':
        fila_pendentes.append(dict_transacao)

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

def pagar_despesa():
    if not fila_pendentes:
        print("Nenhuma despesa pendente")
    else:
        transacao= fila_pendentes.pop(0)
        transacao['status']= STATUS[1]
        pilha_pagamentos.append(transacao)
        print(f"Despesa '{transacao['descricao']}' paga com sucesso")

def exibir_historico():
    if not pilha_pagamentos:
        print("Nenhum pagamento efetuado")
    else:
        for transacao in reversed(pilha_pagamentos):
           print(f"Descrição: {transacao['descricao']}")
           print(f"Valor: {transacao['valor']}")
           print(f"Status: {transacao['status']}")

def exibir_saldo():
    receitas=0
    despesas=0
    for transacao in transacoes:
        if transacao['tipo'] == 'receita':
            receitas+= transacao['valor']
        elif transacao['tipo']== 'despesa' and transacao['status'] == 'pago':
            despesas+= transacao['valor']
    print(f"O seu saldo atual é R${receitas-despesas}")