r1 = float(input('Digite o complimento da primeira reta:'))
r2 = float(input('Digite o complimento da segunda reta:'))
r3 = float(input('Digite o complimento da terçeira:'))

if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:
    print('Sim forma um triangulo')

else:
    print('Não forma um triangulo')