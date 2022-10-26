fav_programming = {
    'Bishwa' : 'Python',
    'Anjali' : 'JavaScript',
    'Deepa'  : 'Rust'
}

friends = ['anjali','deepa']

for name in fav_programming.keys():
    if name.lower() in friends:
        print(" Hi! " + name.title() + ".\nYour Favourite Programming Language is " + fav_programming[name.title()])

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
for name in sorted(favorite_languages.keys()):
 print(name.title() + ", thank you for taking the poll.")
