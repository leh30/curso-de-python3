lista = []
lista1 = []
lista2 =[]
while True:
    numero = int(input('Digite o numero: '))
    res = str(input('Deseja continuar?[S/N]:')).strip().upper()
    lista.append(numero)
    if numero % 2 == 0:
        lista1.append(numero)
    else:
        lista2.append(numero)
    if res in 'Nn':
        break
print('-='* 30)
print(f'Os numeros digitados foram {lista} !')
print(f'Os numeros pares digitados foram {lista1} !')
print(f'Os numeros impares digitados foram {lista2} !')
print('-='*30)