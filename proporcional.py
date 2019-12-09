import numpy as np
import matplotlib.pyplot as plt

data1 = []
data2 = []
data3 = []

hidrogenio = int(input('Digite a quantidade de hidrogenio '))
oxigenio = int(input('Digite a quantidade de oxigenio: '))

media = hidrogenio / 2

if(media > oxigenio):
    media = oxigenio
else:
    oxigenio = media
i = 0
cont1=0
cont2=0
while(1):
    if(i > media):
        break;
        
    data1.append(hidrogenio)
    data2.append(oxigenio)
    data3.append(cont2)

    hidrogenio -= 2
    oxigenio -= 1
    cont2+=1
    i+=1

    

plt.plot(data1, '-g', color = 'red', label='Hidrogênio') 
plt.plot(data2, '-g',color = 'green', label = 'Oxigênio') 
plt.plot(data3, '-g',color = 'blue', label = 'Água') 
plt.legend();
plt.title("Gráfico da reação química da Água")

plt.grid(True)
plt.xlabel("Tempo(ms)")
plt.ylabel("Concentração(mol/l)")
plt.show()
