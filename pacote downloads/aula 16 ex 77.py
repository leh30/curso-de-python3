nome = 'MARIA','JOAO','LETICIA','LUIDE','LUCAS','ELOA','STEFANY','LEANDRO','MARIO','MARCELO'
for palavra in nome:
    print(f'\nO nome {palavra} temos ',end='')
    for letra in palavra:
        if letra in 'AEIOUaeiou':
            print(letra,end=',')
