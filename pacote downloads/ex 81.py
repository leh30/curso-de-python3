valor = []
while True:
    valor.append(int(input('Digite o valor: ')))
    cont = str(input('Deseja continuar?[S/N]: ')).strip().upper()
    if cont in 'Nn':
        break
if 5 in valor:
    print('O valor 5 foi digitado na lista!')
else:
    print('O valor 5 não foi digitado na lista!')
print('-='*30)
print(f'Voçe digitou {len(valor)} valores')
valor.sort(reverse=True)
print(f'A lista de valores de forma decrescente foi {valor}')