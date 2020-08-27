import matplotlib.pylab as plt

#Entradas:  Tiempo de la señal
#           Señal a graficar
#           Nombre del gráfico
#           Etiqueta del gráfico
#           Color del gráfico
#Salidas:   Gráfico en el tiempo de una señal.
#Descripcion: Se grafica la señal en el tiempo, asignando un nombre
#             color y etiqueta a la figura.
def graficarEnTiempo(tiempo, senal, nombre, etiqueta,color):
    plt.figure(figsize=(10, 4))
    #plt.plot(tiempo[0:1000],senal[0:1000])
    plt.plot(tiempo,senal,label=etiqueta,color=color)
    plt.xlabel("tiempo (s)")
    plt.ylabel('Amplitud (cm)')
    plt.title(nombre)
    plt.legend(loc='upper right')
    plt.xlim([2.6025,2.6050]) 
    plt.savefig(nombre)
    plt.grid()

#Entradas:  Frecuencia de la señal
#           Señal a graficar
#           Nombre del gráfico
#           Etiqueta del gráfico
#           Color del gráfico
#Salidas:   Gráfico en la frecuencia de una señal.
#Descripcion: Se grafica la señal en las frecuencias, asignando un nombre
#             color y etiqueta a la figura.
def graficarEnFrecuencias(freq, senal, nombre, etiqueta,color):
    plt.figure(figsize=(10, 4))
    plt.plot(freq, senal,label=etiqueta,color=color)
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel('Amplitud (cm)')
    plt.title(nombre)
    plt.legend(loc='upper right')
    #plt.xlim([-1000,1000])
    plt.savefig(nombre)
    plt.grid()

#Entradas:  Dato o señal a graficar
#           Titulo del gráfico 
#           Nombre del eje X
#           Nombre del eje Y
#           Color del gráfico
#           Cantidad de filas en la figura
#           Cantidad de columnas en la figura
#           Posición del gráfico en la figura
#Salidas:   Grafico estará en una figura más grande
#Descripción:   Se crea subgrafico con un nombre en especifico.
def crearSubGrafico(dato,valorEjeX,titulo,xLabel,yLabel,color,filas,columnas,posicion):
    plt.subplot(filas,columnas,posicion)
    plt.title(titulo)
    plt.plot(valorEjeX,dato,color=color)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)

#Entrada:
#Salida:    Formato de subgraficos en la figura
#Descripción:   Se asigna un formato al subgrafico para una mejor visualización
def formatoGrafico():
    plt.subplots_adjust(hspace=1)
    plt.rc('font', size=15)
    fig = plt.gcf()
    fig.set_size_inches(16, 9)
