def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (KeyboardInterrupt):
            print('\n\033[31mEntrada de dados interrompita pelo usuario!\033[m')
            return  0
        except:
            print('\033[0:31mERRO: por favor digite um numero inteiro!\033[m')
            continue

        else:
            break

    return n
def leiafloat(msg):
    while True:
        try:
            l = float(input(msg))
        except (KeyboardInterrupt):
            print('\n\033[31mEntrada de dados interrompita pelo usuario!\033[m')
            return  0
        except:
            print('\033[0:31mERRO: por favor digite um numero float!\033[m')
            continue
        else:
            break
    return l
n = leiaint("Digite um numero inteiro: ")
l = leiafloat('Digite um numero float: ')
print(f'O valor inteiro foi {n} e o rael foi {l} .')