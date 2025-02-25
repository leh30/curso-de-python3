n = cont =  soma = 0
while True:
    n = int(input('Digite o numero(999 para parar): '))
    if n == 999:
        break
    cont = cont + 1
    soma = soma + n
print(f'Voçe digitou {cont} numeros ea soma entre eles é {soma}.')