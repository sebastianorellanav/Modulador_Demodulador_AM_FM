import scipy.io.wavfile as waves
import numpy as np

#Entrada: string con nombre de archivo
#Salida: muestreo: frecuencia de datos por segundo
#        sonido: contiene datos del sonido
#Descripción: leer archivo con señal de sonido
def leerSenal(nombre):
    frecuencia, sonido = waves.read(nombre)
    return frecuencia, sonido

def obtenerIntervaloTiempo(senal,freq):
    t = np.linspace(0, len(senal)/freq, len(senal))
    return t