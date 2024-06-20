# student_scores = {
#     'Harry': 81,
#     'Ron' : 78,
#     'Hermione' : 99,
#     'Draco' : 74,
#     'Neville' : 62
# }

# student_grades = dict()

# for name, score in student_scores.items():
#     if score >= 91:
#         student_grades[name] = 'Outstanding'
#     elif score >= 81:
#         student_grades[name] = 'Exceeds Expections'
#     elif score >= 71:
#         student_grades[name] = 'Acceptable'
#     else:
#         student_grades[name] = 'Fail'

# print(student_grades)


# travel_log = {
#     "France" : {"cities_visited": ["Paris", "Lille", "Dijon"]},
#     "Germany" : {"cities_visited" : ["Berlin", "Hamburg", "Stuttgart"]}

# }

# print(travel_log["France"]["cities_visited"])


from replit import clear
from art import logo2

def check(worker):
    name = ''
    price = 0
    for key, value in worker.items():
        if value > price:
            price = value
            name = key

    print("The winner is {} with a bid of ${}".format(name, price))

worker = dict()

print(logo2)
print('Welcome to the secret auction program.')

while (True):
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    worker[name] = bid
    bidder = input("Are there any other bidders? Type 'yes' or 'no'.\n")

    if bidder == 'no':
        check(worker)
        break

    else:
        clear()

