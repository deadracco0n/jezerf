#!/usr/bin/env python
# coding: utf-8

# In[6]:


def inverter_string(texto):
    # Inicializa uma variável para armazenar a string invertida
    string_invertida = ''
    
    # Percorre a string original de trás para frente
    for i in range(len(texto) - 1, -1, -1):
        string_invertida += texto[i]
    
    return string_invertida


texto = input("Informe uma string para inverter: ")
resultado = inverter_string(texto)
print(f"String invertida: {resultado}")


# In[ ]:




