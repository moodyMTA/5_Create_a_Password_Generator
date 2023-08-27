import random
list_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
list_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
list_symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
count_letters = int(
    input("How many letters would you like in your password?\n"))
count_symbols = int(input(f"How many symbols would you like?\n"))
count_numbers = int(input(f"How many numbers would you like?\n"))

password = []

for letter in range(1, count_letters + 1):
    password += random.choice(list_letters)

for symbol in range(1, count_symbols + 1):
    password += random.choice(list_symbols)

for number in range(1, count_numbers + 1):
    password += random.choice(list_numbers)

random.shuffle(password)

random_password = ''

for char in password:
    random_password += char

print(f"Your password is: {random_password}")
