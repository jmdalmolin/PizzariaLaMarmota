# -*- coding: UTF-8 -*-

from controle import Controlador
from interface import Interface

c = Controlador
i = Interface

def mostrar(tipo, tamanho,sabores,valor):
    listaSabores = []
    dicSabores = {}
    print("----------------------------------------------------------------")
    if tipo == 1:
        print("------------------- P I Z Z A S   D O C E S --------------------")
        listaSabores = c.listar('listas\\pizzas_doces.csv')
    else:
        print("---------------- P I Z Z A S   S A L G A D A S -----------------")
        listaSabores = c.listar('listas\\pizzas_salgadas.csv')
    print("----------------------------------------------------------------")
    print("Código    | Sabor")

    for linha in listaSabores:
        print("[ " + linha[0] + " ]    |" + linha[1])
        dicSabores[int(linha[0])] = linha[1]
    print("----------------------------------------------------------------")
    print("Qual(is) Sabor(es)?" )


    pedido = []
    sabor = -1
    x = 0

    while x < sabores and sabor != 0:
        sabor = int(input())
        if sabor in dicSabores:
            pedido.append(dicSabores[sabor])
            if x != sabores -1:
                print("Próximo sabor:")
            x = x + 1
        else:
            print("Sabor não encontrado. Por favor, digite outro sabor")

    else:
        if sabor != 0:
            print('\033[1;32mPedido Encaminhado \033[1;m')
            i.mostrarConfirmarCompra(pedido,tamanho,sabores, valor)
        else:
            print('\033[1;31mPedido cancelado \033[1;m')