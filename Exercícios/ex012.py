preço= float(input('Informe o valor do produto para ver o desconto: R$'))
desco= preço - (preço * 5 / 100)
print('O produto, com 5% de desconto, vai para R${:.2f}.'.format(desco))
