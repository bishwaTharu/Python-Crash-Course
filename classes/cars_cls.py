class Cars():
    """ A simple attempt to represent a car """
    def __init__(self , make , model , year) -> None:
        """ Initialize attribute to describe a car """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_discriptive_name(self):
        print(f'{self.year} {self.make} {self.model.title()}')

    def read_odometer(self):
            """ Print a statement showing the car's mileage."""
            print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back odometer")

    def increment_odometer(self, miles):
            """Add the given amount to the odometer reading."""
            self.odometer_reading += miles

my_new_car = Cars("BMW" , "a4" , 2022)
my_new_car.get_discriptive_name()
my_new_car.read_odometer()

# modifing attribute value directly
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# modifing attribute value by method
my_new_car.update_odometer(22)
my_new_car.read_odometer()

# changing attibute by increment
my_used_car = Cars('subaru', 'outback', 2013)
my_used_car.get_discriptive_name()

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()