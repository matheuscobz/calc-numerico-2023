import math

def f(x):
    # Defina a função que deseja integrar
    return  (x)

def regra_trapezio(a, b, n):
    # Calcula o tamanho de cada subintervalo
    h = (b - a) / n

    # Calcula a integral usando a regra do trapézio
    integral = (f(a) + f(b)) / 2.0

    for i in range(1, n):
        x = a + i * h
        integral += f(x)

    integral *= h
    return integral

# Solicita os valores de a, b e n ao usuário
a = float(input("Digite o valor de a (limite inferior): "))
b = float(input("Digite o valor de b (limite superior): "))
n = int(input("Digite o número de subintervalos (n): "))

# Solicita a quantidade de casas decimais desejada
casas_decimais = int(input("Digite o número de casas decimais desejado: "))

# Calcula a integral numérica usando os valores fornecidos
resultado_integral = regra_trapezio(a, b, n)

# Arredonda o resultado para o número de casas decimais desejado
resultado_arredondado = round(resultado_integral, casas_decimais)
print(f"Resultado da integral numérica usando a regra do trapézio:", resultado_arredondado)
