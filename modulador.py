import numpy as np
import matplotlib.pylab as plt
from scipy import interpolate

def modularSenalAM(senal, portadora):
    mod = senal*portadora
    return mod


def modularSenalFM(senal, freq, tiempo):
    pi = np.pi
    freqNyquist = 2*freq        #Se multiplica por 2 para cumplir con teorema de Nyquist
    mod = np.cos(2*pi*freqNyquist*tiempo + (np.cumsum(senal)/freq))
    return mod,freqNyquist
