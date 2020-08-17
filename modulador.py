import numpy as np
import matplotlib.pylab as plt

def modularSenalAM(senal, portadora):
    #Señal portadora -> (definir bien la frecuencia a utilizar)
    mod = senal*portadora

    return mod

def obtenerPortadoraAM(freq, tiempo):
    pi = np.pi
    freqNyquist = 2*freq        #Se multiplica por 2 para cumplir con teorema de Nyquist
    prt = np.cos(2*pi*freqNyquist*tiempo)

    return prt,freqNyquist

def modularSenalFM(senal, freq, tiempo):
    pi = np.pi
    freqNyquist = 2*freq        #Se multiplica por 2 para cumplir con teorema de Nyquist
    mod = np.cos(2*pi*freqNyquist*tiempo + (np.cumsum(senal)/freq))
    return mod,freqNyquist

def tiempoModulada(largoInterpolada,freq):
    return np.linspace(0,largoInterpolada/freq,largoInterpolada)