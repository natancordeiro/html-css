ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano % 4 == 0 and ano != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} não é BISSEXTO'.format(ano))
