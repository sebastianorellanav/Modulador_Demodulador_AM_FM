from scipy.signal import butter, filtfilt, freqz
import scipy.io.wavfile as waves

def demodularAm(modulada,portadora,freq):
    demodulada = modulada*portadora
    b, a = butter(3,4000,'low',fs=freq)
    resultado = filtfilt(b, a,demodulada)

    return resultado

def guardarAudio(nombre,freq,demodulada):
    waves.write(nombre,freq,demodulada)
    