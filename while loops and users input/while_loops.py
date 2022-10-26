active = True

while active:
    message = input("Please, Enter something: ")
    if message == 'quit':
        active = False
    else:
        print(message)
    