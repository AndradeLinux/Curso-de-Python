numero1=int(input('Digite um número: '))
numero2=int(input('Digite outro número: '))
soma=numero1+numero2
multi=numero1**numero2
div=numero1/numero2
divint=numero1//numero2
expo=numero1**numero2
print('A soma {0} e {1} é {2}, o produto é {3} e a divisão é {4:.3f}'.format(numero1, numero2, soma, multi, div))
print('A divisão inteira é {0} e a potência é {1}'.format(divint, expo))
