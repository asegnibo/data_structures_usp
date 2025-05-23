n = 10

for i in range(1,n): # O(n)
    j = i
    while j > 1 : # O número de vezes que um número i pode ser dividido por 2 antes de chegar a 1 é aproximadamente log₂(i). O(log n)
        print(j)
        j = j / 2 
        
# O(n) + O(log n) = O(n log n)
# O(n log n) é a complexidade de tempo total do algoritmo.