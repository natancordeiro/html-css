import math
angulo = int(input('Qual o valor do ângulo? '))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print('O valor de seno é {:.2f}\nO valor do cosseno é {:.2f}\nE o valor da tangente é {:.2f}'.format(sen, cos, tan))