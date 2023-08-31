def lagrange_interpolation(x, y, target_x):
    n = len(x)
    result = 0

    for i in range(n):
        term = y[i]
        for j in range(n):
            if i != j:
                term *= (target_x - x[j]) / (x[i] - x[j])
        result += term

    return result

def inverse_interpolation(x, y, target_y):
    n = len(x)
    result = []

    for i in range(n):
        if y[i] == target_y:
            return x[i]
    
    for i in range(n - 1):
        if (y[i] - target_y) * (y[i + 1] - target_y) < 0:
            result.append(x[i] + (x[i + 1] - x[i]) * (target_y - y[i]) / (y[i + 1] - y[i]))
    
    return result

def main():
    print("Escolha o tipo de interpolação:")
    print("1. Interpolação de Lagrange")
    print("2. Interpolação Inversa")
    
    choice = int(input("Digite 1 ou 2 para selecionar o tipo de interpolação: "))
    
    if choice == 1:
        n = int(input("Digite o número de pontos (n): "))
        x = []
        y = []
        
        for i in range(n):
            xi = float(input(f"Digite o valor de x{i+1}: "))
            yi = float(input(f"Digite o valor de y{i+1}: "))
            x.append(xi)
            y.append(yi)
        
        target_x = float(input("Digite o valor de x para interpolar: "))
        result = lagrange_interpolation(x, y, target_x)
        print(f"O valor interpolado de y para x = {target_x} é {result}")
    
    elif choice == 2:
        n = int(input("Digite o número de pontos (n): "))
        x = []
        y = []
        
        for i in range(n):
            xi = float(input(f"Digite o valor de x{i+1}: "))
            yi = float(input(f"Digite o valor de y{i+1}: "))
            x.append(xi)
            y.append(yi)
        
        target_y = float(input("Digite o valor de y para interpolar: "))
        result = inverse_interpolation(x, y, target_y)
        
        if isinstance(result, float):
            print(f"O valor interpolado de x para y = {target_y} é {result}")
        else:
            print("Não foi possível determinar um valor único para x.")
    
    else:
        print("Escolha inválida. Por favor, selecione 1 ou 2.")

if __name__ == "__main__":
    main()
