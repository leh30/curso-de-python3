pro = float(input ('Digite o preço do produto:'))

des = pro - (pro * 5 / 100)


print('Seu produto de R$: {} reai, com o desconto de 5% fica  R$: {:.2f}% .'.format(pro,des))