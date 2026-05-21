# -*- coding: utf-8 -*-
"""
Created on Mon Dec  8 07:44:05 2025

@author: rocio
"""

import numpy as np
def g(x):
    return -np.exp(x)**0.5
def pto_fijo(g,x0,tol,max_iter):
    i=1
    contador=0 
    errores=[]
    while i<max_iter:
        x=g(x0)
        contador=i
        error=abs(g(x)-x)
        errores.append(error)
        if abs(x-x0)<tol:
            break
        else:
            x0=x
        i=i+1
    return float(x), contador, float(error) 
print(pto_fijo(g,-0.6,0.01,100))

