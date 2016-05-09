# -*- coding: UTF-8 -*-

from controle import Controlador
from interface import Interface

c = Controlador
i = Interface

def mostrar(tipoSabor, quantidade):

    listaSabores = []
    print("----------------------------------------------------------------")
    if(tipoSabor == 1):
        print("------------------- P I Z Z A S   D O C E S --------------------")
        listaSabores = c.listar('listas\\pizzas_doces.csv')
    else:
        print("---------------- P I Z Z A S   S A L G A D A S -----------------")
        listaSabores = c.listar('listas\\pizzas_doces.csv')
    print("----------------------------------------------------------------")
    print("Código        |Sabor                                            ")

    for linha in listaSabores:
        print("[ " + linha[0] + " ]      |" + linha[1])

    print("----------------------------------------------------------------")
    print("Qual(is) Sabor(es)?")

    pedido = []
    x = 1

    while x <= quantidade:
        pedido.append(listaSabores[int(input())])
        x += 1

    i.mostrarConfirmarCompra(pedido)
