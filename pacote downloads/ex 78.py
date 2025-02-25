'''valor =[]
for cont in range(0,5):
    valor.append(int(input(f'Digie o valor na posição {cont}:')))
for c, v in enumerate(valor):
    print(f'Na posição {c} en contrei o valor {v}!')
print(f'O maior valor digitado foi {max(valor)} na posição {c}!')
print(f'O menor valor digitado foi {min(valor)} na posição {valor.index(min(valor))}!')'''

# gustavo guanabara
listanum =[]
maior = 0
menor = 0
for cont in range(0,5):
    listanum.append(int(input('Digite o valor: ')))
    if cont  == 0:
        maior = menor = listanum[cont]
    else:
        if listanum[cont] > maior:
            maior = listanum[cont]
        if listanum[cont] < menor:
            menor = listanum[cont]
print(f'Voçe digitou os valores {listanum} na lista!')
print(f'O maior valor da lista digitado foi {maior} na posição ' ,end='')

for c, v in enumerate(listanum):
    if v == maior:
        print(f'{c}...',end='')
print()
print(f'O menor valor digitado da lista foi {menor} na posição ',end='')
for c, v in enumerate(listanum):
    if v == menor:
        print(f'{c}...',end='')
print()
