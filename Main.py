# -*- coding: UTF-8 -*-

from controle import Controlador
from interface import Interface


c = Controlador
i = Interface

i.mostrarMenuPrincipal()
e = int(input(()))

while(e):

    if e == 1:
        i.mostrarMenuPedido(c.listar('listas\\tamanhos_precos.csv'))


    elif e == 2:
        i.mostrarRelatorio()

    elif e == 0:
        exit()

    else:
        print("Digite um opção válida:")

    e = int(input(()))

