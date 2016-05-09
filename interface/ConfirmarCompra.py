# -*- coding: UTF-8 -*-

def mostrar(pedido):

    print(pedido)
    # for linha in pedido:
    #     print("   " + pedido[1])
    #
    #     selecionar()

def selecionar():
        escolha = int(input())

        if (escolha == 1):
            print("Pedido confirmado! Agradecemos sua preferência")
        elif (escolha == 2):
            print("Pedido cancelado")
        else:
            print("Opção inválida. Por favor digite uma válida:")
            selecionar()
