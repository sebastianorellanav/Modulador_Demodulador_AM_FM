import matplotlib.pylab as plt

def graficarEnTiempo(tiempo, senal, nombre, etiqueta):
    plt.figure(figsize=(9, 5))
    plt.plot(tiempo[0:1000],senal[0:1000])
    plt.xlabel("tiempo (s)")
    plt.ylabel('Amplitud (cm)')
    plt.title(nombre)
    plt.legend(loc='upper right')
    #plt.xlim([0,0.01]) 
    plt.grid()

def graficarEnFrecuencias(freq, senal, nombre, etiqueta):
    plt.figure(figsize=(9, 5))
    plt.plot(freq, senal)
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel('Amplitud (cm)')
    plt.title(nombre)
    #plt.xlim([-1000,1000])
    plt.grid()

def crearSubGraficoTiempo(dato,titulo,xLabel,yLabel,color,filas,columnas,posicion):
    plt.subplot(filas,columnas,posicion)
    plt.title(titulo)
    plt.plot(dato,color=color)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)

def crearSubGrafico(dato,valorEjeX,titulo,xLabel,yLabel,color,filas,columnas,posicion):
    plt.subplot(filas,columnas,posicion)
    plt.title(titulo)
    plt.plot(valorEjeX,dato,color=color)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)

def formatoGrafico():
    plt.subplots_adjust(hspace=1)
    plt.rc('font', size=15)
    fig = plt.gcf()
    fig.set_size_inches(16, 9)
