ailen_0 = {
    'x_position' : 0,
    'y_position' : 25,
    'speed' : 'medium'
 }

x_pos = ailen_0['x_position']
y_pos = ailen_0['y_position']

print(f'Old Position:({x_pos},{y_pos})')

if ailen_0['speed'] == 'slow':
    x_increment = 1
elif ailen_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3 

new_x_position = ailen_0['x_position'] + x_increment
y_position = ailen_0['y_position']

print(f'New Position:({new_x_position},{y_position})')
