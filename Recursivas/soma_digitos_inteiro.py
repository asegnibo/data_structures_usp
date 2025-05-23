# Implemente uma função recursiva que calcule a soma dos dos dígitos de um número inteiro positivo.
n= 123456789
def soma_dig(numero):
    if numero < 10:
        return numero
    else:
        return (numero % 10) + soma_dig(numero//10)
    
print(soma_dig(n))