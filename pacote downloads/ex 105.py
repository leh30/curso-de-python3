
def nota(*num,show=False):
    """
    -> função para analisar notas e situação de varios alunos
    :param num: uma ou mais notas dos alunos (aceita varios )
    :param show: situação opcinal
    :return: Dicionario com varias informação sobre a situção da turma.
    """
    global resp
    aluno = {}
    soma = 0
    for c in num:
        soma = soma + c
    aluno["total"]=(len(num))
    aluno["maior"]=(max(num))
    aluno["menor"]=(min(num))
    aluno["media"]=(soma/len(num))
    if show:
        if aluno["media"] < 5:
            aluno["situação"]='RUIM'
        else:
            aluno["situação"]='BOA'
    resp = aluno
# programa principal
print(nota(9,4,9,10,show=True))
print(resp)
help(nota)