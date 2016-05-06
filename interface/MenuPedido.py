

def mostrar(listaPreco):
    print("-----------------------------------------------------")
    print("---------- T A M A N H O S  E  P R E C O S ----------")
    print("-----------------------------------------------------")
    print("Cód.  |Tamanho        |Sabores     |Fatias     |Preço")
    for linha in listaPreco:
        print("[ " + linha[0] + " ] |" + linha[1] + " |" + linha[2] + " sabor(es) |" + linha[3] + " fatias " + " |R$ " +
              linha[4])
    print("-----------------------------------------------------")
    print("Qual opção de tamanho da pizza?")
