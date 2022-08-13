real= float(input('Informe o valor diponível em sua carteira: R$'))
dolar= real / 5.11
euro= real / 5.21
yuan= real / 0.76
print('Com R${0:.2f} você pode comprar US${1:.2f} €{2:.2f} e {3:.2f}元 '.format(real, dolar, euro, yuan))
