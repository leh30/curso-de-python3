valor = []
for cont in range(0,5):
    numero = int(input('Digite o valor: '))
    if cont == 0 or numero > valor[-1]:
        valor.append(numero)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(valor):
           if numero <= valor[pos]:
               valor.insert(pos,numero)
               print(f'Adicionado na posição {pos} da lista...')
               break
           pos = pos + 1
print('-='*30)
print(f'Esses os numeros de forma ondenada! {valor}')
