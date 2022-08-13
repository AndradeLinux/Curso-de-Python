print('============================\n ALUGUEL DE CARROS DO BRADD\n============================')
kms= float(input('Quantos KMs percorreu com o carro durante o período de aluguel? '))
periodo= float(input('Quantos dias o carro ficou em sua posse? '))
aludia= periodo * 60
alukm= kms * 0.15
print('Valor a ser pago pelo total de {0:.0f} dias: R${1:.2f}.'.format(periodo, aludia))
print('Valor a ser pago pelo total de {0:.0f}KMs: R${1:.2f}.'.format(kms, alukm))
print('Valor total a ser pago pelo aluguel do carro: R${:.2f}.'.format(aludia+alukm))
