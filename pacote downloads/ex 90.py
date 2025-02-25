"""pessoa = {'nome': 'gustavo','sexo':'Masculino','idade': 29}
print(f'meu nome é {pessoa["nome"]} sou do sexo {pessoa["sexo"]} tenho {pessoa["idade"]} de idade')
pessoa['nome'] = 'leandro'
pessoa['peso'] = 65,5
del pessoa['sexo']
for k, v in pessoa.items():
    print(f'meu {k} é {v}')"""

'''estado = {}
brasil = []
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'o campo {k} tem valor {v}.')'''

dic = {}
dic['nome'] = str(input(('Qual seu nome? ')))
dic['media'] = float(input('Qual sua media? '))
print('-='*30)
print(f'- Seu nome é igual a {dic["nome"]}')
if dic['media'] <= 5:
    print(f'- Media é igual {dic["media"]}' )
    print('- Voçe esta Reprovado!')

if  dic['media'] > 5 and dic["media"] < 7:
    print(f'- Media é igual a {dic["media"]}')
    print('- Voçe esta de Reculperação!')

if dic['media'] >= 7:
    print(f'- Media é igual a {dic["media"]}')
    print('- Parabens voçe esta Aprovado! ')
print('-='*30)