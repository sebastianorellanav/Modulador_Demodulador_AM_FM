import numpy as np

def modularSenalAM(freq, senal, tiempo):
    #Señal portadora -> (definir bien la frecuencia a utilizar)
    pi = np.pi
    prt = np.cos(2*pi*freq*tiempo)

    mod = senal*prt

    return mod