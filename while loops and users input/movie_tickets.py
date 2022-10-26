
active = True
msg = input("Do you wish to continue...yes/no: ")

def movie_ticket():
    while active:
        age = int(input("Enter your age: "))
        
        if age < 3:
            print("The ticket is free.")
            break
        elif age >= 3 and age <= 12:
            print("The ticket is $10.")
            break
        else:
            print("The ticket is $15") 
            break

if msg == 'yes':
    movie_ticket()
elif msg == 'no':
    active = False 