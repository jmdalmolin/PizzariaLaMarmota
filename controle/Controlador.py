# -*- coding: UTF-8 -*-

import csv

def listar(caminhoArquivo):
    arquivo = open(caminhoArquivo, 'r')

    reader = csv.reader(arquivo, delimiter=',')

    lista = []

    for linha in reader:
        lista.append(linha)

    arquivo.close()

    return lista