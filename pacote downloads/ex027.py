nome = str(input("Digite seu nome completo:")).strip()


print('Prazer em te conhecer {} !'.format(nome))
print('Primeiro nome é:{}'.format(nome.split()[0]))
print('Útimo nome é:{}'.format(nome.split()[-1]))
