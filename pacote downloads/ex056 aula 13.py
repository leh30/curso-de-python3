soma = 0
maior = 0
maioridadehomem = 0
nomevelho = ''
totalmulher = 0
for c in range(1,5):
    nome = str(input('Qual é seu nome:')).strip()
    idade = int(input('Qual é sua idade '))
    sexo = str(input('Qual seu sexo:'))
    soma = soma + idade
    media = soma / 4
    if c == 1 and sexo == 'masculino':
        idade == 1
        maior = idade
        nomevelho = nome
    if sexo in 'masculino' and idade > maior:
        maior = idade
        nomevelho = nome
        if sexo in 'feminino 'and idade < 20:
            totalmulher = totalmulher + 1

print('A media de idade do grupo é de {}'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(maior,nomevelho))
print('O total são {} mulheres com menos de 20 anos '.format(totalmulher))










