a = b = c =  0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Sexo[M/F]: ')).strip().upper()[0]
    if idade >= 18:
        a = a + 1

    if sexo == "M":
        b = b + 1

    if sexo == 'F' and idade < 20:
        c = c + 1

    res = ' '
    while res not in 'SN':
        res = str(input('Deseja continuar[S/N]: ')).strip().upper()[0]
    if res == 'N':
        break
print(f'Total de pessoas maiores de 18 anos: {a} ')
print(f'Ao todo temos {b} homens cadastrado.')
print(f'E temos {c} mulheres com menos de 20 anos.')