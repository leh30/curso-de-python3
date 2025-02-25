from math import hypot

cateto = float(input('Digite o valor do cateto:'))
adjacente = float(input('Digite o valor da adjacente;'))

hipotenusa =  hypot( cateto , adjacente)


print('Valor do cateto é {}, o valor do adjacente é {}, eo da hepotenusa é {:.2f}'.format(cateto,adjacente,hipotenusa))
