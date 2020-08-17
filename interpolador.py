import numpy as np
from scipy import interpolate

def interpolacionAM(senal,tiempo):
    interpolacion = interpolate.interp1d(tiempo,senal)
    senalInterpolada = interpolacion(tiempo)
    return senalInterpolada
