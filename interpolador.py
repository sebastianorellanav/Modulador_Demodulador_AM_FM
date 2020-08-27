import numpy as np
from scipy import interpolate

#Entradas:  Señal a interpolar
#           Tiempo original
#           Frecuencia de muestreo de la señal
#           Frecuencia de muestreo de la portadora
#Salidas:   Tiempo de la señal interpolada
#           Función de interpolación
#Descripción:   Se obtiene la función de interpolación de la señal respecto al tiempo, 
#               para luego crear un arreglo de tiempo según la señal interpolada.
def obtenerTiempoInterpolado(senal,tiempo,frecuenciaMuestreoSenal,frecuenciaMuestreoPortadora):
    interpolacion = interpolate.interp1d(tiempo,senal)
    tiempoInterpolado = np.arange(0, len(senal)/frecuenciaMuestreoSenal,frecuenciaMuestreoPortadora)
    return tiempoInterpolado,interpolacion

#Entradas:  Función de interpolación
#           Tiempo de la señal interpolada
#Salidas:   Señal interpolada
#Descripción:   Se interpola la señal respecto al tiempo.
def obtenerSenalInterpolada(interpolacion,tiempoInterpolado):
    senalInterpolada = interpolacion(tiempoInterpolado)
    return senalInterpolada
