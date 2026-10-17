import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
# 1. Leemos el archivo omitiendo los comentarios con '#'
datos = np.genfromtxt('Temperatura.txt', delimiter=', ', comments='#')

N_pasos = datos.shape[0] // 10
tensor_temperatura = datos.reshape((N_pasos, 10, 10))


num_pasos, Ny, Nx = tensor_temperatura.shape

fig, ax = plt.subplots(figsize=(6, 5))

# Rangos de temperatura para fijar la escala de color
vmin = np.min(tensor_temperatura)
vmax = np.max(tensor_temperatura)

# Preparamos el objeto de la imagen vacío o con ceros
im = ax.imshow(
    np.zeros((Ny, Nx)), 
    cmap='hot', 
    vmin=vmin, 
    vmax=vmax, 
    origin='lower', 
    interpolation='bicubic'
)

cbar = fig.colorbar(im, ax=ax)
cbar.set_label('Temperatura (°C)', rotation=270, labelpad=15)

ax.set_xlabel('Posición X')
ax.set_ylabel('Posición Y')
titulo = ax.set_title('')

# 1. Función de Inicialización
def init():
    im.set_array(tensor_temperatura[0])
    titulo.set_text('Mapa de Temperatura - Paso 0')
    return [im, titulo]

# 2. Función de Actualización
def actualizar(frame):
    im.set_array(tensor_temperatura[frame])
    titulo.set_text(f'Mapa de Temperatura - Paso {frame}')
    return [im, titulo]

# 3. Animación pasando init_func
ani = animation.FuncAnimation(
    fig, 
    actualizar, 
    init_func=init, 
    frames=num_pasos, 
    interval=1000/60, 
    blit=True
)

# 1. Configurar el escritor de MP4 (FFMpegWriter)
Writer = animation.writers['ffmpeg']
writer = Writer(fps=60, metadata=dict(artist='Simulacion'), bitrate=1800)

# 2. Guardar el video como archivo .mp4
print("Guardando video MP4...")
ani.save('difusion_temperatura_2D.mp4', writer=writer)
print("¡Video guardado con éxito como 'difusion_temperatura_2D.mp4'!")
