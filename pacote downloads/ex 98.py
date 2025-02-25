from time import sleep
print('-='*20)
def contador(*num):
    for v in num:
        print(v,end=' ')
        sleep(0.5)
    print()
print('contagem de 1 até 10 de 1 em 1.')
contador(1,2,3,4,5,6,7,8,9,10,'FIM!')
print('-='*20)
print('Contagem de 10 até 0 de 2 em 2.')
contador(10,8,6,4,2,0,'FIM!')
print('-='*20)
print('Agora é sua vez de personalizar a contagem!')

inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
if passo == 0:
    passo = + 1
def contado(*lst):
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}.')

    for v in range(inicio,fim,passo):
        print(v,end=' ')
        sleep(0.5)
    print('FIM!')

print('-='*20)
contado(inicio,fim,passo)