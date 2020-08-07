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

#Main
#Leer Señal desde el archivo de audio
freqOriginal, senalOriginal = ls.leerSenal('handel.wav')
intervaloTiempo = ls.obtenerIntervaloTiempo(0,9,1/1000)

#obtener transformada de fourier de la señal original
intervaloFreq, transformada = ft.obtenerTransformada(senalOriginal)

#Graficar señal en el tiempo y en la frecuencia
gf.graficarEnTiempo(intervaloTiempo, senalOriginal)
gf.graficarEnFrecuencias(intervaloFreq, transformada)

#modular señal
modulada = mod.modularSenalAM(freqOriginal + 500, senalOriginal, intervaloTiempo)
