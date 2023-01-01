import numpy as np

class Perceptron:
    def __init__ (self, N, alpha = 0.1): #Construtor -> N é o numero de colunas no Vetor e de entrada; ALPHA é a taxa de aprendizado
        # inicializa a matriz de pesos e armazena a taxa de aprendizado 
        self.W = np.random.randn(N + 1) / np.sqrt(N) #Dimensiona a matriz de pesos com numeros aleatórios dividido pelo raiz quadrada do numero de entradas (N)
        self.alpha = alpha

    #Função de ativação: imita o comportamento da equação do degrau se x é positivo retornamos 1, caso contrário, retornamos 0
    def step (self, x):
        res = 0
        if x > 0:
            res = 1
        return res 

    def fit(self, X, y, epochs=10): #X é dado real de um treinamento e y é o que a rede deve prever, epochs é o numero de vezes que o perceptron vai treinar
        # insere uma coluna de 1's como a última entrada no recurso
		# matriz -- este pequeno truque nos permite tratar o viés
		# como um parâmetro treinável dentro da matriz de peso
        X = np.c_[X, np.ones((X.shape[0]))]
	
        # loop sobre o número desejado de épocas
        for epoch in np.arange(0, epochs):
            # loop sobre cada ponto de dados individual
            for (x, target) in zip(X, y):
				# pega o produto escalar entre os recursos de entrada
				# e a matriz de pesos, então passe este valor
				# através da função step para obter a previsão
                p = self.step(np.dot(x, self.W))

				# só realiza uma atualização de peso se nossa previsão
				# não corresponde ao destino
                if p != target:
                    # #determina o erro
                    error = p - target

                # atualiza a matriz de peso
                self.W += -self.alpha * error * x

    def predict(self, X, addBias=True):
        # garante que nossa entrada seja uma matriz
        X = np.atleast_2d(X)

        # verifica se a coluna de bias deve ser adicionada
        if addBias:
            # insere uma coluna de 1's como a última entrada no recurso
            # matriz (bias)
            X = np.c_[X, np.ones((X.shape[0]))]

        # pegue o produto escalar entre os recursos de entrada e o
		# matriz de pesos, então passe o valor pelo passo
		#função
        return self.step(np.dot(X, self.W))

if __name__ == '__main__':
    x_train = [[1, 1], [1, 0], [0, 1], [0,0]]
    y_train = [1, 1, 0, 0]

    model = Perceptron(x_train.shape[1])

    model.fit(x_train, y_train)
    
    x_teste = [[1,0],[1,1],[0,1],[0,0],[1,0]]
    print(f'previsões = {model.Predict(x_teste)}')
    
    print(f'pesos = {model.get_pesos()}')