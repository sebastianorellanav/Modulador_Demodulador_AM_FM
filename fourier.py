import numpy as np
from scipy import signal

#Entradas:  señal original, modulada (AM o FM) o demodulada (AM)
#           frecuencia de la señal
#Salidas:   Transformada de Fourier de la señal de entrada
#           Frecuencia de la señal
#Descripcion: se aplica la Transformada de Fourier de la señal de entrada,
#             para luego obtener su frecuencia según la transformada.
def obtenerTransformada(senal, freq):
    tf = np.fft.fft(senal)
    tf = np.abs(tf)
    freq = np.fft.fftfreq(len(tf), 1/freq)

    return tf, freq

#Entradas:  Señal a aplicar filtro pasa bajo
#           Frecuencia de muestreo de la señal
#           N° taps
#           Frecuencia de corte del filtro
#           Eje para aplicar el filtrado
#Salidas:   Señal filtrada pasa bajo con igual dimensión que la original.
#Descripcion: Se aplica el filtro pasabajo, obteniendo al frecuencia de Nyquist previamente.
def filtroPasaBajo(senal, frecuencia, nfilt, fw_base, axis=0):
    # La frecuencia de Nyquist de la señal es la mitad de la frecuencia de muestreo
    nyqFrec = frecuencia / 2.0
    # Se utiliza un FIR filter con un Hamming window.
    filtro = signal.firwin(nfilt, cutoff=fw_base / nyqFrec, window='hamming')
    # Use lfilter para filtrar con el filtro FIR.
    # Filtramos a lo largo de la segunda dimensión porque eso representa el tiempo
    sonidoFiltrado= signal.filtfilt(filtro, [1.0], senal, axis=axis)
    return sonidoFiltrado
