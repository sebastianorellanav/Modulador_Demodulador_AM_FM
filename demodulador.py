from scipy.signal import butter, filtfilt, freqz
import scipy.io.wavfile as waves

def demodularAm(modulada,portadora):
    demodulada = modulada*portadora
    return demodulada

def guardarAudio(nombre,freq,demodulada):
    waves.write(nombre,freq,demodulada)
    