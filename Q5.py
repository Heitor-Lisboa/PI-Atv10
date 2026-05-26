numero = input("Digite um número inteiro positivo: ")
 
contador = 0

for digito in numero:
    contador = contador + 1
 
print("O número", numero, "possui", contador, "dígitos")
