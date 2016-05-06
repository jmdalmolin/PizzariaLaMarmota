
from interface import Interface

# lista = []
i = Interface

def mostrar(listaPreco):
    flag = 0
    listaPreco = listaPreco
    print("----------------------------------------------------------------")
    print("--------------- T A M A N H O S  E  P R E C O S ----------------")
    print("----------------------------------------------------------------")
    print("Cód.    |Tamanho           |Sabores        |Fatias        |Preço")

    for linha in listaPreco:
        print("[ " + linha[0] + " ]   |" + linha[1] + "    |" + linha[2] + " sabor(es)    |" + linha[3] + " fatias "
              + "    |R$ " + linha[4])

    print("----------------------------------------------------------------")
    codigo = int(input("Qual tamanho de pizza?"))

    for linha in listaPreco:
        if linha[0] == codigo:
            sabores = linha[2]
            preco = linha[4]

    mostrarTipoPizza()

def mostrarTipoPizza():

    print("\n1 Doces")
    print("2 Salgadas")
    print("0 Cancelar Pedido")
    tipoPizza = int(input("Quais tipos de sabores deseja escolher para pizza?"))

    while (tipoPizza):
        if tipoPizza == 1:
            i.mostrarListaPizza('listas\\pizzas_doces.csv')
            break
        elif tipoPizza == 2:
            i.mostrarListaPizza('listas\\pizzas_salgadas.csv')
            break
        elif tipoPizza == 0:
            print("Pedido Cancelado")
        else:
            tipoPizza = int(input("Digite um código válido"))
