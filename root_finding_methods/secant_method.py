# -*- coding: utf-8 -*-
"""
Created on Sun Dec  7 14:06:40 2025

@author: rocio
"""

import numpy as np
def f(x):
    return np.exp(x)-x**2
def metodo_secante(f,x1,x2,tol,max_iter):
    i=1
    contador=0
    valor_c=[]
    while i<max_iter:
        x3=x2-(f(x2)*(x2-x1))/(f(x2)-f(x1))
        f3=f(x3)
        contador=i
        valor_c.extend([x2,x3])
        if abs(f3)<tol:
            break
        else:
             x1=x2 
             x2=x3
        i=i+1
    error=abs(valor_c[-1]-valor_c[-2])
    return float(x3), contador, float(error)
raiz_1=metodo_secante(f,-2.5,0.5,1e-6,20)
print(raiz_1)
raiz_2=metodo_secante(f,-2.5,0.5,0.01,20)
print(raiz_2)
    
