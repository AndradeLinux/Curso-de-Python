from ast import Num


nome=input('informe o nome do aluno: ')
nota1=float(input('Digite a nota do aluno: '))
nota2=float(input('Digite a outra nota do aluno: '))
media=(nota1+nota2)/2
print('A média do aluno {0} é {1:.1f}.'.format(nome, media))
