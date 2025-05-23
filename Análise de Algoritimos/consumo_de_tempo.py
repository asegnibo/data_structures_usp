n = 5

vetor = []
for i in range(1, n + 1):
    vetor.append(i)
    
s = 0
for i in range (1, n + 1): 
    s = s + vetor[i - 1]

m = s/n
k = 1
for i in range (2,n+1): 
    if (vetor[i-1] - m)**2 < (vetor[k] - m)**2:
        k = i
        
print(k)