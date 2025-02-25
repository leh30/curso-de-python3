import random
cont = 0
numero_aleatorio = random.randint(0,11)
print('******* Jogo comtra o computador *******')
c = 1
while c < 10:
    n = int(input('DIgite um numero de 0 a 10 para jogar contra o computador: '))
    if n != numero_aleatorio:
        print('Voçe ERROU!!')
    else:
        cont = + 1
        print('Voçe ACERTOU!')
        print('Foram {} tentativa'.format(cont))
print('FIM DO JOGO!')