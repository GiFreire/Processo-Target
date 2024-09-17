faturamento_por_estado = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}
percentuais ={}
faturamento_total = 0
for faturamento in faturamento_por_estado.values():
    faturamento_total += faturamento
for i, valor in faturamento_por_estado.items():
    percentual = (valor / faturamento_total) * 100

    percentuais[i]=percentual

print("Percentual de representação de cada estado:")
for i, percentual in percentuais.items():
    print(f"{i}: {percentual:.2f}%")



