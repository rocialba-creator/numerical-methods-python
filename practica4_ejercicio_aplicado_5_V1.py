import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d, CubicSpline

# ============================================================
# EJERCICIO 5: Enfriamiento de un cuerpo
# ============================================================

# Cargar datos
data = np.load('relajaT.npz')
t = data['t']
T = data['T']
Ta = data['Ta']

# ============================================================
# APARTADO a) Ajuste con polinomio de orden 4
# ============================================================

coef4 = np.polyfit(t, T, 4)
P4 = np.poly1d(coef4)

plt.figure()
plt.plot(t, T, 'o', label='Datos experimentales', alpha=0.6)
t_plot = np.linspace(t.min(), t.max(), 500)
plt.plot(t_plot, P4(t_plot), 'b-', label='Ajuste grado 4')
plt.xlabel('Tiempo (h)')
plt.ylabel('Temperatura (ºC)')
plt.title('Ajuste polinómico grado 4')
plt.legend()
plt.grid()
plt.show()

# ============================================================
# APARTADO b) Interpolación por Vandermonde (todos los puntos)
# ============================================================

n = len(t)
V = np.vander(t, n)
coef_interp = np.linalg.solve(V, T)
P_interp = np.poly1d(coef_interp)

plt.figure()
plt.plot(t, T, 'o', label='Datos experimentales', alpha=0.6)
plt.plot(t_plot, P_interp(t_plot), 'r-', label=f'Interpolación (grado {n-1})')
plt.xlabel('Tiempo (h)')
plt.ylabel('Temperatura (ºC)')
plt.title('Interpolación por todos los puntos')
plt.legend()
plt.grid()
plt.show()

print("\nResultado inesperado: El polinomio oscila bruscamente (fenómeno de Runge)")
print("Con muchos puntos, la interpolación de alto grado no es adecuada.\n")

# ============================================================
# APARTADO c) Interpolación con 5 puntos específicos
# ============================================================

t_sel = [0, 10, 30, 60, 100]
indices = [np.argmin(np.abs(t - tv)) for tv in t_sel]
tp = t[indices]
Tp = T[indices]

V5 = np.vander(tp, 5)
coef5 = np.linalg.solve(V5, Tp)
P5 = np.poly1d(coef5)

plt.figure()
plt.plot(t, T, 'o', label='Datos experimentales', alpha=0.6)
plt.plot(t_plot, P4(t_plot), 'b-', label='Ajuste grado 4')
plt.plot(t_plot, P5(t_plot), 'g-', label='Interpolación 5 puntos')
plt.plot(tp, Tp, 'r*', markersize=12, label='Puntos seleccionados')
plt.xlabel('Tiempo (h)')
plt.ylabel('Temperatura (ºC)')
plt.title('Interpolación con 5 puntos')
plt.legend()
plt.grid()
plt.show()

print("El polinomio de 5 puntos NO sirve para interpolar en todo [0,100].\n")

# ============================================================
# APARTADO d) Interpolación con resolución 0.1 h
# ============================================================

t_hr = np.arange(t.min(), t.max(), 0.1)

f_nearest = interp1d(t, T, kind='nearest')
f_linear = interp1d(t, T, kind='linear')
f_cubic = CubicSpline(t, T)

T_nearest = f_nearest(t_hr)
T_linear = f_linear(t_hr)
T_cubic = f_cubic(t_hr)

plt.figure(figsize=(14, 8))

# Gráfica completa
plt.subplot(2, 2, 1)
plt.plot(t, T, 'o', markersize=3, alpha=0.5)
plt.plot(t_hr, T_nearest, '-', label='Orden cero')
plt.plot(t_hr, T_linear, '-', label='Lineal')
plt.plot(t_hr, T_cubic, '-', label='Splines cúbicos')
plt.xlabel('Tiempo (h)')
plt.ylabel('Temperatura (ºC)')
plt.title('Interpolación resolución 0.1 h')
plt.legend()
plt.grid()

# Zoom 1
plt.subplot(2, 2, 2)
mask = (t_hr >= 20) & (t_hr <= 30)
mask_d = (t >= 20) & (t <= 30)
plt.plot(t[mask_d], T[mask_d], 'o', markersize=5)
plt.plot(t_hr[mask], T_nearest[mask], '-', label='Orden cero')
plt.plot(t_hr[mask], T_linear[mask], '-', label='Lineal')
plt.plot(t_hr[mask], T_cubic[mask], '-', label='Splines cúbicos')
plt.xlabel('Tiempo (h)')
plt.ylabel('Temperatura (ºC)')
plt.title('Zoom: [20, 30] h')
plt.legend()
plt.grid()

# Zoom 2
plt.subplot(2, 2, 3)
mask = (t_hr >= 60) & (t_hr <= 70)
mask_d = (t >= 60) & (t <= 70)
plt.plot(t[mask_d], T[mask_d], 'o', markersize=5)
plt.plot(t_hr[mask], T_nearest[mask], '-', label='Orden cero')
plt.plot(t_hr[mask], T_linear[mask], '-', label='Lineal')
plt.plot(t_hr[mask], T_cubic[mask], '-', label='Splines cúbicos')
plt.xlabel('Tiempo (h)')
plt.ylabel('Temperatura (ºC)')
plt.title('Zoom: [60, 70] h')
plt.legend()
plt.grid()

# Zoom 3
plt.subplot(2, 2, 4)
mask = (t_hr >= 85) & (t_hr <= 95)
mask_d = (t >= 85) & (t <= 95)
plt.plot(t[mask_d], T[mask_d], 'o', markersize=5)
plt.plot(t_hr[mask], T_nearest[mask], '-', label='Orden cero')
plt.plot(t_hr[mask], T_linear[mask], '-', label='Lineal')
plt.plot(t_hr[mask], T_cubic[mask], '-', label='Splines cúbicos')
plt.xlabel('Tiempo (h)')
plt.ylabel('Temperatura (ºC)')
plt.title('Zoom: [85, 95] h')
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()

# ============================================================
# APARTADO e) Extrapolación t=[101, 120] h
# ============================================================

t_ext = np.arange(0, 121, 1)

plt.figure()
plt.plot(t, T, 'o', label='Datos experimentales', alpha=0.6)
plt.plot(t_ext, P4(t_ext), 'b-', label='Ajuste grado 4')
plt.plot(t_ext, P5(t_ext), 'g-', label='Interpolación 5 puntos')
plt.axvline(x=100, color='r', linestyle='--', label='Límite datos')
plt.xlabel('Tiempo (h)')
plt.ylabel('Temperatura (ºC)')
plt.title('Extrapolación t=[101, 120] h')
plt.legend()
plt.grid()
plt.show()

print("Los modelos polinómicos NO sirven para extrapolar.\n")

# ============================================================
# APARTADO f) Transformación al espacio logarítmico
# ============================================================

T_diff = T - Ta[0]
mask_pos = T_diff > 0
t_val = t[mask_pos]
ln_T_diff = np.log(T_diff[mask_pos])

plt.figure()
plt.plot(t_val, ln_T_diff, 'o')
plt.xlabel('Tiempo (h)')
plt.ylabel('ln|T - Ta|')
plt.title('Datos en espacio logarítmico')
plt.grid()
plt.show()

print("En el espacio logarítmico hay tendencia lineal.")
print("El ruido es significativo. Acotar datos útiles.\n")

# ============================================================
# APARTADO g) Ajuste lineal en espacio transformado
# ============================================================

# Acotar datos útiles (T - Ta > 1 ºC)
umbral = 1.0
mask_util = T_diff[mask_pos] > umbral
t_util = t_val[mask_util]
ln_util = ln_T_diff[mask_util]

coef_log = np.polyfit(t_util, ln_util, 1)
P_log = np.poly1d(coef_log)

plt.figure()
plt.plot(t_val, ln_T_diff, 'o', label='Datos válidos', alpha=0.4)
plt.plot(t_util, ln_util, 'o', label='Datos útiles')
t_aj = np.linspace(t_util.min(), t_util.max(), 300)
plt.plot(t_aj, P_log(t_aj), 'r-', label='Ajuste lineal')
plt.xlabel('Tiempo (h)')
plt.ylabel('ln|T - Ta|')
plt.title('Ajuste lineal en espacio logarítmico')
plt.legend()
plt.grid()
plt.show()

# ============================================================
# APARTADO h) Cálculo de constantes k1 y k2
# ============================================================

# log(T - Ta) = log(k1) - k2·t
k2 = -coef_log[0]
k1 = np.exp(coef_log[1])

print(f"Constantes del modelo T(t) = Ta + k1·exp(-k2·t):")
print(f"k1 = {k1:.4f} ºC")
print(f"k2 = {k2:.6f} h⁻¹")
print(f"Ta = {Ta[0]:.1f} ºC\n")

# ============================================================
# APARTADO i) Modelo exponencial
# ============================================================

def modelo(t, k1, k2, Ta):
    return Ta + k1 * np.exp(-k2 * t)

t_mod = np.arange(0, 121, 1)
T_mod = modelo(t_mod, k1, k2, Ta[0])

plt.figure()
plt.plot(t, T, 'o', label='Datos experimentales', alpha=0.6)
plt.plot(t_mod, T_mod, 'r-', linewidth=2, label='Modelo exponencial')
plt.axhline(y=Ta[0], color='g', linestyle='--', label=f'Ta={Ta[0]:.1f}ºC')
plt.axvline(x=100, color='b', linestyle='--', alpha=0.5)
plt.xlabel('Tiempo (h)')
plt.ylabel('Temperatura (ºC)')
plt.title('Modelo exponencial de enfriamiento')
plt.legend()
plt.grid()
plt.xlim(0, 120)
plt.show()

# ============================================================
# APARTADO j) Desviación estándar y margen de confianza
# ============================================================

T_mod_datos = modelo(t, k1, k2, Ta[0])
sigma = np.sqrt(np.sum((T - T_mod_datos)**2) / (len(t) - 1))

print(f"Desviación estándar: σ = {sigma:.4f} ºC")
print(f"Margen de confianza: ±3σ = ±{3*sigma:.4f} ºC\n")

T_sup = T_mod + 3 * sigma
T_inf = T_mod - 3 * sigma

plt.figure()
plt.plot(t, T, 'o', label='Datos experimentales', alpha=0.6)
plt.plot(t_mod, T_mod, 'r-', linewidth=2, label='Modelo')
plt.fill_between(t_mod, T_inf, T_sup, alpha=0.2, color='red', label=f'±3σ')
plt.axhline(y=Ta[0], color='g', linestyle='--', label=f'Ta={Ta[0]:.1f}ºC')
plt.xlabel('Tiempo (h)')
plt.ylabel('Temperatura (ºC)')
plt.title('Modelo con margen de confianza')
plt.legend()
plt.grid()
plt.xlim(0, 120)
plt.show()

"""
CONCLUSIONES:
- Los ajustes polinómicos son inadecuados para este fenómeno físico.
- La interpolación de alto grado produce oscilaciones no físicas.
- El modelo exponencial T(t) = Ta + k1·exp(-k2·t) es el correcto.
- Permite extrapolar correctamente y tiene base física (ley de Newton).
"""