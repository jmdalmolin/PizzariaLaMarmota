# -*- coding: UTF-8 -*-

from controle import Controlador
from interface import Interface

c = Controlador
i = Interface

def mostrar(pizza):
    listaSabores = []
    print("----------------------------------------------------------------")
    if pizza[3] == 1:
        print("------------------- P I Z Z A S   D O C E S --------------------")
        listaSabores = c.listar('listas\\pizzas_doces.csv')
    else:
        print("---------------- P I Z Z A S   S A L G A D A S -----------------")
        listaSabores = c.listar('listas\\pizzas_doces.csv')
    print("----------------------------------------------------------------")
    print("Código    | Sabor")

    for linha in listaSabores:
        print("[ " + linha[0] + " ]    |" + linha[1])

    print("----------------------------------------------------------------")
    print("Qual(is) Sabor(es)?")


    x = 0
    #
    # while x < :
    #     flag = 0
    #     sabor = int(input())
    #     while linha in listaSabores:
    #         if linha[0] == sabor:
    #             pedido.append(linha[1])
    #             flag = 1
    #             x = x + 1
    #     else:
    #         if flag:
    #             if x == quantidade:
    #                 print("Pedido Encaminhado")
    #             else:
    #                 print("Próximo sabor:")
    #         else:
    #             print("Sabor não encontrado. Por favor, digite outro sabor")
    #             x = x - 1
    #
    # i.mostrarConfirmarCompra(pedido)
