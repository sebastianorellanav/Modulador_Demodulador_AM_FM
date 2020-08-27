from scipy.signal import butter, filtfilt, freqz
import scipy.io.wavfile as waves

#Entradas:  señal modulada AM
#           señal portadora
#Salida:    señal demodulada AM
#Descripcion: obtiene la señal demodulada, a partir de la multiplicación
#             entre Señal modulada AM y la portadora
def demodularAm(modulada,portadora):
    demodulada = modulada*portadora
    return demodulada


    