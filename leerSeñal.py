import scipy.io.wavfile as waves
import numpy as np

#Entrada: string con nombre de archivo
#Salida: muestreo: frecuencia de datos por segundo
#        sonido: contiene datos del sonido
#Descripción: leer archivo con señal de sonido
def leerSenal(nombre):
    frecuencia_muestreo_senal, sonido = waves.read(nombre)
    return frecuencia_muestreo_senal, sonido

#Entradas:  Señal donde se obtendrá el tiempo
#           Frecuencia de muestreo de la señal
#Salidas:   Arreglo del tiempo de la señal
#Descripción:   Se obtiene un arreglo de tiempo con un largo igual al de la señal
def obtenerIntervaloTiempo(senal,frecuencia_muestreo_senal):
    t = np.linspace(0, len(senal)/frecuencia_muestreo_senal, len(senal))
    return t