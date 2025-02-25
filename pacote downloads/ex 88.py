'''from random import randint
from time import sleep
lista = list()
jogos = list()

print('-='*30)
print('                    JOGO DA MEGA SENA!      ')
print('-='*30)
valor = int(input('Quantas jogos sera gerado?  '))
tot = 1
while tot <= valor:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont = cont+1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot = tot + 1
print('-='*3,f'SORTEANDO {valor} JOGOS ','-='*3)
for i , l in enumerate(jogos):
    print(f'jogo {i+1} {l}')
    sleep(2)'''

from random import randint
print('-='*5,'PALPITES JOGOS DA MEGA SENA!','-='*5)
lista = []
jogo =[]
tot = 1
quar = int(input('Quantos jogos deseja gerar? '))
while tot <= quar:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont = cont + 1
        if cont >= 6:
            break

    lista.sort()
    jogo.append(lista[:])
    lista.clear()
    tot = tot + 1
print('-='*3,f'SORTEANDO {quar} JOGOS ','-='*3)
for i , l in enumerate(jogo):
    print(f'JOGOS {i+1}:{l}')
