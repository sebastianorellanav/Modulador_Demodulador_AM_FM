import scipy.io.wavfile as waves
import numpy as np

#Entrada: string con nombre de archivo
#Salida: muestreo: frecuencia de datos por segundo
#        sonido: contiene datos del sonido
#Descripción: leer archivo con señal de sonido
def leerSenal(nombre):
    frecuencia, sonido = waves.read(nombre)
    return frecuencia, sonido