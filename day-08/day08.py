import math

# def paint_calc(h, w, coverage):
#     num_cans = h * w / coverage
    
#     print(math.ceil(num_cans))

# h = int(input())
# w = int(input())

# coverage = 5

# paint_calc(h, w, coverage)


# def prime_checker(number):
#     for i in range(2, int(math.sqrt(number)+1)):
#         if (number % i == 0):
#             return False
        
#     return True


# n = int(input())
# print(prime_checker(n))


from art import logo

def encode(text, shift):
    for alpha in text:
        if alpha in alphabet:
            word.append(alphabet[(alphabet.index(alpha)+shift) % 26])

        else:
            word.append(alpha)

    return word

def decode(text, shift):
    for alpha in text:
        if alpha in alphabet:
            word.append(alphabet[(alphabet.index(alpha)-shift) % 26])

        else:
            word.append(alpha)

    return word

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

while(True):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction != 'encode' and direction != 'decode':
        print('type again')
        continue

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    word = []

    if direction == 'encode':
        word = encode(text, shift)

    else:
        word = decode(text, shift)

    print(''.join(word))

    again = input("Type 'yes' if you want to go again. Otherwise type 'no'\n")
    if again == 'no':
        break
