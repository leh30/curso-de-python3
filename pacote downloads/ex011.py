largura = float(input('Digite a largura da parede:'))
altura = float(input('Digite a altura da parede:'))

cal = largura * altura
print('Sua parede tem a dimensão de {} x {} e sua area quadrada é {:.3f} m2'.format(largura,altura,cal))

tinta = cal / 2


print('Para pintar essa parede voçe preçisa de {:.3f} m2 litros de tinta.'.format( tinta))