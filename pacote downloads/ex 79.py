valor =[]
cont = ' '
while True:
    n = int(input('Digite o valor:'))
    if n not in  valor:
        valor.append(n)
    else:
        print(f'Numero {n} duplicado! Não sera adicionado na lista!')
    cont=str(input('Deseja continuar[S/N]: ')).strip().upper()
    if cont == 'N':
        break
print(f'Os valores da lista foram {valor}')
print(f'OS VALORES EM ONDER CRECENTE FORÃO {sorted(valor)}')
print('FIM DO PROGRAMA!')

