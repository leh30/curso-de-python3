n = 0
calculo = 0
while True:
    n = int(input('Digite o numero que deseja ver a TABUADA: '))
    print('*'*30)
    if n < 0:
        break
    for c in range(0,11):
        calculo = c * n
        print(f'{c} x {n} = {calculo}')
    print('*'*30)
print('FIM DO PROGRAMA!\n OBRIGADO!')



