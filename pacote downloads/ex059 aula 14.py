n = 1
print('**** Escola a opção do menu ****')
print('''[1] somar
[2] multiplicar
[3] maior
[4] novos numeros
[5] sair do programa''')
while n :
    v = int(input('Digite o primeiro valor:'))
    v1 = int(input('Digite o sengundo valor: '))
    menu = int(input('Qual é a opção: '))
    if menu == 1:
        soma = v + v1
        print('A soma do valores foi {}'.format(soma))
    elif menu == 2:
        mul = v * v1
        print('A multiplicação dos valores foi {}'.format(mul))
    elif menu == 3:
        if v > v1:
            print('Maior numero é {}'.format(v))
        if v1 > v:
            print('Maior numero é {}'.format(v1))
    elif menu == 4:
        print('Novo numero')
    else:
        menu == 5
        print('Saindo do programa')
    print('Fim do pograma')




