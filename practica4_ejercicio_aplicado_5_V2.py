import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# ============================================================
# EJERCICIO 5: Enfriamiento de un cuerpo
# ============================================================

# Cargar datos desde el archivo relajaT.npz
data = np.load('relajaT.npz')
t = data['t']    # Tiempo (h)
T = data['T']    # Temperatura medida (ºC)
Ta = data['Ta']  # Temperatura ambiente (ºC)

print("=" * 70)
print("EJERCICIO 5: Enfriamiento de un cuerpo")
print("=" * 70)
print(f"Número de datos: {len(t)}")
print(f"Temperatura ambiente: {Ta[0]:.1f} ºC")
print(f"Rango de tiempo: {t.min():.1f} - {t.max():.1f} h")
print(f"Rango de temperatura: {T.min():.1f} - {T.max():.1f} ºC")

# ============================================================
# APARTADO a) Ajuste con polinomio de orden 4
# ============================================================

coef_ajuste4 = np.polyfit(t, T, 4)
P_ajuste4 = np.poly1d(coef_ajuste4)

plt.figure(figsize=(12, 6))
plt.plot(t, T, 'o', markersize=4, label='Datos experimentales', alpha=0.6)
t_plot = np.linspace(t.min(), t.max(), 500)
plt.plot(t_plot, P_ajuste4(t_plot), 'b-', linewidth=2, label='Ajuste polinómico grado 4')
plt.xlabel('Tiempo (h)', fontsize=12)
plt.ylabel('Temperatura (ºC)', fontsize=12)
plt.title('Apartado a) Ajuste con polinomio de orden 4', fontsize=14)
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# ============================================================
# APARTADO b) Polinomio de interpolación por Vandermonde
# (pasa por TODOS los puntos)
# ============================================================

n_puntos = len(t)
V = np.vander(t, n_puntos)
coef_interp = np.linalg.solve(V, T)
P_interp_todos = np.poly1d(coef_interp)

plt.figure(figsize=(12, 6))
plt.plot(t, T, 'o', markersize=4, label='Datos experimentales', alpha=0.6)
plt.plot(t_plot, P_interp_todos(t_plot), 'r-', linewidth=2, 
         label=f'Interpolación Vandermonde (todos los puntos, n={n_puntos})')
plt.xlabel('Tiempo (h)', fontsize=12)
plt.ylabel('Temperatura (ºC)', fontsize=12)
plt.title('Apartado b) Interpolación por todos los puntos', fontsize=14)
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

print("\n" + "=" * 70)
print("APARTADO b) Análisis del resultado inesperado")
print("=" * 70)
print(f"Grado del polinomio de interpolación: {n_puntos-1}")
print("El polinomio oscila bruscamente entre los puntos (fenómeno de Runge).")
print("Con muchos puntos, la interpolación de alto grado no es adecuada.")
print("=" * 70)

# ============================================================
# APARTADO c) Interpolación con 5 puntos específicos
# ============================================================

# Extraer puntos para t = 0, 10, 30, 60, 100 h
indices_sel = []
t_sel_valores = [0, 10, 30, 60, 100]

for t_val in t_sel_valores:
    idx = np.argmin(np.abs(t - t_val))
    indices_sel.append(idx)

tp = t[indices_sel]
Tp = T[indices_sel]

print("\n" + "=" * 70)
print("APARTADO c) Puntos seleccionados para interpolación")
print("=" * 70)
for i, (ti, Ti) in enumerate(zip(tp, Tp)):
    print(f"Punto {i+1}: t = {ti:.1f} h, T = {Ti:.2f} ºC")

# Polinomio de interpolación con estos 5 puntos
V5 = np.vander(tp, 5)
coef_interp5 = np.linalg.solve(V5, Tp)
P_interp5 = np.poly1d(coef_interp5)

plt.figure(figsize=(12, 6))
plt.plot(t, T, 'o', markersize=4, label='Datos experimentales', alpha=0.6)
plt.plot(t_plot, P_ajuste4(t_plot), 'b-', linewidth=2, label='Ajuste grado 4')
plt.plot(t_plot, P_interp5(t_plot), 'g-', linewidth=2, label='Interpolación 5 puntos')
plt.plot(tp, Tp, 'r*', markersize=15, label='Puntos interpolados')
plt.xlabel('Tiempo (h)', fontsize=12)
plt.ylabel('Temperatura (ºC)', fontsize=12)
plt.title('Apartado c) Comparación ajuste vs interpolación 5 puntos', fontsize=14)
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

print("\nAnálisis: El polinomio de interpolación con 5 puntos oscila fuera del")
print("intervalo de datos y NO es adecuado para interpolar en todo t=[0,100].")

# ============================================================
# APARTADO d) Interpolación con alta resolución (0.1 h)
# ============================================================

t_alta_res = np.arange(t.min(), t.max(), 0.1)

# Interpolación de orden cero (nearest)
f_orden0 = interp1d(t, T, kind='nearest')
T_orden0 = f_orden0(t_alta_res)

# Interpolación lineal
f_lineal = interp1d(t, T, kind='linear')
T_lineal = f_lineal(t_alta_res)

# Interpolación por splines cúbicos
from scipy.interpolate import CubicSpline
f_cubic = CubicSpline(t, T)
T_cubic = f_cubic(t_alta_res)

plt.figure(figsize=(14, 10))

# Gráfica completa
plt.subplot(2, 2, 1)
plt.plot(t, T, 'o', markersize=3, label='Datos originales', alpha=0.5)
plt.plot(t_alta_res, T_orden0, '-', linewidth=1, label='Orden cero', alpha=0.8)
plt.plot(t_alta_res, T_lineal, '-', linewidth=1, label='Lineal', alpha=0.8)
plt.plot(t_alta_res, T_cubic, '-', linewidth=1, label='Splines cúbicos', alpha=0.8)
plt.xlabel('Tiempo (h)')
plt.ylabel('Temperatura (ºC)')
plt.title('Interpolación con resolución 0.1 h')
plt.legend()
plt.grid(True, alpha=0.3)

# Zoom en región t=[20, 30]
plt.subplot(2, 2, 2)
mask_zoom = (t_alta_res >= 20) & (t_alta_res <= 30)
mask_datos = (t >= 20) & (t <= 30)
plt.plot(t[mask_datos], T[mask_datos], 'o', markersize=5, label='Datos originales')
plt.plot(t_alta_res[mask_zoom], T_orden0[mask_zoom], '-', linewidth=2, label='Orden cero')
plt.plot(t_alta_res[mask_zoom], T_lineal[mask_zoom], '-', linewidth=2, label='Lineal')
plt.plot(t_alta_res[mask_zoom], T_cubic[mask_zoom], '-', linewidth=2, label='Splines cúbicos')
plt.xlabel('Tiempo (h)')
plt.ylabel('Temperatura (ºC)')
plt.title('Zoom: t ∈ [20, 30] h')
plt.legend()
plt.grid(True, alpha=0.3)

# Zoom en región t=[60, 70]
plt.subplot(2, 2, 3)
mask_zoom2 = (t_alta_res >= 60) & (t_alta_res <= 70)
mask_datos2 = (t >= 60) & (t <= 70)
plt.plot(t[mask_datos2], T[mask_datos2], 'o', markersize=5, label='Datos originales')
plt.plot(t_alta_res[mask_zoom2], T_orden0[mask_zoom2], '-', linewidth=2, label='Orden cero')
plt.plot(t_alta_res[mask_zoom2], T_lineal[mask_zoom2], '-', linewidth=2, label='Lineal')
plt.plot(t_alta_res[mask_zoom2], T_cubic[mask_zoom2], '-', linewidth=2, label='Splines cúbicos')
plt.xlabel('Tiempo (h)')
plt.ylabel('Temperatura (ºC)')
plt.title('Zoom: t ∈ [60, 70] h')
plt.legend()
plt.grid(True, alpha=0.3)

# Zoom en región t=[85, 95]
plt.subplot(2, 2, 4)
mask_zoom3 = (t_alta_res >= 85) & (t_alta_res <= 95)
mask_datos3 = (t >= 85) & (t <= 95)
plt.plot(t[mask_datos3], T[mask_datos3], 'o', markersize=5, label='Datos originales')
plt.plot(t_alta_res[mask_zoom3], T_orden0[mask_zoom3], '-', linewidth=2, label='Orden cero')
plt.plot(t_alta_res[mask_zoom3], T_lineal[mask_zoom3], '-', linewidth=2, label='Lineal')
plt.plot(t_alta_res[mask_zoom3], T_cubic[mask_zoom3], '-', linewidth=2, label='Splines cúbicos')
plt.xlabel('Tiempo (h)')
plt.ylabel('Temperatura (ºC)')
plt.title('Zoom: t ∈ [85, 95] h')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# ============================================================
# APARTADO e) Extrapolación t = 101:1:120 h
# ============================================================

t_extrap = np.arange(101, 121, 1)

plt.figure(figsize=(12, 6))
plt.plot(t, T, 'o', markersize=4, label='Datos experimentales', alpha=0.6)
t_completo = np.linspace(0, 120, 500)
plt.plot(t_completo, P_ajuste4(t_completo), 'b-', linewidth=2, label='Ajuste grado 4')
plt.plot(t_completo, P_interp5(t_completo), 'g-', linewidth=2, label='Interpolación 5 puntos')
plt.axvline(x=100, color='r', linestyle='--', linewidth=1, label='Límite datos')
plt.xlabel('Tiempo (h)', fontsize=12)
plt.ylabel('Temperatura (ºC)', fontsize=12)
plt.title('Apartado e) Extrapolación en t ∈ [101, 120] h', fontsize=14)
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.xlim(0, 120)
plt.tight_layout()
plt.show()

print("\n" + "=" * 70)
print("APARTADO e) Conclusión sobre extrapolación")
print("=" * 70)
print("Ninguno de los modelos polinómicos es adecuado para extrapolar.")
print("La interpolación diverge rápidamente fuera del intervalo de datos.")
print("Se necesita un modelo físico apropiado (exponencial).")
print("=" * 70)

# ============================================================
# APARTADO f) Transformación al espacio logarítmico
# ============================================================

# Transformación: log(T - Ta)
# Filtrar datos donde T > Ta para evitar logaritmos negativos o de cero
T_diff = T - Ta[0]
mask_validos = T_diff > 0
t_validos = t[mask_validos]
T_validos = T[mask_validos]
T_diff_validos = T_diff[mask_validos]

ln_T_diff = np.log(T_diff_validos)

plt.figure(figsize=(12, 6))
plt.plot(t_validos, ln_T_diff, 'o', markersize=4, alpha=0.6)
plt.xlabel('Tiempo t (h)', fontsize=12)
plt.ylabel('ln|T - Ta| ', fontsize=12)
plt.title('Apartado f) Datos en espacio logarítmico', fontsize=14)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

print("\n" + "=" * 70)
print("APARTADO f) Análisis del espacio logarítmico")
print("=" * 70)
print(f"Datos válidos (T > Ta): {len(t_validos)} de {len(t)}")
print("En el espacio logarítmico se observa una tendencia aproximadamente lineal,")
print("especialmente al inicio. El ruido es significativo en tiempos largos.")

# Acotar datos útiles (eliminar los de mayor ruido al final)
# Criterio: usar datos donde T - Ta > umbral (ej: 1 ºC)
umbral = 1.0
mask_utiles = T_diff_validos > umbral
t_utiles = t_validos[mask_utiles]
T_utiles = T_validos[mask_utiles]
ln_T_diff_utiles = ln_T_diff[mask_utiles]

print(f"Datos útiles seleccionados (T - Ta > {umbral} ºC): {len(t_utiles)}")
print("=" * 70)

# ============================================================
# APARTADO g) Ajuste lineal en el espacio transformado
# ============================================================

coef_log = np.polyfit(t_utiles, ln_T_diff_utiles, 1)
P_log = np.poly1d(coef_log)

pendiente_log = coef_log[0]  # -k2
ordenada_log = coef_log[1]   # log(k1)

plt.figure(figsize=(12, 6))
plt.plot(t_validos, ln_T_diff, 'o', markersize=4, label='Datos válidos', alpha=0.4)
plt.plot(t_utiles, ln_T_diff_utiles, 'o', markersize=5, label='Datos útiles', alpha=0.7)
t_ajuste_plot = np.linspace(t_utiles.min(), t_utiles.max(), 300)
plt.plot(t_ajuste_plot, P_log(t_ajuste_plot), 'r-', linewidth=2, label='Ajuste lineal')
plt.xlabel('Tiempo t (h)', fontsize=12)
plt.ylabel('ln|T - Ta|', fontsize=12)
plt.title('Apartado g) Ajuste lineal en espacio logarítmico', fontsize=14)
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# ============================================================
# APARTADO h) Cálculo de constantes k1 y k2
# ============================================================

# De la ecuación: log(T - Ta) = log(k1) - k2·t
# Comparando con: y = ordenada + pendiente·t
# log(k1) = ordenada_log
# -k2 = pendiente_log

k2 = -pendiente_log
k1 = np.exp(ordenada_log)

print("\n" + "=" * 70)
print("APARTADO h) Cálculo de constantes del modelo exponencial")
print("=" * 70)
print(f"Ecuación del ajuste lineal: ln|T - Ta| = {ordenada_log:.6f} + ({pendiente_log:.6f})·t")
print(f"\nConstantes del modelo T(t) = Ta + k1·exp(-k2·t):")
print(f"k1 = {k1:.4f} ºC")
print(f"k2 = {k2:.6f} h⁻¹")
print(f"Ta = {Ta[0]:.1f} ºC (temperatura ambiente)")
print("=" * 70)

# ============================================================
# APARTADO i) Representación del modelo exponencial
# ============================================================

def modelo_exponencial(t, k1, k2, Ta):
    return Ta + k1 * np.exp(-k2 * t)

t_modelo = np.arange(0, 121, 1)
T_modelo = modelo_exponencial(t_modelo, k1, k2, Ta[0])

plt.figure(figsize=(12, 6))
plt.plot(t, T, 'o', markersize=4, label='Datos experimentales', alpha=0.6)
plt.plot(t_modelo, T_modelo, 'r-', linewidth=2, label=f'Modelo: T = {Ta[0]:.1f} + {k1:.2f}·exp(-{k2:.4f}·t)')
plt.axhline(y=Ta[0], color='g', linestyle='--', linewidth=1, label=f'Ta = {Ta[0]:.1f} ºC')
plt.axvline(x=100, color='b', linestyle='--', linewidth=1, alpha=0.5, label='Límite datos')
plt.xlabel('Tiempo (h)', fontsize=12)
plt.ylabel('Temperatura (ºC)', fontsize=12)
plt.title('Apartado i) Modelo exponencial de enfriamiento', fontsize=14)
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.xlim(0, 120)
plt.tight_layout()
plt.show()

# ============================================================
# APARTADO j) Cálculo de desviación estándar y margen de confianza
# ============================================================

# Temperatura del modelo para los tiempos de los datos experimentales
T_modelo_datos = modelo_exponencial(t, k1, k2, Ta[0])

# Desviación estándar
n = len(t)
sigma = np.sqrt(np.sum((T - T_modelo_datos)**2) / (n - 1))

print("\n" + "=" * 70)
print("APARTADO j) Desviación estándar")
print("=" * 70)
print(f"σ = {sigma:.4f} ºC")
print(f"Margen de confianza: ±3σ = ±{3*sigma:.4f} ºC")
print("=" * 70)

# Bandas de confianza
T_superior = T_modelo + 3 * sigma
T_inferior = T_modelo - 3 * sigma

plt.figure(figsize=(12, 6))
plt.plot(t, T, 'o', markersize=4, label='Datos experimentales', alpha=0.6)
plt.plot(t_modelo, T_modelo, 'r-', linewidth=2, label='Modelo exponencial')
plt.fill_between(t_modelo, T_inferior, T_superior, alpha=0.2, color='red', 
                 label=f'Margen ±3σ (±{3*sigma:.2f} ºC)')
plt.axhline(y=Ta[0], color='g', linestyle='--', linewidth=1, label=f'Ta = {Ta[0]:.1f} ºC')
plt.xlabel('Tiempo (h)', fontsize=12)
plt.ylabel('Temperatura (ºC)', fontsize=12)
plt.title('Apartado j) Modelo con margen de confianza ±3σ', fontsize=14)
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.xlim(0, 120)
plt.tight_layout()
plt.show()

print("\n" + "=" * 70)
print("CONCLUSIONES FINALES")
print("=" * 70)
print("1. El ajuste polinómico es inadecuado para este fenómeno físico.")
print("2. La interpolación de alto grado produce oscilaciones no físicas.")
print("3. El modelo exponencial T(t) = Ta + k1·exp(-k2·t) es físicamente correcto.")
print("4. El modelo exponencial permite extrapolar correctamente fuera del rango de datos.")
print(f"5. La desviación estándar σ = {sigma:.4f} ºC indica un buen ajuste.")
print("6. La mayoría de los datos están dentro del margen de confianza ±3σ.")
print("=" * 70)