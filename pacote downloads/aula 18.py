'''teste = list()
teste.append('gustavo')
teste.append(40)
galera =list()
galera.append(teste[:])
teste[0] = 'maria'
teste[1] = 22
galera.append(teste[:])
print(galera)'''

'''galera =[['joão',19],['maria',22],['joaquim',40],['ana',20]]
for pessoa in galera:
    print(f'Meu nome é {pessoa[0]} e tenho {pessoa[1]} de idade!')'''

galera = []
dado = []
maior = menor = 0
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade!')
        maior= maior + 1
    else:
        print(f'{p[0]} é menor de idade!')
        menor = menor +1

print(f'Temos {maior} pessoas maior de idade e {menor} pessoas menor de idade!')