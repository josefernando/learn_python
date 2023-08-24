
#tuplas - listas imutáveis
dias_da_semana = ("segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo")

print(dias_da_semana)

#dicionáros
pessoa = {"nome":"Antonio" , "idade":35 , "doador":True}

print(pessoa)

print(pessoa["nome"])
print(pessoa.keys())
print(pessoa.items())

pessoa["peso"] = 85
print(pessoa)

print(pessoa.values)


#set não repetem valores

time = {"goleiro", "defesa", "ataque", "goleiro", "técnico"}

print(time)
