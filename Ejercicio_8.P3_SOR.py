import numpy as np

def sor_matricial(A, b, x0, w, tol, itmax):
    """
    Resuelve un sistema de ecuaciones Ax=b mediante el método SOR (Successive Over-Relaxation)
    en forma matricial.
    
    Parámetros:
    -----------
    A : array (n x n)
        Matriz de coeficientes del sistema
    b : array (n x 1) o (n,)
        Vector de términos independientes
    x0 : array (n x 1) o (n,)
        Solución inicial
    w : float
        Parámetro de amortiguamiento (0 < w < 2)
    tol : float
        Tolerancia máxima entre dos iteraciones sucesivas
    itmax : int
        Número máximo de iteraciones permitido
    
    Retorna:
    --------
    xs : array (n x 1)
        Vector solución del sistema
    it : int
        Número de iteraciones realizadas
    error : float
        Error relativo entre las dos últimas iteraciones
    radio_espectral : float
        Radio espectral de la matriz de iteración
    """
    
    # Obtener dimensiones
    nf, nc = np.shape(A)
    
    # Asegurar que b y x0 sean vectores columna
    if b.ndim == 1:
        b = b.reshape(-1, 1)
    if x0.ndim == 1:
        x0 = x0.reshape(-1, 1)
    
    # Inicialización
    xs = x0.copy()
    xs1 = b.copy()
    it = 0
    
    # Descomposición de A en D, L, U
    D = np.diag(np.diag(A))
    U = np.triu(A) - D
    L = np.tril(A) - D
    
    # Calcular (D - w*L)^(-1)
    D_wL_inv = np.linalg.inv(D - w * L)
    
    # Matriz de iteración del método SOR
    # M = (D - w*L)^(-1) * ((1-w)*D + w*U)
    M = D_wL_inv.dot((1 - w) * D + w * U)
    
    # Calcular radio espectral
    autovalores = np.linalg.eigvals(M)
    radio_espectral = np.max(np.abs(autovalores))
    
    # Verificar condición de convergencia
    if radio_espectral >= 1:
        print(f"ERROR: El método NO converge.")
        print(f"Radio espectral de la matriz de iteración: {radio_espectral:.6f}")
        print(f"Para convergencia se requiere que el radio espectral < 1")
        return None, 0, None, radio_espectral
    
    # Vector constante f = w * (D - w*L)^(-1) * b
    f = w * D_wL_inv.dot(b)
    
    # Primera iteración
    xs1 = f + M.dot(xs)
    error = np.linalg.norm(xs1 - xs)
    it += 1
    
    # Iteraciones sucesivas
    while (error > tol) and (it < itmax):
        xs = xs1.copy()
        xs1 = f + M.dot(xs)
        error = np.linalg.norm(xs1 - xs)
        it += 1
    
    return xs1, it, error, radio_espectral


# Ejemplo de uso
print("="*60)
print("MÉTODO SOR (SUCCESSIVE OVER-RELAXATION) MATRICIAL")
print("="*60)

# Ejemplo 1: Sistema 3x3
print("\n--- Ejemplo 1 ---")
A = np.array([[4, -1, 0],
              [-1, 4, -1],
              [0, -1, 4]], dtype=float)

b = np.array([15, 10, 10], dtype=float)
x0 = np.zeros(3)
w = 1.2
tol = 1e-6
itmax = 100

print(f"\nMatriz A:\n{A}")
print(f"\nVector b: {b}")
print(f"Solución inicial x0: {x0}")
print(f"Parámetro w: {w}")
print(f"Tolerancia: {tol}")
print(f"Iteraciones máximas: {itmax}")

xs, it, error, rho = sor_matricial(A, b, x0, w, tol, itmax)

if xs is not None:
    print(f"\n--- RESULTADOS ---")
    print(f"Radio espectral: {rho:.8f}")
    print(f"Solución encontrada:\n{xs.flatten()}")
    print(f"Número de iteraciones: {it}")
    print(f"Error relativo final: {error:.2e}")
    
    # Verificación
    residuo = np.linalg.norm(A.dot(xs) - b.reshape(-1, 1))
    print(f"Residuo ||Ax - b||: {residuo:.2e}")

# Ejemplo 2: Comparación de diferentes valores de w
print("\n\n--- Ejemplo 2: Comparación de diferentes valores de w ---")
A2 = np.array([[10, -1, 2, 0],
               [-1, 11, -1, 3],
               [2, -1, 10, -1],
               [0, 3, -1, 8]], dtype=float)

b2 = np.array([6, 25, -11, 15], dtype=float)
x0_2 = np.zeros(4)

valores_w = [0.5, 1.0, 1.2, 1.5]

print(f"\nMatriz A:\n{A2}")
print(f"Vector b: {b2}")

for w_test in valores_w:
    print(f"\n--- w = {w_test} ---")
    xs2, it2, error2, rho2 = sor_matricial(A2, b2, x0_2, w_test, tol, itmax)
    
    if xs2 is not None:
        print(f"Radio espectral: {rho2:.8f}")
        print(f"Iteraciones: {it2}")
        print(f"Error final: {error2:.2e}")

# Ejemplo 3: Caso que no converge
print("\n\n--- Ejemplo 3: Caso sin convergencia ---")
A3 = np.array([[1, 2, 3],
               [2, 1, 2],
               [3, 2, 1]], dtype=float)

b3 = np.array([6, 5, 6], dtype=float)
x0_3 = np.zeros(3)
w3 = 1.8

print(f"\nMatriz A:\n{A3}")
print(f"Vector b: {b3}")
print(f"Parámetro w: {w3}")

xs3, it3, error3, rho3 = sor_matricial(A3, b3, x0_3, w3, tol, itmax)
A = np.array([[4, 2, -1],
              [3, -5, 1],
              [1, -1, 6]], dtype=float)
b = np.array([[5], [-4], [17]], dtype=float)
x0 = np.array([[0], [0], [0]], dtype=float)
print(sor_matricial(A,b,x0,3,0.00001,30))