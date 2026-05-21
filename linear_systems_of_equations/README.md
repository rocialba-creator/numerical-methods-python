# Linear Systems of Equations (Iterative Methods)

This folder contains numerical methods for solving linear systems of the form:

    Ax = b

where A is a square matrix, b is the independent term vector, and x is the unknown solution vector.

The goal is to approximate the solution using iterative methods instead of direct factorization methods.

---

## 📌 Methods implemented

### 1. Gauss-Seidel (Simple)
File: `gauss_seidel_simple.py`

Iterative method where each component of x is updated sequentially using the most recent available values.

No matrix decomposition is used explicitly.

---

### 2. Gauss-Seidel (Matrix Form)

File: `gauss_seidel_matrix.py`

This version is based on the decomposition of matrix A:

    A = D + L + U

where:
- D is the diagonal part
- L is the lower triangular part
- U is the upper triangular part

The iteration is written in matrix form:

    x^(k+1) = -(D + L)^(-1) U x^(k) + (D + L)^(-1) b

The method also computes the **spectral radius** of the iteration matrix to check convergence.

---

### 3. Damped Jacobi Method
File: `damped_jacobi.py`

Improved Jacobi method with relaxation parameter ω:

    x^(k+1) = (1 - ω)x^(k) + ω D^(-1)(b - (L + U)x^(k))

The relaxation parameter helps control convergence speed and stability.

---

### 4. Successive Over-Relaxation (SOR)
File: `sor_method.py`

Extension of Gauss-Seidel that introduces relaxation:

    A = D + L + U

Iteration:

    x^(k+1) = (D - ωL)^(-1) [(1 - ω)D + ωU] x^(k) + ω(D - ωL)^(-1)b

This method can significantly accelerate convergence when ω is well chosen.

---

## 📊 Convergence analysis

For matrix-based methods, convergence is analyzed using the **spectral radius (ρ)** of the iteration matrix:

- ρ < 1 → method converges
- ρ ≥ 1 → method does not converge

The stopping criterion for all methods is:

    ||x^(k+1) - x^(k)|| < tolerance

---

## 🧠 Key concepts used

- Matrix factorization: A = D + L + U  
- Iterative numerical methods  
- Relaxation techniques (ω parameter)  
- Spectral radius for convergence analysis  
- Error based stopping criteria  

---
