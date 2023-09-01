import numpy as np

# Função para realizar a decomposição LU
def decomposicao_lu(matriz):
    n = len(matriz)
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for i in range(n):
        # Fator de escala da linha i
        U[i, i:] = matriz[i, i:]
        L[i:, i] = matriz[i:, i] / U[i, i]
        for j in range(i + 1, n):
            U[j, i:] -= L[j, i] * U[i, i:]

    return L, U

# Função para receber os coeficientes do sistema do usuário
def obter_coeficientes():
    n = int(input("Informe o número de equações: "))
    matriz_coeficientes = np.zeros((n, n + 1))

    print("Informe os coeficientes do sistema:")
    for i in range(n):
        for j in range(n):
            matriz_coeficientes[i, j] = float(input(f"Digite o coeficiente a[{i+1}][{j+1}]: "))
        matriz_coeficientes[i, n] = float(input(f"Digite o termo independente b[{i+1}]: "))

    print("\nMatriz de Coeficientes:")
    print(matriz_coeficientes)

    return matriz_coeficientes

# Função para resolver o sistema de equações com base na decomposição LU
def resolver_sistema_lu(matriz_coeficientes):
    L, U = decomposicao_lu(matriz_coeficientes[:, :-1])
    b = matriz_coeficientes[:, -1]

    # Resolvendo Ly = b usando substituição progressiva
    n = len(b)
    y = np.zeros(n)
    for i in range(n):
        y[i] = b[i] - np.dot(L[i, :i], y[:i])

    # Resolvendo Ux = y usando substituição regressiva
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - np.dot(U[i, i+1:], x[i+1:])) / U[i, i]

    return x

# Programa principal
coeficientes = obter_coeficientes()
solucao = resolver_sistema_lu(coeficientes)
print("\nSolução do sistema:")
for i, x in enumerate(solucao):
    print(f"x[{i+1}] = {x}")
