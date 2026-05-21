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
print("="*70)
print("INTEGRACIÓN DE ECUACIÓN DIFERENCIAL - TEMPERATURA DE CASA")
print("="*70)

k = 10.0          # Kcal / (h·°C)
C = 200.0         # Kcal / °C
Fi = 20.0         # Kcal / h
To = 10.0         # °C
T0 = 30.0         # °C

dt = 0.2          # horas
t_max = 100.0     # horas

print("\n--- PARÁMETROS DEL SISTEMA ---")
print(f"Coeficiente de intercambio térmico (k): {k} Kcal/(h·°C)")
print(f"Capacidad calorífica de la casa (C): {C} Kcal/°C")
print(f"Flujo de calor interno (Fi): {Fi} Kcal/h")
print(f"Temperatura exterior (To): {To} °C")
print(f"Temperatura inicial (T0): {T0} °C")

print("\n--- PARÁMETROS DE SIMULACIÓN ---")
print(f"Paso de tiempo (dt): {dt} horas")
print(f"Tiempo total de simulación: {t_max} horas")
print(f"Número de pasos: {int(t_max / dt)}")

# ---------------------------------------------------------
# Simulación
# ---------------------------------------------------------
print("\n" + "="*70)
print("APARTADO b) SIMULACIÓN CON MÉTODO DE EULER")
print("="*70)

t, T = euler(T0, C, k, Fi, To, dt, t_max)

# ---------------------------------------------------------
# Impresión de resultados numéricos
# ---------------------------------------------------------
print("\n--- RESULTADOS DE LA SIMULACIÓN ---\n")

# Temperatura de equilibrio teórica
T_equilibrio = (Fi + k * To) / k
print(f"Temperatura de equilibrio teórica: {T_equilibrio:.2f} °C")
print(f"Temperatura final alcanzada: {T[-1]:.2f} °C")
print(f"Diferencia: {abs(T[-1] - T_equilibrio):.4f} °C\n")

# Tabla de valores en tiempos específicos
print("Tabla de valores de temperatura en diferentes tiempos:")
print("-" * 50)
print(f"{'Tiempo (h)':>12} | {'Temperatura (°C)':>18}")
print("-" * 50)

# Mostrar valores cada 10 horas
indices = [0]  # Tiempo inicial
for tiempo in range(10, int(t_max) + 1, 10):
    idx = int(tiempo / dt)
    if idx < len(t):
        indices.append(idx)

for idx in indices:
    print(f"{t[idx]:>12.1f} | {T[idx]:>18.4f}")

print("-" * 50)

# Estadísticas adicionales
print(f"\nTemperatura máxima: {np.max(T):.4f} °C en t = {t[np.argmax(T)]:.1f} h")
print(f"Temperatura mínima: {np.min(T):.4f} °C en t = {t[np.argmin(T)]:.1f} h")

# Tasa de cambio inicial
tasa_inicial = Tdot(T0, C, k, Fi, To)
print(f"\nTasa de cambio inicial (dT/dt): {tasa_inicial:.4f} °C/h")

# ---------------------------------------------------------
# Gráfica de resultados (Apartado c)
# ---------------------------------------------------------
print("\n" + "="*70)
print("APARTADO c) REPRESENTACIÓN GRÁFICA")
print("="*70)
print("\nGenerando gráfica...\n")

plt.figure(figsize=(10, 6))
plt.plot(t, T, 'b-', linewidth=2, label='Temperatura interior')
plt.axhline(y=T_equilibrio, color='r', linestyle='--', linewidth=1.5, 
            label=f'Temperatura de equilibrio ({T_equilibrio:.2f}°C)')
plt.axhline(y=To, color='g', linestyle='-.', linewidth=1.5, 
            label=f'Temperatura exterior ({To:.2f}°C)')
plt.xlabel("Tiempo (horas)", fontsize=12)
plt.ylabel("Temperatura interior (°C)", fontsize=12)
plt.title("Evolución de la temperatura de la casa (Método de Euler)", fontsize=14)
plt.grid(True, alpha=0.3)
plt.legend(loc='best')
plt.tight_layout()
plt.show()

print("Simulación completada.")