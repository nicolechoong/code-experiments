import random
import time
import copy

class Card:

    def __init__(self, colour, value, special):
        self.colour = colour
        self.value = value
        self.special = special

    def __str__(self):
        colKey = {"R":"Red ","Y":"Yellow ","G":"Green ","B":"Blue ",None:""}

        if self.special:
            valKey = {"S":"Skip","R":"Reverse","+2":"Draw 2","+4":"Draw 4", "WC":"Wildcard"}
            return colKey[self.colour] + valKey[self.value]

        else:
            return colKey[self.colour] + self.value

# DECK CONTROLLING FUNCTIONS

def genDeck():
    global deck

    for i in ["R","Y","G","B"]:
        for j in range(0,10):
            deck.append(Card(i,str(j), False))

        for j in ["+2","S","R"]:
            deck.append(Card(i,j, True))

    for i in range(0,2):
        deck.append(Card(None, "+4", True))
        deck.append(Card(None, "WC", True))

def randomCard():
    global deck, topcard, pile

    if len(deck) == 0:
        deck = copy.deepcopy(pile)

        for i in deck:
            print(i)


        if topcard in ["WC", "+4"]:
            topcard.colour = None
            pile = [topcard]

    card = deck[random.randint(0,len(deck)-1)]
    deck.remove(card)

    return card

# VARIOUS SHARED TURN FUNCTIONS

def chooseColour(play):
    if play == player:
        while True:
            colour = input("\nChoose the colour:\n   > ").upper()

            if colour in ["R","Y","G","B"]:
                return colour

            elif colour in ["RED","YELLOW","GREEN","BLUE"]:
                return colour[0]

            print("\nInvalid colour")
    else:
        for card in com:

            if card.colour in ["R","Y","G","B"]:
                return card.colour

def isChainValid(cards, topcard):
    if cards[0].colour is None:
        return True

    if topcard.value == cards[0].value:
        return True

    if topcard.colour != cards[0].colour:
        return False

    else:
        val = cards[0].value
        for cardIndex in cards:

            if cardIndex.value != val:
                return False

    return True

def cardsCheck(cards):
    if player[int(cards[0])-1].colour is None:
        return True

    for card in cards:
        try:
            if int(card) not in range(1,len(player)+1):
                return False
        except:
            return False
    return True

def drawCard(op,n):
    if op == player:
        print("\nPlayer draws",str(n),"cards!")

    else:
        print("\nComputer draws",str(n),"cards!")

    for i in range(0,n):
        op.append(randomCard())

def chainDraw(cards, op):
    if cards[0].value == "+2":
        drawCard(op, 2*len(cards))

    elif cards[0].value == "+4":
        drawCard(op, 4*len(cards))

# PLAYER'S TURN CODE

def displayDeck():
    print("\nYour deck: ")
    for i in range(1,len(player)+1):
        print("[%s] %s" %(str(i), player[i-1]))

def inputCard(topcard):
    global player
    while True:
        displayDeck()
        cardInput = input("\nPlease choose a card from your deck or DRAW:\n   > ")

        if cardInput != "":

            if cardInput.upper() == "DRAW":
                print("\nPlayer Draws!")
                player.append(randomCard())
                return topcard, True

            else:
                try:
                    cardsIndex = cardInput.split("&")

                    for i in range(0,len(cardsIndex)):
                        cardsIndex[i] = int(cardsIndex[i])

                    if cardsCheck(cardsIndex):
                        cards = []
                        for i in range(0,len(cardsIndex)):
                            cards.append(player[cardsIndex[i]-1])

                        if isChainValid(cards, topcard):
                            if len(cards) > 1:
                                for i in cards:
                                    pile.append(i)

                                chain = sorted(cardsIndex, reverse=True)
                                for index in chain:
                                    player.pop(index-1)

                                chainDraw(cards, com)

                                topcard = cards[-1]
                                return topcard, False

                            else:
                                player.remove(cards[0])
                                pile.append(cards[0])
                                topcard = cards[-1]
                                chainDraw(cards, com)
                                return topcard, False

                        else:
                            print("\nPlease select an option from the menu above!\n\nTopcard: "+str(topcard))

                    else:
                        print("\nPlease select an option from the menu above!\n\nTopcard: "+str(topcard))

                except:
                        print("\nPlease select an option from the menu above!\n\nTopcard: "+str(topcard))

        else:
            print("\nPlease select an option from the menu above!\n\nTopcard: "+str(topcard))

# COMPUTER'S TURN CODE

def comChain(firstCard):
    chain = [firstCard]
    com.remove(firstCard)
    pile.append(firstCard)

    for card in com:
        if card.value == firstCard.value and card.colour is not None:
            chain.append(card)
            com.remove(card)
            pile.append(card)

    return chain

def comChoose(topcard):
    global com

    time.sleep(random.randint(1,3))
    for card in com:

        if topcard.colour == card.colour or topcard.value == card.value :
            card = comChain(card)

            output = ""
            for i in card:
                output += str(i) + " & "
            print("\nComputer: "+output[:-3])
            chainDraw(card, player)

            return card[-1], False

    print("\nComputer Draws!")
    com.append(randomCard())
    return topcard, True

# TURN CONTROLLER

def turn(topcard, play):
    while True:
        print("\nTopcard: "+str(topcard))

        if play == player:
            topcard, draw = inputCard(topcard)

        else:
            topcard, draw = comChoose(topcard)

        endGame = checkEnd(play)

        if draw == False:
            if topcard.colour is None:
                topcard = Card(chooseColour(play), copy.deepcopy(topcard.value), True)

            if topcard.value != "S":
                break
        else:
            break
    return topcard, endGame

# GAME CONTROL

def startGame():
    global player, com

    for i in [player,com]:
        for j in range(0,8):
            i.append(randomCard())

    topcard = randomCard()

    while topcard.value in ["S","+2","R", "+4","WC"]:
        topcard = randomCard()

    return topcard

def checkEnd(play):
    if len(play) == 0:
        if play == player:
            return "Player"
        else:
            return "Computer"
    else:
        return False

def main():
    global player, com, deck, pile, topcard

    player = []
    com = []
    deck = []
    genDeck()
    topcard = startGame()
    pile = [topcard]

    endGame = False
    count = 0

    while endGame == False:
        count += 1

        if count%2 == 1:
            topcard, endGame = turn(topcard, player)

        else:
            topcard, endGame = turn(topcard, com)

    print("\n"+endGame,"wins!")

# MENU

def menu():
    while True:
        page = input("\nTEXT-BASED ARCADE: UNO\n\t[1] Instructions\n\t[2] Play!\n\t[3] Quit\n\n   > ")

        if page == "1":
            print("\nHELLO!")
            print("THIS IS TEXT-BASED UNO.")
            print("To play a card, just enter its index number into the field.")
            print("If you have no playable cards, you can draw by typing 'DRAW'")
            print("\nALSO! You can chain cards using the & symbol between two cards (Eg. Y4&B4).")

        elif page == "2":
            main()

        elif page == "3":
            break

        else:
            print("\nPlease select an option from the menu above!")

player = []
com = []
deck = []
pile = []
topcard = ""

menu()
