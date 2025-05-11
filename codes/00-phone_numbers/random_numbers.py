import random

part_1 = "09"

numbers = [part_1 + str(random.randint(10000000, 99999999)) for _ in range(10)]


winners = random.sample(numbers, 3)

for w in winners:
    print(f'{w[0:3]}****{w[-4:]}')
