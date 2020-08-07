import matplotlib.pylab as plt

def graficarEnTiempo(tiempo, senal):
    plt.figure(figsize=(9, 5))
    plt.plot(tiempo,senal, label='f(t) = cos(2pi * 3t) + sen(2pi * 2t)')
    plt.xlabel("tiempo (s)")
    plt.ylabel('Amplitud (cm)')
    plt.title("Señal Original")
    plt.legend(loc='upper right')
    plt.grid()

def graficarEnFrecuencias(freq, senal):
    plt.figure(figsize=(9, 5))
    plt.plot(freq, tf.real)
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel('Amplitud (cm)')
    plt.title("Transformada de Fourier de la Señal Original")
    #plt.xlim([-9,9]) -> depende del grafico
    plt.grid()