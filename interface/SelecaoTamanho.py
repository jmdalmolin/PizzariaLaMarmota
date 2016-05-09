# -*- coding: UTF-8 -*-

from interface import Interface
from controle import Controlador

i = Interface
c = Controlador

sabores = preco = 0

def mostrar():
    listaPreco = c.listar('listas\\tamanhos_precos.csv')
    listaPreco = listaPreco
    print("----------------------------------------------------------------")
    print("----------------------- T A M A N H O S ------------------------")
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
            print(sabores)
            print(preco)
            i.mostrarListaPizza(tipoPizza, sabores)
            break
        elif tipoPizza == 2:
            i.mostrarListaPizza(tipoPizza, sabores)
            break
        elif tipoPizza == 0:
            print("Pedido Cancelado")
        else:
            tipoPizza = int(input("Digite um código válido"))
