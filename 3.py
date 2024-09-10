#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import json

def calcular_faturamento(faturamento_diario):
    # Filtrar dias com faturamento > 0
    faturamento_valido = [dia['valor'] for dia in faturamento_diario if dia['valor'] > 0]
    
    # Calcular o menor e o maior valor de faturamento
    menor_faturamento = min(faturamento_valido)
    maior_faturamento = max(faturamento_valido)
    
    # Calcular a média mensal ignorando dias sem faturamento
    media_mensal = sum(faturamento_valido) / len(faturamento_valido)
    
    # Calcular número de dias com faturamento superior à média
    dias_acima_da_media = sum(1 for dia in faturamento_valido if dia > media_mensal)
    
    return menor_faturamento, maior_faturamento, dias_acima_da_media

with open('faturamento.json', 'r') as file:
    faturamento_diario = json.load(file)

menor, maior, dias_acima_media = calcular_faturamento(faturamento_diario)

print(f"Menor faturamento: {menor:.2f}")
print(f"Maior faturamento: {maior:.2f}")
print(f"Dias com faturamento acima da média: {dias_acima_media}")


# In[ ]:




