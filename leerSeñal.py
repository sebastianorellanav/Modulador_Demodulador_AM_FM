import scipy.io.wavfile as waves
import numpy as np

#Entrada: string con nombre de archivo
#Salida: muestreo: frecuencia de datos por segundo
#        sonido: contiene datos del sonido
#Descripción: leer archivo con señal de sonido
def leerSenal(nombre):
    frecuencia_muestreo_senal, sonido = waves.read(nombre)
    return frecuencia_muestreo_senal, sonido

def obtenerIntervaloTiempo(senal,frecuencia_muestreo_senal):
    t = np.linspace(0, len(senal)/frecuencia_muestreo_senal, len(senal))
    return t