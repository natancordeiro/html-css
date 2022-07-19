print('\033[34m-='*20)
print('        DETECTOR DE PALÍDROMO')
print('-='*20, '\033[m')
fr = str(input('Qual frase deseja verificar: ')).strip().upper()
palavra = fr.split()
junto = ''.join(palavra)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palídromo!')
else:
    print('A frase não é um palídromo!')