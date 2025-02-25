tab = 'LAPIS' , 1.00 ,'CANETA', 2.00,'BORRACHA', 1.50,'APORTADOR', 1.70,'ERROREX',3.00,'ESTOJO', 10.00,'MUCHILA',20.00
print('-'*40)
print('TABELA DE PREÇOS!'.center(40))
print('-'*40)
for elemento in range(0,len(tab)):
    if elemento % 2 == 0:
        print(f'{tab[elemento]:.<30}',end=' ')
    else:
        print(f'{tab[elemento]:.2f}')

print('-'*40)