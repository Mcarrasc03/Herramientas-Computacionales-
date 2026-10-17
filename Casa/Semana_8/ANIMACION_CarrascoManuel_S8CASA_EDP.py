import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
import time

t_inicio = time.perf_counter()

print("¡¡¡ADVERTENCIA!!!: Este codigo suele demorar en correr al rededor de 5 minutos, no alarmarse por demora")
print("En caso de no querer esperar, detener el código \nLas imagenes de PLOTS ya fueron creadas si se usó el makefile y los videos van adjuntados en la tarea")
DatosForzado = np.genfromtxt("ExtremoForzado.txt", delimiter=", ")

xf = DatosForzado[0, :]
dt= (0.5/300)*0.02
num_frames = DatosForzado.shape[0] - 1


fig, ax = plt.subplots(figsize=(10, 6))
ax.set_title(r"Cuerda extremo forzado periodico w= 100 $\pi$ y A=0.05", fontsize=16)

ymin = DatosForzado[1:].min()
ymax = DatosForzado[1:].max()
ax.set_xlim(-0.1, 2.1)
ax.set_ylim(ymin, ymax)
ax.set_xlabel("X [m]", fontsize=14)
ax.set_ylabel("Amplitud u(x,t)[m]", fontsize=14)
ax.grid(False)

(line,) = ax.plot([], [], lw=2, color='red', label=' ')
legend = ax.legend(loc='upper right')


def init():
    line.set_data([], [])
    legend.get_texts()[0].set_text(' ')
    return line, legend


def update(frame):

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

writer = animation.FFMpegWriter(fps=60, bitrate=1800)
ani.save('CuerdaForzada.mp4', writer=writer)

plt.close()

t_intermedio= time.perf_counter()
tiempo_parcial = t_intermedio - t_inicio
minutos = tiempo_parcial//60
segundos = tiempo_parcial%60

print(f"Video de Cuerda Forzada creado en {minutos:.0f}:{segundos:.2f} \nCreando video Extremos fijos")


#"""
DatosFijo = np.genfromtxt("ExtremosFijos.txt", delimiter=", ")

x = DatosFijo[0, :]

num_frames = DatosFijo.shape[0] - 1
fig, ax = plt.subplots(figsize=(10, 6))

ax.set_title("Cuerda con extremos fijos", fontsize=16, pad=12)


ax.set_xlim(-0.1, 2.1)
ax.set_ylim(-0.150, 0.150)
ax.set_xlabel("X [m]", fontsize=14)
ax.set_ylabel("Amplitud u(x,t) [m]", fontsize=14)
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
#"""
print(f"Video de Cuerda extremos fijos creado")
t_final= time.perf_counter()
tiempo_final = t_final - t_inicio
minutosf = tiempo_final//60
segundosf = tiempo_final%60
print(f"Tiempo total de ejecucion: {minutosf:.0f}:{segundosf:.2f}")
