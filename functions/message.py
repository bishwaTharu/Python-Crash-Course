def display_message():
    print("Thank you for learning function in python")

display_message()

def favourite_book(title):
    print(f'One of my favourite book is {title.title()}')

favourite_book("python crash courses")

def pets( animal_type , animal_name):
    """Displays animal type and animal name"""
    print(f"My pet is {animal_type}, and it's name is {animal_name}")

pets(animal_type="Dog" , animal_name= "Tony")

def get_formatted_name(first_name, middle_name ,last_name):
 """Return a full name, neatly formatted."""
 full_name = first_name + ' ' + middle_name + ' ' + last_name
 return full_name.title()
 
musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)
