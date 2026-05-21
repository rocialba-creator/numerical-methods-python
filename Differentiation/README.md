# 📘 Diferenciación Numérica

Este directorio contiene métodos numéricos para aproximar derivadas tanto de funciones analíticas como de datos experimentales.

---

## 📌 Contenido

Se implementan técnicas para estimar la derivada cuando:

- la función es conocida
- solo se dispone de datos tabulados

---

## ⚙️ Métodos implementados

### 🔹 Diferenciación de funciones

Se aproximan derivadas usando:

- Diferencia adelantada (2 puntos)
- Diferencia centrada (2 puntos)
- Diferencia adelantada (3 puntos)

Estos métodos permiten estimar:

f'(x) ≈ Δf / Δx

---

### 🔹 Diferenciación de datos tabulados

Cuando solo se dispone de datos (x, y), se usa:

- Diferencia adelantada (bordes)
- Diferencia centrada (interiores)
- Diferencia atrasada (último punto)

---

## 🧮 Idea matemática

La derivada se aproxima mediante el concepto de pendiente:

dy/dx ≈ (y₂ - y₁) / (x₂ - x₁)

---

## 📂 Archivos

- `derivadas_funciones.py`  
  Derivación numérica de funciones matemáticas.

- `derivadas_tablas.py`  
  Derivación a partir de datos experimentales tabulados.

---

## 📊 Aplicaciones

- estimación de pendientes
- análisis de datos experimentales
- física (velocidad, aceleración)
- ingeniería y señales

---

## 📌 Observaciones

- El error depende fuertemente del paso `h`.
- Métodos centrados suelen ser más precisos.
- Datos ruidosos pueden afectar la derivada significativamente.

---
