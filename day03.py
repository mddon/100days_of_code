# print("\nWelcome to rollercoaster")
# height = int(input("What is your height in cm? "))
#
# if height > 120:
#     print("You can ride the rollercoaster")
# else:
#     print("Sorry you have to grow tailer before you can ride.")

# number = int(input("Enter a number\n"))
# if number % 2 == 0:
#     print(f"{number} is an even number")
# else:
#     print(f"{number} is not an even number")

print("\nWelcome to rollercoaster")
height = int(input("What is your height in cm?\n"))

if height <= 120:
    print("Sorry you have to grow tailer before you can ride.")
else:
    print("Congrats! You can ride the rollercoaster.")
    age = int(input("How old are you?\n"))
    if age > 18:
        print("Kindly pay $12")
    elif age >= 12:
        print("Kindly pay $7")
    else:
        print("Kindly pay $5")
