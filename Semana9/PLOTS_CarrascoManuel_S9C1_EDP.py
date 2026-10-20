import numpy as np
import matplotlib.pyplot as plt

datos = np.genfromtxt('Temperatura_ExtremosFijos.txt', delimiter=', ', comments='#')

N_pasos = datos.shape[0] // 10
tensor_temperatura = datos.reshape((N_pasos, 10, 10))

fig, ax = plt.subplots(2, 2, figsize=(6, 6))

# Rangos de temperatura para fijar la escala de color
vmin = np.min(tensor_temperatura)
vmax = np.max(tensor_temperatura)

# Preparamos el objeto de la imagen vacío o con ceros
ax[0,0].imshow(
    tensor_temperatura[0,:,:], 
    cmap='hot', 
    vmin=vmin, 
    vmax=vmax, 
    origin='lower', 

)
ax[0,1].imshow(
    tensor_temperatura[500,:,:], 
    cmap='hot', 
    vmin=vmin, 
    vmax=vmax, 
    origin='lower', 

)
ax[1,0].imshow(
    tensor_temperatura[2000,:,:], 
    cmap='hot', 
    vmin=vmin, 
    vmax=vmax, 
    origin='lower', 
)
ax[1,1].imshow(
    tensor_temperatura[4000,:,:], 
    cmap='hot', 
    vmin=vmin, 
    vmax=vmax, 
    origin='lower', 
)
plt.savefig("Difusion.png")
