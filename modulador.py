import numpy as np

def modularSenalAM(freq, senal):
    #Señal portadora -> (definir bien la frecuencia a utilizar)
    prt = np.cos(2*pi*100*t)

    mod = senal*prt

    return mod