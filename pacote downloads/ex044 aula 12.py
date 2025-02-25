print('{:=^50}'.format('LOJAS LS'))

preco = float(input('Digite o valor do produto: R$'))
print('O preço normal do produto é {} R$'.format(preco))

print('[1] a vista dinheiro, ou cheque 10%')
print('[2] a vista no cartão, 5%')
print('[3] 2x no cartão, preço normal')
print('[4] 3x no cartão, 20% de juros')
a = preco - (preco * 10 / 100)
b = preco - (preco * 5 / 100)
c = preco
d = preco + (preco * 20 / 100)
forma = (input('Forma de pagamento: '))
if forma == '1':
    print('''Voçe escoleu a forma de pagamento a vista com desconto de 10 %.
 Seu produto de {:.2f} R$ ,saira por {:.2f} R$'''.format(preco,a))
elif forma == '2':
    print('''voçe escoleu a forma de pagamento a vista no cartão com  desconto de 5 %.
 Seu produto de {:.2f} R$ ,saira por {:.2f} R% '''.format(preco,b))
elif forma == '3':
    parcela = preco / 2
    print(''' Voçe escoleu a forma de pagamento em 2x no cartão.
 Seu produto de {:.2f} R$ ,saira por 2x de {:.2f} R$ '''.format(preco,parcela))
elif forma == '4':
    parcela = d / 4
    print('''Voçe escoleu a forma de pagamento em 3x no cartão.
Seu produto de {:.2f} R$ , Saira por 4x de {:.2f} R$ '''.format(preco,parcela))
else:
    print('Operação invalida!')




