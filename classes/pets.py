class Dog():
    def __init__(self , name , age):
        """ Initialize attributes """
        self.name = name
        self.age = age 

    def sit(self):
        """ sit in response to the commend """
        print(f'{self.name.title()} is now sitting')

    def roll_over(self):
        """ roll over in response to the commend """
        print(f'{self.name.title()} rolled over')

pet = Dog(name = 'tony' , age = 2)
pet.sit()

pet.roll_over()
print(pet.name)
print(str(pet.age) + " years")


