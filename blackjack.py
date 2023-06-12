import random
deck = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']*4
userHand = []
dealerHand = []

#DEALING CARDS
def dealCard(p):
    card = random.choice(deck)
    p.append(card)
    deck.remove(card)

#CALCULATING TOTAL
def calcScore(p):
    t = 0
    face = ['K','Q','J']

    for c in p:
        if c in range(1,11):
            t += c
        elif c in face:
            t += 10
        else:
            if t>11:
                t += 1
            else:
                t += 11
    return t

#CHECKING FOR WINNER
def revealDHand():
    if len(dealerHand) == 2:
        return dealerHand[0]
    elif len(dealerHand)>2:
        return dealerHand[0], dealerHand[1]