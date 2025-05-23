# Implemente uma função recursiva para calcular a soma dos elementos de uma matriz m×n, passada como uma lista de listas.

listinha=[[1,2,3],[4,5,6],[7,8,4]]
def soma_matriz(matriz):
    if not matriz:
        return 0
    else:
        return sum(matriz[0]) + soma_matriz(matriz[1:])
    

resultado = soma_matriz(listinha)
print(resultado) # Saída: 45