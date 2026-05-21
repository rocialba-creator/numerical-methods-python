# 📘 Ecuaciones Diferenciales Ordinarias (EDO) — Método de Euler

Este directorio contiene la implementación y simulación numérica de ecuaciones diferenciales ordinarias (EDO), resueltas mediante el método de Euler explícito.

---

## 📌 Contenido

Se estudia la evolución temporal de la temperatura interior de una casa mediante un modelo físico basado en un balance energético:

- Intercambio térmico con el exterior
- Flujo de calor interno
- Capacidad calorífica del sistema

---

## ⚙️ Modelo matemático

La ecuación diferencial utilizada es:

dT/dt = (Fi - k·T + k·To) / C

donde:

- T → temperatura interior (°C)
- To → temperatura exterior (°C)
- Fi → flujo de calor interno (Kcal/h)
- k → coeficiente de intercambio térmico
- C → capacidad calorífica

---

## 🧮 Método numérico

Se utiliza el método de Euler explícito:

T_{n+1} = T_n + dt · f(T_n)

Este método permite aproximar la solución de la EDO paso a paso en el tiempo.

---

## 📂 Archivos

- `euler_casa_temperatura.py`  
  Simulación completa del modelo térmico con:
  - resolución numérica
  - análisis de resultados
  - representación gráfica

---

## 📊 Resultados

El sistema evoluciona hacia una temperatura de equilibrio determinada por los parámetros físicos del modelo.

Se estudian además:
- estabilidad del sistema
- evolución temporal
- comparación con equilibrio teórico

---

## 📌 Observaciones

- El método de Euler es simple pero sensible al tamaño del paso `dt`.
- Un `dt` demasiado grande puede introducir errores numéricos.
- El sistema converge a un estado estacionario físicamente coherente.
