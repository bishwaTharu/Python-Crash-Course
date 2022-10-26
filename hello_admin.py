usernames = ['Bishwa','Harry','Mohan','Gita','Jhon']
admin = 'Bishwa'

# greetings to each user and special greeting to admin
for user in usernames:
    if user is admin:
        print('Hello admin, Would you like to see a status report?')
    else:
       print(f'Hello {user}, thank you for logging in again.')

for _ in range(len(usernames)):
    usernames.pop()
    if usernames == []:
        print('We need to find some users!')




