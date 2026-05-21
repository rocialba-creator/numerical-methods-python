import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# Cargar datos desde el archivo datos.txt
# Columnas:
# 1ª columna -> x
# 2ª columna -> y1
# 3ª columna -> y2
# ============================================================

datos = np.loadtxt("datos.txt")

x = datos[:, 0]
y1 = datos[:, 1]
y2 = datos[:, 2]

# ============================================================
# APARTADO a)
# Representación y = f(x) (segunda columna frente a la primera)
# Ajuste lineal y polinómico grados 2, 3 y 4
# ============================================================

plt.figure()
plt.plot(x, y1, '.', label='Datos experimentales')

# Ajustes
grados = [1, 2, 3, 4]
x_plot = np.linspace(x.min(), x.max(), 500)

for g in grados:
    coef = np.polyfit(x, y1, g)
    P = np.poly1d(coef)
    plt.plot(x_plot, P(x_plot), label=f'Ajuste grado {g}')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Ajustes sobre la segunda columna')
plt.legend()
plt.grid()
plt.show()

# ============================================================
# APARTADO b)
# Repetir el proceso con la tercera columna
# ============================================================

plt.figure()
plt.plot(x, y2, '.', label='Datos experimentales')

for g in grados:
    coef = np.polyfit(x, y2, g)
    P = np.poly1d(coef)
    plt.plot(x_plot, P(x_plot), label=f'Ajuste grado {g}')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Ajustes sobre la tercera columna')
plt.legend()
plt.grid()
plt.show()

# ============================================================
# COMENTARIO FINAL (teórico)
# ============================================================

"""
El mejor ajuste es aquel que sigue la tendencia general de los datos
sin introducir oscilaciones artificiales.
Normalmente los polinomios de grado 2 o 3 ofrecen un buen compromiso.
Los de grado alto pueden provocar sobreajuste.
"""
