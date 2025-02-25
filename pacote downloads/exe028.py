import random

numero_aleatorio= random.randint(0 ,5)
numero=int(input('Digite o numero escolido:'))
print('Voçe escoleu o numero {}'.format(numero))


if numero_aleatorio == numero:
    print('Parabens voçe acerto')

else:
    print('Voçe errou')



