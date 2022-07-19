vel = float(input('Qaul a velocidade do carro? '))
multa = (vel - 80) * 7
if vel > 80:
    print('VOCÊ FOI MULTADO!')
    print('Sua multa foi de R${:.0f},00'.format(multa))
else:
    print('Você estava na velocidade adequada!')
