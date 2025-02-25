sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Comando invalido,digite o sexo novamente [M/F]: ')).strip().upper()[0]
print('Voçe digitou sexo {} resgistrado com susseso'.format(sexo))
print('FIM DO PROGRAMA!')



