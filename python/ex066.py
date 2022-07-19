tot = soma = 0
while True:
    n = int(input('Digite um número [999 para parar]: '))
    if n == 999:
        break
    soma += n
    tot += 1
#print('Você digitou {} números e a soma entre eles foi {}.'.format(tot, soma))
print(f'Você digitou {tot} números e a soma entre eles foi {soma}')