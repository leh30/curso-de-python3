print('-='*20)
def voto(nu):
    from datetime import date
    atual = date.today().year
    idade = atual - nu
    if idade < 16 :
        return f'Com {idade} anos, voto NEGADO '
    elif  16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos, seu é voto OPCIONAL'
    else:
        return f'Com {idade} anos, seu é voto OBRIGATORIO'

print(voto(int(input("Qual o ano do seu nacimento: "))))
print('<< FIM DO PROGRAMA >>')
print('-='*20)