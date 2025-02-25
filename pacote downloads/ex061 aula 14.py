termo = int(input('Digite o termo:'))
razao = int (input('Digite a razao: '))
n = termo
cont= 1
while cont <= 10 :
    print('{}-'.format(n),end='')
    n = n + razao
    cont= cont + 1
print('FIM')

