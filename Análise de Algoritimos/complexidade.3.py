import math

def Processa(n):
    if n <= 1 : #O(1)
        return
    for i in range(1,n+1): #O(n)
        print(i)
    Processa(math.floor(n/2)) # tamanho n/2
    Processa(math.floor(n/2)) # tamanho n/2
    
Processa(4)

#T(n) = 2T(n/2) + O(n)
#Se o trabalho que você faz fora das chamadas recursivas é igual a n, e você divide o problema em dois do tipo n/2, então a resposta é:
#T(n) = O(n log n)
