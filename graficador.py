import matplotlib.pylab as plt

def graficarEnTiempo(tiempo, senal, nombre, etiqueta):
    plt.figure(figsize=(9, 5))
    plt.plot(tiempo, senal)
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