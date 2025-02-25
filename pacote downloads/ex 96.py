print(' '*10 , "CONTROLE DO TERRENOS")
print('-'*40)
lar = float(input('LARGURA do terreno (M): '))
com = float(input('COMPRIMENTO do terreno (M): '))
def ves(a , b):
    v = a * b
    print(f'A área do terreno {a}x{b} é de {v}m².')
print('-'*40)
ves(a = lar,b = com)