dados = {}
partidas = []
time = []
while True:
    dados.clear()
    dados['nome'] = str(input("Nome do jogador? "))
    tot = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
    partidas.clear()
    for c in range(0,tot):
        partidas.append(int(input(f"Quantos gols na {c+1}° partidas? ")))
    dados['gols'] = partidas[:]
    dados['total'] = sum(partidas)
    time.append(dados.copy())
    while True:
        res = str(input('Deseja continuar?[S/N]')).upper()[0]
        if res in 'SN':
            break
        print('ERRO, apenas S/N.')
    if res == 'N':
        break
print('-='*20)
print('cod ', end='')
for i in dados.keys():
    print(f'{i:<15}', end='')
print()
print('-='*20)
for k, v in enumerate(time):
    print(f'{k:>3}',end=' ')
    for d in v.values():
        print(f'{str(d):<15}',end=' ')
    print()
print('-='*20)
while True:
    busca = int(input('Mpstrar o nome de qual jogador?(999 para parar)'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO, Não existe jogador com o codigo da {busca}!')
    else:
        print(f'-- Levantamento do jogador {time[busca]["nome"]}')
        for i, g in enumerate(time[busca]["gols"]):
          print(f'    No jogo {i} fez {g} gols.')
    print('-='*20)
print('<< volte sempre >>')
