class Users():
    def __init__(self , first , last ):
        self.f_name = first
        self.l_name = last

    def describe_user(self,**user_info):
        profile = {}
        profile['Full Name'] = self.f_name + self.l_name
            
        for key , value in user_info.items():
            profile[key] = value

        return profile

    def greet_user(self):
        print(f' Hello, {self.f_name} {self.l_name}. Have a good day!')

user_1 = Users(first = "Bishwa" , last = "Tharu")
print(user_1.describe_user(field = "Data Science" , Education = "Bsc."))
user_1.greet_user()

        