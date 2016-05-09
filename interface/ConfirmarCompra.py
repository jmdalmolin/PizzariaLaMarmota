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
            print("Pedido confirmado! Agradecemos sua preferencia")
        elif (escolha == 2):
            print("Pedido cacelado")
        else:
            print("Opcao invalida, favor digite uma valida:")
            selecionar()
