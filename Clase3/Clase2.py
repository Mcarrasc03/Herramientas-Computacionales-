import numpy as np 
def fun(x):
    return (x*x)
def integralr(func, i, f, n):
    area=0
    dx=(f-i)/n
    j=i
    while(j<f):
        area+= func(j)*dx
        j+=dx
    return area 
print(integralr(fun, -1, 1, 1000))
def integralt(func, i, f, n):
    area=0
    dx=(f-i)/n
    j=i
    while(j<f):
        k=j+dx
        area+= ((func(k)+func(j))/2)*dx
        j+=dx
    return area 
print(integralt(fun, -1, 1, 1000))
def integralsim(func, i, f, n):
    if (n%2 != 0):
        print("ERROR: ingresa un numero par de subintervalos")
    else:
        dx= (f-i)/(n)
        h=(f-i)/(3*n)
        area=h*func(i)+4*h*func(i+dx)+h*func(f)+h*func(f-dx)
        j=i+(2*dx)
        while (j<(f-dx)):
            area+=(2*h*func(j))
            j+=dx
    return area
print(integralsim(fun, -1, 1, 1000))
