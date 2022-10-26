aliens = []

# make 30 green aliens
for alien_number in range(30):
    new_ailen = {
        'color' : 'green',
        'points' : 5,
        'speed' : 'medium'
    }
    aliens.append(new_ailen)

for alien in aliens[:5]:
    print(alien['color'] == 'green')
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'slow'
        alien['points'] = 10

for alien in aliens[:3]:
    print(alien)
print("...")

# display total number of aliens
print(f'total number of aliens: {len(aliens)}')