
r1 = float(input('Digite a primeira reta:'))
r2 = float(input('Digite a segunda reta:'))
r3 = float(input('Digite a terceira reta:'))
forma =  r1+r2 > r3 or r2+r3 > r1 and r1+r3 > r2

if forma and r1 == r2 and r3:
    print('forma triangul, equilatero, lados são iguais')
elif forma and r1 == r2 or r2 == r3 or r1 ==r3:
    print('forma um triangulo,isóscelas dois lados iguais')
elif forma and r1 != r2  and r2 != r3 and r1 != r3:
    print(' forma um triangulo triangulo, escaleno todos os lados diferentes')
else:
    print('Não form um triangulo')

