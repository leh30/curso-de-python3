
from  datetime import date
atual = date.today().year
cont = 0
cont1 = 0
for c in range(1,8):
    idade = int(input('Digite a {}° ano de nacimento: '.format(c)))
    ano = atual - idade
    if ano >= 21:
        cont = cont + 1
    elif ano < 21:
        cont1 = cont1 + 1

print('{} pesssoa maior de idade'.format(cont))
print('{} pessoas menor de idade'.format(cont1))


print('Fim de programa')