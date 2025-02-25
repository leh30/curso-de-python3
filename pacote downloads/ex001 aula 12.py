casa = int(input('Qual o valor da casa que voçe desja comprar? '))
salario = int(input('Qual sua media salarial? '))
ano = int(input('Em quantos anos vcoçe deseja quitar o imovel?'))

calculo = (ano * 12)
calculo1 = (calculo * salario) / casa
calculo2 = (salario * 30) / 100

if calculo2 < salario:
    print('emprestemo liberado')
else:
    print('nao foi possivel fazer o emprestemo')