import numpy as np
import scipy.integrate as integrate

def modularSenalAM(senal, portadora):
    mod = senal*portadora
    return mod


def modularSenalFM(Ac,senalInterpolada, tiempoInterpolado,frecuenciaInicialPortadora):
    senalIntegrada = integrate.cumtrapz(senalInterpolada,tiempoInterpolado,initial=0) 
    modulacionFM = Ac*np.cos(2*np.pi*frecuenciaInicialPortadora*tiempoInterpolado + 20*senalIntegrada)
    return modulacionFM