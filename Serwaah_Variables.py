


print(" Exercise 1")


my_name = "Serwaah Nhyirah Johnson"
my_age = 20
fav_language = "Python"
class_completed = True

print(f"Name: {my_name}")
print(f"Age: {my_age}")
print(f"Favorite Language: {fav_language}")
print(f"Completed Today's Class: {class_completed}")
print("\n")



print("Exercise 2: ")

num1 = 15
num2 = 4

# Calculation variables
sum = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient= num1 / num2

print(f"Number 1: {num1}, Number 2: {num2}")
print(f"Sum (15 + 4): {sum}")
print(f"Difference (15 - 4): {difference}")
print(f"Product (15 * 4): {product}")
print(f"Quotient (15 / 4): {quotient}")
print("\n")


print("Exercise 3: ")

first_name = "Serwaah"
last_name = "Johnson"

# 1. Full name with a space
full_name = first_name + " " + last_name
print(f"Full Name: {full_name}")

# 2. Name in uppercase letters
uppercase_name = full_name.upper()
print(f"Uppercase Name: {uppercase_name}")

# 3. Introduction sentence using an f-string
intro_sentence = f"Hello! My name is {full_name}, and I am learning {fav_language} with enthusiasm."
print(f"Introduction: {intro_sentence}")
print("\n")



print("Exercise 4: User Input")
# Use input() to capture user data
fav_food = input("What is your favorite food? ")
# Note: The second input captures a string, which we assume is a number for the summary.
eat_frequency = input("How many times per week do you eat it? ")

# Display the summary using an f-string
summary_message = f"Summary: You love to eat {fav_food} approximately {eat_frequency} times a week. Enjoy!"
print(summary_message)
print("\n")




print("Exercise 5:")

age = "25"
height = 5.8

fixed_output = "I am " + age + " years old and " + str(height) + " feet tall."
print(fixed_output)
print("\n")




print(" Exercise 6: ")

celsius_temp = 30.5

fahrenheit_temp = (celsius_temp * 9/5) + 32

print(f"The temperature in Celsius is: {celsius_temp}°C")
print(f"The converted temperature in Fahrenheit is: {fahrenheit_temp}°F")

print("\n")

