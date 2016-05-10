# -*- coding: UTF-8 -*-

from interface import Interface

i = Interface

def mostrar():
    print("1 Fazer Pedido")
    print("2 Ver Relatório")
    print("0 Sair")
    print("Digite sua opção\n")
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