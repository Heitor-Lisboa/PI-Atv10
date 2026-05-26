total_vendas = 0.0
vendas_meses = []

for mes in range(1, 7):
    valor = float(input(f"Digite o valor do mês {mes}: "))
    total_vendas = total_vendas + valor
    vendas_meses.append(valor)

media_mensal = total_vendas / 6
meses_acima_da_media = 0

for valor in vendas_meses:
    if valor > media_mensal:
        meses_acima_da_media = meses_acima_da_media + 1

print("Total vendido: R$", total_vendas)
print("Média mensal: R$", media_mensal)
print("Meses acima da média:", meses_acima_da_media)