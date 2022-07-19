while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    print('-' * 15)
    for m in range(0, 10):
        m += 1
        r = n * m

        print(f'{n} X {m} = {r}')
    print('-'*15)
print('PROGRAMA ENCERRADO!')
