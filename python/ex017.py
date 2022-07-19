from math import sqrt
a = float(input('Qual o comprimento do cateto oposto? '))
b = float(input('Qual o comprimento do cateto adjacente? '))
h = (a * a) + (b * b)
print('O comprimento da hipotenusa do triângulo é {:.2f}'.format(sqrt(h)))
