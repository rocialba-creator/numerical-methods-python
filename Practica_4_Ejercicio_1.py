import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d, CubicSpline
from numpy.polynomial import Polynomial

# Datos
x = np.array([0.5, 1.0, 2.0, 3.0, 4.0])
T = np.array([8.8, 7.2, 6.0, 4.2, 2.8])

# a) Representación de los datos
plt.plot(x, T, 'o', label='Datos experimentales')
plt.xlabel('x (m)')
plt.ylabel('T (ºC)')
plt.grid()

# b) Polinomio interpolador P4(x) usando Vandermonde
V = np.vander(x, 5)
coef = np.linalg.solve(V, T)
P4 = np.poly1d(coef)

# c) Estimación en x = 1.5 y 2.5 m
x_int = np.array([1.5, 2.5])
T_int = P4(x_int)

print("Interpolación con P4(x):")
print("T(1.5 m) =", T_int[0])
print("T(2.5 m) =", T_int[1])

# d) Superposición del polinomio y puntos interpolados
x_plot = np.linspace(0, 4.5, 300)
plt.plot(x_plot, P4(x_plot), 'b', label='P4(x)')
plt.plot(x_int, T_int, 'g*', markersize=12, label='Interpolados')
plt.legend()
plt.show()

# e) Comprobación con interp1d y CubicSpline
f_linear = interp1d(x, T, kind='linear')
f_cubic = CubicSpline(x, T)

print("\ninterp1d:")
print("T(1.5 m) =", f_linear(1.5))
print("T(2.5 m) =", f_linear(2.5))

print("\nCubicSpline:")
print("T(1.5 m) =", f_cubic(1.5))
print("T(2.5 m) =", f_cubic(2.5))

# f) Ajuste por mínimos cuadrados (Polynomial.fit)
P_fit = Polynomial.fit(x, T, deg=4)

print("\nAjuste por mínimos cuadrados:")
print("T(1.5 m) =", P_fit(1.5))
print("T(2.5 m) =", P_fit(2.5))
