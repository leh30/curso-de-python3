'''total = maiormil = cont = menor = 0
barato = ' '
while True:
    nome = str(input('Qual o nome do produto? '))
    preco = float(input('Qual o preço do produto? R$ '))
    total = total + preco
    cont = cont + 1
    if preco > 1000:
        maiormil = maiormil + 1
    if cont == 1:
        menor = preco
        barato = nome
    else:
        if preco < menor:
            menor = preco
            barato = nome

    res = ' '
    while res not in 'SN':
        res = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if res == 'N':
        break

print('FIM DO PROGRAMA!')
print(f'O total gasto da compra foi {total} R$.')
print(f'Ouveram {maiormil} produtos que foram maior de 1000 R$ ')
print(f'O nome do produto mais brato foi {barato},seu preço foi de {menor} R$.')'''

total = mil = cont = menor = 0
barato = ' '
while True:
    nome = str(input('Qual o nome do produto? '))
    preco = float(input('Qual o preço do produto? '))
    total = total + preco
    cont = cont + 1
    if preco > 1000:
        mil = mil + 1
    if cont == 1:
        menor = preco
        barato = nome
    else:
        if  preco < menor:
            menor = preco
            barato = nome
    res = ' '
    while res not in 'SN':
        res = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]

    if res == 'N':
        break
print('FIM DE PROGRAMA!')
print(f'O total da compra foi {total} R$')
print(f'Foram {mil}, produtos acima de 1000 R$.')
print(f'O nome do produto mais barato é {barato},e seu valor é {menor} R$.')