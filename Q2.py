inteiro = int(input("Digite um número inteiro: "))
 
print("Múltiplos de", inteiro, "de 1 até 10:")

for i in range(1, 11):
    print(inteiro, "x", i, "=", inteiro * i)
