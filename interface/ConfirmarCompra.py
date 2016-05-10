# -*- coding: UTF-8 -*-
from random import*

from controle import Controlador

c = Controlador

def mostrar(pedido,tamanho,sabores, valor):

    tipo = randint(0, 2)
    if (tipo == 0):
        print('\033[1;32m---------------------------------------------------------------- \033[1;m')
        print('\033[1;32m--------------- C O N F I R M A R   C O M P R A  --------------- \033[1;m')
        print('\033[1;32m---------------------------------------------------------------- \033[1;m')
    elif(tipo == 1):
        print('\033[1;33m---------------------------------------------------------------- \033[1;m')
        print('\033[1;33m--------------- C O N F I R M A R   C O M P R A  --------------- \033[1;m')
        print('\033[1;33m---------------------------------------------------------------- \033[1;m')
    elif(tipo == 2):
        print('\033[1;34m---------------------------------------------------------------- \033[1;m')
        print('\033[1;34m--------------- C O N F I R M A R   C O M P R A  --------------- \033[1;m')
        print('\033[1;34m---------------------------------------------------------------- \033[1;m')

    print("\n" + tamanho + "       R$ " + valor + ",00")
    for linha in pedido:
        print("  -  " + linha)

    print("1 Confirmar compra")
    print("0 Cancelar Pedido")

    selecionar(pedido,tamanho,sabores, valor)

def selecionar(pedido,tamanho, sabores, valor):
        escolha = int(input())

        if (escolha == 1):
            if c.registrarVenda(pedido, tamanho, sabores, valor):
                print("Pedido confirmado! Agradecemos sua preferência")
            else:
                print("Erro ao salvar")
        elif (escolha == 0):
            print("Pedido cancelado")
        else:
            print("Opção inválida. Por favor digite uma válida:")
            selecionar(pedido,tamanho, sabores, valor)