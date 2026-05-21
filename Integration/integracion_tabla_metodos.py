# -*- coding: utf-8 -*-
"""
Created on Sat Dec 13 01:18:11 2025

@author: rocio
"""
import numpy as np
from matplotlib import pyplot as pl
# ======================================================
#   2) FUNCIÓN PARA INTEGRAR TABLAS DE DATOS
# ======================================================

def integrar_tabla(y, h, metodo):
    """
    Integra datos tabulados equiespaciados usando:
      - 'trap'      : método del trapecio
      - 'simpson'   : método de Simpson 1/3
      - 'simpson38' : método de Simpson 3/8

    Corrige automáticamente:
      - Simpson 1/3 -> n divisible entre 2
      - Simpson 3/8 -> n divisible entre 3
    """
    y = np.array(y, dtype=float)
    n = len(y) - 1  # nº de intervalos

    # ---------------------------
    # Trapecio
    # ---------------------------
    if metodo == "trap":
        return h * (0.5*y[0] + np.sum(y[1:-1]) + 0.5*y[-1])

    # ---------------------------
    # Simpson 1/3
    # ---------------------------
    elif metodo == "simpson":
        if n % 2 != 0:
            I_simp = (h/3) * (y[0] + y[-2] +
                              4*np.sum(y[1:-2:2]) +
                              2*np.sum(y[2:-3:2]))
            I_trap = h * (y[-2] + y[-1]) / 2
            return I_simp + I_trap

        else:
            return (h/3) * (y[0] + y[-1] +
                            4*np.sum(y[1:-1:2]) +
                            2*np.sum(y[2:-2:2]))

    # ---------------------------
    # Simpson 3/8
    # ---------------------------
    elif metodo == "simpson38":
        if n % 3 != 0:
            resto = n % 3
            m = n - resto

            y_main = y[:m+1]

            I38 = (3*h/8)*(y_main[0] + y_main[-1] +
                           3*np.sum(y_main[1:-1:3]) +
                           3*np.sum(y_main[2:-1:3]) +
                           2*np.sum(y_main[3:-1:3]))

            y_rest = y[m:]

            if resto == 1:
                I_rest = h * (y_rest[0] + y_rest[1]) / 2

            else:  # resto == 2
                I_rest = (h/3) * (y_rest[0] + 4*y_rest[1] + y_rest[2])

            return I38 + I_rest

        else:
            return (3*h/8) * (y[0] + y[-1] +
                               3*np.sum(y[1:-1:3]) +
                               3*np.sum(y[2:-1:3]) +
                               2*np.sum(y[3:-1:3]))

    else:
        raise ValueError("Método no reconocido")



# ======================================================
#   3) EJECUCIÓN DIRECTA DEL APARTADO (c)
# ======================================================

x = [0, 0.314, 0.628, 0.942, 1.256, 1.570, 1.884, 2.199, 2.513, 2.827, 3.141]
y = [0, 0.309, 0.587, 0.809, 0.951, 1.000, 0.951, 0.809, 0.587, 0.309, 0.000]

h = x[1] - x[0]

print("\n========= INTEGRACIÓN =========\n")
print("h =", h)
print("Trapecio    =", integrar_tabla(y, h, "trap"))
print("Simpson 1/3 =", integrar_tabla(y, h, "simpson"))
print("Simpson 3/8 =", integrar_tabla(y, h, "simpson38"))

import scipy.integrate as integ
def probando(x):
    return np.sin(x)
print(integ.quad(probando,0,np.pi))


