# Root Finding Methods (Nonlinear Equations)

This folder contains numerical methods to approximate solutions of nonlinear equations of the form:

    f(x) = 0

The goal is to find roots using iterative numerical algorithms.

---

## 📌 Methods included

### 1. Bisection Method
File: `bisection_method.py`

A bracketing method that starts with an interval [a, b] such that:

    f(a) · f(b) < 0

The interval is repeatedly halved using:

    c = (a + b) / 2

The method guarantees convergence if the initial interval is valid.

---

### 2. Fixed Point Iteration
File: `fixed_point_iteration.py`

Transforms the equation into:

    x = g(x)

Then iterates:

    x_(n+1) = g(x_n)

Convergence depends on the choice of g(x) and the initial guess.

---

### 3. Regula Falsi (False Position Method)
File: `regula_falsi_method.py`

Combines bracketing with linear interpolation:

    c = b - f(b)(b - a) / (f(b) - f(a))

Improves convergence compared to bisection while keeping the root bracketed.

---

### 4. Secant Method
File: `secant_method.py`

Uses two previous points without derivatives:

    x_(n+1) = x_n - f(x_n)(x_n - x_(n-1)) / (f(x_n) - f(x_(n-1)))

Faster than bisection but not guaranteed to converge.

---

### 5. Newton-Raphson Method
File: `newton_raphson_method.py`

Uses derivative information:

    x_(n+1) = x_n - f(x_n) / f'(x_n)

Very fast convergence near the root, but depends strongly on the initial guess.

---

## 📊 Convergence criteria

All methods stop when:

    |f(x)| < tolerance
or
    |x_(n+1) - x_n| < tolerance

A maximum number of iterations is also used.

---

## 🧠 Key concepts used

- Bracketing methods (Bisection, Regula Falsi)
- Open methods (Newton, Secant, Fixed Point)
- Iterative root approximation
- Convergence and stability analysis
- Use of derivatives (Newton method)

---
