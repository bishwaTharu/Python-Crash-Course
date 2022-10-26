# # much code can be improved by using a datastructe.
# SUFFIXES = {1: 'st', 2: 'nd', 3: 'rd'}
# def ordinal(num):
#     # I'm checking for 10-20 because those are the digits that
#     # don't follow the normal counting scheme. 
#     if 10 <= num % 100 <= 20:
#         suffix = 'th'
#     else:
#         # the second parameter is a default.
#         suffix = SUFFIXES.get(num % 10, 'th')
#     return str(num) + suffix

# print(ordinal(num=2000))

nums = list(range(1,10))

for num in nums:
    if num == 1:
        suffix = 'st'
        print(str(num)+suffix)

    elif num == 2:
        suffix = 'nd'
        print(str(num)+suffix)

    elif num == 3:
        suffix = 'rd'
        print(str(num)+suffix)

    else:
        suffix = 'th'
        print(str(num)+suffix)