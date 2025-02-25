pessoas = {'nome':'leandro','sexo':'Masculino','idade':30}
print(f'{pessoas["nome"]} é do sexo {pessoas["sexo"]} tem {pessoas["idade"]} anos de idade!')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
#del pessoas['sexo']
pessoas['nome'] = 'gustavo'
pessoas['peso'] = 63.5
for k, v in pessoas.items():
    print(f'{k} = {v}')

'''brasil = []
estado1 = {'uf':'rio de janeiro','sigla':'rj'}
estado2 = {'uf':'são paulo','sigla':'sp'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0]['uf'])
print(brasil[1]['sigla'])'''

estado = {}
brasil = []
for c in range(0,3):
    estado['uf'] = str(input('Unidasde federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
print(brasil)