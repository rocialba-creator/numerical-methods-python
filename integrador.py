#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 30 20:07:01 2025

@author: mariaguijarro

6 """
import numpy as np 
 
from matplotlib import pyplot as pl

def integra(fun, met, inter, dib=False):
    """
    fun  -> función que queremos integrar
    met  -> método ('trap', 'simpson' o 'simpson38')
    inter -> intervalo de integración [a, b]
    dib -> si True, dibuja la aproximación polinómica usada
    """

    # ============================
    # MÉTODO DEL TRAPECIO
    # ============================
    if met == 'trap':
        f0 = fun(inter[0])      # Valor de la función en el extremo a
        f1 = fun(inter[1])      # Valor de la función en el extremo b
        h = inter[1] - inter[0] # Longitud del intervalo

        # Fórmula del trapecio: área del trapecio entre a y b
        intg = h * (f0 + f1) / 2

        if dib:
            # Dibujamos la función original y el trapecio
            x = np.linspace(inter[0], inter[1], 100)   # Puntos para la curva real
            y = np.array([fun(i) for i in x])          # Valores reales de f

            # Recta que une los puntos (polinomio de grado 1)
            ypol = f0 + (x - inter[0]) * (f1 - f0) / h

            # Rellenamos el área del trapecio
            pl.fill_between(x, ypol,
                            where=(inter[0] <= x) & (x <= inter[1]))

            pl.plot(x, y, 'b')  # Dibujamos la función real en azul

    # ============================
    # MÉTODO DE SIMPSON 1/3
    # ============================
    elif met == 'simpson':
        pmedio = (inter[1] + inter[0]) / 2  # Punto medio del intervalo

        # Valores de la función en los tres puntos: a, (a+b)/2, b
        f0 = fun(inter[0])
        f1 = fun(pmedio)
        f2 = fun(inter[1])

        h = (inter[1] - inter[0]) / 2       # Tamaño de subintervalos

        # Fórmula de Simpson 1/3
        intg = h * (f0 + 4*f1 + f2) / 3

        if dib:
            x = np.linspace(inter[0], inter[1], 100)  # Puntos para la curva real
            y = np.array([fun(i) for i in x])

            # Polinomio cuadrático que interpola f0, f1, f2
            ypol = f0 \
                   + (x - inter[0]) * (f1 - f0) / h \
                   + (x - inter[0]) * (x - pmedio) * (f2 - 2*f1 + f0) / (2 * h**2)

            # Rellenamos el área bajo la parábola
            pl.fill_between(x, ypol,
                            where=(inter[0] <= x) & (x <= inter[1]))
            pl.plot(x, ypol, 'k')  # Parábola en negro
            pl.plot(x, y, 'b')     # Función real en azul

    # ============================
    # MÉTODO DE SIMPSON 3/8
    # ============================
    elif met == 'simpson38':
        # Dividimos el intervalo en 4 puntos igualmente espaciados
        inter = np.linspace(inter[0], inter[1], 4)

        # Evaluamos la función en esos 4 puntos
        f = np.array([fun(i) for i in inter])

        h = inter[1] - inter[0]  # Distancia entre puntos

        # Fórmula de Simpson 3/8
        intg = 3 * h * (f[0] + 3*f[1] + 3*f[2] + f[3]) / 8

        if dib:
            x = np.linspace(inter[0], inter[3], 100)   # Puntos para representar
            y = np.array([fun(i) for i in x])

            # Polinomio cúbico que interpola los 4 puntos
            ypol = f[0] \
                   + (x - inter[0]) * (f[1] - f[0]) / h \
                   + (x - inter[0]) * (x - inter[1]) * (f[2] - 2*f[1] + f[0]) / (2 * h**2) \
                   + (x - inter[0]) * (x - inter[1]) * (x - inter[2]) \
                        * (f[3] - 3*f[2] + 3*f[1] - f[0]) / (6 * h**3)

            pl.fill_between(x, ypol,
                            where=(inter[0] <= x) & (x <= inter[3]))
            pl.plot(x, ypol, 'k')  # Dibujamos el cúbico en negro
            pl.plot(x, y, 'b')     # Función real en azul

    return intg  # Devolvemos la aproximación de la integral
sol1=integra(np.sin, 'trap', [0,np.pi], dib=True)
print(np.round(sol1),3)
sol2=integra(np.sin, 'simpson', [0,np.pi], dib=True)
print(np.round(sol2),3)
sol3=integra(np.sin, 'simpson38', [0,np.pi], dib=True)
print(np.round(sol3),3)