soma = 0
 
for i in range(1, 21):
    valor = float(input("Digite o valor " + str(i) + ": "))
    soma = soma + valor
 
media = soma / 20
 
print("A média dos 20 valores é:", media)
 
