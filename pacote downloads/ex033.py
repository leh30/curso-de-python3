a = int(input('Digite primeiro numero:'))
b = int(input('Digite o segundo numero:'))
c = int(input('Digete o terceiro numero:'))

menor = a

if b < a and b < c:
    menor = b

if c < a and c < b:
    menor = c
# verificando o maior
maior = a
if b > a and b > c:
    maior = b
if  c > a and c > b:

    maior = c

print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))




