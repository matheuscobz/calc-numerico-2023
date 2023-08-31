import math

def f(x):
    # Defina a função que deseja integrar
    return  (x)

def simpson_1_3(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("O número de subintervalos (n) deve ser um número par.")
    
    # Calcula o tamanho de cada subintervalo
    h = (b - a) / n
    integral = f(a) + f(b)

    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            integral += 2 * f(x)
        else:
            integral += 4 * f(x)

    integral *= h / 3
    return integral

# Solicita os valores de a, b e n ao usuário
a = float(input("Digite o valor de a (limite inferior): "))
b = float(input("Digite o valor de b (limite superior): "))
n = int(input("Digite o número de subintervalos (n): "))

# Solicita a quantidade de casas decimais desejada
casas_decimais = int(input("Digite o número de casas decimais desejado: "))

resultado_integral = simpson_1_3(f, a, b, n)

# Arredonda o resultado para o número de casas decimais desejado
resultado_arredondado = round(resultado_integral, casas_decimais)
print(f"Resultado da integral numérica usando a regra 1/3 de Simpson", resultado_arredondado)
