user_0 = {
 'username': 'efermi',
 'first': 'enrico',
 'last': 'fermi',
 }

for key , value in user_0.items():
    print(f'Key:{key} | value:{value}')

# looping through keys
keys = []

for key in sorted(user_0.keys()):
    keys.append(key)

print(keys)

# loop through values 
for val in sorted(user_0.values()):
    print(f' Hello {val}, thanks for taking the poll ')