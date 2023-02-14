# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input(f"How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

random_letters = []
for i in range(0, nr_letters):
    a = random.randrange(len(letters))
    letter = letters[a]
    random_letters += [letter]
print(random_letters)

random_symbols = []
for i in range(0, nr_symbols):
    a = random.randrange(len(symbols))
    symbol = symbols[a]
    random_symbols += [symbol]
print(random_symbols)

random_numbers = []
for i in range(0, nr_numbers):
    a = random.randrange(len(numbers))
    number = numbers[a]
    random_numbers += [number]
print(random_numbers)

pa = random_letters + random_symbols + random_numbers
random.shuffle(pa)
password = ""
for i in pa:
    password += i
print(password)


# #Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# random_letters = []
# for i in range(0, nr_letters):
#     a = random.randrange(len(letters))
#     letter = letters[a]
#     random_letters += [letter]
# print(random_letters)
#
# random_symbols = []
# for i in range(0, nr_symbols):
#     a = random.randrange(len(symbols))
#     symbol = symbols[a]
#     random_symbols += [symbol]
# print(random_symbols)
#
# random_numbers = []
# for i in range(0, nr_numbers):
#     a = random.randrange(len(numbers))
#     number = numbers[a]
#     random_numbers += [number]
# print(random_numbers)
#
# pa = random_letters + random_symbols + random_numbers
# password = ""
# for i in pa:
#     password += i
# print(password)
