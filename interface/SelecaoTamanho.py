# -*- coding: UTF-8 -*-

from interface import Interface
from controle import Controlador
from random import*

i = Interface
c = Controlador

def mostrar():
    tamanho = sabores = valor = 0

    listaPreco = c.listar('listas\\tamanhos_precos.csv')

    cor = randint(0, 1)
    if(cor == 0):
        print()
        print('\033[1;33m---------------------------------------------------------------- \033[1;m')
        print('\033[1;33m----------------------- T A M A N H O S ------------------------ \033[1;m')
        print('\033[1;33m---------------------------------------------------------------- \033[1;m')
        print('\033[1;33mCód.    |Tamanho           |Sabores        |Fatias        |Preço \033[1;m')
        print()
    elif(cor == 1):
        print()
        print('\033[1;32m---------------------------------------------------------------- \033[1;m')
        print('\033[1;32m----------------------- T A M A N H O S ------------------------ \033[1;m')
        print('\033[1;32m---------------------------------------------------------------- \033[1;m')
        print('\033[1;32mCód.    |Tamanho           |Sabores        |Fatias        |Preço \033[1;m')
        print()
    elif(cor == 2):
        print()
        print('\033[1;34m---------------------------------------------------------------- \033[1;m')
        print('\033[1;34m----------------------- T A M A N H O S ------------------------ \033[1;m')
        print('\033[1;34m---------------------------------------------------------------- \033[1;m')
        print('\033[1;34mCód.    |Tamanho           |Sabores        |Fatias        |Preço \033[1;m')
        print()





    for linha in listaPreco:
        print("[ " + linha[0] + " ]   |" + linha[1] + "    |" + linha[2] + " sabor(es)    |" + linha[3] + " fatias "
              + "    |R$ " + linha[4])


    if(cor == 0):
        print('\033[1;32m---------------------------------------------------------------- \033[1;m')
        codigo = int(input('\033[1;34mQual tamanho de pizza? \033[1;m'))
    elif(cor == 1):
        print('\033[1;34m---------------------------------------------------------------- \033[1;m')
        codigo = int(input('\033[1;33mQual tamanho de pizza? \033[1;m'))
    elif(cor == 2):
        print('\033[1;33m---------------------------------------------------------------- \033[1;m')
        codigo = int(input('\033[1;32mQual tamanho de pizza? \033[1;m'))




    for linha in listaPreco:
        if int(linha[0]) == codigo:
            tamanho = linha[1]
            sabores = int(linha[2])
            valor = linha[4]
    i.mostrarSelecaoTipo(tamanho,sabores,valor)



