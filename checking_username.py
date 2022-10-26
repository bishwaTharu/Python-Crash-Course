current_users = ['Bishwa','Harry','John','Hritik','Chandan']

new_users = ['Bishwa','Shayam','JOHN','Rohan','Deepa']

for index , user in enumerate(new_users):
    if user.upper() in current_users[index].upper():
        print('Please enter a new username')
    else:
        print('User is available')



