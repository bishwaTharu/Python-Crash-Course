unconfirmed_users = ['alice','bob','john','eric']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f'varifying {current_user.title()}...')
    confirmed_users.append(current_user)

for user in confirmed_users:
    print(f'{user.title()}...varified')