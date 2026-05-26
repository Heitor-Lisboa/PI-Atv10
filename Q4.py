primeiro = float(input("Digite o número 1: "))
maior = primeiro
menor = primeiro
soma = primeiro

for i in range(2, 6):
    numero = float(input("Digite o número " + str(i) + ": "))
    soma = soma + numero
 
    if numero > maior:
        maior = numero
 
    if numero < menor:
        menor = numero
 
media = soma / 5

print("Maior número:", maior)
print("Menor número:", menor)
print("Média aritmética:", media)