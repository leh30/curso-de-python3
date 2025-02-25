num = 0
cont = 0
soma = 0
num = int(input('Digite um numero [999 para parar]: '))
while num != 999:
    cont = cont + 1
    soma = soma + num
    num = int(input('Digite um numero [ 999 para parar]: '))
print('Voçe digitou {} numeros e a soma dos numero foi {}'.format(cont,soma))
