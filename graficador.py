import matplotlib.pylab as plt

def graficarEnTiempo(tiempo, senal, nombre, etiqueta):
    plt.figure(figsize=(9, 5))
    plt.plot(tiempo, senal, label=etiqueta)
    plt.xlabel("tiempo (s)")
    plt.ylabel('Amplitud (cm)')
    plt.title(nombre)
    plt.legend(loc='upper right')
    plt.xlim([0,0.01]) 
    plt.grid()

def graficarEnFrecuencias(freq, senal, nombre, etiqueta):
    plt.figure(figsize=(9, 5))
    plt.fill_between(freq, senal.real)
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel('Amplitud (cm)')
    plt.title(nombre)
    #plt.xlim([-9,9]) -> depende del grafico
    plt.grid()