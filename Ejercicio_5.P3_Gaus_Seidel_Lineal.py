# -*- coding: utf-8 -*-
"""
Created on Sat Dec 13 00:38:25 2025

@author: rocio
"""
#5. Construye un programa que resuelva un sistema de ecuaciones de dimensi´on arbitraria,
#empleando el m´etodo de Gauss-Seidel simple (no en forma matricial). El programa deber´a
#admitir como variables de entrada, una matriz de coeficientes A, (n × n), un vector de
#t´erminos independientes b, (n×1), una soluci´on inicial x0, (n×1), un valor para la tolerancia
#m´axima entre dos iteraciones sucesivas y un n´umero m´aximo de iteraciones permitido. El
#programa deber´a devolver un vector columna con las soluciones del sistema, el n´umero de
#iteraciones empleado y el error relativo entre las dos ´ultimas iteraciones realizadas.
import numpy as np

def gauss_seidel_lineal(A, b, x0, tol, itmax):
    [nf, nc] = np.shape(A)
    
    xs1 = np.array(x0, dtype=float)  # solución inicial
    it = 0
    error = tol + 1  # para entrar al bucle

    while it < itmax:
        xs = xs1.copy()
        
        for i in range(nf):
            suma = 0.0
            
            # términos j < i → valores ya actualizados
            for j in range(i):
                suma += A[i, j] * xs1[j]
            
            # términos j > i → valores de la iteración anterior
            for j in range(i + 1, nf):
                suma += A[i, j] * xs[j]
            
            xs1[i] = (b[i] - suma) / A[i, i]
        
        # error relativo
        error = np.linalg.norm(xs1 - xs) / np.linalg.norm(xs1)
        it += 1
        
        if error < tol:
            break

    return xs1, it, float(error)
A = np.array([[4, 2, -1],
              [3, -5, 1],
              [1, -1, 6]], dtype=float)
b = np.array([[5], [-4], [17]], dtype=float)
x0 = np.array([[0], [0], [0]], dtype=float)

sol= gauss_seidel_lineal(A, b, x0, 1e-6, 50)
print(sol)

