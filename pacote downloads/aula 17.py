'''num = [2,3,8,9]
num [0] = 7
num.append(10)
num.sort()
num.sort(reverse=True)
num.insert(2,3)
if 11 in num:
    num.remove(11)
else :
    print('Não achei o numero 11')
print(num)
print(f'Essa lista tem {len(num)} elementoas')'''

'''valor = []
valor.append(1)
valor.append(4)
valor.append(3)
valor.append(77)
for v in valor:
    print(f'{v} ...',end= '|')'''

'''valor =[]
for cont in range(0,5):
    valor.append(int(input('Digite o valor:')))
for c, v in enumerate(valor):
    print(f'Na posição {c +1} encontre o valor {v}!')
print('FIM DA LISTA!')'''

a = [1,2,3,4]
b = a[:]
b[2] = 8
print(f'lista A:  {a}')
print(f'lista B   {b}')