n = int(input('Qual valor deseja ver a tabuada? '))
for c in range(1, 11):
    print('{} X {:2} = {}'.format(n, c, n*c))
