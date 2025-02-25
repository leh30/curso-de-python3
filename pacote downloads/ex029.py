velocidade = float(input('Informe a velocidade do veiculo:'))
print('Sua velocidade foi de {} km por hora '.format(velocidade))

if velocidade > 80 :
    print('Voçe foi mutado por esse de velocidade!')

    muta = (velocidade - 80) * 7
    print('Valor da muta é de {} Reais'.format(muta))

print('Fim do proceso!')