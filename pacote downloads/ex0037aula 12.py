
print('''Escolha uma das base para converte
[1] converte para BINARIO
[2] converte para OCTAL
[3] converte para HEXADECIMAL''')
numero = int(input('Digite o numero que voçe deseja tensforma:'))
opção = int(input('Sua opção'))
if opção == 1:
    print('{} Convertido para binario é {}'.format(numero,bin(numero)[2:]))
elif opção == 2:
    print('{} Convertido para octal é {}'.format(numero,oct(numero)[2:]))
elif opção == 3:
    print('{} Convertido para hexadecimal é {}'.format(numero,hex(numero)[2:]))
else:
    print('opção invalida')
