idade = int(input("Digite sua idade:"))

peso = int(input("Digite seu peso: "))

sono = int(input("Quantas horas dormiu nas últimas 24 horas?:"))

bidade = False
bpeso  = False
bsono  = False

if(idade < 15 or idade > 69):
    bidade = False
else:
    bidade = True
print(f"idade: {bidade}" )
if(peso > 50):
    bpeso = True
print(f"peso: {bpeso}" )

if(sono >= 6):
    bsono = True
print(f"sono: {bsono}" )

if(bidade and bpeso and bsono):
    print("Doador!") 
else:
    print("Não doador!") 


