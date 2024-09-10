#!/usr/bin/env python
# coding: utf-8

# In[1]:


def calcular_percentual(faturamento_por_estado):
    # Calcular o faturamento total
    faturamento_total = sum(faturamento_por_estado.values())
    
    # Calcular o percentual de cada estado e exibir
    percentuais = {}
    for estado, faturamento in faturamento_por_estado.items():
        percentual = (faturamento / faturamento_total) * 100
        percentuais[estado] = percentual
    
    return percentuais

# Dicionário com os valores de faturamento por estado
faturamento_por_estado = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

# Calcula os percentuais
percentuais = calcular_percentual(faturamento_por_estado)

# Exibe os percentuais
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")


# In[ ]:




