# file: casa_temperatura.py

import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# Definición de la ecuación diferencial de la temperatura
# ---------------------------------------------------------
def Tdot(T: float, C: float, k: float, Fi: float, To: float) -> float:
    """
    Calcula la derivada de la temperatura interior de la casa
    según el balance energético.
    
    Parámetros:
    - T : Temperatura interior actual (°C)
    - C : Capacidad calorífica de la casa (Kcal/°C)
    - k : Coeficiente de intercambio térmico (Kcal/(h·°C))
    - Fi: Flujo de calor interno (Kcal/h)
    - To: Temperatura exterior (°C)
    """
    return (Fi - k * T + k * To) / C


# ---------------------------------------------------------
# Método de Euler explícito para integrar la ecuación
# ---------------------------------------------------------
def euler(T0: float, C: float, k: float, Fi: float, To: float,
          dt: float, t_max: float):
    """
    Integra la ecuación diferencial usando el método de Euler.
    
    Parámetros:
    - T0    : Temperatura inicial (°C)
    - C, k  : Parámetros físicos del sistema
    - Fi, To: Flujo interno y temperatura exterior
    - dt    : Paso de integración (horas)
    - t_max : Tiempo total de simulación (horas)
    
    Devuelve:
    - t : vector de tiempos
    - T : vector de temperaturas interiores
    """
    n_steps = int(t_max / dt)               # número de pasos
    t = np.linspace(0, t_max, n_steps + 1)  # vector de tiempos
    T = np.zeros(n_steps + 1)               # vector de temperaturas

    T[0] = T0  # condición inicial

    # Iteración con el método de Euler
    for i in range(n_steps):
        T[i + 1] = T[i] + dt * Tdot(T[i], C, k, Fi, To)

    return t, T


# ---------------------------------------------------------
# Parámetros del problema (se ejecutan directamente)
# ---------------------------------------------------------
k = 10.0          # Kcal / (h·°C)
C = 200.0         # Kcal / °C
Fi = 20.0         # Kcal / h
To = 10.0         # °C
T0 = 30.0         # °C

dt = 0.2          # horas
t_max = 100.0     # horas

# ---------------------------------------------------------
# Simulación
# ---------------------------------------------------------
t, T = euler(T0, C, k, Fi, To, dt, t_max)

# ---------------------------------------------------------
# Gráfica de resultados
# ---------------------------------------------------------
plt.figure()
plt.plot(t, T)
plt.xlabel("Tiempo (horas)")
plt.ylabel("Temperatura interior (°C)")
plt.title("Evolución de la temperatura de la casa")
plt.grid(True)
plt.show()