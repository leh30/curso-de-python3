from math import radians,sin,cos,tan

angulo = float(input('Digite o valor do angulo:'))
seno = sin(radians(angulo))
cosseno= cos(radians(angulo))
tangente = tan(radians (angulo))

print('O seno é {:.2f},O cosseno é {:.2f}, O tangente é{:.2f}'.format(seno,cosseno,tangente))