# Desenvolva uma função recursiva que conte quantos elementos pares existem em uma lista de inteiros.

lista = [1, 2, 3, 4, 5, 6, 8, 8, 8, 10]

def contar_pares(lista, i=0):
    if lista[i] % 2 == 0:
        return 1 + contar_pares(lista, i+1) if i<len(lista)-1 else 1
    else:
        return contar_pares(lista, i+1) if i<len(lista)-1 else 0
    
print(contar_pares(lista)) # Saída: 5 (os números pares são 2, 4, 6, 8 e 10)