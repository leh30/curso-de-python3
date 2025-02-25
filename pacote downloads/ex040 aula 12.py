nota1 = float(input('Digite sua primeira nota:'))
nota2 = float(input('Digite sua segunda nota:'))
media =(nota1 + nota2) / 2

if media < 5:
    print('Voçe foi reprovado com media {}'.format(media))
elif  media >= 5 and media < 7:
    print('Voçe esta de recuperação com media {}'.format(media))
elif media >  7:
    print('Voçe foi aprovado com a media {}'.format(media))