import json

try:

    with open('faturamento.json', 'r') as arquivo:
        dados = json.load(arquivo)


    faturamento = [dia['valor'] for dia in dados if dia['valor'] > 0]


    menor_valor = min(faturamento)
    maior_valor = max(faturamento)
    media_mensal = sum(faturamento) / len(faturamento)
    
    
    dias_acima_media = sum(1 for valor in faturamento if valor > media_mensal)

    
    print(f"\nResultados da análise de faturamento:")
    print(f"Menor valor de faturamento: R$ {menor_valor:.2f}")
    print(f"Maior valor de faturamento: R$ {maior_valor:.2f}")
    print(f"Média mensal: R$ {media_mensal:.2f}")
    print(f"Número de dias acima da média: {dias_acima_media}")

except FileNotFoundError:
    print("Erro: Arquivo faturamento.json não encontrado!")
except json.JSONDecodeError:
    print("Erro: Arquivo JSON mal formatado!")
except Exception as e:
    print(f"Erro inesperado: {str(e)}")