from random import randint

class perceptron():
    def __init__(self):
        self.pesos = [0,0,0]                    # inicia os pesos com 0
    
    
    def somatorio(self,lista: list):            #net, soma as entradas multiplicadas pelos pesos
        
        sum = self.pesos[0]     # como o primeiro é o bias soma ele fora do loop
        
        for i in range(len(lista)):
            sum += lista[i] * self.pesos[i + 1] # i+1 pois já somou o bias
        
        return sum
    
    
    def step(self,x):
        if x <= 0 : return 0
        return 1
    
    
    def fit(self, x_train: list, y_train: list):    
        
        
        boolean = True                             # True para rodar mais uma época ou False para parar
        
        while boolean:              
            
            boolean = False                   # seta boolean False, ou seja, não terá outra época
            lista = x_train.copy()             # copia as listas
            label = y_train.copy()
          
            for i in range(len(x_train)):       
           
                index = randint(0,len(lista)-1)     # gera um indíce aleatório entre os valores restantes dessa interação
                
                sum = self.somatorio(lista[index])    # soma os elementos da interação atual
                saida = self.step(sum)              # aplica a função de ativação
                
                erro = label[index] - saida           # calcula o erro 
               
                
                if erro != 0 :
                    self.BackPropagation(erro,lista[index])    # se houve erro faz o BackPropagation e seta Boolean para True para que haja outra época
                    boolean = True

                lista.pop(index)    # retira o valor testado nessa interação da lista de teste e da label
                label.pop(index)
                
        
    def BackPropagation(self,erro,lista):
        
        self.pesos[0] = self.pesos[0] + (erro * 1 * 1)  # ajusta o peso do bias

        for i in range(len(lista)):
            self.pesos[i + 1] = self.pesos[i + 1] + (erro * 1 * lista[i])   # ajusta o peso das demais entradas
        
    
    
    def Predict(self,lista: list):
        listaSaida = []         
        for i in lista:                 # para cada elemento da lista calcula a saída com os pesos atuais
            sum = self.somatorio(i)
            saida = self.step(sum)
            listaSaida.append(saida)
        
        return listaSaida 
    
    
    def get_pesos(self):
        return self.pesos


if __name__ == '__main__':
    x_train = [[1,1],[1,0],[0,1],[0,0]]
    y_train = [1,1,0,0]

    model = perceptron()

    model.fit(x_train,y_train)
    
    x_teste = [[1,0],[1,1],[0,1],[0,0],[1,0]]
    print(f'previsões = {model.Predict(x_teste)}')
    
    print(f'pesos = {model.get_pesos()}')