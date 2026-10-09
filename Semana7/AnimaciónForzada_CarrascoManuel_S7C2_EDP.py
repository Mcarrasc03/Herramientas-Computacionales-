import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

dat4 = np.genfromtxt("ExtremoForzado.txt", delimiter=", ")
# Extraer el vector X (fila 0)
xf = dat4[0, :]
dt= (0.5/300)*0.02
# Número de fotogramas (filas 1 a 2999)
num_frames = dat4.shape[0] - 1

# Configuración de la figura y límites fijos para evitar brincos en la escala
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_title(r"Cuerda extremo forzado periodico w= 800 $\pi$ ", fontsize=16)
y_min = -0.150
y_max = 0.150

ax.set_xlim(-0.1, 2.1)
ax.set_ylim(y_min, y_max)
ax.set_xlabel("X", fontsize=14)
ax.set_ylabel("Amplitud u(x,t)", fontsize=14)
ax.grid(True)

(line,) = ax.plot([], [], lw=2, color='blue', label=' ')
legend = ax.legend(loc='upper right')

# Función de inicialización
def init():
    line.set_data([], [])
    legend.get_texts()[0].set_text(' ')
    return line, legend


# Función que actualiza cada fotograma
def update(frame):
    # 'frame' va de 0 a num_frames-1, por lo que la fila de Y es frame + 1
    yf = dat4[frame + 1, :]

    line.set_data(xf, yf)
    legend.get_texts()[0].set_text(f't= {frame*dt:.4f}')
    
    return line, legend


ani = animation.FuncAnimation(
    fig,
    update,
    frames=num_frames,
    init_func=init,
    blit=True,
    interval=1000 / 60,
)

# Guardar animación (utiliza PillowWriter para GIF si aún no has instalado FFmpeg)
writer = animation.FFMpegWriter(fps=60, bitrate=1800)
ani.save('CuerdaForzada.mp4', writer=writer)

plt.close()