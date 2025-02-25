'''n = str(input('Digite o nome: '))
# codigo de cores
vermelho = "\033[31m"
verde = "\033[32m"
amarelo = "\033[33m"
azul = "\033[34m"

# Cores de fundo
BG_RED = "\033[41m"
BG_GREEN = "\033[42m"
BG_YELLOW = "\033[43m"
BG_BLUE = "\033[44m"

print(f'{vermelho}{n} ' )
print(f'{verde}{n}')
print(f'{azul}{n}')
print(f'{amarelo}{n}')'''


try:
    a = int(input('numerador: '))
    b = int(input('Denumindor: '))
    c =  a / b

except(ValueError,TypeError):
    print('Tivemos um problema com os tipos de dados que voçe digitou.')
except ZeroDivisionError:
    print("Não é possivel dividir um numero por zero!")
except KeyboardInterrupt :
    print('O usuário preferiu não informa os dados.')
except Exception as erro:
    print(f'Problema encontrado foi {erro.__class__} ')
    print('Infelizmente tivemos um pobrema!')
else:
    print(f'o resultado é  {c:.2f}')
finally:
    print('Volte sempre! Muito obrigado!')
