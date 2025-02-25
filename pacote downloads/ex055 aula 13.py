maior = 0
menor = 0
for c in range(1,6):
    peso = int(input('Qual é o {}° peso kg: '.format(c)))
    if c ==1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso é {}'.format(maior))
print('O menor peso é {}'.format(menor))





print('FIM DO PROGRAMA')
