import random

CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card(quantity=1):
    """Раздает указанное количество случайных карт"""
    return [random.choice(CARDS) for _ in range(quantity)]

arr = deal_card(2)
print(f'arr>>>init', arr)

print(f'arr[0]>>>, {arr[0]}')
arr.extend(deal_card())
print(f'arr>>>final', arr)

