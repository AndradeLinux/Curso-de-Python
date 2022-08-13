import math

cat_op = float(input('Digite o valor do cateto oposto: '))
cat_aj = float(input('Digite o valor do cateto adjacente: '))
hipo = math.hypot(cat_op, cat_aj)
print('A hipotenusa é igual a {:.2f}'.format(hipo))
