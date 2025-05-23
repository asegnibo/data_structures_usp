# Implemente uma fun¸c˜ ao recursiva que verifique se uma matriz (lista de listas) n×n ´e sim´ etrica (ou seja, todo elemento na posi¸c˜ ao (i,j) ´ e igual ao elemento (j,i))

matriz = [
    [1, 2, 3],
    [2, 5, 6],
    [3, 6, 9]
]

def ver_simetria(matriz, i=0 , j=0):
    if i >= len(matriz):
        return True
    if j >= len(matriz):
        return ver_simetria(matriz, i + 1, 0)
    if matriz[i][j] != matriz[j][i]:
        return False
    else:
        return ver_simetria(matriz, i, j + 1)
    
resultado = ver_simetria(matriz)
print(resultado) # Saída: True (a matriz é simétrica)