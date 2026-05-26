triangulo = int(input("Digite um número para o triângulo: "))
 
for linha in range(triangulo, 0, -1):
    for coluna in range(linha):
        print("*", end="")
    print()
