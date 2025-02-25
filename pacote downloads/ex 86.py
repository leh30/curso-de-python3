'''matris = []
for c in range(1,10):
    matris.append(int(input(f'Digite {c}° elementos da matris: ')))
print([matris[0]] ,[matris[1]] ,[matris[2]])
print([matris[3]] ,[matris[4]] ,[matris[5]])
print([matris[6]] ,[matris[7]] ,[matris[8]])'''


# versão do guanabara
matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for c in range(0,3):
       matriz[l] [c] = int(input(f'Digite um valor para [{l},{c}]: '))
print('-=' *30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
    print()
