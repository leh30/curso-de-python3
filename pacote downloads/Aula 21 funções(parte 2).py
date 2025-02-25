from time import sleep
def contador(i,f,p):
    """docstrings

    --> Faz uma contagem e mostra na tela.
    :param i: inicio da contagem
    :param f:fim da contagem
    :param p:passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c = c + p
        sleep(1)
    print('FIM')
help(contador)
print('-='*20)


# parametros opcionais
def somar(a,b=0,c=0):
    s = a+b+c
    print(f'As somas vale {s}')
somar(3,2,5)
somar(2,4)
somar(3)
somar(c=3,a=2)
print('-='*20)


#escopo de variáveis
def funcao():
    # variáveil local
    n1 = 4
    print(f'N1 dentro vale {n1}')

# variável global
n1 =2
funcao()
print(f'N1 fora vale {n1}')
print('-='*20)

#retorno de valores
def somar(a=0,b=0,c=0):
    s = a+b+c
    return s

r1=somar(3,2,5)
r2=somar(2,2)
r3=somar(6)
print(f'Os resultados foram {r1}, {r2} e {r3}!')
print('-='*20)

def fatorial(num=1):
    f=1
    for c in range(num,0,-1):
        f = f * c
    return f
n = int(input('Digite um numero:'))
print(fatorial(n))

def par (n=0):
    if n % 2 == 0:
        return True
    else:
        return False
num = int(input('Digite um numero: '))
print(par(n))
if par(num):
    print('É par!')
else:
    print('Não é par!')