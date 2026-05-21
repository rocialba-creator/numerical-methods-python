# -*- coding: utf-8 -*-
"""
Created on Sun Dec  7 11:16:01 2025

@author: rocio
"""
import numpy as np
def f(x):
    return np.exp(x)-x**2
def inter_lineal(f,a,b,tol,max_iter):
    i=1
    contador=0
    valor_c=[]
    if f(a)*f(b)<0:
        while i<=max_iter:
            c=b-(f(b)/(f(b)-f(a)))*(b-a)
            fc=f(c)
            contador=i
            valor_c.append(c)
            
            if abs(fc)<tol:
                break
            if f(a)*f(c)<0:
                b=c
            else:
                a=c
            i=i+1
        error=abs(valor_c[-1]-valor_c[-2])
        return float(c), contador, float(valor_c[-1]-valor_c[-2]), error
    else:
        print("El intervalo no es válido")
        return None,0

    
raiz_1=inter_lineal(f,-2,2,1e-6,50)
print(raiz_1)
raiz_2=inter_lineal(f,2,3,1e-6,50)
print(raiz_2)

    
