import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft2, ifft2, fftshift, ifftshift


Luna = plt.imread('moon.jpg')

rows, cols = Luna.shape


Lfrec = fft2(Luna)
LfrecS = fftshift(Lfrec)

mag = np.abs(LfrecS)
log_mag = np.log(mag + 1e-5) # Magnitud en escala logarítmica


k_size = 17  # Ventana de N x N vecinos 
kernel = np.ones((k_size, k_size)) / (k_size * k_size) #Promedio local de alrededores usando convolución en espectro 

# Alinear el kernel con las dimensiones de la imagen para la convolución FFT
kernel_padded = np.zeros((rows, cols))
kernel_padded[:k_size, :k_size] = kernel
kernel_padded = np.roll(kernel_padded, -k_size // 2, axis=0)
kernel_padded = np.roll(kernel_padded, -k_size // 2, axis=1)
espectro_promedio = ifft2(fft2(log_mag) * fft2(kernel_padded)).real


diferencia = log_mag - espectro_promedio #Comparar cada frecuencia con sus alrededores y detectar anomalías
std_diff = np.std(diferencia)

sensibilidad = 1.8
mascara_ruido = diferencia > (sensibilidad * std_diff)

#No eliminar las bajas frecuencias del centro (Al inicio no se incluyo esto 
#pero la imagen quedaba sin iluminación, esta fue la solución y ahi mejoro la imagen)
cy, cx = rows // 2, cols // 2
radio_centro = 10
y_grid, x_grid = np.ogrid[:rows, :cols]
dist_al_centro = np.sqrt((x_grid - cx)**2 + (y_grid - cy)**2)

mascara_ruido[dist_al_centro <= radio_centro] = False


LfrecS_limpio = LfrecS.copy()
fases = np.angle(LfrecS)
mag_corregida = np.exp(espectro_promedio)

#LfrecS_limpio1[mascara_ruido] = mag_corregida[mascara_ruido] * np.exp(1j * fases[mascara_ruido]) 
#Esta fue en vez de volverla 0 cambiarla a la de los alrededores, pero dio mejor volviendolas 0 
LfrecS_limpio[mascara_ruido] = 0

f_ishift = ifftshift(LfrecS_limpio)
Luna_limpia = np.abs(ifft2(f_ishift))

plt.figure(figsize=(14, 5))

plt.subplot(121)
plt.imshow(Luna, cmap='gray')
plt.title('Imagen Original')

plt.subplot(122)
plt.imshow(Luna_limpia, cmap='gray')
plt.title('Imagen Filtrada')

plt.tight_layout()
plt.show()


# 1) Cargar los datos de fase y magnitud
# Si los archivos son texto plano, se usa np.loadtxt
amplitud = np.loadtxt('magnitude.dat')
fase = np.loadtxt('phase.dat')

# 2) Construir la transformada de Fourier en forma compleja: Z = A * e^(i * fase)
f_compleja = amplitud * np.exp(1j * fase)

# 3) Obtener la imagen aplicando la transformada inversa
imagen_recuperada = np.abs(ifft2(f_compleja))

# NOTA: Si los datos de amplitud y fase provenían de un espectro centrado (fftshift),
# deshaz el centrado antes de calcular la IFFT descomentando la siguiente línea:
# imagen_recuperada = np.abs(ifft2(ifftshift(f_compleja)))

# Mostrar la imagen reconstruida
plt.figure(figsize=(6, 6))
plt.imshow(imagen_recuperada, cmap='gray')
plt.title('Imagen Recuperada')
plt.axis('off')
plt.show()