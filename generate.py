from random import choice
coin = choice(["heads","tails"])
for i in range(10):
    print(coin)

import random 
number = random.randint(1,200)
print (number)

cards=["jack","queen","king","ace"]
random.shuffle(cards)
for cards in cards:
    print (cards)