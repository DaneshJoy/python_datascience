import random

part_1 = "09"

numbers = []
for i in range(10):
    part_2 = str(random.randint(10000000, 99999999))
    number = part_1 + part_2
    numbers.append(number)


winners = random.sample(numbers, 3)

for w in winners:
    w_new = w[0:3] + '****' + w[-4:]
    w_new = f'{w[0:3]}****{w[-4:]}'
    print(w_new)