heard = input().split(', ')

if heard[-1] == 'wolf':
    print('Please go away and stop eating my sheep')
else:
    sheep = heard[::-1].index('wolf')
    print(f'Oi! Sheep number {sheep}! You are about to be eaten by a wolf!')
