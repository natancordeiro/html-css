r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro  segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[32mOs segimento acima PODEM FORMAR um triângulo!\033[m')
    if r1 == r2 and r1 == r3 and r2 == r3:
        print('O triângulo é EQUILÁTERO!')
    elif r1 == r2 or r1 == r3 and r2 == r3 or r2 == r1 and r3 == r1 or r3 == r2:
        print('O triângulo é ISÓSCELES!')
    elif r1 != r2 and r2 != r3 and r1 != r3:
        print('O triângulo é ESCALENO!')
else:
    print('\033[31mOs seguimentos acima NÃO PODEM FORMAR um trriângulo!\033[m')
