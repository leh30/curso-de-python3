galera = []
dado = []
maior = menor  = 0

while True:
    dado.append(str(input('Qual seu nome: ')))
    dado.append(float(input('Qual seu peso: ')))
    if len(galera) == 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        if dado[1] < menor:
            menor = dado[1]

    galera.append(dado[:])
    dado.clear()
    res = str(input(('Deseja continuar[S/N]: '))).strip().upper()

    if res == 'N':
        break
print(f'As pessoas cadastradas forarm {galera}!')
print(f'Foram {len(galera)} pessoas cadastrada!')
print(f'O maior peso digitado foi {maior} KG, e foi de ' ,end='')
for p in galera:
    if p[1] == maior:
        print(f'{p[0]} ', end='')
print()
print(f'O menor peso digitado foi {menor} KG, e foi de ', end='')
for p in galera:
    if p[1] == menor:
        print(f'{p[0]}!')
print()
