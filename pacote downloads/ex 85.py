valor = [[],[]]
num = 0
for c in range(1,8):
    num = int(input(f'Digite os {c}° valores: '))
    if num % 2 == 0:
        valor[0].append(num)
    else:
        valor[1].append(num)
print('*'*40)
print(f'Os numeros pares digitados foram {sorted(valor[0])}!')
print(f'Os numeros impares digitados foram {sorted(valor[1])}!')
print('*'*40)