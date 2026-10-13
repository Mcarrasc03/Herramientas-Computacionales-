import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

print("¡¡¡ADVERTENCIA!!!: Este codigo suele demorar en correr al rededor de 5 minutos, no alarmarse por demora")
DatosForzado = np.genfromtxt("ExtremoForzado.txt", delimiter=", ")

xf = DatosForzado[0, :]
dt= (0.5/300)*0.02
num_frames = DatosForzado.shape[0] - 1


fig, ax = plt.subplots(figsize=(10, 6))
ax.set_title(r"Cuerda extremo forzado periodico w= 800 $\pi$ ", fontsize=16)

ax.set_xlim(-0.1, 2.1)
ax.set_ylim(-0.150, 0.150)
ax.set_xlabel("X", fontsize=14)
ax.set_ylabel("Amplitud u(x,t)", fontsize=14)
ax.grid(False)

(line,) = ax.plot([], [], lw=2, color='red', label=' ')
legend = ax.legend(loc='upper right')

# Función de inicialización
def init():
    line.set_data([], [])
    legend.get_texts()[0].set_text(' ')
    return line, legend


# Función que actualiza cada fotograma
def update(frame):
    # 'frame' va de 0 a num_frames-1, por lo que la fila de Y es frame + 1
    yf = DatosForzado[frame + 1, :]

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


DatosFijo = np.genfromtxt("ExtremosFijos.txt", delimiter=", ")

x = DatosFijo[0, :]

num_frames = DatosFijo.shape[0] - 1
fig, ax = plt.subplots(figsize=(10, 6))

ax.set_title("Cuerda con extremos fijos", fontsize=16, pad=12)


ax.set_xlim(-0.1, 2.1)
ax.set_ylim(-0.150, 0.150)
ax.set_xlabel("X", fontsize=14)
ax.set_ylabel("Amplitud u(x,t)", fontsize=14)
ax.grid(False)

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
    y = DatosFijo[frame + 1, :]

    line.set_data(x, y)
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
ani.save('Cuerda.mp4', writer=writer)

plt.close()