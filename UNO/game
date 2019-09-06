# 1 PLAYER VS COMPUTER, COMPUTER MAKES RANDOM MOVES

import random
import time
player = []
com = []
deck = []

def genDeck():
    for i in ["R","Y","G","B"]:
        for j in range(0,10):
            card = i+str(j)
            deck.append(card)
        for j in ["S","T","R"]:
            card = i+str(j)
            deck.append(card)
    deck.append("+4")
    deck.append("+4")
    deck.append("WC")
    deck.append("WC")

def randomCard():
    card = deck[random.randint(0,len(deck)-1)]
    deck.remove(card)
    return card

def startGame():
    for i in [player,com]:
        for j in range(0,8):
            i.append(randomCard())
    topcard = randomCard()

    while topcard[1] in ["S","T","R"] or topcard in ["+4","WC"]:
        topcard = randomCard()

    return topcard

def findAndRemove(card, col, val):
    if card in player and (card[0] == col or card[1] == val or card in ["WC", "+4"]):
        player.remove(card)

def isChainValid(chain, col, val):
    for card in chain:

        if card not in player:
            return False

        if card[0] != col and card[1] != val:
            return False

        else:
            val = card[1]

    return True

def drawCard(op,n):
    if op == player:
        print("\nPlayer draws",str(n),"cards!")

    else:
        print("\nComputer draws",str(n),"cards!")

    for i in range(0,n):
        op.append(randomCard())

def chainDraw(chain):
    drawcount = 2*chain.count("T")

    if drawcount > 0:
        drawCard(com, drawcount)

    drawcount = 4*chain.count("+")

    if drawcount > 0:
        drawCard(com, drawcount)

def inputCard(col, val):
    while True:
        print("Your deck: ")
        print(player)
        card = input("Please choose a card from your deck:\n   > ")

        if card == "DRAW":
            print("Player Draws!")
            player.append(randomCard())
            card = col+val
            return card, True

        elif "&" in card:
            chain = card.split("&")

            if isChainValid(chain, col, val):
                for chaincard in chain:
                    findAndRemove(chaincard,col,val)
                    col, val = chaincard[0], chaincard[1]
                chainDraw(card)
                return chaincard, False

            else:
                print("Invalid card\n")

        elif "&" not in card and card in player and (card[0] == col or card[1] == val or card in ["WC", "+4"]):
            findAndRemove(card,col,val)
            return card, False

        else:
            print("Invalid card\n")

def comChain(i):
    chain = i
    com.remove(i)
    if i == "+4":
        for card in com:

            if card[1] == i[1] and card[0] != "+":
                chain += "&" + card
                com.remove(card)
    chainDraw(chain)
    return chain

def comChoose(col,val):
    time.sleep(random.randint(1,3))
    for i in com:

        if i[0] == col or i[1] == val or i in ["WC", "+4"]:
            i = comChain(i)
            print("Computer: "+i)
            return i, False

    com.append(randomCard())
    card = col+val
    print("Computer Draws!")
    return card, True

def chooseColour(play):
    if play == player:
        while True:
            col = input("Choose the colour:\n   > ")

            if col in ["R","G","Y","B"]:
                return col

            print("Invalid colour")
    else:
        for i in com[0]:

            if i[0] in ["R","G","Y","B"]:
                return i[0]

def checkEnd(play):
    if len(play) == 0:
        return True

def turn(topcard, play, op):
    endGame = False
    while True:
        print()
        print("Topcard: "+topcard)
        col, val = topcard[0],topcard[1]

        if play == player:
            card,draw = inputCard(col, val)

        else:
            card,draw = comChoose(col, val)

        if checkEnd(play):
            if play == player:
                endGame = "Player"

            else:
                endGame = "Computer"
            break

        col, val = card[0],card[1]

        if draw == False:
            if card == "WC":
                col = chooseColour(play)

            elif card == "+4":
                drawCard(op,4)
                col = chooseColour(play)
                val = "C"
            topcard = col+val

            if val != "S":
                break
        else:
            break
    return topcard, endGame

def main():
    genDeck()
    endGame = False
    count = 0
    topcard = startGame()
    while endGame == False:
        count += 1

        if count%2 == 1:
            topcard, endGame = turn(topcard,player,com)

        else:
            topcard, endGame = turn(topcard,com,player)

    print("\n"+endGame,"wins!")

def menu():
    while True:
        page = input("\nTEXT-BASED ARCADE: UNO\n\t[1] Instructions\n\t[2] Play!\n\t[3] Quit\n\n   > ")

        if page == "1":
            print("HELLO!")
            print("THIS IS TEXT-BASED UNO.")
            print("\nStandard cards are represented by a letter representing the colour (R/Y/G/B) followed by its number (0-9).")
            print("For example, green 6 would become G6.")
            print("Instead of a number, special cards are represented according to the following key:")
            print("\tS: Skip\n\tR: Reverse (no u)\n\tT: Draw 2")
            print("Draw 4 cards are represented simply as '+4'")
            print("To play a card, just type it into the field.")
            print("If you have no playable cards, you can draw by typing 'DRAW'")
            print("\nALSO! You can chain cards using the & symbol between two cards (Eg. Y4&B4).")

        elif page == "2":
            main()

        elif page == "3":
            break

        else:
            print("\nPlease select an option from the menu above!")

menu()
