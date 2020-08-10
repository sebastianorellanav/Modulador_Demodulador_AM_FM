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
gf.graficarEnTiempo(intervaloTiempo, senalOriginal)
gf.graficarEnFrecuencias(intervaloFreq, transformada)

#modular señal
modulada = mod.modularSenalAM(freqOriginal + 500, senalOriginal, intervaloTiempo)

plt.show()