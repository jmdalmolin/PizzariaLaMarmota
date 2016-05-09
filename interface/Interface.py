# -*- coding: UTF-8 -*-

from random import*
from subprocess import call
from interface import RelatorioVendas
from interface import SelecaoSabor
from interface import SelecaoTamanho
from interface import Menu
from interface import SelecaoTipo
from interface import ConfirmarCompra


menu = Menu
selecaoTamanho = SelecaoTamanho
selecaoTipo = SelecaoTipo
selecaoSabor = SelecaoSabor
confirmarCompra = ConfirmarCompra
relatorioVendas = RelatorioVendas


def mostrarLogo():
    tipo = randint(0,6)
    if(tipo == 0):
        print('\033[1;34m################################################################ \033[1;m')
        print('\033[1;34m#--------------------------------------------------------------# \033[1;m')
        print('\033[1;34m#----------- P I Z Z A R I A  L A  M A R M O T A ------------- # \033[1;m')
        print('\033[1;34m#--------------------------------------------------------------# \033[1;m')
        print('\033[1;34m################################################################ \033[1;m')
    elif(tipo == 1):
        print('\033[1;33m################################################################ \033[1;m')
        print('\033[1;33m#--------------------------------------------------------------# \033[1;m')
        print('\033[1;33m#----------- P I Z Z A R I A  L A  M A R M O T A ------------- # \033[1;m')
        print('\033[1;33m#--------------------------------------------------------------# \033[1;m')
        print('\033[1;33m################################################################ \033[1;m')
    elif(tipo == 2):
        print('\033[1;46m################################################################ \033[1;m')
        print('\033[1;46m#--------------------------------------------------------------# \033[1;m')
        print('\033[1;46m#----------- P I Z Z A R I A  L A  M A R M O T A ------------- # \033[1;m')
        print('\033[1;46m#--------------------------------------------------------------# \033[1;m')
        print('\033[1;46m################################################################ \033[1;m')
    elif(tipo == 3):
        print('\033[1;31m################################################################ \033[1;m')
        print('\033[1;31m#--------------------------------------------------------------# \033[1;m')
        print('\033[1;31m#----------- P I Z Z A R I A  L A  M A R M O T A ------------- # \033[1;m')
        print('\033[1;31m#--------------------------------------------------------------# \033[1;m')
        print('\033[1;31m################################################################ \033[1;m')
    elif(tipo == 4):
        print('\033[1;35m################################################################ \033[1;m')
        print('\033[1;35m#--------------------------------------------------------------# \033[1;m')
        print('\033[1;35m#----------- P I Z Z A R I A  L A  M A R M O T A ------------- # \033[1;m')
        print('\033[1;35m#--------------------------------------------------------------# \033[1;m')
        print('\033[1;35m################################################################ \033[1;m')
    elif(tipo == 5):
        print('\033[1;32m################################################################ \033[1;m')
        print('\033[1;32m#--------------------------------------------------------------# \033[1;m')
        print('\033[1;32m#----------- P I Z Z A R I A  L A  M A R M O T A ------------- # \033[1;m')
        print('\033[1;32m#--------------------------------------------------------------# \033[1;m')
        print('\033[1;32m################################################################ \033[1;m')



def mostrarMenu():
    mostrarLogo()
    menu.mostrar()

def mostrarSelecaoTamanho():
    mostrarLogo()
    selecaoTamanho.mostrar()

def mostrarSelecaoTipo(pizza):
    mostrarLogo()
    selecaoTipo.mostrar(pizza)

def mostrarSelecaoSabor(pizza):
    mostrarLogo()
    selecaoSabor.mostrar(pizza)


def mostrarConfirmarCompra(pedido):
    mostrarLogo()
    confirmarCompra.mostrar(pedido)


def mostrarRelatorio():
    mostrarLogo()
    relatorioVendas.mostrar()

