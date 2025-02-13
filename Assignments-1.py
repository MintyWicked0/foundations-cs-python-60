age = int(input("Enter your age: "))

if age <= 18:
    print("The ticket price is $5")
elif age >= 19:
    print("The ticket price is $10")
else:
    print("The ticket price is $15")