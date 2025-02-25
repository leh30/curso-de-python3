'''matriz =[[0,0,0],[0,0,0],[0,0,0]]
spar = maior = slinha = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite o valor para [{l},{c}] : '))
print('-='*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
        if matriz[l][c] % 2 == 0:
            spar = spar + matriz[l][c]
    print()
print('-='*30)
print(f'A somas dos numeros pares foram {spar}')
for l in range(0,3):
    slinha = slinha + matriz[l][2]
print(f'A soma dos valores da terçeira coluna foram {slinha}')
for c in range(0,3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]

print(f'O maior valor da segunda coluna foi {maior}')'''

matriz =[[0,0,0],[0,0,0],[0,0,0]]
par = scol = maior = 0
for c in range(0,3):
    for l in range(0,3):
        matriz[c][l] = int(input(f'Digite os valores para [{c} {l}]: '))
for c in range(0,3):
    for l in range(0,3):
        print(f'[{matriz[c][l]:^5}]',end='')
        if matriz[c][l] % 2 == 0:
            par = par + matriz[c][l]

    print()
print(f'A soma de todos os valores pares digitado foram {par}.')
for l in range(0,3):
    scol = scol + matriz[l][2]
print(f'A soma de todos os numeros da coluna foi {scol}.')
for c in range(0,3):
    if c == 0:
        maior = matriz[c][1]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior numero da segunda linha foi {maior}.')