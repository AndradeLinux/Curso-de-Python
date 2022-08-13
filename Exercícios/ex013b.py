preco= float(input('Informe o valor do produto: R$'))
opcao= input('Pagamento à vista?(sim ou nao): ')
if opcao == 'sim':
    print('Produto com 5% de desconto. \nTotal a pagar: R${:.2f}.'.format(preco - (preco * 5 / 100)))
elif opcao == 'nao':
    vezes= float(input('Deseja pagar em quantas vezes? '))
    nopre= preco + (preco * 8 / 100)
    parc= float(nopre / vezes)
    print('Total a pagar: R${0:.2f}\n{1:.0f} parcelas de R${2:.2f}'.format(nopre, vezes, parc))
else:
    print('OPÇÃO INCORRETA.')
