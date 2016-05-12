# -*- coding: UTF-8 -*-

from interface import Interface
from random import*

i = Interface

def mostrar():
    cor = randint(0, 2)
    if(cor == 0):
        print('\033[1;32m1 Fazer Pedido \033[1;m')
        print('\033[1;32m2 Ver Relatório \033[1;m')
        print('\033[1;32m0 Sair \033[1;m')
        print('\033[1;32mDigite sua opção\n \033[1;m')
    elif(cor == 1):
        print('\033[1;33m1 Fazer Pedido \033[1;m')
        print('\033[1;33m2 Ver Relatório \033[1;m')
        print('\033[1;33m0 Sair \033[1;m')
        print('\033[1;33mDigite sua opção\n \033[1;m')
    elif(cor == 2):
        print('\033[1;34m1 Fazer Pedido \033[1;m')
        print('\033[1;34m2 Ver Relatório \033[1;m')
        print('\033[1;34m0 Sair \033[1;m')
        print('\033[1;34mDigite sua opção\n \033[1;m')
    selecionar()

def selecionar():
        escolha = int(input())

        if (escolha == 1):
            i.mostrarSelecaoTamanho()
        elif (escolha == 2):
            i.mostrarRelatorio()
        elif (escolha == 0):
            exit(0)
        else:
            print("Opcao inválida. Por favor digite uma válida")
            selecionar()
        i.mostrarMenu()