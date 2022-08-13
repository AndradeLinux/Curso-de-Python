larg=float(input('Informe a largura da parede: '))
altu=float(input('Informe a altura da parede: '))
dime= larg * altu
tinta= dime / 2
print('Sua parede tem a dimensão de {0}x{1} e sua área é de {2}m². \nPara pintar essa parede você precisará de {3}l de tinta.'.format(larg, altu, dime, tinta))
