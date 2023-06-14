#RULES?
#BETS?

#uBank = int(input("Enter your buy-in Amount"))####
#dBank = 0

play = True

while play:
    import random
    userIn = True
    dealerIn = True

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
                if t>=11:
                    t += 1
                else:
                    t += 11
        return t
    
    def splCalcScore(p):
        t = 0
        facee = ['K','Q','J']

        for c in p:
            if c in range(1,11):
                t += c
            elif c in facee:
                t += 10
            else:
                t += 11
        return t

    #CHECKING FOR WINNER
    def revealDHand():
        if len(dealerHand) == 2:
            return dealerHand[0]
        elif len(dealerHand)>2:
            return dealerHand[0], dealerHand[1]
        
    #GAME LOOP

    #ROUND BEGINS
    bet = int(input("Enter your bet "))
    #uBank -= bet###

    for _ in range(2):
        dealCard(userHand)
        dealCard(dealerHand)

    userScore = calcScore(userHand)

    while userIn or dealerIn:
        print(f"\nDealer has {revealDHand()} and ?")
        print(f"You have {userHand}\tTOTAL:{userScore}\n")

        if userIn:
            ch = int(input("1. Stay\n2. Hit \n"))

        if calcScore(dealerHand) > 16:
            dealerIn = False

        else:
            dealCard(dealerHand)
        
        if ch == 2: #HIT
            print("You have decided to Hit.")
            dealCard(userHand)

            if ('A' in userHand and splCalcScore(userHand) > 21): #SPLCASE
                userScore = splCalcScore(userHand) - 10
            else:
                userScore = calcScore(userHand)
                
        else: #STAY
            print("You have decided to Stay.")
            userIn = False

        if userScore > 21:
            break
        elif calcScore(dealerHand) > 21:
            break

    if userScore == calcScore(dealerHand):
        print(f"\nYou have {userHand} for a total of {userScore}\nThe Dealer has {dealerHand} for a total of {calcScore(dealerHand)}\n")
        print("Its a Draw!")
        #uBank += bet
        
    elif userScore == 21:
        print(f"\nYou have {userHand} for a total of {userScore}\nThe Dealer has {dealerHand} for a total of {calcScore(dealerHand)}\n")
        print(f"You have a Blackjack! You win! You recieve {bet*1.5}")
        #uBank += bet*1.5

    elif calcScore(dealerHand) == 21:
        print(f"\nYou have {userHand} for a total of {userScore}\nThe Dealer has {dealerHand} for a total of {calcScore(dealerHand)}\n")
        print("The Dealer has a Blackjack! The Dealer Wins!")
        #dBank += bet

    elif userScore > 21:
        print(f"\nYou have {userHand} for a total of {userScore}\nThe Dealer has {dealerHand} for a total of {calcScore(dealerHand)}\n")
        print("You Bust! The Dealer Wins!")
        #dBank += bet
        
    elif calcScore(dealerHand) > 21:
        print(f"\nYou have {userHand} for a total of {userScore}\nThe Dealer has {dealerHand} for a total of {calcScore(dealerHand)}\n")
        print(f"Dealer busts! You win! You recieve {bet}!")
        #uBank += bet

    elif 21 - calcScore(dealerHand) < 21 - userScore:
        print(f"\nYou have {userHand} for a total of {userScore}\nThe Dealer has {dealerHand} for a total of {calcScore(dealerHand)}\n")
        print("Dealer wins!")
        #dBank += bet

    elif 21 - calcScore(dealerHand) > 21 - userScore:
        print(f"\nYou have {userHand} for a total of {userScore}\nThe Dealer has {dealerHand} for a total of {calcScore(dealerHand)}\n")
        print(f"You win! You recieve {bet}")
        #uBank += bet

    #print(f"Remaining Balance:{uBank}")
    print("---------------------------------------------------------------")
    
    pa = input("\nPlay Again?\nY or N\n")

    if pa == 'N' or pa == 'n':
        play = False
