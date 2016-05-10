
from interface import Interface

i = Interface

def mostrar(tamanho,sabores,valor):
    print("1 Doces")
    print("2 Salgadas")
    print("0 Cancelar Pedido")
    print("Qual tipo de sabor desejas escolher para pizza?")
    selecionar(tamanho,sabores,valor)

def selecionar(tamanho,sabores,valor):
    tipo = int(input())
    if tipo == 1 or tipo == 2:
        i.mostrarSelecaoSabor(tipo, tamanho,sabores,valor)
    elif tipo == 0:
        print("Pedido Cancelado")
    else:
        print("Digite um código válido")
        selecionar(tamanho,sabores,valor)