age = int(input("Enter your age: "))

if age < 5:
    print("The ticket price is $0")
elif age <= 12:
    print("The ticket price is $5")
elif age <= 18:
    print("The ticket price is $10")
else:
    print("The ticket price is $15")