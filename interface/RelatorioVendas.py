# -*- coding: UTF-8 -*-
from controle import Controlador

c = Controlador

def mostrar():
    lista = c.listar('registro\\vendas.csv')
    x = 0
    for linha in lista:
        if int(linha[0]) == 0:
            print(""+linha[1]+" R$ "+linha[2]+",00")

        elif int(linha[0]) == 1:
            if x != int(linha[0]):
                print("\nTAMANHOS DE PIZZA")
                print("Qntd   Tamanho")
                x = 1
            print(linha[2] +"x     "+linha[1])
        elif int(linha[0]) == 2:
            if x != int(linha[0]):
                print("\nPIZZAS DOCES")
                print("Qntd     Sabor")
                x = 2
            if int(linha[2]) != 0:
                print(""+linha[2] + "x     " + linha[1])
        elif int(linha[0]) == 3:
            if x != int(linha[0]):
                print("\nPIZZAS SALGADAS")
                print("Qntd     Sabor")
                x = 3
            if int(linha[2]) != 0:
                print("" + linha[2] + "x     " + linha[1])