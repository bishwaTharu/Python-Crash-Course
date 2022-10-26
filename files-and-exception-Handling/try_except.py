# a = 5/0
# print(a)
# try:
#  print(5/0)
# except ZeroDivisionError:
#  print("You can't divide by zero!")

my_dict = {
    'num1': 1,
    'num2': 2,
    'num2' : 3
}

key = 'num3'
try:
    print(my_dict[key])
except KeyError:
    print(f'{key} not found')


for key , value in my_dict.items():
    try:
        print(my_dict[key] == value)
    except KeyError:
        print(f"{key} not found")