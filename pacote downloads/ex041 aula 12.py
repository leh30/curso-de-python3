from datetime import date
atual = date.today().year
ano = int(input('Digite o ano de nacimento:'))
media = atual - ano
print('Por voçe tem {} anos'.format(media))
if media <=9:
    print('voçe esta nivel mirim ')
elif media <=14:
    print('Voçe esta no nivel infantil')
elif media <=19:
    print('Voçe esta no nivel junil')
elif media <=25:
    print('Voçe esta no nivel senior')
else:
    print('Voçe esta no nivel master')
