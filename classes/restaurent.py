class Restaurant:
    def __init__(self , restaurant_name:str , cuisine_type:str):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def open_restaurant(self):
        print(f"The {self.restaurant_name.title()} Restaurant is open.")

    def describe_restaurant(self):
        print(f'The {self.restaurant_name} is located at kathmandu.')

res1 = Restaurant("Willie" , cuisine_type = "Italian")
res1.open_restaurant()
print(res1.restaurant_name)
print(res1.cuisine_type)

res1.describe_restaurant()

res2 = Restaurant("White Villa" , "Nepali")
res2.describe_restaurant()

res3 = Restaurant("Dark Villa " , "Indian")
res3.describe_restaurant()