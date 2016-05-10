# -*- coding: UTF-8 -*-
from datetime import datetime
import csv

def listar(caminhoArquivo):
    arquivo = open(caminhoArquivo, 'r')

    reader = csv.reader(arquivo, delimiter = ',')

    lista = []

    for linha in reader:
        lista.append(linha)

    arquivo.close()

    return lista


def registrarVenda(pedido, tamanho, sabores, valor):
    now = datetime.now()
    lista = listar('registro\\vendas.csv')

    for linha in lista:
        if int(linha[0]) == 0:
            x = int(linha[2])+int(valor)
            linha[2] = str(x)
        elif int(linha[0]) == 1:
            if tamanho == linha[1]:
                x = int(linha[2]) + 1
                linha[2] = str(x)
        else:
            for sabor in pedido:
                if sabor[0] == linha[1]:
                    x = int(linha[2]) + 1
                    linha[2] = str(x)

    vendas = open('registro\\vendas.csv', 'w')
    for linha in lista:
        vendas.write(linha[0]+','+linha[1]+','+linha[2]+',\n')
    vendas.close()



    return 1