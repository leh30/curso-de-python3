print('~~' * 15)
print('   \033[0;31mSISTEMA DE AJUDA PYHELP\033[m')
print('~~' * 15)

def manual(msg):
    while True:

        from time import sleep
        print('~'*(30+len(msg)))
        print(f'\033[0;31mAcessando o manual do comando {msg}\033[m,')
        print('~'*(30+len(msg)))
        sleep(1)
        help(msg)
        res =str(input('Função ou Biblioteca > '))
        if res == 'fim':
            break
    print("FIM DO PROGRAMA!")

manual(str(input('Função ou Biblioteca > ')))