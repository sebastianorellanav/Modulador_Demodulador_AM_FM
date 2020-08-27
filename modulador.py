import numpy as np
import scipy.integrate as integrate

#Entradas:  Señal a modular AM
#           Portadora en el tiempo
#Salidas:   Señal modulada AM
#Descripción:   Se multiplica la señal de entrada con la portadora en el tiempo
def modularSenalAM(senal, portadora):
    mod = senal*portadora
    return mod

#Entradas:  Amplitud de modulación
#           Señal interpolada
#           Tiempo de interpolación
#           Frecuencia inicial de la portadora en el tiempo
#Salidas:   Señal modulada FM
#Descripción:   Se integra la señal interpolada respecto al tiempo, para luego obtener la modulación FM.
def modularSenalFM(Ac,senalInterpolada, tiempoInterpolado,frecuenciaInicialPortadora):
    senalIntegrada = integrate.cumtrapz(senalInterpolada,tiempoInterpolado,initial=0) 
    modulacionFM = Ac*np.cos(2*np.pi*frecuenciaInicialPortadora*tiempoInterpolado + 20*senalIntegrada)
    return modulacionFM