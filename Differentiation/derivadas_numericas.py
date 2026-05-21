# -*- coding: utf-8 -*-
"""
Created on Fri Dec 12 22:55:52 2025
#PRÁCTICA 5. DIFERENCIACIÓN E INTEGRACIÓN NUMÉRICAS.
@author: rocio
"""
#1. Crea una funci´on en Python que tome como variables de entrada otra funci´on f, un valor
#x0, un intervalo h y una ´ultima variable metodo que contenga el nombre de un m´etodo,
#y devuelva el valor de la derivada de f calculada en el punto x0, empleando el m´etodo
#indicado en la variable metodo. Los m´etodos pueden ser:
#- metodo = ’2ad’: diferencia de dos puntos adelantada
#- metodo = ’2ce’: diferencia de dos puntos centrada
#- metodo = ’3ad’: diferencia de tres puntos adelantada
#Emplea la funci´on que acabas de crear para obtener la derivada de la funci´on f(x) = 1/x
#en el punto x0 = 1. Prueba para valores de h 0.1, 0.5, 1.5. Explica los resultados.
import numpy as np


def derivada(f, x0, h, metodo):
    """
    Derivada numérica de f en x0.
    Métodos permitidos:
        - '2ad' : diferencia adelantada (2 puntos)
        - '2ce' : diferencia centrada   (2 puntos)
        - '3ad' : diferencia adelantada (3 puntos)
    """
    if metodo == "2ad":
        return (f(x0 + h) - f(x0)) / h

    elif metodo == "2ce":
        return (f(x0 + h) - f(x0 - h)) / (2 * h)

    elif metodo == "3ad":
        return (-3*f(x0) + 4*f(x0 + h) - f(x0 + 2*h)) / (2 * h)

    else:
        raise ValueError("Método no reconocido.")


def derivar_tabla(x, y):
    """
    Calcula dy/dx usando datos tabulados mediante:
      - diferencia adelantada   en el primer punto
      - diferencia centrada     en los puntos interiores
      - diferencia atrasada     en el último punto

    Implementado usando NumPy para mayor precisión.
    """
    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)

    dydx = np.zeros_like(y)

    # primer punto → diferencia adelantada
    dydx[0] = (y[1] - y[0]) / (x[1] - x[0])

    # puntos interiores → diferencia centrada
    dydx[1:-1] = (y[2:] - y[:-2]) / (x[2:] - x[:-2])

    # último punto → diferencia atrasada
    dydx[-1] = (y[-1] - y[-2]) / (x[-1] - x[-2])

    return dydx


# -------------------------------------------------------
# PRUEBA 1 → derivada de f(x)=1/x en x0=1 con varios h
# -------------------------------------------------------

def f(x):
    return 1/x

x0 = 1
hs = [0.1, 0.5, 1.5]
metodos = ["2ad", "2ce", "3ad"]

print("Derivada exacta f'(1) = -1\n")

for h in hs:
    print(f"=== h = {h} ===")
    for m in metodos:
        print(f"  Método {m}: {derivada(f, x0, h, m)}")
    print()


# -------------------------------------------------------
# PRUEBA 2 → derivada de la tabla de datos
# -------------------------------------------------------

x = [0.952, 1.015, 1.079, 1.142, 1.206, 1.269, 1.333, 1.396, 1.460, 1.523]
y = [-0.832, -0.866, -0.896, -0.922, -0.9458, -0.964, -0.978, -0.989, -0.997, -1]

dydx = derivar_tabla(x, y)

print("\nDerivada aproximada de los datos tabulados:\n")
print("x\t\tdy/dx")
for xi, di in zip(x, dydx):
    print(f"{xi:.3f}\t{di:.6f}")
