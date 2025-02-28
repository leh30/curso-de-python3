def fatorial(n,show=False):
    """
    fatorial (n,show=False)
    :param n:O número a ser calculado
    :param show:(opcional) Mostrar ou não a conta.
    :return:O valor do fatorial de um número n.
    """
    f = 1
    for c in range(n,0,-1):
        if show:
            print(c,end=' ')
            if c>1:
                print('x',end=' ')
            else:
                print('=',end=' ')

        f = f * c
    return f
help(fatorial)