ailen_0 = {
    'color' : 'green',
    'points' : 5
}

color = ailen_0['color']
points = ailen_0['points']

print(f'The Color is {color} and points earned is {points}.')

# adding new key-value in the dictionary
ailen_0['X-Position'] = 0
ailen_0['Y-Position'] = 0

print(ailen_0)

# mofiying values in dictionary
ailen_0['X-Position'] = 0
ailen_0['Y-Position'] = 1

print(f'Modified Dictionary: {ailen_0}')