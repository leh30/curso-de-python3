n = int(input('Verificar se é numero primo:'))
cont = 0
for c in range(1,n+1):
    if n % c == 0:
        print('\033[34m',end=' ')
        cont=  cont + 1
    else:
        print('\033[33m',end=' ')
    print('{}'.format(c),end=' ')
print('\n\033[m0 numero {} foi divisivel {} vezes'.format(n,cont))
if  cont== 2:
    print('O numero {} é primo'.format(n))
else:
    print('O numero {} não é primo'.format(n))



