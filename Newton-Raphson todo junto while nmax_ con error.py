# -*- coding: utf-8 -*-
"""
Created on Sun Dec  7 13:36:36 2025

@author: rocio
"""


import numpy as np


def f(x):
    return 0.5*x**2-4*x*np.sin(x)+2*(np.sin(x))**2+1.5
def df(x):
    return x-4*np.sin(x)-4*x*np.cos(x)+2*np.sin(2*x)
def newton_raphson(f,x,tol,max_iter):
    i=1
    contador=0
    valor_c=[]
    while i<max_iter:
        c=x-f(x)/df(x)
        fc=f(c)
        contador=i
        valor_c.append(c)
        if abs(fc)<tol:
            break
        else:
            x=c
        i=i+1
    error=abs(valor_c[-1]-valor_c[-2])
    return float(c), contador, float(error)
tol=1e-4
max_iter=100
raices=newton_raphson(f,1,tol,max_iter)
print('La raiz es: ' , np.round(raices,4))

