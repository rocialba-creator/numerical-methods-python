import numpy as np

def jacobi_amortiguado(A, b, x0, w, tol, itmax):
    """
    Resuelve un sistema de ecuaciones Ax=b mediante el método de Jacobi amortiguado.
    
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
    
    # Calcular D^(-1)
    invD = np.linalg.inv(D)
    
    # Matriz de identidad
    I = np.eye(nf)
    
    # Matriz de iteración del método de Jacobi amortiguado
    # M = (1-w)*I + w*D^(-1)*(L+U) = I - w*D^(-1)*A
    M = I - w * invD.dot(A)
    
    # Calcular radio espectral
    autovalores = np.linalg.eigvals(M)
    radio_espectral = np.max(np.abs(autovalores))
    
    # Verificar condición de convergencia
    if radio_espectral >= 1:
        print(f"ERROR: El método NO converge.")
        print(f"Radio espectral de la matriz de iteración: {radio_espectral:.6f}")
        print(f"Para convergencia se requiere que el radio espectral < 1")
        return None, 0, None, radio_espectral
    
    # Vector constante f = w * D^(-1) * b
    f = w * invD.dot(b)
    
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
print("MÉTODO DE JACOBI AMORTIGUADO")
print("="*60)

# Ejemplo 1: Sistema 3x3
print("\n--- Ejemplo 1 ---")
A = np.array([[4, -1, 0],
              [-1, 4, -1],
              [0, -1, 4]], dtype=float)

b = np.array([15, 10, 10], dtype=float)
x0 = np.zeros(3)
w = 0.8
tol = 1e-6
itmax = 100

print(f"\nMatriz A:\n{A}")
print(f"\nVector b: {b}")
print(f"Solución inicial x0: {x0}")
print(f"Parámetro w: {w}")
print(f"Tolerancia: {tol}")
print(f"Iteraciones máximas: {itmax}")

xs, it, error, rho = jacobi_amortiguado(A, b, x0, w, tol, itmax)

if xs is not None:
    print(f"\n--- RESULTADOS ---")
    print(f"Radio espectral: {rho:.8f}")
    print(f"Solución encontrada:\n{xs.flatten()}")
    print(f"Número de iteraciones: {it}")
    print(f"Error relativo final: {error:.2e}")
    
    # Verificación
    residuo = np.linalg.norm(A.dot(xs) - b.reshape(-1, 1))
    print(f"Residuo ||Ax - b||: {residuo:.2e}")

# Ejemplo 2: Caso que no converge
print("\n\n--- Ejemplo 2: Caso sin convergencia ---")
A2 = np.array([[1, 2, 3],
               [2, 1, 2],
               [3, 2, 1]], dtype=float)

b2 = np.array([6, 5, 6], dtype=float)
x0_2 = np.zeros(3)
w2 = 1.5

print(f"\nMatriz A:\n{A2}")
print(f"Vector b: {b2}")
print(f"Parámetro w: {w2}")

xs2, it2, error2, rho2 = jacobi_amortiguado(A2, b2, x0_2, w2, tol, itmax)
A = np.array([[4, 2, -1],
              [3, -5, 1],
              [1, -1, 6]], dtype=float)
b = np.array([[5], [-4], [17]], dtype=float)
x0 = np.array([[0], [0], [0]], dtype=float)
print(jacobi_amortiguado(A,b,x0,3,0.00001,30))
