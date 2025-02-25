'''from random import randint
numeros = [[],[],[]]

def sorteia(num):
    for valor in range(1,6):
        numeros[0].append(randint(1,10))

sorteia(numeros[0])
print(f'Sorteado 5 valores da lista {numeros[0]} PRONTO!')

def somapar(num):
    for valor in numeros[0]:
        if valor % 2 == 0:
            numeros[1].append(valor)
    numeros[2].append( sum(numeros[1]))
somapar(numeros[1])
print(f'A soma dos falores pares de {numeros[1]}, temos {numeros[2]}')'''

from random import randint

def sorteia(lista):
    print('sorteando 5 valores da lista:',end=' ')
    for valor in range(1,6):
        n= randint(1,10)
        lista.append(n)
        print(f'{n}',end=' ')
    print('PRONTO!')
def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma = soma + valor
    print(f'Somando os valores pares de {lista}, temos {soma}')
numeros = []
sorteia(numeros)
somapar(numeros)