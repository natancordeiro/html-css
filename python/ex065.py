cont = 'S'
tot = 0
contador = 0
while cont in 'S':
    n = float(input('Digite um número: '))
    cont = str(input('Quer continuar? [S/N] ')).strip().upper()
    tot += n
    contador += 1
    if contador == 1:
        maior = n
        menor = n
    else:
        if n >= maior:
            maior = n
        elif n <= menor:
            menor = n
media = tot / contador
print('A média entre todos os valores digitados foi {:.1f}.'.format(media))
print(' O maior valor digitado foi {:.0f} e o menor foi {:.0f}.'.format(maior, menor))
