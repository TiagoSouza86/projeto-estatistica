def calcular_varianca(numeros):
    numero1 = float(input("Insira quatro números: "))
    numero2 = float(input("Insira quatro números: "))
    numero3 = float(input("Insira quatro números: "))
    numero4 = float(input("Insira quatro números: "))

    numeros = [numero1, numero2, numero3, numero4]
    media = sum(numeros) / len(numeros)
    varianca = sum((x - media) ** 2 for x in numeros) / len(numeros)
    return varianca

varianca_calculada = calcular_varianca([])
print(f"A variância dos números inseridos é: {varianca_calculada}")
print("Verificado por Thyérrisson")

        


