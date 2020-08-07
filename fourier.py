import numpy as np

def obtenerTransformada(senal):
    tf = np.fft.fft(senal)
    tf = np.fft.fftshift(tf)
    freq = np.fft.fftfreq(len(tf), 1/1000)
    freq = np.fft.fftshift(freq)

    return freq, tf