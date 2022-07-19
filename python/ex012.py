valor = float(input('Qual o preço do produto? R$'))
desc = valor - (valor*5/100)
print('O produto que custava R${}, na promoção de 5% vai custar R${}'.format(valor, desc))
