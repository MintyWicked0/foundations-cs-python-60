age = int(input("Enter your age: "))

if age > 15:
    print("You can run this code")
else:
    print("You cannot run this code")

print("Program is done")

grade = int(input("Enter your grade: "))

if grade >= 90:
    print("You got an A")
elif grade >= 80:
    print("You got a B")
elif grade >= 70:
    print("You got a C")
elif grade >= 60:
    print("You got a D")
else:
    print("You got an F")


password = input("Enter your password: ")

if password >= 10:
    print("Long")
else:
    print("Short")