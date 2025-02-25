from datetime import datetime
from time import sleep
dicionario = {}

dicionario['nome'] = str(input('NOME:'))
dicionario['ano'] = int(input('ANO DE NACIMENTO:  '))
dicionario['idade'] = (datetime.now().year-dicionario['ano'])
dicionario['carteira'] = int(input('CARTEIRA DE TRABALHO (0 NÃO TEM): '))
if dicionario['carteira'] == 0:
    print('-='*20)
    for k, v in dicionario.items():
        print(f'- {k} o valor {v}')
        sleep(1)
dicionario['aponsetadoria'] = (dicionario['idade'] + 35)
if dicionario['carteira'] != 0 :
    dicionario['contratacao'] = int(input('ANO DE CONTRATAÇÃO: '))
    dicionario['salario'] = float(input('SALARIO: R$ '))
    print('-='*20)
    for k , v in dicionario.items():
        print(f'- {k} tem o valor {v}')
        sleep(1)
print('-='*20)