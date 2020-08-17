import scipy.io.wavfile as waves
import numpy as np
import matplotlib.pylab as plt
from scipy.io import wavfile

fs, data = wavfile.read('handel.wav')

t_data = np.linspace(0, len(data)/fs, len(data))

plt.figure()
plt.plot(t_data, data)

carrier = np.cos(2 * np.pi * 2000 * t_data)

plt.figure()
plt.plot(t_data,carrier)
plt.title("grafico malo")

t_mio = np.linspace(0,len(data)/fs, 200000)
carrier2 = np.cos(2 * np.pi * 2000 * t_mio)

plt.figure()
plt.plot(t_mio,carrier2)
plt.title("MI teoria")

plt.show()

