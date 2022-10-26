prompt = "Enter Two numbers and It returns sum of those numbers"
print(prompt)

try:
    num1 = int(input("Enter num first: "))
    num2 = int(input("Enter num second: "))
except ValueError:
    print('Please Enter a valid number')

# addition of nums
try:
    print(num1+num2)
except Exception as e:
    print(e)