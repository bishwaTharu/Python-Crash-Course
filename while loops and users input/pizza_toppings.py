active = True
ingredients = []

while active:
    prompt =  input("Enter the pizza toppings.Enter quit to Exit: ")

    if prompt == 'quit':
        print(f'adding {ingredients} ...\n')
        print(f'Your Pizza is ready. Enjoy your Meal!')
        active = False
    else:
        print(f'{prompt}...some more?\n')
        ingredients.append(prompt)
        