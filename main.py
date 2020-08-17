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
import demodulador as dem
import fourier as ft
import graficador as gf
import interpolador as inter
import matplotlib.pylab as plt
import numpy as np

#Main

#################### Pasos previos ####################

#Leer Señal desde el archivo de audio
freqOriginal, senalOriginal = ls.leerSenal('handel.wav')
intervaloTiempo = ls.obtenerIntervaloTiempo(senalOriginal, freqOriginal)

#obtener transformada de fourier de la señal original
intervaloFreq, transformada = ft.obtenerTransformada(senalOriginal, freqOriginal)

#Graficar señal en el tiempo y en la frecuencia
gf.graficarEnTiempo(intervaloTiempo, senalOriginal, "Señal Original", "f(t) = ")
gf.graficarEnFrecuencias(intervaloFreq, transformada, "Transformada de la original", "Transformada")

#Obtener señal interpolada en el tiempo
interpolada = inter.interpolacionAM(senalOriginal,intervaloTiempo)
#Obteniendo rango de tiempo de señal interpolada que corresponde a tiempo de la señal modulada
largoInterpolado = len(interpolada)
tiempoModulada = mod.tiempoModulada(largoInterpolado,freqOriginal) 

####################### Portadora #######################

#Obteniendo señal portadora en el tiempo y graficando
portadora,freqNyquist = mod.obtenerPortadoraAM(freqOriginal, tiempoModulada)
gf.graficarEnTiempo(tiempoModulada, portadora, "Señal Portadora", "f(t) = ")

#Obteniendo portadora en frecuencia y graficando
intervaloFreqPortadora, transformada = ft.obtenerTransformada(portadora,freqOriginal)
gf.graficarEnFrecuencias(intervaloFreqPortadora, transformada, "Transformada de la Portadora", "")

#################### Modular señal AM ####################

#Obteniendo AM en el tiempo y graficando
moduladaAM = mod.modularSenalAM(senalOriginal, portadora)
gf.graficarEnTiempo(intervaloTiempo, moduladaAM, "Señal Modulada AM", "f(t) = ")

#Obteniendo AM en frecuencias y graficando
intervaloFreq, transformadaModuladaAM = ft.obtenerTransformada(moduladaAM, freqNyquist)
gf.graficarEnFrecuencias(intervaloFreq, transformadaModuladaAM, "Transformada de AM", "")


#################### Modular señal FM ####################

#Obteniendo FM en el tiempo y graficando
moduladaFM,freqNyquist = mod.modularSenalFM(senalOriginal,freqOriginal,tiempoModulada)
gf.graficarEnTiempo(intervaloTiempo, moduladaFM, "Señal Modulada FM", "f(t) = ")

#Obteniendo FM en frecuencias y graficando
intervaloFreq, transformadamoduladaFM = ft.obtenerTransformada(moduladaFM, freqNyquist)
gf.graficarEnFrecuencias(intervaloFreq, transformadamoduladaFM, "Transformada de FM", "")

#################### Demodular señal AM ####################

#Obteniendo Demodulada AM en el tiempo y graficando
demodulada = dem.demodularAm(moduladaAM,portadora,freqOriginal)
gf.graficarEnTiempo(intervaloTiempo, demodulada, "Señal Modulada FM", "f(t) = ")
print(demodulada)

#Obteniendo Demodulada AM en frecuencia y graficando
intervaloFreq, transformadaDemodulada = ft.obtenerTransformada(demodulada, freqOriginal)
gf.graficarEnFrecuencias(intervaloFreq, transformadaDemodulada, "Demodulada de AM", "")

#Guardando sonido demulado
dem.guardarAudio("demodulado.mp3",freqOriginal,demodulada)

plt.show()