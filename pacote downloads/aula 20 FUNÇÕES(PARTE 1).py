a = 4
b = 5
s = a + b
print(s)

a = 8
b = 9
s = a + b
print(s)

a = 2
b = 1
s = a + b
print(s)

def soma(a,b):
    s = a + b
    print(s)


#Programa principal
soma(4,5)
soma(8,9)
soma(2,1)

def soma(a,b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')
soma(b=4, a=5)
soma(7,2)


# empacotamento
def contador(*num):
    tam = len(num)
    print(f'Resebi os valores {num} e são ao todo {tam} numero!')
contador(2,1,7)
contador(8,0)
contador(4,4,6,2)
print('-'*20)
def soma(*valores):
    s = 0
    for num in valores:
        s= s + 1
    print(f"somando os valores {valores} temos {s}")

soma(5,2)
soma(2,9,4)

def dobra (lst):
    pos =0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [2,4,5,6,7]
dobra(valores)
print(valores)

def soma(a ,b):
    s = a + b
    print(s)
soma(3,4)
soma(2,1)