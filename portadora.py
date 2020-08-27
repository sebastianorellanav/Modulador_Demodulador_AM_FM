import numpy as np

#Entradas:  Amplitud de la portadora
#           Frecuencia de la portadora
#           Tiempo de interpolado
#Salidas:   Portadora en el tiempo.
#Descripción:   Se obtiene la portadora en el tiempo, en este caso haciendo uso de la función coseno.
def obtenerPortadora(Ac,frecuenciaPortadora,tiempoInterpolado):
    portadora = Ac*np.cos(2*np.pi*frecuenciaPortadora*tiempoInterpolado)
    return portadora