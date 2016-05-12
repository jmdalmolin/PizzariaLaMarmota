
from interface import Interface
from random import*

i = Interface

def mostrar(tamanho,sabores,valor):

    cor = randint(0,2)
    if(cor == 0):
        print('\033[1;33m---------------------------------------------------------------- \033[1;m')
        print('\033[1;33m------------------- T I P O  D A  P I Z Z A -------------------- \033[1;m')
        print('\033[1;33m---------------------------------------------------------------- \033[1;m')
    elif(cor == 1):
        print('\033[1;32m---------------------------------------------------------------- \033[1;m')
        print('\033[1;32m------------------- T I P O  D A  P I Z Z A -------------------- \033[1;m')
        print('\033[1;32m---------------------------------------------------------------- \033[1;m')
    elif(cor == 2):
        print('\033[1;34m---------------------------------------------------------------- \033[1;m')
        print('\033[1;34m------------------- T I P O  D A  P I Z Z A -------------------- \033[1;m')
        print('\033[1;34m---------------------------------------------------------------- \033[1;m')
    print('\033[1;37m1 Doces \033[1;m')
    print('\033[1;37m2 Salgadas \033[1;m')
    print('\033[1;37m0 Cancelar Pedido \033[1;m')
    print('\033[1;37mQual tipo de sabor desejas escolher para pizza? \033[1;m')
    selecionar(tamanho,sabores,valor)

def selecionar(tamanho,sabores,valor):
    tipo = int(input())
    if tipo == 1 or tipo == 2:
        i.mostrarSelecaoSabor(tipo, tamanho,sabores,valor)
    elif tipo == 0:
        print('\031[1;32mPedido Cancelado \033[1;m')
    else:
        print('\031[1;32mDigite um código válido \033[1;m')
        selecionar(tamanho,sabores,valor)