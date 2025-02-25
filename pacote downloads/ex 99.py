from time import sleep
def maior(*num):
    print('-='*20)
    print('Análisando os valores passado...')
    cont = maior = 0
    for valor in num:
        print(f'{valor}', end=' ')
        sleep(0.5)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
              maior = valor
        cont = cont + 1
    print(f'Foram informados {cont} valores ao todos.')
    print(f'O maior valor informado foi {maior}.')
    sleep(0.5)
# programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
