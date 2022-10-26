def build_profile(first , last , **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last

    for key , value in user_info.items():
        profile[key] = value
    return profile

print(build_profile(first = 'Bishwa', 
                    last = 'Tharu', 
                    location = 'Nepal', 
                    field = 'Physics'))