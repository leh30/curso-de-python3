
frase = str(input('Escreva uma frase:')).upper().strip()
print('A letra A apareceu {} veses na frases'.format(frase.count('A')))
print('A letra A parece na {} posição'.format(frase.find('A')+1))
print('A letra A parece na {} posição'.format(frase.rfind('A')+1))