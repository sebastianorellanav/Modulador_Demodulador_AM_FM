import numpy as np
import matplotlib.pylab as plt

def modularSenalAM(senal, portadora):
    #Señal portadora -> (definir bien la frecuencia a utilizar)
    mod = senal*portadora

    return mod

def obtenerPortadora(freq, tiempo):
    pi = np.pi
    prt = np.cos(2*pi*freq*tiempo)

    return prt