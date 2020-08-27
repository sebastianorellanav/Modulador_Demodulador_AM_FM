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
import interpolador as inter
import portadora as portadora
import modulador as mod
import fourier as ft
import demodulador as dem
import graficador as gf
import escribirSeñal as esc
import matplotlib.pylab as plt
import numpy as np

################################## 1. Información para trabajar ##################################

#Datos:
Ac = 1                                              #Amplitud de coseno
frecuenciaInicialPortadora = 20000                  #Frecuencia de portadora
frecuenciaMuestreoPortadora = 0.00001               #Frecuencia muestreo de portadora

#Se obtiene señal de audio
frecuenciaMuestreoSenal, senal = ls.leerSenal('handel.wav')

#Obtención de tiempo del audio
tiempo = ls.obtenerIntervaloTiempo(senal,frecuenciaMuestreoSenal)

#Interpolando tiempo con la señal original
tiempoInterpolado,interpolacion = inter.obtenerTiempoInterpolado(senal,tiempo,frecuenciaMuestreoSenal,frecuenciaMuestreoPortadora)
senalInterpolada = inter.obtenerSenalInterpolada(interpolacion,tiempoInterpolado)

#Interpolando en frecuencia la señal original
transformadaOriginal,frecuenciaOriginal = ft.obtenerTransformada(senal,frecuenciaMuestreoSenal)

################################## 2. Obtención de Portadora ##################################

#Obteniendo portadora
portadora = portadora.obtenerPortadora(Ac,frecuenciaInicialPortadora,tiempoInterpolado)

#Interpolando en frecuencia la portadora
transformadaPortadora,frecuenciaPortadora = ft.obtenerTransformada(portadora,frecuenciaMuestreoPortadora)

################################## 3. Modulación AM ##################################

#Obteniendo modulación AM en el tiempo
moduladacionAM = mod.modularSenalAM(senalInterpolada,portadora)

#Obteniendo modulación AM en el frecuencia
transformadaAM,frecuenciaAM = ft.obtenerTransformada(moduladacionAM,frecuenciaMuestreoPortadora)

################################### 4. Demodulación AM ##################################

#Obteniendo demodulación AM en el tiempo
demodulacionAM = dem.demodularAm(moduladacionAM,portadora)
taps = 200			#numero de pulsos
cutoff = 1700		#frecuencia de corte
#Aplicando filtro pasabajos en demodulación
demodulacionAM = ft.filtroPasaBajo(demodulacionAM,frecuenciaMuestreoSenal,taps,cutoff,0)

#Obteniendo demodulación AM en la frecuencia
transformadaDemoduladaAM,frecuenciaDemoduladaAM =  ft.obtenerTransformada(demodulacionAM,frecuenciaMuestreoSenal)

################################## 5. Modulación FM ##################################

#Obteniendo demodulación FM en el tiempo
moduladacionFM = mod.modularSenalFM(Ac,senalInterpolada, tiempoInterpolado,frecuenciaInicialPortadora)

#Obteniendo modulación FM en el frecuencia
transformadaFM,frecuenciaFM = ft.obtenerTransformada(moduladacionFM,frecuenciaMuestreoPortadora)

################################### 6. Graficos ############################################

### Graficos ###
#1. Graficos AM en el tiempo
gf.graficarEnTiempo(tiempo,senal,'Señal original en el tiempo',"f(t) = señal original","g")
gf.graficarEnTiempo(tiempoInterpolado,portadora,'Señal portadora en el tiempo',"portadora = cos(2*pi*fc*t)","r")
gf.graficarEnTiempo(tiempoInterpolado,moduladacionAM,'Señal AM en el tiempo',"y(t) = K*m(t)*cos(2*pi*fc*t)","purple")
gf.graficarEnTiempo(tiempoInterpolado,demodulacionAM,'Señal AM Demodulada',"f(t) = señal demodulada AM","g")

#2. Graficos AM en la frecuencia
gf.graficarEnFrecuencias(frecuenciaOriginal,transformadaOriginal,'Señal original en la frecuencia',"ftt(f(t)) = señal en frecuencia","g")
gf.graficarEnFrecuencias(frecuenciaPortadora,transformadaPortadora,'Portadora en la frecuencia',"fft(portadora) = portadora en frecuencia","r")
gf.graficarEnFrecuencias(frecuenciaAM,transformadaAM,'AM en la frecuencia',"ftt(y(t)) = AM en frecuencia","purple")
gf.graficarEnFrecuencias(frecuenciaDemoduladaAM,transformadaDemoduladaAM,'Demodulada AM en la frecuencia',"ftt(Demodulada) = Demodulada en frecuencia","g")

#3. Graficos FM en el tiempo
gf.graficarEnTiempo(tiempo,senal,'Señal original en el tiempo',"f(t) = señal original","g")
gf.graficarEnTiempo(tiempoInterpolado,portadora,'Señal portadora en el tiempo',"portadora = cos(2*pi*fc*t)","r")
gf.graficarEnTiempo(tiempoInterpolado,moduladacionFM,'Señal FM en el tiempo',"y(t) = cos(2*pi*fc*t + k*integral(m(T)dT))","purple")

#4. Graficos FM en la frecuencia
gf.graficarEnFrecuencias(frecuenciaOriginal,transformadaOriginal,'Señal original en la frecuencia',"ftt(f(t)) = señal en frecuencia","g")
gf.graficarEnFrecuencias(frecuenciaPortadora,transformadaPortadora,'Portadora en la frecuencia',"fft(portadora) = portadora en frecuencia","r")
gf.graficarEnFrecuencias(frecuenciaFM,transformadaFM,'FM en la frecuencia',"ftt(y(t)) = FM en frecuencia","purple")

plt.show()


### Subgraficos ###
#1. Graficos AM en el tiempo
plt.suptitle("Gráficos señal en el tiempo y modulación AM")
gf.crearSubGrafico(senal,tiempo,'Señal original en el tiempo','Tiempo (s)','Amplitud','g',4,1,1)
gf.crearSubGrafico(portadora,tiempoInterpolado,'Señal portadora en el tiempo','Tiempo (s)','Amplitud','r',4,1,2)
gf.crearSubGrafico(moduladacionAM,tiempoInterpolado,'Señal AM en el tiempo','Tiempo (s)','Amplitud','purple',4,1,3)
gf.crearSubGrafico(demodulacionAM,tiempoInterpolado,'Señal AM Demodulada','Tiempo (s)','Amplitud','g',4,1,4)
gf.formatoGrafico()
plt.show()

#2. Graficos AM en la frecuencia
plt.suptitle("Gráficos señal en la frecuencia y modulación AM")
gf.crearSubGrafico(transformadaOriginal,frecuenciaOriginal,'Señal original en la frecuencia','Frecuencia (s)','Amplitud','g',4,1,1)
gf.crearSubGrafico(transformadaPortadora,frecuenciaPortadora,'Portadora en la frecuencia','Frecuencia (s)','Amplitud','r',4,1,2)
gf.crearSubGrafico(transformadaAM,frecuenciaAM,'AM en la frecuencia','Frecuencia (s)','Amplitud','purple',4,1,3)
gf.crearSubGrafico(transformadaDemoduladaAM,frecuenciaDemoduladaAM,'Demodulada AM en la frecuencia','Frecuencia (s)','Amplitud','g',4,1,4)
gf.formatoGrafico()
plt.show()

#3. Graficos FM en el tiempo
plt.suptitle("Gráficos señal en el tiempo y modulación FM")
gf.crearSubGrafico(senal,tiempo,'Señal original en el tiempo','Tiempo (s)','Amplitud','g',3,1,1)
gf.crearSubGrafico(portadora,tiempoInterpolado,'Señal portadora en el tiempo','Tiempo (s)','Amplitud','r',3,1,2)
gf.crearSubGrafico(moduladacionFM,tiempoInterpolado,'Señal FM en el tiempo','Tiempo (s)','Amplitud','purple',3,1,3)
gf.formatoGrafico()
plt.show()

#2. Graficos FM en la frecuencia
plt.suptitle("Gráficos señal en la frecuencia y modulación FM")
gf.crearSubGrafico(transformadaOriginal,frecuenciaOriginal,'Señal original en la frecuencia','Frecuencia (s)','Amplitud','g',3,1,1)
gf.crearSubGrafico(transformadaPortadora,frecuenciaPortadora,'Portadora en la frecuencia','Frecuencia (s)','Amplitud','r',3,1,2)
gf.crearSubGrafico(transformadaFM,frecuenciaFM,'FM en la frecuencia','Frecuencia (s)','Amplitud','purple',3,1,3)
gf.formatoGrafico()
plt.show()

################################## Almacenamiento de audio ############################################

esc.guardarWav("salidaDemodulada",100000,demodulacionAM) #Valor 100000 permite tener el audio original
esc.guardarWav("salidadModulada",100000,moduladacionAM)