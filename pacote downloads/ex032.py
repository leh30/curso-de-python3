from datetime import date

ano= int(input('Digite o ano escolido para a verificação:'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100!= 0 or ano % 400 == 0:
    print('sim o ano {} é bissexto!'.format(ano))

else:
    print('O ano {} Nao é bissexto!'.format(ano))