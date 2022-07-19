n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
print('Sua média foi {:.1f}'.format(m))
if m < 5.0:
    print('\033[31mVOCÊ FOI REPROVADO!\033[m')
elif 5 <= m < 7:
    print('\033[33mVOCÊ ESTÁ DE RECUPERAÇÃO!\033[m')
elif 7 <= m < 10:
    print('\033[32mVOCÊ FOI APROVADO!\033[m')
