import math

# Defina a função que deseja integrar
def f(x):
    return (x) 


def gauss_legendre_quadrature(func, a, b, n):
    #Tabela da quadratura de Gauss-Legendre
    gauss_legendre_points = {
        1:(
            [0], 
            [2.0]
        ),
        
        2:(
            [-0.5773502691896257, 0.5773502691896257], 
            [1.0, 1.0]
        ),
        
        3:(
            [-0.7745966692414834, 0, 0.7745966692414834],
            [0.5555555555555556, 0.8888888888888888, 0.5555555555555556]
        ),
        
        4:(
            [-0.8611363115940526, -0.3399810435848563, 0.3399810435848563, 0.8611363115940526],
            [0.3478548451374538, 0.6521451548625461, 0.6521451548625461, 0.3478548451374538]
        ),
        
        5:(
            [-0.9061798459386640, -0.5384693101056831, 0, 0.5384693101056831, 0.9061798459386640],
            [0.2369268850561891, 0.4786286704993665, 0.5688888888888889, 0.4786286704993665, 0.2369268850561891]
        ),
        
        6:(
            [-0.9324695142031521, -0.6612093864662645, -0.2386191860831969,
            0.2386191860831969, 0.6612093864662645, 0.9324695142031521],
            [0.1713244923791704, 0.3607615730481386, 0.4679139345726910,
            0.4679139345726910, 0.3607615730481386, 0.1713244923791704]
        )
    }

    if n not in gauss_legendre_points:
        raise ValueError("Número de pontos de quadratura não suportado.")

    x, w = gauss_legendre_points[n]

    # Mapear os pontos de [a, b] para [-1, 1]
    mapped_x = [((b - a) * xi / 2) + ((a + b) / 2) for xi in x]
    
    # Calcular a soma ponderada da função nos pontos de Gauss
    integral = sum(w[i] * func(mapped_x[i]) for i in range(n))

    # Ajustar o resultado para o intervalo [a, b]
    integral *= (b - a) / 2

    return integral



# Solicita os valores de a, b e n ao usuário
a = float(input("Digite o valor de a (limite inferior): "))
b = float(input("Digite o valor de b (limite superior): "))

# Número de pontos de Gauss (1, 2, 3, 4, 5 ou 6)
n = int(input("Digite o número de pontos (n): "))

resultado = gauss_legendre_quadrature(f, a, b, n)
print("Resultado da integral:", resultado)
