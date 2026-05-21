import numpy as np
import matplotlib.pyplot as plt

x = np.array([4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5])
f = np.array([2.2, 3.5, 4.0, 6.0, 6.5, 7.3, 8.2, 8.7])
m = len(x)

print("Grado | Norma residuos | ECM")
print("-----------------------------")

for grado in range(1, 6):
    coef = np.polyfit(x, f, grado)
    P = np.poly1d(coef)
    
    residuos = f - P(x)
    NR = np.sqrt(np.sum(residuos**2))
    ECM = NR / np.sqrt(m)
    
    print(f"{grado:5d} | {NR:14.6f} | {ECM:.6f}")


x_plot = np.linspace(3, 8, 400)

plt.plot(x, f, 'o', label='Datos')

for grado in [2, 3, 4]:
    coef = np.polyfit(x, f, grado)
    P = np.poly1d(coef)
    plt.plot(x_plot, P(x_plot), label=f'Grado {grado}')

plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid()
plt.show()


"""Al aumentar el grado del polinomio, el ajuste mejora dentro de los puntos,
pero el polinomio de grado máximo tiende a oscilar entre ellos.
Esto indica sobreajuste y peor comportamiento fuera del intervalo de datos.
"""