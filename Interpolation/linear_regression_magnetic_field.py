import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# EJERCICIO 4: Cálculo de la permeabilidad magnética
# ============================================================

# Cargar datos
datos = np.loadtxt("practicaB.txt")
I = datos[:, 0]  # Intensidad (A)
B = datos[:, 1]  # Campo magnético (T)

# ============================================================
# Representación gráfica y ajuste lineal
# B = μ₀·I/(2a) → relación lineal B = m·I
# ============================================================

plt.figure()
plt.plot(I, B, 'ro', markersize=8, label='Datos experimentales')
plt.xlabel('Intensidad I (A)')
plt.ylabel('Campo magnético B (T)')
plt.title('Campo magnético vs Intensidad')
plt.grid()

# Ajuste lineal
coef = np.polyfit(I, B, 1)
P_ajuste = np.poly1d(coef)

pendiente = coef[0]  # m = μ₀/(2a)
ordenada = coef[1]   # Idealmente ≈ 0

# Superponer ajuste
I_plot = np.linspace(I.min(), I.max(), 300)
plt.plot(I_plot, P_ajuste(I_plot), 'b-', linewidth=2, label='Ajuste lineal')
plt.legend()
plt.show()

# ============================================================
# Cálculo de μ₀
# De B = μ₀·I/(2a) → μ₀ = 2a·(B/I) = 2a·pendiente
# ============================================================

# IMPORTANTE: El radio 'a' debe obtenerse de la documentación
# de la práctica 20 del Laboratorio de Física I o de las
# medidas experimentales tomadas durante la práctica.
# Introducir aquí el valor del radio de la espira en METROS.

a = 0.10  # metros (MODIFICAR con el valor de la práctica)

mu_0_exp = 2 * a * pendiente
mu_0_teo = 4 * np.pi * 1e-7  # T·m/A

error_rel = abs(mu_0_exp - mu_0_teo) / mu_0_teo * 100

print(f"Ecuación del ajuste: B = {pendiente:.6e}·I + {ordenada:.6e}")
print(f"\nRadio de la espira: a = {a:.4f} m")
print(f"μ₀ experimental: {mu_0_exp:.6e} T·m/A")
print(f"μ₀ teórico:      {mu_0_teo:.6e} T·m/A")
print(f"Error relativo:  {error_rel:.2f} %")

# ============================================================
# Análisis de residuos
# ============================================================

B_pred = P_ajuste(I)
residuos = B - B_pred
NR = np.sqrt(np.sum(residuos**2))
ECM = NR / np.sqrt(len(I))

print(f"\nNorma de residuos: {NR:.6e}")
print(f"Error cuadrático medio: {ECM:.6e}")

# Gráfica de residuos
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(I, residuos, 'go', markersize=8)
plt.axhline(y=0, color='r', linestyle='--')
plt.xlabel('Intensidad I (A)')
plt.ylabel('Residuos (T)')
plt.title('Distribución de residuos')
plt.grid()

plt.subplot(1, 2, 2)
plt.hist(residuos, bins=10, color='skyblue', edgecolor='black')
plt.xlabel('Residuos (T)')
plt.ylabel('Frecuencia')
plt.title('Histograma de residuos')
plt.grid(axis='y')

plt.tight_layout()
plt.show()

"""
CONCLUSIONES:
- El ajuste lineal es adecuado (residuos distribuidos aleatoriamente).
- La ordenada en el origen debe ser ≈ 0 (relación pasa por el origen).
- El valor de μ₀ obtenido debe compararse con el valor teórico.
- Un error relativo bajo (<5%) indica buena precisión experimental.
"""
