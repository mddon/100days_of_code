name = input("What is your name?\n")
length_of_string = str(len(name))
print("The length of string is " + length_of_string)

height = 1.65
weight = 84
# Write your code here.
# Calculate the bmi using weight and height.
bmi = weight/height ** 2
print(bmi)
print(round(bmi, 2))

# f-string
print(f"My name is {name}, my height and weight are {height} & {weight} respectively")
