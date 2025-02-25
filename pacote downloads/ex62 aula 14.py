termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
n = termo
cont = 1
total = 0
mais  = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{}-'.format(n),end='')
        n = n + razao
        cont= cont + 1
    print('PAUSA')
    mais = int(input('Quantos termos voçe deseja a mais? '))
print('PROGRESSÃO FINALIZADA COM {} TERMOS MOSTRADO'.format(total))




