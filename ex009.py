import random

numero = random.randint(1,51)

guess = False

print(numero)

while (guess == False):
    pick = int(input("Escolha um numero de 1 a 50:"))
    if (pick == numero):
        print(f"Parabéns,  você acertou. O número é  {numero}")
        guess = True
    else:
        if(numero > pick):
            print("O número é maior.")
        else:
            print("O número é menor.")
