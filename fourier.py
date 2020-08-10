import numpy as np

def obtenerTransformada(senal, freq):
    tf = np.fft.fft(senal)
    tf = np.fft.fftshift(tf)
    tf = np.abs(tf)
    freq = np.fft.fftfreq(len(tf), 1/freq)
    freq = np.fft.fftshift(freq)

    return freq, tf