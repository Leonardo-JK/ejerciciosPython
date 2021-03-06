from genrnd import genrnd
from media import media
from mediana import mediana
from rango import rango
from varianza import varianza
from minimo import minimo
from maximo import maximo


import time



def ejecutar(n):
    try:
        inicio = time.time()
        vector = genrnd(n)
        mediaValor  = media(vector)
        medianaValor = mediana(vector)
        rangoValor = rango(vector)
        varianzaValor = varianza(vector, mediaValor)
        minimoValor = minimo(vector)
        maximoValor = maximo(vector)
        return time.time() - inicio
    except KeyboardInterrupt:
        print("Proceso interrumpido!")
    
print(ejecutar(50))