import numpy as np
import matplotlib.pylab as plt
import cmath
from scipy.fftpack import fft, fftfreq

# Construcción de la señal
N = 128 # number of point in the whole interval
f = 200.0 #  frequency in Hz
dt = 1 / (f * 32 ) #32 samples per unit frequency
t = np.linspace( 0, (N-1)*dt, N)
y = np.cos(2 * np.pi * f * t) - 0.4 * np.sin(2 * np.pi * (2*f) * t )+ 0.17*np.sin(2 * np.pi * (15*f) * t )
T_k=np.zeros(N, dtype= complex)
n=np.linspace(0,N-1, N, dtype=int)
k_1=np.linspace(0,N-1, N, dtype=int)

for k in range (N):
    T_k[k]=np.sum(y*np.exp(-1j*2*np.pi*k*n/N))
# 1) implemente de la transformada de fourier discreta
T_k=T_k/np.max(T_k)
# 2) Genere el arreglo de las frecuencias (ver documentación de fftfreq):(bonus)
plt.plot(k_1,T_k)
#plt.xlim(1,-1)
plt.show()
#x_n=np.zeros(N, dtype=complex)
#k=np.linspace(0,N-1, N, dtype=int)
#for n in range (N):
#    x_n[n]=np.sum(y[:N]*np.exp(1j*2*np.pi*n/N)*np.exp(k))
#plt.plot(t, x_n)
#plt.show()
# 3) Haga una gráfica comparando método propio con implementación de scipy.fftpack.fft
fft_x = fft(y) / N # FFT Normalized
freq = fftfreq(N, dt) # Recuperamos las frecuencias
plt.plot(freq, np.abs(T_k))
plt.show()
# 1) Almacene los datos de signal.dat. La columna 1 es el tiempo y la columna 2 es su señal f(t).
#Grafique su señal en función del tiempo.
signal=np.genfromtxt('signal.dat', delimiter=",")
time=signal[:,0]
señal=signal[:,1]
plt.plot(time, signal)
plt.show()
# 2) Use fftfreq (BONO si usa su implementación propia) y haga una gráfica de su transformada de fourier en función de las frecuencias.

# 3) Haga un filtro pasa bajos que le permita filtrar el ruido de la señal del punto 1. #
#Use la gráfica de la transformada de fourier del punto 3 para determinar un valor apropiado de la frecuencia de corte que debe usar para filtrar dicho ruido de alta frecuencia.

# 4) Grafique la señal filtrada
