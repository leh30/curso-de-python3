nome = str(input('Qual é seu nome?'))
if nome == 'gustavo':
   print('Que lindo seu nome {}'.format(nome))

elif nome == 'joao' or 'maria' or 'mario' or 'jose':
    print('Seu nome é muito normal {}.'.format(nome))

else:
    print('SEu nome é comum {}'.format(nome))

print('Tenha um bom dia {} !'.format(nome))