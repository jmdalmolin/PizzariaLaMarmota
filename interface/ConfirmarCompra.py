# -*- coding: UTF-8 -*-

from controle import Controlador

c = Controlador

def mostrar(pedido,tamanho,sabores, valor):
    print("----------------------------------------------------------------")
    print("--------------- C O N F I R M A R   C O M P R A  ---------------")
    print("----------------------------------------------------------------")

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