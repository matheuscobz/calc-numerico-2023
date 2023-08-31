import math

# Defina a função que deseja integrar
def f(x):
    return (x)  

def regra_3_8_simpson(f, a, b, n):
    
    h = (b - a) / n
    integral = f(a) + f(b)

    for i in range(1, n):
        x = a + i * h
        if i % 3 == 0:
            integral += 2 * f(x)
        else:
            integral += 3 * f(x)

    integral *= (3 * h) / 8
    return integral


# Solicita os valores de a, b e n ao usuário
a = float(input("Digite o valor de a (limite inferior): "))
b = float(input("Digite o valor de b (limite superior): "))
n = int(input("Digite o número de subintervalos (n): "))

# Solicita a quantidade de casas decimais desejada
casas_decimais = int(input("Digite o número de casas decimais desejado: "))

resultado_integral = regra_3_8_simpson(f, a, b, n)
# Arredonda o resultado para o número de casas decimais desejado

resultado_arredondado = round(resultado_integral, casas_decimais)
print(f"Resultado da integral numérica usando a regra 3/8 de Simpson:", resultado_arredondado)
