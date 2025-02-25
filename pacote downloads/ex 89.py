'''ficha = []
while True:
    nome = str(input('NOME: '))
    nota1 = float(input('NOTA 1: '))
    nota2 = float(input('NOTA 2: '))
    media = (nota1 + nota2)/2
    ficha.append([nome,[nota1,nota2],media])
    res = str(input('Deseja continuar?[S/N]: ')).strip().upper()
    if res in 'N':
        break

print('-='*20)
print('         LISTA DE NOTAS E MEDIAS DOS ALUNOS')
print(f'{"N.":<4}{"NOTAS":<10}{"MEDIAS":<10}')
for i, a in enumerate(ficha):
    print(f'{i} {a[0]:<4} {a[1]} {a[2]}')
print('-='*20)
while True:
    op = int(input('Deseja ver algum aluno?[999 para]: '))
    if op <= len(ficha)-1:
        print(f'Notas {ficha[op][0]}, são {ficha[op][1]}, media {ficha[op][2]}.')
    if media < 5:
        print(f'{ficha[op][0]} REPROVADO (a)!')
    else:
        print('APROVADO!')
    if op ==  999:
        break'''

ficha= []
while True:
    nome = str(input('NOME: '))
    nota1 = float(input('NOTA: '))
    nota2 = float(input('NOTA: '))
    res = str(input('Deseja continuar?: '))
    media = (nota1 + nota2)/2
    ficha.append([nome,[nota1,nota2],media])
    if res in 'Nn':
        break
print('-='*20)
print('NO. NOME   MÉDIA')
print('-'*25)
for i , a in enumerate(ficha):
    print(f'{i} {a[0]}  {a[2]:.2f} ')
print('-'*20)
while True:
    op = int(input('Motrar a nota de qual aluno[999 para]: '))
    if op <= len(ficha)-1:
        print(f'As notas de {ficha[op][0]}, são {ficha[op][1]}')
    if op == 999:
        print('FIM DO PROGRAMA!')
        break

