import random
deck = [x for x in range(0, 52)]

randomCard1 = random.randint(0, 52)
randomCard1Number = randomCard1 % 13 + 1
randomCard1Suite = ""
randomCard2 = random.randint(0, 52)
randomCard2Number = randomCard2 % 13 + 1
randomCard2Suite = ""
randomCard3 = random.randint(0, 52)
randomCard3Number = randomCard3 % 13 + 1
randomCard3Suite = ""
randomCard4 = random.randint(0, 52)
randomCard4Number = randomCard4 % 13 + 1
randomCard4Suite = ""


if randomCard1Number / 13 == 0:
    randomCard1Suite = "Spades"
elif randomCard1Number / 13 == 1:
    randomCard1Suite = "Hearts"
elif randomCard1Number / 13 == 2:
    randomCard1Suite = "Diamonds"
else:
    randomCard1Suite = "Clubs"

if randomCard2Number / 13 == 0:
    randomCard2Suite = "Spades"
elif randomCard2Number / 13 == 1:
    randomCard2Suite = "Hearts"
elif randomCard2Number / 13 == 2:
    randomCard2Suite = "Diamonds"
else:
    randomCard2Suite = "Clubs"

if randomCard3Number / 13 == 0:
    randomCard3Suite = "Spades"
elif randomCard3Number / 13 == 1:
    randomCard3Suite = "Hearts"
elif randomCard3Number / 13 == 2:
    randomCard3Suite = "Diamonds"
else:
    randomCard3Suite = "Clubs"

if randomCard4Number / 13 == 0:
    randomCard4Suite = "Spades"
elif randomCard4Number / 13 == 1:
    randomCard4Suite = "Hearts"
elif randomCard4Number / 13 == 2:
    randomCard4Suite = "Diamonds"
else:
    randomCard4Suite = "Clubs"


if randomCard1 == 10:
    randomCard1Number = "Jack"
if randomCard1 == 11:
    randomCard1Number = "Queen"
if randomCard1 == 12:
    randomCard1Number = "King"

print("Card Number", randomCard1, "is", randomCard1Number, "and the suite is", randomCard1Suite)
print("Card Number", randomCard2, "is", randomCard2Number, "and the suite is", randomCard2Suite)
print("Card Number", randomCard3, "is", randomCard3Number, "and the suite is", randomCard3Suite)
print("Card Number", randomCard4, "is", randomCard4Number, "and the suite is", randomCard4Suite)