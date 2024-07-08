import random

# randn = random.randint(0,2) # 0부터 2까지
# print(randn)

# randn2 = random.random() #0부터 1사이의 소수점
# print(randn2)


# coin = random.randint(0,1)
# if coin == 0:
#     print('Tails')

# else:
#     print('Heads')


# _name = input()
# name = _name.split(', ')
# randn = random.randint(0,len(name)-1)

# print(name[randn], 'is going to buy the meal today!')


# line1 = ['□','□','□']
# line2 = ['□','□','□']
# line3 = ['□','□','□']
# map = [line1, line2, line3]

# position = input()

# x = ord(position[0]) - 65
# y = int(position[1]) - 1

# map[y][x] = 'x'

# print('{}\n{}\n{}'.format(line1, line2, line3))


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rsp = [rock, paper, scissors]

my = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))
computer = random.randint(0,2)

print(rsp[my])
print('Computer chose:')
print(rsp[computer])

if my == computer:
    print('You draw')

elif my == 0:
    if computer == 1:
        print('You lose')
    else:
        print('You win')

elif my == 1:
    if computer == 2:
        print('You lose')
    else:
        print('You win')

else:
    if computer == 0:
        print('You lose')
    else:
        print('You win')

