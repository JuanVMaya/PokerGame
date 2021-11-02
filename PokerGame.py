"""
PokerGame
Created on Thu  Oct 17, 2019
Author: Juan Vanegas Maya
Purpose: To develop a running program that imitates the card game poker
"""
import random,time
def dealCards(deck, n): #n is number of cards to be dealt
    cardsDealt=[]
    for i in range(0,n):
        while True:
            randomCardIndex=random.randint(1,52)
            if randomCardIndex in deck:
                break
            else:
                continue                
        cardsDealt.append(deck[randomCardIndex])
        deck.pop(randomCardIndex, None)
    return cardsDealt

        
def findCategory(cards) :
    category=[]
    if isStraightFlush(cards):
        category.append("SF")
    elif isFourOfAKind(cards):
        category.append("4K")
    elif isFullHouse(cards):
        category.append("FH")
    elif isFlush(cards):
        category.append("FL")
    elif isStraight(cards):
        category.append("ST")  
    elif isThreeOfAKind(cards):
        category.append("3K")
    elif isTwoPair(cards):
        category.append("2P")
    elif isOnePair(cards):
        category.append("1P")
    elif isHighCard(cards):
        category.append("HC")      
    return cards+category    

 
def isHighCard(cards) : 
    if not(isOnePair(cards) or isTwoPair(cards) or isThreeOfAKind(cards) or isStraight(cards) or isFlush(cards) or isFullHouse(cards) or isFourOfAKind(cards) or isStraightFlush(cards)):
        return 1 
def isOnePair(cards) :
    numbers="a23456789tjqk"
    cardNumbers=[]
    for i in range(0,7):
        cardNumbers+=cards[i][0]
    cardNumbers=''.join(cardNumbers)
    for j in range(len(numbers)):
        if countChar(cardNumbers,numbers[j])==2:
            return 1     
    return 0
def isTwoPair(cards) :
    numbers="a23456789tjqk"
    cardNumbers=[]
    for i in range(0,7):
        cardNumbers+=cards[i][0]
    cardNumbers=''.join(cardNumbers)
    twoPairFlag=0
    for j in range(len(numbers)):
        if countChar(cardNumbers,numbers[j])==2:
            twoPairFlag+=1
            if twoPairFlag==2:
                return 1     
    return 0
def isThreeOfAKind(cards) :
    numbers="a23456789tjqk"
    cardNumbers=[]
    for i in range(len(cards)):
        cardNumbers+=cards[i][0]
    cardNumbers=''.join(cardNumbers)
    for j in range(len(numbers)):
        if countChar(cardNumbers,numbers[j])==3:
            return 1     
    return 0   
def isStraight(cards) :
    numbers="23456789tjqka"
    cardNumbers={}
    for i in range(0,7):
        cardNumbers[i]=cards[i][0]
    straightCounter=0
    for j in range(len(numbers)):        
        if countChar(cardNumbers,numbers[j])>=1:
            straightCounter+=1    
            if straightCounter>=5:
                return 1
        else:
            straightCounter=0
    return 0
def isFlush(cards) :
    suits="hcsd"
    cardSuits=[]
    for i in range(0,7):
        cardSuits+=cards[i][1]
    cardSuits=''.join(cardSuits)
    for j in range(len(suits)):
        if countChar(cardSuits,suits[j])>=5:
            return 1     
    return 0
def isFullHouse(cards) :
    if isThreeOfAKind(cards) and isOnePair(cards):
        return 1
    else:
        return 0 
def isFourOfAKind(cards) :
    numbers="a23456789tjqk"
    cardNumbers=[]
    for i in range(0,7):
        cardNumbers+=cards[i][0]
    cardNumbers=''.join(cardNumbers)
    for j in range(len(numbers)):
        if countChar(cardNumbers,numbers[j])==4:
            return 1     
    return 0 
def isStraightFlush(cards) :
    suits="cshd"
    numbers="23456789tjqka"
    cardSuits=[]
    cardNumbers={}
    cards = sorted(cards, key=lambda x: x[1])
    for i in range(0,7):
        cardSuits+=cards[i][1]
        cardNumbers[i]=cards[i][0]
    cardSuits=''.join(cardSuits)
    straightFlushCounter=0
    for j in range(len(suits)):
        if countChar(cardSuits,suits[j])>=5:
            desiredSuit=suits[j]
            for k in range(len(numbers)):
                if countSF(cardNumbers,numbers[k],cardSuits,desiredSuit)>=1:
                    straightFlushCounter+=1    
                    if straightFlushCounter>=5:
                        return 1
                else:
                    straightFlushCounter=0
    return 0         
def countChar(string, item): 
    count = 0
    for i in range(len(string)):  
        if (string[i] == item) : 
            count += 1
    return count    
def countSF(string, number,cardSuits,suit): 
    count = 0
    for i in range(len(string)):  
        if (string[i] == number) and (cardSuits[i]==suit) : 
            count += 1
    return count    
categories=["SF","4K","FH", "FL", "ST","3K","2P","1P","HC"]

option='y' #This starts the program
while (option=='Y' or option=='y'):
    deck={1:"2h", 2:"3h", 3:"4h", 4:"5h", 5:"6h", 6:"7h", 7:"8h", 8:"9h", 9:"th", 10:"jh", 11:"qh", 12:"kh", 13:"ah",
          14:"2c", 15:"3c", 16:"4c", 17:"5c", 18:"6c", 19:"7c", 20:"8c", 21:"9c", 22:"tc",23:"jc", 24:"qc", 25:"kc", 26:"ac",
          27:"2s", 28:"3s", 29:"4s", 30:"5s", 31:"6s", 32:"7s", 33:"8s", 34:"9s", 35:"ts", 36:"js", 37:"qs", 38:"ks", 39:"as", 
          40:"2d", 41:"3d", 42:"4d", 43:"5d", 44:"6d", 45:"7d", 46:"8d", 47:"9d", 48:"td", 49:"jd", 50:"qd", 51:"kd", 52:"ad"}
    print(' ')
    print("WELCOME TO PYTHON POKER-----------------")
    while True:
        try:
            players=int(input("How many players will play today (2 to 5)?"))
        except ValueError:
            print("Sorry, that is not a valid input. Please try again")
            continue
        if players>5 or players<2:
            print("'",players, "' is not a valid number of players. Please try again")
            continue
        else:
            break
    #players=2 # Remove after testing
    communityCards=dealCards(deck, 5)
    print("CommunityCards: ", list(communityCards))
    playerCards=[]
    for n in range(1,players+1):
        playerCards.append(dealCards(deck,2))
        time.sleep(1)
        print("Player",n,":",list(playerCards[n-1]))
        #Community cards: [2d, 3h, 7h, ts, ac]
    time.sleep(1)
    resultGame=[]
    for j in range(0,players):
        cardsForTesting=communityCards+playerCards[j]
#        cardsForTesting=['3h', '2c', 'jh', 'th', 'qh', 'kh', '9h']#Delete this line after testing
        resultGame.append(findCategory(cardsForTesting))
    winnerFlag=0
    winners=[]
    for category in categories:
        if winnerFlag==0:
            for i in range(0,len(resultGame)):
                if(resultGame[i][-1]==category):
                    winners.append(i+1)
                    winners.append(resultGame[i][0:7])
                    winners.append(resultGame[i][-1])
                    winnerFlag+=1                  
    if winnerFlag>1:   
        print("TIE!")       
        for i in range(0,len(winners),3):
            print("Player", winners[i] ,":" ,winners[i+1], winners[i+2])
    elif winnerFlag==1:          
        print("Player", winners[0] ,"wins!" ,winners[1], winners[2])  
    while True:
        try:
            option=input("Do you wish  to play another game? ('y|Y'es or 'n|N'o): ")
        except ValueError:
            print("Sorry, that is not a valid input. Please try again")
            continue
        if option!='y' and option!='n' and option!='N' and option!='Y':
            print("This is not a valid option. Please try again")
            continue
        else:
            break