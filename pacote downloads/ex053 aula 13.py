
frase = str(input('Digite a  fase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso =junto[::-1]
print('o inverso de {} é {}'.format(junto,inverso))
if inverso == junto:
    print('Temos um palinmetro')
else:print('A frase nao é palinmetro')