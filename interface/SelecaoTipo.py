
from interface import Interface

i = Interface

pedido = []

def mostrar(pizza):
    print("1 Doces")
    print("2 Salgadas")
    print("0 Cancelar Pedido")
    print("Qual tipo de sabor desejas escolher para pizza?")
    selecionar(pizza)

def selecionar(pizza):
    pizza[3] = int(input())
    if pizza[3] == 1 or pizza[3] == 2:
        i.mostrarSelecaoSabor(pizza[3])
    elif pizza[3] == 0:
        print("Pedido Cancelado")
    else:
        print("Digite um código válido")
        selecionar(pizza)