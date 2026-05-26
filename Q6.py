total = 0
maior_consumo = 0
produto_maior = 1
 
for i in range(1, 8):
    consumo = float(input("Digite o consumo de matéria-prima (kg) do produto " + str(i) + ": "))
    total = total + consumo
 
    if consumo > maior_consumo:
        maior_consumo = consumo
        produto_maior = i
 
print("Consumo total:", total, "kg")
print("Produto que mais consome: Produto", produto_maior, "com", maior_consumo, "kg")
