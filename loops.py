import random
print("Welcome to the password generator")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ['!', '/' ,':' ,'*', '?', '"', '<', '>', '|']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

letters_inp= int(input("How many letters do you want?"))
symbols_inp= int(input("How many letters do you want?"))
numbers_inp= int(input("How many letters do you want?"))

password_list = []
for char in range(0, letters_inp):
    password_list.append(random.choice(letters))

for char in range(0, symbols_inp):
    password_list.append(random.choice(symbols))

for char in range(0, numbers_inp):
    password_list.append(random.choice(numbers))

print(password_list)

random.shuffle(password_list)
print(password_list)

password = ""
for pas in password_list:
    password+=pas
print(f"Your password is: {password}")
