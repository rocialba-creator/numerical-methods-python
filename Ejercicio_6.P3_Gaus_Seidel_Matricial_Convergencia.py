# -*- coding: utf-8 -*-
"""
Created on Sat Dec 13 00:54:04 2025

@author: rocio
"""
#6. Repite el ejercicio anterior empleando ahora el m´etodo de Gauss-Seidel matricial. A˜nade el
#c´odigo necesario para que calcule en primer lugar el radio espectral de la matriz del m´etodo
#y caso de no cumplirse la condici´on de convergencia, el programa interrumpa su ejecuci´on
#y devuelva un mensaje de error indicando el valor del radio espectral.

import numpy as np

def gauss_seidel_matricial(A, b, x0, tol, itmax):
    """
    Método de Gauss-Seidel en forma matricial.
    Entradas:
      - A: matriz de coeficientes (n x n)
      - b: vector de términos independientes (n,)
      - x0: vector inicial (n,)
      - tol: tolerancia de error
      - itmax: número máximo de iteraciones
    Salidas:
      - x: vector solución aproximada
      - it: número de iteraciones realizadas
      - error: error relativo entre las dos últimas iteraciones
    """

    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float).reshape(-1)
    x = np.array(x0, dtype=float).reshape(-1)

    # Descomposición de A
    D = np.diag(np.diag(A))
    L = np.tril(A) - D
    U = np.triu(A) - D

    # Matrices del método
    invDL = np.linalg.inv(D + L)
    f = invDL @ b
    H = -invDL @ U

    # Radio espectral
    eig = np.linalg.eig(H)[0]
    radio = np.max(np.abs(eig))
    print("Radio espectral de H =", radio)

    # Comprobación de convergencia
    if radio >= 1:
        return f"ERROR: Gauss-Seidel no converge, radio espectral = {radio}"

    # Bucle iterativo
    it = 0
    error = tol + 1
    while it < itmax:
        x_new = f + H @ x                  # calcular iteración
        error = np.linalg.norm(x_new - x)  # error relativo
        x = x_new.copy()                   # actualizar solución
        it += 1
        if error < tol:                    # criterio de parada
            break

    return x, it, error

# -------- PROBAR --------
# Caso que converge
A1 = np.array([[4, 2, -1],
               [3, -5, 1],
               [1, -1, 6]], dtype=float)
b1 = np.array([5, -4, 17], dtype=float)
x0 = np.array([0, 0, 0], dtype=float)

sol, iters, err = gauss_seidel_matricial(A1, b1, x0, 1e-6, 50)
print("Solución:", np.round(sol, 6))
print("Iteraciones:", iters)
print("Error relativo:", err)

# Caso que no converge
A2 = np.array([[1, 2, 2],
               [2, 1, 2],
               [2, 2, 1]], dtype=float)
b2 = np.array([1, 1, 1], dtype=float)

print(gauss_seidel_matricial(A2, b2, x0, 1e-5, 30))
