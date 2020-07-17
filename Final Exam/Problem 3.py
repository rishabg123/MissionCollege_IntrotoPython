import random
deck = []
suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
rankedVal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
sum = 0
countHand=0

for i in range(52):
    deck.append(i)

isCard = True
while (isCard == True):
  random.shuffle(deck)

  for i in range(4):
    suit = suits[int(deck[i]/13)]
    rank = rankedVal[deck[i] % 13]
    sum += rank

    if (rank == 1):
        print("Ace " + suit);

    elif(rank ==11):
        print("Jack of " + suit);

    elif (rank == 12):
	    print("Queen of " + suit);

    elif(rank==13):
	    print("King of " + suit);
    else:
        print(rank, "of" , suit)

if (sum == 24):
    isCard = False
print("Sum of four cards is " + sum)
sum =0
countHand= countHand+ 1

print("Number of hands drawn until 24 was reached : " + (countHand))


