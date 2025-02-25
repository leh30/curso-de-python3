from datetime import date
ano = int(input('Qual seu ano de nacimento?' ))
media = (2024 - ano)
cal =  media - 18
cal1 = 18 - media
if media < 18 :
    print('''Por enquanto voçe não vai se alistar.
    Falta {} anos para seu alistamento'''.format(cal1))
elif media == 18:
    print('Agora é a hora de vpçe se alistar.')
elif media > 18:
    print('''Já pasou do tempo do alistamento.
    Se passou {} anos do seu alistamento'''.format(cal))