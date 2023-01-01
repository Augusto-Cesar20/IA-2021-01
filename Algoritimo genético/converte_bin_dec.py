import random

def decimal(list_val): #recebe uma lista de inteiros com 0s e 1s, em seguida transforma ela em um numero binario para converte-lo para decimal
    #transforma valor binario da lista que está como int em string
    val = []
    for i in list_val:
        val.append(str(i))

    val = "".join(val) #concatena todos os valores da lista para virar uma string unica
    aux_val = int(val) #atribui um valor inteiro para o numero binário val
    print("Em Binario:", aux_val)

    #Converte aux_val para decimal
    n_val = len(str(aux_val)) #pega o tamanho do aux val
    decimal_val = 0
    i = 0
    while n_val >= 0:
        resto = aux_val % 10
        decimal_val = decimal_val + (resto * (2**i))
        n_val = n_val - 1
        i = i + 1
        aux_val = aux_val // 10

    return decimal_val

def main():
    #Gera um cromossomo aleatorio com 44 valores, sendo eles 0 ou 1
    cromo = [random.randint(0, 1) for x in range(6)]
    print("Comossomo: ", cromo)

    #divide a lista em duas, x com os primeiros 22 birarios e y com os outros 22
    list_x = cromo[0:3]
    list_y = cromo[3:]
    print("X -> ", list_x)
    print("Y -> ", list_y)

    x = decimal(list_x)
    y = decimal(list_y)
    print("Decimal (x): ", x)
    print("Decimal (y): ", y)

if __name__ == "__main__":
    main()