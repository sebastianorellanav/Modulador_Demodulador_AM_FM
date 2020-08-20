from scipy.io.wavfile import write
import numpy as np

def guardarWav(titulo, frecuenciaMuestreo, senal):
        write( titulo + ".wav", frecuenciaMuestreo, senal.astype(np.int16))