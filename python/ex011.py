larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
print('Sua parede tem a dimensão de {:.2f} X {:.2f} e sua área é de {:.2f}m²'.format(larg, alt, area))
tinta = area / 2
print('Você precisasá de {}L de tinta para pintar essa área!'.format(tinta))