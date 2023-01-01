class Perceptron:
    # inicializa os pesos e armazena a taxa de aprendizado 
    def __init__ (self, alpha = 0.1): 
        self.W = [0, 0, 0] #Inicializa os pesos com 0
        self.bias = self.W[0] #Tendencia? viés? -> primeiro elemento do vetor de pesos
        self.alpha = alpha #ALPHA é a taxa de aprendizado

    #Função de ativação: imita o comportamento da equação do degrau se x é positivo retornamos 1, caso contrário, retornamos 0
    def step (self, u):
        res = 0

        if u > 0:
            res = 1

        return res

    #Soma as entradas multiplicadas pelo peso -> x0*w0 + x1*w1 + x2*w2...
    def sum_f (self, X):            
        sum = self.bias

        for i in range (1, len(X)+1):
            sum = sum + X[i - 1] * self.W[i] 
        
        return sum

    #Função de saida
    def Predict (self, X):    
        u = self.sum_f(X)
        saida = self.step(u)
  
        return saida

    #Retorna as saidas para um caso de teste
    def Predictions (self, entradas):
        saidas = []

        for i in entradas:
            saida = self.Predict(i)                
            saidas.append(saida)
        
        return saidas

    #Ajuste dos pesos: Novo wi -> wi = wi + alpha * (d - y) * xi
    def BackPropagation (self, erro, X):
        self.bias = self.W[0] + self.alpha * (erro)  # ajusta o peso do bias

        for i in range (1, len(X)+1):
            self.W[i] = self.W[i] + self.alpha * (erro) * X[i - 1]   # ajusta o peso das demais entradas

    #Faz o treinamento da função
    def fit (self, tx, ty, epochs = 5): #tx é dado real de um treinamento e ty é o que a rede deve prever, epochs(épocas) é o numero de vezes que o perceptron vai treinar
        # loop sobre o número desejado de épocas
        for epoch in range (epochs):
            for i in range (len(tx)):
                d = ty[i] # O que desejamos

                saida = self.Predict(tx[i])  # aplica a função de saida
                erro = d - saida  # Erro = di - yi
                #print ("X =", tx[i], "; Y =", ty[i], "; Saida =", saida, "; ERRO =", erro)
                #print("Pesos", self.W)

                if erro != 0 :
                    self.BackPropagation(erro, tx[i])

    def get_weights(self):
        return self.W

if __name__ == '__main__':
    tx = [[1, 1], [1, 0], [0, 1], [0, 0]]
    ty = [1, 1, 0, 0]
    p = Perceptron()
    p.fit(tx, ty)
    
    x_teste = [[1, 0], [1, 1], [0, 1], [0, 0], [1, 0]]
    print("Previsões do teste", p.Predictions(x_teste))
    print("Pesos", p.get_weights())


