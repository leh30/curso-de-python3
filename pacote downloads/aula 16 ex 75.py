valor = int(input('Digite o primeiro valor: ')),int(input('Digite o segundo valor: ')),int(input('Digite oterçeiro valor: ')),int(input('Digite o quarto valor: '))

print(f'Voçe Digitou o valor {valor}')
if 9 in valor:
    print(f'O valor 9 Apareçeu {valor.count(9)} veses no programa')
else:
    print('Valor 9 não foi digitado no programa!')
if 3 in valor:
    print(f'O valor 3 foi digitado na {valor.index(3)+1} posição')
else:
    print('Valor 3 não foi digitado no programa!')
print('Os numeros pares digitados foram ', end=' ')
for n in valor:
   if (n % 2) == 0:
       print(n,end=' ')



