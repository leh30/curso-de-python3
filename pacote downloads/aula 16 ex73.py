cont = 0
print('TABELA CAMPEONATO BRASILEIRO')
print('-='*20)
colocacao = 'palmeiras','vasco','sao paulo','atletico','chapecoense','corintheans','santos','flamengo','cruzeiro','goias','america','atletico_mg','botafogo','novo horizontino','cuiaba','bahia','bragantino','fortaleza','juventude','gremio'
for c in colocacao:
    cont = cont+1
    print(cont,'º',c)
print('-='*20)
print(f'OS 5 PRIMEIROS COLOCADOS SÃO',colocacao[:5])
print('-='*20)
print(f'OS 4 ÚLTIMOS COLOCADOS SÃO',colocacao[-4:])
print('-='*20)
print(f'LISTA DE TIMES POR ONDEM ALFABÉTICA ',sorted(colocacao))
print('-='*20)
print(f'OS CLUBE DO CHAPECOENSE ESTA POSIÇÃO',(colocacao.index('chapecoense')+1),'º')