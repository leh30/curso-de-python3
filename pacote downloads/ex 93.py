'''dados = {}
partidas = []
dados['nome'] = str(input('Nome do jogador? '))
tot = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
print('-='*20)
soma = 0
for c in range(0,tot):
    partidas.append( int(input(f'Quantos gols na {c+1}° partida? ')))

dados['gols'] = partidas[:]
dados["total"] = sum(partidas)
print('-='*20)
print(dados)
print('-='*20)
for k, v in dados.items():
    print(f'O campo {k} tem o valor de {v}.')
print('-='*20)
print(f'O jogador {dados["nome"]} jogou {tot} partidas.')
for i, v in enumerate(dados['gols']):
        print(f'=> Na partida {i+1}, fez {v} gols. ')
print(f'Foi um total de {dados["total"]} gols.')
print('-='*20)'''''

dados = {}
partidas = []
dados['nome'] = str(input("Nome do jogador? "))
tot = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
for c in range(0,tot):
    partidas.append(int(input(f"Quantos gols na {c+1}° partidas? ")))
dados['gols'] = partidas[:]
dados['total'] = sum(dados["gols"])
print('-='*20)
print(dados)
print('-='*20)
for k, v in dados.items():
    print(f'O compo {k} tem o valor {v}.')
print('-='*20)
print(f'O jogador {dados["nome"]} jogou {tot}.')
for c, i in enumerate (dados["gols"]):
    print(f'=> Na {c+1}° partida, fez {i}.')
print('-='*20)