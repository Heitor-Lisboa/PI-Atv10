numero = int(input("Digite um número inteiro: "))
digito = input("Digite o dígito que deseja contar (0 a 9): ")
 
contador = 0

for caractere in str(numero):
    if caractere == digito:
        contador = contador + 1
 
print("Resultado:", contador, "(O dígito", digito, "aparece", contador, "vezes)")
