numero1 = int(input("Digite o primeiro número:"))
numero2 = int(input("Digite o segundo número:"))

if((numero1 + numero2) > 20):
    result = numero1 + numero2 + 8
    print(f"Resultado: {result}")
else:
    result = numero1 + numero2 - 5
    print(f"Resultado: {result}")