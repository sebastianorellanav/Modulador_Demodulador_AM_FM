##########################################################################################################
###########################      Laboratorio 3: Modulador AM - FM       ##################################
###########################         Sebastian Orellana Verdejo          ##################################
###########################            Franco Tapia Cabañas             ##################################
###########################                                             ##################################
###########################            Redes de Computadores            ##################################
##########################################################################################################
###########################    Nota:                                    ##################################
##########################################################################################################

#Importar Librerías
import leerSeñal as ls
import modulador as mod
import fourier as ft
import graficador as gf
import matplotlib.pylab as plt

#Main
#Leer Señal desde el archivo de audio
freqOriginal, senalOriginal = ls.leerSenal('handel.wav')
intervaloTiempo = ls.obtenerIntervaloTiempo(senalOriginal, freqOriginal)

#obtener transformada de fourier de la señal original
intervaloFreq, transformada = ft.obtenerTransformada(senalOriginal)

#Graficar señal en el tiempo y en la frecuencia
gf.graficarEnTiempo(intervaloTiempo, senalOriginal, "Señal Original", "f(t) = ")
gf.graficarEnFrecuencias(intervaloFreq, transformada, "Transformada de la original", "Transformada")

#modular señal
portadora = mod.obtenerPortadora(freqOriginal+500, intervaloTiempo)
intervaloFreq, transformada = ft.obtenerTransformada(portadora)
gf.graficarEnFrecuencias(intervaloFreq, transformada, "Transformada de la Portadora", "")

modulada = mod.modularSenalAM(senalOriginal, portadora)


gf.graficarEnTiempo(intervaloTiempo, modulada, "Señal Modulada", "f(t) = ")

plt.show()