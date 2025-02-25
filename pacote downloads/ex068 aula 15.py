from random import randint
computador=randint(0,11)
escolha = 'PAR IMPAR'
n = 0

while True:
    escolha = str(input('Qual voçe desseja[PAR OU IMPAR]: ')).upper()
    n = int(input('Digite o numero de [0 a 10]: '))
    if escolha == 'PAR':
        soma = computador + n
        print( 'VOÇE ESCOLEU PAR')
        print(f'o computador digitou {computador}')
        print(f'a soma foi {soma}')
        if soma % 2 == 0:
            print('VOÇE VENCEU!')

        else:
            print('VOÇE PERDEU COMPUTADOR VENCEU')
            break
    if escolha == 'IMPAR':
        soma = computador + n
        if soma % 2 != 0:
            print('VOÇE VENCEU')
            print(f'O computador escoleu par , eo numero {computador} a soma do dois numeros foi {soma}')
            break
        else:
            print('voçe perdeu')
            print(f'O computador escoleu par, eo numero {computador}  a soma do dois numeros foi {soma}')

