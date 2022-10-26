def make_car(car_name , model , tow_package = True , **car_info):
    car_profile = {}
    car_profile['Brand'] = car_name
    car_profile['Model'] = model

    for key , value in car_info.items():
        car_profile[key] = value
    

    if tow_package == True:
        print('Thank you purchasing this car')
    elif tow_package == False:
         print('Its Okay, Thank you for purchasing')

    return car_profile


