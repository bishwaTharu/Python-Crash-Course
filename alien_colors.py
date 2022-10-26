alien_colors = ['green','red','yellow']

# alien_color = 'red'

# if alien_color == 'green':
#     print('Players Have Earned 5 points')

# elif alien_color in alien_colors:
#     print('Player Have Earned 10 points')

# else:
#     print('Player Have Earned 0 points :(')  
alien_color = 'red'

if alien_color in alien_colors:
    if alien_color == 'green':
        print('Earned 5 points')

    elif alien_color == 'yellow':
        print('Earned 10 points')

    else:
        print('Earned 15 points')

else:
    print('Oops! Something went wrong')