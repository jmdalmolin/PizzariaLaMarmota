# -*- coding: UTF-8 -*-

from subprocess import call
from interface import MenuPedido

menuPedido = MenuPedido

def mostrarLogo():
    # call("clear")
    print('\033[1;34m##################################################### \033[1;m')
    print('\033[1;34m#---------------------------------------------------# \033[1;m')
    print('\033[1;34m#------- P I Z Z A R I A  L A  M A R M O T A -------# \033[1;m')
    print('\033[1;34m#---------------------------------------------------# \033[1;m')
    print('\033[1;34m##################################################### \033[1;m')


def mostrarMenuPrincipal():
    mostrarLogo()
    print("1 Fazer Pedido")
    print("2 Ver Relatório")
    print("0 Sair")

def mostrarMenuPedido(listaPreco):
    mostrarLogo()
    menuPedido.mostrar(listaPreco)

def mostrarListaPizza():
    print("")

def mostrarRelatorio():
    print("Comprei um Patin")
