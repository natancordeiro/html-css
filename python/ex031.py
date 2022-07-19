dis = float(input('Qual a distância da sua viagem? '))
menor = 0.50 * dis
maior = 0.45 * dis
if dis <= 200:
    print('Sua passagem vai custar R${:.2f}'.format(menor))
else:
    print('Sua passagem vai custar R${:.2f}'.format(maior))
