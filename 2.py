#!/usr/bin/env python
# coding: utf-8

# In[8]:


def verifica_fibonacci(num):
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    return b == num or num == 0

def mensagem_fibonacci(num):
    if verifica_fibonacci(num):
        return f"O número {num} pertence à sequência de Fibonacci."
    else:
        return f"O número {num} NÃO pertence à sequência de Fibonacci."


numero = int(input("Informe um número: "))
print(mensagem_fibonacci(numero))


# In[ ]:




