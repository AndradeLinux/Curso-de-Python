import math

ang = float(input('Informe o valor do ângulo: '))
seno = math.sin(math.radians(ang))
coss = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))
print('O ângulo de {0} tem o SENO de {1:.2f}'.format(ang, seno))
print('O ângulo de {0} tem o COSSENO de {1:.2f}'.format(ang, coss))
print('O ângulo de {0} tem a TANGENTE DE {1:.2f}'.format(ang, tang))
