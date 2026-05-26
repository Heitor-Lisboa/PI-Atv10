print("Digite 8 números inteiros:")

for i in range(1, 9):
    numero = int(input("Número " + str(i) + ": "))
    if numero % 4 == 0:
        print(numero, "é divisível por 4")