numero = 0
cont = 0
contagem = 'ZERO','UM','DOIS','TRES','QUATRO','CINC0','SEIS', 'SETE','OITO','NOVE','DEZ','ONZE','DOZE','TREZE','QUATORZE','QUINZE','DEZESEIS','DEZESETE','DEZOITO','DESENOVE','VINTE',
while True:
    numero = int(input('Qual numero desseja escoler [0/20]: '))
    if 0 <=numero <= 20:
        break
    print('TENTE NOVAMENTE!', end='')
print(f'Voçe digitou o numero',contagem[numero])
while True:
    cont = str(input('Deseja continuar?[S/N]: ')).strip().upper()[0]
    if cont == 'S':
        numero = int(input('Qual numero desseja escoler [0/20]: '))
        print(f'Voçe digitou o numero', contagem[numero])
    elif cont == 'N':
        break







