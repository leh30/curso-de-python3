'''print('############# BANCO CURSO VIDEO ###########')

valor = int(input('Qual valor voçe deseja sacar? R$ '))
a = valor / 50
b = (valor % 50) / 20
c = (valor % 20) /10
d = (valor % 10) / 1
print(f'Total de {a:.0f} cédula de 50 R$')
print(f'Total de {b:.0f} cédula de 20 R$ ')
print(f'Total de {c:.0f} cédula de 10 R$')
print(f'Total de {d:.0f} cédula de 1 R$')

print('Volte sempre ao BANCO CURSO VIDEO! Tenha um bom dia!')'''

valor = int(input('Digite o valor a ser sacado? '))
ced = 50
cont = 0
total = valor

while True:
    if total >= ced:
        total -= ced
        cont += 1
    else:
        if cont > 0:
            print(f'total de {cont} cedula de R$ {ced}')
        if ced == 50:
             ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        con = 0
        if total == 0:
            break


