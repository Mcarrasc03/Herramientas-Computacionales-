import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np


Datos = np.genfromtxt("Datos_LF_PLANETAS.txt", delimiter=", ")


x_tierra = Datos[:, 2]
y_tierra = Datos[:, 3]
x_sol = Datos[:, 6]
y_sol = Datos[:, 7]

num_frames = Datos.shape[0]


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))


ax1.set_aspect('equal')
ax1.set_title("Órbitas 2 cuerpos", fontsize=14, pad=10)
ax1.plot(x_tierra, y_tierra, color="#173489", alpha=0.3, linestyle="--")
ax1.plot(x_sol, y_sol, color="#FFD700", alpha=0.3, linestyle="--")

(line1,) = ax1.plot([], [], "o", color="#173489", markersize=8, label="Tierra")

(line2,) = ax1.plot([], [], "o", color="#FFD700", markersize=14, label="Sol")

ax1.set_xlim(-1.2, 1.2)
ax1.set_ylim(-1.2, 1.2)
ax1.set_xlabel("X [UA]", fontsize=12)
ax1.set_ylabel("Y [UA]", fontsize=12)
ax1.grid(False)
ax1.legend(loc="upper right")

time_text = ax1.text(0.02, 0.93, "", transform=ax1.transAxes, fontsize=12)


ax2.set_title("Zoom: Movimiento del Sol", fontsize=14, pad=10)
ax2.set_aspect('equal')
ax2.plot(x_sol, y_sol, color="#FFD700", alpha=0.4, linestyle="--")

(line3,) = ax2.plot(
    [], [], "o", color="#FFD700", markersize=12, label="Sol"
)


margin_x = (
    (np.max(x_sol) - np.min(x_sol)) * 0.2
    if np.max(x_sol) != np.min(x_sol)
    else 0.05
)
margin_y = (
    (np.max(y_sol) - np.min(y_sol)) * 0.2
    if np.max(y_sol) != np.min(y_sol)
    else 0.05
)

ax2.set_xlim(np.min(x_sol) - margin_x, np.max(x_sol) + margin_x)
ax2.set_ylim(np.min(y_sol) - margin_y, np.max(y_sol) + margin_y)
ax2.set_xlabel("X [UA]", fontsize=12)
ax2.set_ylabel("Y [UA]", fontsize=12)
ax2.grid(False)
ax2.legend(loc="upper right")


plt.tight_layout()



def init():
    line1.set_data([], [])
    line2.set_data([], [])
    line3.set_data([], [])
    time_text.set_text("")
    return line1, line2, line3, time_text


def update(frame):
    xt = Datos[frame, 2]
    yt = Datos[frame, 3]

    xs = Datos[frame, 6]
    ys = Datos[frame, 7]


    line1.set_data([xt], [yt])
    line2.set_data([xs], [ys])

    line3.set_data([xs], [ys])

    # Reloj de tiempo
    t_actual = Datos[frame, 0]
    time_text.set_text(f"t = {t_actual:.2f} días")

    return line1, line2, line3, time_text


# Creación y renderizado de la animación
ani = animation.FuncAnimation(
    fig,
    update,
    frames=num_frames,
    init_func=init,
    blit=True,
    interval=1000 / 60,
)

writer = animation.FFMpegWriter(fps=60, bitrate=1800)
ani.save("Órbitas.mp4", writer=writer)
plt.close()