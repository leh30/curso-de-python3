ex = str(input('Digite a expressão: '))
lista = []
for letra in ex:
    if letra == '(':
        lista.append('(')
    elif letra == ')':
        if len(lista)> 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista)== 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')