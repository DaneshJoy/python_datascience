import random

phone_numbers = ['09123456733', '09112345675',
                 '09153485764', '09357563823',
                 '09204758374', '09187564734']

winners = random.sample(phone_numbers, 3)


for i, w in enumerate(winners):
    first_4_numbers = w[0:4]
    last_4_numbers = w[-4:]
    
    result = f'{i+1}: {first_4_numbers}***{last_4_numbers}'
    print(result)

