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
    # call("clear")
    tipo = randint(0,4)
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
        print('\033[1;31m################################################################ \033[1;m')
        print('\033[1;31m#--------------------------------------------------------------# \033[1;m')
        print('\033[1;31m#----------- P I Z Z A R I A  L A  M A R M O T A ------------- # \033[1;m')
        print('\033[1;31m#--------------------------------------------------------------# \033[1;m')
        print('\033[1;31m################################################################ \033[1;m')
    elif(tipo == 3):
        print('\033[1;35m################################################################ \033[1;m')
        print('\033[1;35m#--------------------------------------------------------------# \033[1;m')
        print('\033[1;35m#----------- P I Z Z A R I A  L A  M A R M O T A ------------- # \033[1;m')
        print('\033[1;35m#--------------------------------------------------------------# \033[1;m')
        print('\033[1;35m################################################################ \033[1;m')
    elif(tipo == 4):
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

def mostrarSelecaoTipo(tamanho,sabores,valor):
    mostrarLogo()
    selecaoTipo.mostrar(tamanho,sabores,valor)

def mostrarSelecaoSabor(tipo,tamanho,sabores,valor):
    mostrarLogo()
    selecaoSabor.mostrar(tipo,tamanho,sabores,valor)


def mostrarConfirmarCompra(pedido,tamanho,sabores,valor):
    mostrarLogo()
    confirmarCompra.mostrar(pedido,tamanho,sabores,valor)


def mostrarRelatorio():
    mostrarLogo()
    relatorioVendas.mostrar()

