from scipy.io.wavfile import write
import numpy as np

#Entradas:  Nombre del audio de salida
#           Frecuencia de muestreo para obtener un tiempo de sonido de 8 segundos
#           Señal modulada o demodulada AM
#Salida:    Archivo .wav con audio de salida de la señal modulada o demodulada AM
#Descripcion: Se escribe un archivo .wav con la señal de audio modulada o demodulada AM
def guardarWav(nombre, frecuenciaMuestreo, senal):
        write( nombre + ".wav", frecuenciaMuestreo, senal.astype(np.int16))