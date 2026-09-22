import numpy as np
import matplotlib.pyplot as plt
# Función a integrar
def funcion(x1):
    	return np.cos(x1)

M=9999
a=0
b=3*np.pi/2
x = np.linspace(a, b, M, dtype = float)
def integral(x):
    return np.sum(x)

z=100
nmr=np.arange(2, z+2)
errorr = np.zeros(z)
for m in range (2, z+2):
      h=(b-a)/(m-1)
      xr = np.linspace(a, b, m, dtype = float)
      fxr = funcion(xr)
      rec = h*fxr
      errorr[m-2]= (np.abs(integral(rec) - (-1)))
plt.plot(nmr, errorr)    
plt.xlabel("Numero de divisiones")
plt.ylabel("Error absoluto")
plt.title("Error para metodo de rectángulos")
#plt.savefig("ErrorRectangulos2.pdf", format="pdf", bbox_inches="tight")      
#plt.show()

nmt=np.arange(2, z+2)
errort = np.zeros(z)
for m in range (2, z+2):
      h=(b-a)/(m-1)
      xt = np.linspace(a, b, m, dtype = float)
      fxt = funcion(xt)
      rec = h*fxt
      area= integral(rec)-(h/2)*funcion(x[0])-(h/2)*funcion(x[M-1])
      errort[m-2]= np.abs(area - (-1))
plt.plot(nmt, errort)    
plt.xlabel("Numero de divisiones")
plt.ylabel("Error absoluto")
plt.title("Error para metodo de trapecios")
#plt.savefig("ErrorTrapecios2.pdf", format="pdf", bbox_inches="tight")        
#plt.show()
nms=np.arange(2, z+2)
errors = np.zeros(z)
print(np.shape(nms))
print(np.shape(errors))
for m in range (2, (2*z)+2, 2):
      ws=np.zeros(m)
      h=(b-a)/(m-1)
      ws[0]=h/3
      ws[-1]=h/3
      ws[1:-2:2]=4*h/3
      ws[2:-3:2]=2*h/3
      xs = np.linspace(a, b, m, dtype = float)
      fxs = funcion(xs)
      sim=ws*fxs
      i=int((m/2)-1)
      errors[i]= np.abs(integral(sim) - (-1))
plt.plot(nms, errors)  
plt.xlabel("Numero de divisiones")
plt.ylabel("Error absoluto")
plt.title("Error para metodo de Simpson")
plt.legend(["Rectangulos", "Trapecios", "Simpson"])
#plt.savefig("ErrorSimpson2.pdf", format="pdf", bbox_inches="tight") 
#plt.show
plt.savefig("ErrorTodosLosMetodos.pdf", format="pdf")   
plt.show()