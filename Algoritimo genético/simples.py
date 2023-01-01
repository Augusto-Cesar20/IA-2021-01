import random
import numpy as np

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

#Recebe uma lista de decimais e retorna a soma de todos eles
def total_fitness(lista_dec):
    soma = 0
    for i in lista_dec:
        soma = soma + i

    return soma

#Recebe uma lista de decimais (fitness) e retorna uma lista com a probabilidade de cada posição
def probabilidade(lista_dec):
    f_total = total_fitness(lista_dec)
    #print("Fitness total(soma de todos os pesos):", f_total)

    prob = []
    for i in lista_dec:
        prob.append(round(i*100/f_total, 5)) #Regra de 3 (probabilidade -> 100 e valor -> valor total)

    return prob

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
    f1_x = casal[0][0:3]
    f1_y = casal[0][3:]
    #print("f1 => X->", f1_x, "Y->", f1_y)
    
    f2_x = casal[1][0:3]
    f2_y = casal[1][3:]
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

#Escolhe o melhor individuo entre dois
def melhor (individuos):
    ind1 = binario(individuos[0])
    ind2 = binario(individuos[1])
    #print(individuos)

    if(ind1 > ind2):
        melhor = individuos[0]
    else:
        melhor = individuos[1]
    
    #print("Melhor Individuo:", melhor)
    return melhor


# Recebe os dois filhos gerado pelo casal e a população anterior, em seguida substitui o pior pai pelo melhor filho
def troca(filhos, old_pop, pos_pai1, pos_pai2):
    new_pop = old_pop
    #print(old_pop)
    #print(pos_pai1, pos_pai2)

    m_filho = melhor(filhos) #Seleciona o melhor filho
    m_pai = melhor([old_pop[pos_pai1], old_pop[pos_pai2]]) #seleciona o melhor pai

    if(pos_pai1 != pos_pai2):
        new_pop[pos_pai1] = m_filho
        new_pop[pos_pai2] = m_pai
    else: # caso do mesmo pais gerar os filhos
        new_pop[pos_pai1] = melhor([m_filho, m_pai]) #seleciona o melhor entre o melhor pai e o melhor filho

    return new_pop

def main():
    #Gera uma população de cromossomo aleatorio, numeros de 0 ou 1
    populacao = np.random.randint(0,2, (10,6))
    print("Matriz com minha população INICIAL aleatória:\n", populacao) 

    pop = []
    bin = []
    dec = []
    n = 0
    for c in populacao:
        pop.append(cromossomo_str(c))
        bin.append(binario(pop[n])) #Numero em binario agrupado no formato de inteiro
        dec.append(decimal(bin[n])) #Converte o binario em decimal
        n = n + 1
    print("Lista da população INICIAL:", pop)
    #print("Lista com os numeros binários da minha população INICIAL:", bin)
    print("Lista com os numeros DECIMAIS da minha população INICIAL:", dec)

    for geracao in range(0, 400):
        prob = probabilidade(dec) #Lista com a probabilidade de escolha de cada elemento em ordem
        #print("Lista com a probabilidade de ocorrer determinado elemento da minha população:", prob)

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
        filhos = gera_filhos(casal)#A partir do casal(cromo 1 e 2) geram-se dois filhos que é uma lista filhos com dois elementos
        #print("Filhos=>", filhos, "; em Binario->", binario(filhos[0]), binario(filhos[1]))

        new_pop = troca(filhos, pop, rol1, rol2)
        #print("NOVA população:", new_pop)

        pop = new_pop
        bin = []
        dec = []
        n = 0
        for c in pop:
            bin.append(binario(c)) #Numero em binario agrupado no formato de inteiro
            dec.append(decimal(bin[n])) #Converte o binario em decimal
            n = n + 1
        #print(geracao, "->Lista com os numeros binários da minha população:", bin)
        #print(geracao, "->Lista com os numeros decimais da minha população:", dec)

    print(">>>População FINAL:", pop)
    print(">>>DECIMAL:", dec)

if __name__ == "__main__":
    main()

