import random2

aluno1 = input('Informe o nome do primeiro aluno: ')
aluno2 = input('Informe o nome do segundo aluno: ')
aluno3 = input('Informe o nome do terceiro aluno: ')
aluno4 = input('Informe o nome do quarto aluno: ')
lista = [aluno1, aluno2, aluno3, aluno4]
random2.shuffle(lista)
print('aluno que irá apagar o quadro será {}.'.format(lista))
