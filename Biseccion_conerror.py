# -*- coding: utf-8 -*-
"""
Created on Sun Dec  7 10:38:43 2025

@author: rocio
"""
import numpy as np
def f(x):
    return np.exp(x)-x**2
def biseccion(f,a,b,tol,max_iter):
    if f(a)*f(b)<0:
        i=1
        contador=0
        errores=[]
        while i<=max_iter:
            c=(a+b)/2
            fc=f(c)
            contador=i
            error=(b-a)/2
            errores.append(error)
            if abs(fc)<tol:
                break
            if f(a)*f(c)<0:
                b=c
            else:
                a=c
            i=i+1
        return c, contador, error, errores
    else:
        print("El intervalo no es correto")
        return None, 0 
raiz_1=biseccion(f,-2,2,1e-6,50)
print(raiz_1)
raiz_2=biseccion(f,2,3,1e-6,50)
print(raiz_2)

 
