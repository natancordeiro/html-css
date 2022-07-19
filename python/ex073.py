times = ('Suns','Warriors', 'Grizzlies', 'Jazz', 'Mavericks', 'Nuggets',
         'Timberwolvs', 'Clippers', 'Lakers', 'Pelicans', 'Trail Blazers',
         'Spurs', 'Kings', 'Thunder', 'Rockets')
print('{:=^30}'.format('CONFERÊNCIA OESTE'))
print(f'Lista dos times da NBA: {times}')
print('=-'*14)
print(f'Os 5 primeiros são: {times[:5]}')
print('=-'*14)
print(f'Os 4 ultimos são: {times[-4:]}')
print('=-'*14)
print(f'Times em ordem alfabética: {sorted(times)}')
print('=-'*14)
print(f'O Lakers está na {times.index("Lakers")}º posição')
