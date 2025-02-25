dados = {}
guar = []
soma = media = 0
while True:
    dados.clear()
    dados['nome'] = str(input('Nome: '))
    while True:
        dados['sexo'] = str(input('Sexo[M/F]: ')).upper()[0]
        if dados['sexo'] in 'MF':
            break
        print('ERRO,Por favor ,digite apenas M ou F.')
    dados['idade'] = int(input('Idade: '))
    soma = soma + dados['idade']
    guar.append(dados.copy())
    while True:
        res = str(input('Deseja continuar?[S/N]: ')).upper()[0]
        if res in 'SN':
            break
        print('ERRO, Responda S ou N.')
    if res == 'N':
        break
media = soma / len(guar)
print('-='*20)
print(f'A - Foram {len(guar)} cadastradas.')
print('-='*20)
print(f'B - A media de idade é {media:.2f}')
print('-='*20)
print('C - As mulheres foram ', end= '')
for g in guar:
    if g['sexo'] == 'F':
        print(f'{g["nome"]}',end=' ')
print()
print('-='*20)
print('D - As pessoas acima da media foram ',end=' ')
for g in guar:
    if g['idade'] > media:
        print(f'{g["nome"]}',end=' ')
print()