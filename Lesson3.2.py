import random

def get_numbers_ticket(min_num, max_num, quantity):
    lottery_numbers = []
    if min_num >=1 and max_num <= 1000 and quantity <= (max_num - min_num + 1):
        lottery_numbers = sorted(random.sample(range(min_num, max_num+1), quantity))

    return lottery_numbers

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Your_lottery_numbers:", lottery_numbers)