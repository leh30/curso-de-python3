salario = float(input('Digite o valor do seu salario:'))
print('Seu salario atual é de {:.2f} reais '.format(salario))

almento1 =(salario * 10 / 100) + salario
almento2 =(salario * 15 / 100) + salario
if salario >= 1.250:
    print('Voçe resebel um almento de 15 %, com o ajuste voçe passa a ganhar {:.2f}'.format(almento2))

else:
    print('Voçe resebel um almento de 10 %, com o ajuste vc passa a ganhar {:.2f} rais'.format(almento1))
