v = 0
maior = 0
menor = 0
for c in range(1,6):
    v += 1
    peso = float(input('Peso da {}º pessoa: '.format(v)))
    if c ==1:
        maior = peso
        menor = peso
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print('O maior peso digitado foi o {}Kg, e o menor foi o {}Kg'.format(maior, menor))
