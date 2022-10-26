"""
A list comprehension allows you to generate 
this same list in just one line of code 
"""
is_list = []

for value in range(2,11):
    if value % 2 == 0:
        sqr = value ** 2
        is_list.append(sqr)
print(f'is_list:{is_list}')

is_sqr_list = [ value ** 2 for value in range(2,11) if value % 2 == 0]
print(f'comprehension method:{is_sqr_list}') 

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:])