# looping through entrie list

is_list = ['Harry','Bishwa','Ram','Sita']

for is_name in is_list:
    print(is_name)
print('\n')

# get index and item in the list
for index , is_name in enumerate(is_list):
    print(f'Index:{index} and value_is: {is_name}\n')
    print(f'{is_name} is a good python programmer\n')
print('Thanks Everyone for Learning Python!! :)')

# list of numerical values
nums = list(range(1,6))
print(nums)

even_nums = list(range(2,6,2))
print(even_nums)

# append something in the empty list
sqr_nums = []

for i in range(1,6):
    sqr = i ** 2
    sqr_nums.append(sqr)

print(sqr_nums)

# Simple Statistics with a List of Numbers

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print(f'minuimum: {min(digits)}')
print(f'Maximum : {max(digits)}')
print(f'sum of digits : {sum(digits)}')

