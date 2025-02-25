casa = float(input('Qual valor da casa?'))
salario = float(input('Qual seu salario?'))
anos = int(input('Quantos anos voçe irar pagar?'))
prestacao = casa / (anos * 12)
print('valor da casa de {:.2f} r$ e o valor da prestação é de {:.2f} r$' .format(casa,prestacao))

if prestacao > (salario * 30 / 100):
    print('Voçe não poderar fazer o vinançiamento passou de 30% do seu salario ')
else:
    print('Vinançiamento aprovado, parabens!')