foods = ('Pizza','Mo:Mo','Chicken Chilli', 'Choumin','Sea food')

print('Old Menu\n')
for food in foods:
    print(f'{food}\n')

# this code throws an assignment error since tuples are immutable .
# foods[0] = 'Burger'
# print(foods)


foods = ('Burger','Chichi','Pizza','Mo:Mo','Chicken Chilli')

print('Menu Updated\n')
for food in foods:
    print(food)
    print("\n")