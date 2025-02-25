'''from random import randint
from time import sleep
from operator import itemgetter
res = {'jogador1': randint(1,6),
       'jogador2': randint(1,6),
       'jogador3': randint(1,6),
       'jogador4': randint(1,6)}
ranking =[]
for k, v in res.items():
    print(f'{k} tirou {v} no dado.')
    sleep(2)
print('-='*20)
ranking =sorted(res.items(),key=itemgetter(1),reverse=True)
print('== RANKING DO JOGADORES ==')
for i , v in enumerate(ranking):
    print(f'{i+1}° {v[0]} com {v[1]}.')
    sleep(2)
print('-='*20)'''

from random import randint
from time import sleep
from operator import itemgetter
res = {'jogador 1': randint(1,6) ,
       'jogador 2': randint(1,6),
       'jogador 3': randint(1,6),
       'jogador 4': randint(1,6)}
ranking = list()
print('Valores sorteados!')
for k, v in res.items():
    print(f'O jogador {k} sorteo {v}!')
    sleep(2)

ranking = sorted(res.items(), key=itemgetter(1),reverse=True)
print('-='*30)
print('    -= RANKING =-')
for i, v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}.')
    sleep(2)