import numpy as np
import matplotlib.pylab as plt
import cmath
from scipy.fftpack import fft, fftfreq
from scipy.io import wavfile
# Construcción de la señal
N = 128 # number of point in the whole interval
f = 200.0 #  frequency in Hz
dt = 1 / (f * 32 ) #32 samples per unit frequency
t = np.linspace( 0, (N-1)*dt, N)
y = np.cos(2 * np.pi * f * t) - 0.4 * np.sin(2 * np.pi * (2*f) * t )+ 0.17*np.sin(2 * np.pi * (15*f) * t )
T_k=np.zeros(N, dtype= complex)
n=np.linspace(0,N-1, N, dtype=int)

# 1) implemente de la transformada de fourier discreta
def Transformada1(T, fun, en, EN):
    for k in range (EN):
        T[k]=np.sum(fun*np.exp(-1j*2*np.pi*k*en/EN))
    return (T/np.max(T))
def Inversa(T, fun, kn, EN):
    for n in range (EN):
        T[n]=np.sum(fun*np.exp(1j*2*np.pi*kn*n/EN))
    return (T/np.max(T))
T_k= Transformada1(T_k, y, n, N) 

# 2) Genere el arreglo de las frecuencias (ver documentación de fftfreq):(bonus)
fft_x = fft(y) 
fft_x_norm = fft_x/np.max(fft_x)

freq = fftfreq(N, dt) # Recuperamos las frecuencias

# 3) Haga una gráfica comparando método propio con implementación de scipy.fftpack.fft

plt.plot(freq, np.abs(T_k), label="Implementación propia", lw=2)
plt.plot(freq, np.abs(fft_x_norm), label="Implementación scipy", lw=1)
plt.legend()
plt.show()

#_____________________________________________________________________________________________________
#Ejercicio 2 
# 1) Almacene los datos de signal.dat. La columna 1 es el tiempo y la columna 2 es su señal f(t).
#Grafique su señal en función del tiempo y guarde dicha gráfica sin mostrarla en signal.png.
signal=np.genfromtxt('signal.dat', delimiter=",")
time=signal[:,0]
señal=signal[:,1]
plt.plot(time, señal)
plt.savefig("signal.png")
plt.close()
# 2) Use fftfreq (BONO si usa su implementación propia) y haga una gráfica de su transformada de
#fourier en función de las frecuencias. Guarde dicha gráfica sin mostrarla en Fourier_trans.png
Ns = len(señal)
ns=np.linspace(0,Ns-1, Ns, dtype=int)
dts = time[1]-time[0]
S_k= np.zeros(Ns, dtype= complex)
S_k = Transformada1(S_k, señal, ns, Ns)
freqs = fftfreq(Ns, dts)
plt.plot(freqs, np.abs(S_k))
plt.savefig("Fourier_trans.png")
plt.close()
# 3) Haga un filtro pasa bajos que le permita filtrar el ruido de la señal del punto 1. Use la gráfica de la
#transformada de fourier del punto 3 para determinar un valor apropiado de la frecuencia de corte que
#debe usar para filtrar dicho ruido de alta frecuencia.
for l in range(Ns):
    Frecu=freqs[l]
    if (np.abs(Frecu) > 600):
        S_k[l]= 0
    else: 
        continue  
# 4) Grafique su señal filtrada
s_n=np.zeros(Ns, dtype=complex)

s_n=Inversa(s_n, S_k,ns, Ns )
plt.plot(time, np.real(s_n))
plt.savefig("Señal_Filtrada.png")
#____________________________________________________________________________________________________________
#Ejercicio 3 
#violin

rate_v, data_v = wavfile.read('violin.wav')

N_v = len(data_v)
n_v= np.linspace(0,N_v-1, N_v, dtype=int)
dt_v = 1.0 / rate_v
tiempo_v = np.arange(N_v) * dt_v

plt.plot(tiempo_v, data_v, color='navy')
plt.title('Señal en función del tiempo - Violín')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')
plt.savefig('violin.png')
plt.close()

fft_v = fft(data_v)
freqs_v = fftfreq(N_v, dt_v)
idx_v = np.argsort(freqs_v)
freqs_v_sorted = freqs_v[idx_v]
fft_v_mag_sorted = np.abs(fft_v[idx_v])

plt.figure(figsize=(10, 4))
plt.plot(freqs_v, np.abs(fft_v), color='darkred')
plt.title('Transformada de Fourier - Violín')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Magnitud')
plt.xlim(-rate_v / 2, rate_v / 2)
plt.savefig('Fourier_trans_violin.png')
plt.close()
#Eliminación del pico principal
pos_mask_v = freqs_v > 0
pico_idx_v = np.argmax(np.abs(fft_v[pos_mask_v]))
frec_pico_v = freqs_v[pos_mask_v][pico_idx_v]

fft_v_sin_pico = fft_v.copy()
fft_v_sin_pico[np.abs(np.abs(freqs_v) - frec_pico_v) < 25] = 0
sig_v_sin_pico = np.real(np.fft.ifft(fft_v_sin_pico))

# Filtro Pasaaltos
fc_alto = 4000  # Frecuencia de corte en Hz
fft_v_pasaaltos = fft_v.copy()
fft_v_pasaaltos[np.abs(freqs_v) < fc_alto] = 0
sig_v_pasaaltos = np.real(np.fft.ifft(fft_v_pasaaltos))

#Filtro Pasabajos
fc_bajo = 400  # Frecuencia de corte en Hz
fft_v_pasabajos = fft_v.copy()
fft_v_pasabajos[np.abs(freqs_v) > fc_bajo] = 0
sig_v_pasabajos = np.real(np.fft.ifft(fft_v_pasabajos))


fig, axes = plt.subplots(3, 1, figsize=(11, 8), sharex=True)

axes[0].plot(tiempo_v, sig_v_sin_pico, color='purple')
axes[0].set_title(f'Violín sin pico principal ({frec_pico_v:.1f} Hz eliminados)')
axes[0].set_ylabel('Amplitud')


axes[1].plot(tiempo_v, sig_v_pasaaltos, color='green')
axes[1].set_title(f'Violín Pasaaltos (f > {fc_alto} Hz)')
axes[1].set_ylabel('Amplitud')


axes[2].plot(tiempo_v, sig_v_pasabajos, color='orange')
axes[2].set_title(f'Violín Pasabajos (f < {fc_bajo} Hz)')
axes[2].set_xlabel('Tiempo [s]')
axes[2].set_ylabel('Amplitud')


plt.tight_layout()
plt.savefig('filtroviolin.png')
plt.close()

wavfile.write('violin_sin_pico.wav', rate_v, sig_v_sin_pico.astype(data_v.dtype))
wavfile.write('violin_pasaaltos.wav', rate_v, sig_v_pasaaltos.astype(data_v.dtype))
wavfile.write('violin_pasabajos.wav', rate_v, sig_v_pasabajos.astype(data_v.dtype))

#Trompeta 

rate_t, data_t = wavfile.read('trumpet.wav')


N_t = len(data_t)
dt_t = 1.0 / rate_t
tiempo_t = np.arange(N_t) * dt_t

plt.figure(figsize=(10, 4))
plt.plot(tiempo_t, data_t, color='navy', alpha=0.8)
plt.title('Señal en función del tiempo - Trompeta')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')
plt.savefig('trumpet.png')
plt.close()


fft_t = fft(data_t)
freqs_t = fftfreq(N_t, d=dt_t)

plt.figure(figsize=(10, 4))
plt.plot(freqs_t, np.abs(fft_t), color='darkred')
plt.title('Transformada de Fourier - Trompeta')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Magnitud')
plt.xlim(-rate_t / 2, rate_t / 2)

plt.savefig('Fourier_trans_trumpet.png')
plt.close()


# Eliminación del pico principal
pos_mask_t = freqs_t > 0
pico_idx_t = np.argmax(np.abs(fft_t[pos_mask_t]))
frec_pico_t = freqs_t[pos_mask_t][pico_idx_t]

fft_t_sin_pico = fft_t.copy()
fft_t_sin_pico[np.abs(np.abs(freqs_t) - frec_pico_t) < 25] = 0
sig_t_sin_pico = np.real(np.fft.ifft(fft_t_sin_pico))

#Filtro Pasaaltos
fft_t_pasaaltos = fft_t.copy()
fft_t_pasaaltos[np.abs(freqs_t) < fc_alto] = 0
sig_t_pasaaltos = np.real(np.fft.ifft(fft_t_pasaaltos))

# Filtro Pasabajos
fft_t_pasabajos = fft_t.copy()
fft_t_pasabajos[np.abs(freqs_t) > fc_bajo] = 0
sig_t_pasabajos = np.real(np.fft.ifft(fft_t_pasabajos))


fig, axes = plt.subplots(3, 1, figsize=(11, 8), sharex=True)

axes[0].plot(tiempo_t, sig_t_sin_pico, color='purple')
axes[0].set_title(f'Trompeta sin pico principal ({frec_pico_t:.1f} Hz eliminados)')
axes[0].set_ylabel('Amplitud')
axes[0].grid(True)

axes[1].plot(tiempo_t, sig_t_pasaaltos, color='green')
axes[1].set_title(f'Trompeta Pasaaltos (f > {fc_alto} Hz)')
axes[1].set_ylabel('Amplitud')
axes[1].grid(True)

axes[2].plot(tiempo_t, sig_t_pasabajos, color='orange')
axes[2].set_title(f'Trompeta Pasabajos (f < {fc_bajo} Hz)')
axes[2].set_xlabel('Tiempo [s]')
axes[2].set_ylabel('Amplitud')
axes[2].grid(True)

plt.tight_layout()
plt.savefig('filtrotrompeta.png')
plt.close()

wavfile.write('trumpet_sin_pico.wav', rate_t, sig_t_sin_pico.astype(data_t.dtype))
wavfile.write('trumpet_pasaaltos.wav', rate_t, sig_t_pasaaltos.astype(data_t.dtype))
wavfile.write('trumpet_pasabajos.wav', rate_t, sig_t_pasabajos.astype(data_t.dtype))