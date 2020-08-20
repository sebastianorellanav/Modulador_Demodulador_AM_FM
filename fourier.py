import numpy as np
from scipy import signal

def obtenerTransformada(senal, freq):
    tf = np.fft.fft(senal)
    tf = np.abs(tf)
    freq = np.fft.fftfreq(len(tf), 1/freq)

    return tf, freq

def filtroPasaBajo(senal, frecuencia, nfilt=80, fw_base=4000, axis=0):
    # La frecuencia de Nyquist de la señal es la mitad de la frecuencia de muestreo
    nyqFrec = frecuencia / 2.0
    # Se utiliza un FIR filter con un Hamming window.
    fultro = signal.firwin(nfilt, cutoff=fw_base / nyqFrec, window='hamming')
    # Use lfilter para filtrar con el filtro FIR.
    # Filtramos a lo largo de la segunda dimensión porque eso representa el tiempo
    sonidoFiltrado= signal.filtfilt(fultro, [1.0], senal, axis=axis)
    return sonidoFiltrado
