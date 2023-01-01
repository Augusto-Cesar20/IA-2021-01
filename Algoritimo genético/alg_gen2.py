import random
import numpy as np
import math

#Recebe uma lista de 0s e 1s e retorna uma string com o valores em binario
def cromossomo_str (lista):
    aux = []
    for i in lista:
        aux.append(str(i))

    aux = "".join(aux) #concatena todos os valores da lista para virar uma string única de 0s e 1s

    return aux

#Recebe uma palavra que representa um numero binario e converte para inteiro
def binario (lista):
    
    bin = int(lista) #atribui um valor inteiro para a string em binário
    #print("Binário:", bin)

    return bin

#recebe um numero em binario e retorna seu valor em decimal
def decimal(bin):
    tam = len(str(bin)) #pega o tamanho do numero binario
    decimal = 0
    i = 0
    while tam >= 0:
        resto = bin % 10
        decimal = decimal + (resto * (2**i))
        tam = tam - 1
        i = i + 1
        bin = bin // 10

    return decimal

def dividir_xy(cromo):
    resp = []
    resp.append(cromo[0:22])
    resp.append(cromo[22:])

    return resp

def melhor(lista_prob, pop, xy):
    m = 0.0
    p = 0
    n = 0
    for i in lista_prob:
        #print(i)
        if (i > m):
            p = n
            m = i
        n = n + 1

    #print("MELHOR => Individuo:", pop[p], " - X =", xy[p][0], "_ Y = ", xy[p][1], "- F6 =",  m, "- Posição:", p)
    print("MELHOR => Individuo:", pop[p], "- F6 =",  m, "- Posição:", p)

    return pop[p]

def f6 (x, y):
    resp = 0.5 - (math.sin(math.sqrt(x**2+y**2))**2 - 0.5)/(1 + 0.001*(x**2 + y**2))**2
    #print("F6 =", resp)
    return resp

#função F6 que faz o calculo da probabilidade
def lista_f6 (lista_dec):
    resp = []

    m = 0.0
    p = 0
    n = 0
    for i in lista_dec:
        #print(lista_dec[n])
        x = ((int(lista_dec[n][0]))*(200/((2**22)-1))) - 100
        y = ((int(lista_dec[n][1]))*(200/((2**22)-1))) - 100
        #print("X =", x ,"<_> Y =", y)
        r_f6 = round(f6(x, y), 5)
        if (r_f6 > m):
            Fx = x
            fy = y
            p = n
            m = r_f6
        resp.append(r_f6)
        n = n + 1

    #print("Lista de F6", resp)
    print('X =', Fx, "<_> Y=", fy)
    #print("MELHOR AQUI =>",  m, "- Posição:", p)

    return resp

#Recebe a lista de probabilidade e retorna a posição do escolhido de forma aleatoria
def roleta(lista_prob):
    tam = len(lista_prob) #Indica o tamanho da lista de probabilidade, que também indica a quantidade de elementos na minha população
    #print("Tamanho da minha população:", tam)

    posicao = [] #O vetor posição será usado como auxiliar na roleta. Nele indicamos a posição de cada peso e consequentemente de cada elemento da população
    for n in range(0, tam):
        posicao.append(n)
    #print("Lista das possiveis possições:", posicao)

    result = random.choices(posicao, weights=lista_prob, k=1) #retorna a posição

    return result[0] #A posição retornada pode variar de 0 a 5 pois são 6 elementos

#Avalia se ocorre ou não a mutação dos genes, se o individuo sofrer mutação, um gene troca de valor
def mutacao ():
    possibilidade = [True, False]

    result = random.choices(possibilidade, weights=[0.05, 0.95], k=1) #Existe 5% de chance de True = ocorrer mutação

    return result[0]

#recebe um casal e retorna seus filhos (divide o binario do casal ao meio e troca)
def gera_filhos(casal):
    
    d = random.randint(1, 43)#gera um numero aleatorio, referente a onde vai ser trocado

    f1_x = casal[0][0:d]
    f1_y = casal[0][d:]
    #print("f1 => X->", f1_x, "Y->", f1_y)
    
    f2_x = casal[1][0:d]
    f2_y = casal[1][d:]
    #print("f2 => X->", f2_x, "Y->", f2_y)

    filho1 = f1_x + f2_y
    m1 = mutacao()
    #print("Resultado da mutação:", m1)
    if (m1):
        a = random.randint(0,len(filho1)-1)
        #print("Posição", a)
        filho1 = list(filho1)
        if(filho1[a] == '1'):
            filho1[a] = '0'
        else:
            filho1[a] = '1'
        filho1 = "".join(filho1)
    #print("Primeiro filho:", filho1)

    filho2 = f2_x + f1_y
    m2 = mutacao()
    #print("Resultado da mutação:", m2)
    if (m2):
        a = random.randint(0,len(filho2)-1)
        #print("Posição", a)
        filho2 = list(filho2)
        if(filho2[a] == '1'):
            filho2[a] = '0'
        else:
            filho2[a] = '1'
        filho2 = "".join(filho2)
    #print("Segundo filho:", filho2)

    result = []
    result.append(filho1)
    result.append(filho2)

    return result

def main():
    #Gera uma população de cromossomo aleatorio, numeros de 0 ou 1
    populacao = np.random.randint(0,2, (100, 44))
    #print("Matriz com minha população INICIAL aleatória:\n", populacao) 

    pop = []
    #bin = []
    #dec = []
    div_xy = []
    dec_xy = []
    n = 0
    for c in populacao:
        pop.append(cromossomo_str(c))
        #bin.append(binario(pop[n])) #Numero em binario agrupado no formato de inteiro
        #dec.append(decimal(bin[n])) #Converte o binario em decimal
        div_xy.append(dividir_xy(pop[n]))
        dec_xy.append([decimal(binario(div_xy[n][0])), decimal(binario(div_xy[n][1]))])
        n = n + 1
    #print("Lista da população INICIAL:", pop)
    #print("Lista com os numeros binários da minha população INICIAL:", bin)
    #print("Lista com os numeros DECIMAIS da minha população INICIAL:", dec)
    #print("Lista com meus individuos divididos em X e Y =>", div_xy)
    #print("Lista DECIMAL do individuos divididos em X e Y =>", dec_xy)

    for geracao in range(4000): #quantidade de gerações
        prob = lista_f6(dec_xy) #Lista com a probabilidade de escolha de cada elemento em ordem
        #print(geracao, "- Lista F6", prob)
        m_indv = melhor(prob, pop, div_xy) 
        #print("Melhor: ", m_indv) 
        new_pop = []
        for i in range(50): #gerar filhos com a metade da população
            rol1 = roleta(prob) #escolhe uma posição de acordo com cada probabilidade
            #print("Posição do meu elemento(01) escolhido:", rol1)
            cromo1 = pop[rol1] #Cromossomo do individuo escolhido
            #elemento1 = bin[rol1] #O numero dele em binário #sem necessicdade ###
            #print("Elemento(01) da posição", rol1, "é:", cromo1, "->", elemento1)

            rol2 = roleta(prob) #escolhe uma posição de acordo com cada probabilidade
            #print("Posição do meu elemento(02) escolhido:", rol2)
            cromo2 = pop[rol2] #Cromossomo do individuo escolhido
            #elemento2 = bin[rol2] #O numero dele em binário #sem necessicdade ###
            #print("Elemento(02) da posição", rol2, "é:", cromo2, "->", elemento2)
            
            casal = []
            casal.append(cromo1)
            casal.append(cromo2)
            #print("Casal:", casal) 

            filhos = gera_filhos(casal) #A partir do casal(cromo 1 e 2) geram-se dois filhos que é uma lista filhos com dois elementos
            #print("Filhos=>", filhos, "; em Binario->", binario(filhos[0]), binario(filhos[1]))

            for j in filhos:
                new_pop.append(j)
        
        d = random.randint(0, 99)#gera um numero aleatorio, referente a onde vai ser trocado um dos filhos pelo melhor pais
        new_pop[d] = m_indv 
        #print("NOVA população:", new_pop)
        
        pop = new_pop
        #bin = []
        #dec = []
        div_xy = []
        dec_xy = []
        n = 0
        for c in pop:
            #bin.append(binario(c)) #Numero em binario agrupado no formato de inteiro
            #dec.append(decimal(bin[n])) #Converte o binario em decimal
            div_xy.append(dividir_xy(pop[n]))
            dec_xy.append([decimal(binario(div_xy[n][0])), decimal(binario(div_xy[n][1]))])
            n = n + 1
        #print(geracao, "->Lista com os numeros binários da minha população:", bin)
        #print(geracao, "->Lista com os numeros decimais da minha população:", dec)
        #print("Lista com meus individuos divididos em X e Y =>", div_xy)

    #print(">>>População FINAL:", pop)
    #print(">>>DECIMAL:", dec)

if __name__ == "__main__":
    main()
