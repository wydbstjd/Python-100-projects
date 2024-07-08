# student_heights = input().split()

# for i in range(0,len(student_heights)):
#     student_heights[i] = int(student_heights[i])

# sum = 0
# for height in student_heights:
#     sum += height

# avg = sum / len(student_heights)
# print(avg)


# target = int(input())
# sum = 0
# for i in range(2,target+1,2):
#     sum += i

# print(sum)


# for i in range(1,101):
#     if i % 15 == 0:
#         print('FizzBuzz')
#     elif i % 3 == 0:
#         print('Fizz')
#     elif i % 5 == 0:
#         print('Buzz')
#     else:
#         print(i)


print('Welcome to the PyPassword Generator!')
nr_letter = int(input('How many letters would you like in your password?\n'))
nr_symbol = int(input('How many symbols would you like?\n'))
nr_number = int(input('How many numbers would you like?\n'))

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#1
# password = list()

# for i in range(nr_letter):
#     password.append(letters[random.randint(0,len(letters)-1)]) 

# for i in range(nr_symbol):
#     password.append(symbols[random.randint(0,len(symbols)-1)]) 

# for i in range(nr_number):
#     password.append(numbers[random.randint(0,len(numbers)-1)])

# print(''.join(password))
# random.shuffle(password)
# print(''.join(password))

#2
password = list()
for i in range(nr_letter):
    password.append(random.choice(letters))

for i in range(nr_symbol):
    password.append(random.choice(symbols))

for i in range(nr_number):
    password.append(random.choice(numbers))

print(''.join(password))
random.shuffle(password)
print(''.join(password))
