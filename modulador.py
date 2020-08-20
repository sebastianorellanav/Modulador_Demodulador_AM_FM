import numpy as np
import scipy.integrate as integrate

def modularSenalAM(senal, portadora):
    mod = senal*portadora
    return mod


def modularSenalFM(Ac,senal,senalInterpolada, tiempoInterpolado,frecuenciaInicialPortadora):
    senalIntegrada = integrate.cumtrapz(senalInterpolada,tiempoInterpolado,initial=0) 
    modulacionFM = Ac*np.cos(np.pi*frecuenciaInicialPortadora*tiempoInterpolado + np.pi*senalIntegrada)
    return modulacionFM