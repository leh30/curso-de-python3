
while True:
    def escreva(ecv):
        tam =len(ecv)+4
        print('~'*tam)
        print(f' {ecv}!')
        print('~'*tam)
    escreva(str(input('Escreva uma flase qualquer: ')))
    while True:
        res = str(input('Deseja continuar[S/N]:')).upper()[0]
        if res in 'SN':
            break
        print('ERRO, apenas S ou N.')
    if res == 'N':
        break
print('FIM DO PROGRAMA!')
