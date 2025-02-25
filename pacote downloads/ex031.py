
  distancia = float(input('Digite a distaçia percorrida:'))
print('Voçe esta preste a começar uma viagem de {} km'.format(distancia))
if distancia <= 200:
    soma1 = distancia * 0.50
    print('Valor por km rodado {}'.format(soma1))
else:
    soma2 = distancia * 0.45
    print('Valor percorri'
          'do para viagem mais lonhga é {}'.format(soma2))