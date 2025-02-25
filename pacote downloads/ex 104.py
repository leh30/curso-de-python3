def leiaint(msg):
    ok = False
    cont = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            cont = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um valor valido.\033[m,')
        if ok:
            break
    return cont
n = leiaint('Digite um número: ')
print(f'Voçe acabou de digitar o número {n}!')