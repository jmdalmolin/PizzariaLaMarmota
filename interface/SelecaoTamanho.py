# -*- coding: UTF-8 -*-

from interface import Interface
from controle import Controlador

i = Interface
c = Controlador

def mostrar():
    tamanho = sabores = valor = 0

    listaPreco = c.listar('listas\\tamanhos_precos.csv')

    print('\n'+
          "----------------------------------------------------------------")
    print("----------------------- T A M A N H O S ------------------------")
    print("----------------------------------------------------------------")
    print("Cód.    |Tamanho           |Sabores        |Fatias        |Preço"+'\n')

    for linha in listaPreco:
        print("[ " + linha[0] + " ]   |" + linha[1] + "    |" + linha[2] + " sabor(es)    |" + linha[3] + " fatias "
              + "    |R$ " + linha[4])

    print("----------------------------------------------------------------")
    codigo = int(input("Qual tamanho de pizza?" ))

    for linha in listaPreco:
        if int(linha[0]) == codigo:
            tamanho = linha[1]
            sabores = int(linha[2])
            valor = linha[4]
    i.mostrarSelecaoTipo(tamanho,sabores,valor)



