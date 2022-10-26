users = {
    'bishwa_tharu_' : {
        'first' : 'bishwa',
        'last' : 'Tharu',
        'location' : 'Nepal'
    },
    'shayam' : {
        'first' : 'Shayam',
        'last' : 'Tharu',
        'location' : 'India'
    }
}

# loop through users
for username , user_info in users.items():
    print(f'Username: {username}')
    print(user_info['first'].title()+ " " + user_info['last'] + "\nlocation: " + user_info['location'] + "\n")