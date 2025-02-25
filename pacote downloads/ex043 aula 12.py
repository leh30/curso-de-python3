peso = float(input('Qual é seu peso? (kg) '))
altura = float(input('Qual sua altura? (m) '))

media = peso / altura**2
print('Seu IMC é {:.1f}'.format(media))
if media <= 18.5:
    print('Abaixo do peso')
elif media <= 25:
    print('peso ideal')
elif media <= 30:
    print('Sobrepeso')
elif media <= 40:
    print('Obesidade')
else:
    print('Obesidade morbida')