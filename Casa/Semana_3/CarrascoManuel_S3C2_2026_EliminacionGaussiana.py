import numpy as np
N=np.random.randint(3, 7)
M=(np.random.random((N,N))*10.0)-5.0
B=(np.random.random((N,))*10.0)-5.0
#compare sus resultados con el paquete de numpy:
#https://numpy.org/doc/stable/reference/generated/numpy.linalg.solve.html
sol=np.linalg.solve(M,B)
print(f"La matiz es {M}")
print(f"El tamaño es {N}")
print(f"La solucion por numpy es {sol}")   
for i in range (N):
    B[i]=B[i]/M[i,i]
    M[i,:]=M[i,:]/M[i,i]
    for j in range (i+1, N):
        B[j]-=B[i]*M[j,i]
        M[j,:]-=M[i,:]*M[j,i]
#print(M)
X = np.zeros(N)
#Lo que esta aca abajo es lo hecho en clase que esta mal porque solo funciona para 4x4 
#X[N-1]=B[N-1]
#X[N-2]=(B[N-2]-M[N-2,N-1]*X[N-1])
#X[N-3]=(B[N-3]-M[N-3,N-2]*X[N-2]-M[N-3,N-1]*X[N-1])
#X[N-4]=(B[N-4]-M[N-4,N-2]*X[N-2]-M[N-4,N-1]*X[N-1]-M[N-4,N-3]*X[N-3])
#for i in range (1,N+1):
#    X[N-i]=(B[N-i]-M[N-i,N-2]*X[N-2]-M[N-i,N-1]*X[N-1]-M[N-i,N-3]*X[N-3])
#------------------------------------------------------------------------------
for i in range (N):
    X[N-1-i]= (B[N-1-i]-np.sum(X[N-i:N]*M[N-1-i, N-i:N])) # /M[N-1-i, N-1-i] todos los elementos de la diagonal son 1 
print(f"La solución por eliminacion es {X}")
 