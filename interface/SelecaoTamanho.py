# -*- coding: UTF-8 -*-

from interface import Interface
from controle import Controlador

i = Interface
c = Controlador

pizza = []


def mostrar():
    listaPreco = c.listar('listas\\tamanhos_precos.csv')
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
            pizza[0] = linha[1]
            pizza[1] = linha[2]
            pizza[2] = linha[3]
            break

    i.mostrarSelecaoTipo(pizza)



