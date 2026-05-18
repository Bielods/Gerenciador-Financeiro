def linha():
    print("="*40)

def titulo(texto):
    linha()
    print(texto.center(40))
    linha()

titulo("Gerenciador Financeiro")

def ler_valor():
    while True:
        try:
            valor= float(input("Digite um valor: "))
            print("Valor registrado")
            return  valor
        except:
            print("Valor inválido. Tente novamente")