import numpy as np

def obtenerPortadora(Ac,frecuenciaPortadora,tiempoInterpolado):
    portadora = Ac*np.cos(2*np.pi*frecuenciaPortadora*tiempoInterpolado)
    return portadora