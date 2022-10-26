with open('pi_digits.txt') as f:
    contents = f.read()
    print(contents.rstrip())

# reading line by line
with open('pi_digits.txt') as file_object:
    for line in file_object:
        print(line.rstrip())

# making a list of line from a file
with open('pi_digits.txt') as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

