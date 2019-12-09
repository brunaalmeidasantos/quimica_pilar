import numpy as np
import matplotlib.pyplot as plt

data1 = []
data2 = []

reagente = float(input('Digite o valor da concentração: '))
tempo = float(input('Digite o tempo da reação: '))

velocidade_produto = 0.0

velocidade = reagente / tempo
i = 0 
count = 0
ponto_grafico = velocidade / 1000


while(1):

    velocidade_produto += ponto_grafico
    reagente -= ponto_grafico
    i+=1

    if(velocidade_produto >= reagente):
        while(count < (i/5)):

            data1.append(velocidade_produto)
            data2.append(reagente)
            count += 1
            
        break;

    data1.append(velocidade_produto)
    data2.append(reagente)

    

plt.plot(data1, '-g', color = 'red', label='Água') 

plt.plot(data2, '-g',color = 'blue', label = 'H + O') 
plt.legend();
plt.title("Gráfico de Equilíbrio Químico de H2O")

plt.grid(True)
plt.xlabel("Tempo(ms)")
plt.ylabel("Concentração(mol/l)")
plt.show()
