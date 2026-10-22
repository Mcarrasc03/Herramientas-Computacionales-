import numpy as np
import matplotlib.pyplot as plt

datosf = np.genfromtxt('Temperatura_ExtremosFijos.txt', delimiter=', ', comments='#')
datosa = np.genfromtxt('Temperatura_ExtremosAbiertos.txt', delimiter=', ', comments='#')

N_pasosf = datosf.shape[0] // 10
tensor_temperaturaf = datosf.reshape((N_pasosf, 10, 10))

fig, ax = plt.subplots(2, 2, figsize=(6, 6))

# Rangos de temperatura para fijar la escala de color
vmin = np.min(tensor_temperaturaf)
vmax = np.max(tensor_temperaturaf)

# Preparamos el objeto de la imagen vacío o con ceros
ax[0,0].imshow(
    tensor_temperaturaf[0,:,:], 
    cmap='hot', 
    vmin=vmin, 
    vmax=vmax, 
    origin='lower', 

)
ax[0,1].imshow(
    tensor_temperaturaf[500,:,:], 
    cmap='hot', 
    vmin=vmin, 
    vmax=vmax, 
    origin='lower', 

)
ax[1,0].imshow(
    tensor_temperaturaf[5000,:,:], 
    cmap='hot', 
    vmin=vmin, 
    vmax=55, 
    origin='lower', 
)
ax[1,1].imshow(
    tensor_temperaturaf[10000,:,:], 
    cmap='hot', 
    vmin=vmin, 
    vmax=51, 
    origin='lower', 
)
plt.savefig("Difusion.png")


N_pasosa = datosa.shape[0] // 10
tensor_temperaturaa = datosa.reshape((N_pasosa, 10, 10))

fig, ax = plt.subplots(2, 2, figsize=(6, 6))

# Rangos de temperatura para fijar la escala de color
vmin = np.min(tensor_temperaturaa)
vmax = np.max(tensor_temperaturaa)

# Preparamos el objeto de la imagen vacío o con ceros
ax[0,0].imshow(
    tensor_temperaturaa[0,:,:], 
    cmap='hot', 
    vmin=vmin, 
    vmax=vmax, 
    origin='lower', 

)
ax[0,1].imshow(
    tensor_temperaturaa[500,:,:], 
    cmap='hot', 
    vmin=vmin, 
    vmax=vmax, 
    origin='lower', 

)
ax[1,0].imshow(
    tensor_temperaturaa[5000,:,:], 
    cmap='hot', 
    vmin=vmin, 
    vmax=55, 
    origin='lower', 
)
ax[1,1].imshow(
    tensor_temperaturaa[10000,:,:], 
    cmap='hot', 
    vmin=vmin, 
    vmax=55, 
    origin='lower', 
)
plt.savefig("Difusion_Ab.png")
