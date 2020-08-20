import numpy as np
from scipy import interpolate

def obtenerTiempoInterpolado(senal,tiempo,frecuenciaMuestreoSenal,frecuenciaMuestreoPortadora):
    interpolacion = interpolate.interp1d(tiempo,senal)
    tiempoInterpolado = np.arange(0, len(senal)/frecuenciaMuestreoSenal,frecuenciaMuestreoPortadora)
    return tiempoInterpolado,interpolacion

def obtenerSenalInterpolada(interpolacion,tiempoInterpolado):
    senalInterpolada = interpolacion(tiempoInterpolado)
    return senalInterpolada
