# Para o faturamento diário:

import json


with open('faturamento.json', 'r') as file:
    dados = json.load(file)


faturamento = [dia['valor'] for dia in dados if dia['valor'] > 0]

menor_valor = min(faturamento)
maior_valor = max(faturamento)
media_mensal = sum(faturamento) / len(faturamento)

dias_acima_media = sum(1 for valor in faturamento if valor > media_mensal)

print(f"Menor valor: R$ {menor_valor:.2f}")
print(f"Maior valor: R$ {maior_valor:.2f}")
print(f"Dias acima da média: {dias_acima_media}")