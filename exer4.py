nome=["joao","carlos","maria","luiza","isabel"]
nomea=input("digite seu nome:")
for i in range(len(nome)):
    if nome[i]==nomea:
        mens=f"{nome}  na posicao {i}"
    print(f"{nomea} esta na posicao {i} ")
else:
    mens = "nome nao encontrado"
print (mens)
