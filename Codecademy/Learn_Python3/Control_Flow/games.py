import random

money = 100

#######################
###### Coin Flip ######
#######################

def coin_event():
    a = random.randint(0,1)
    if a==0:
        return "Heads"
    else:
        return "Tails"

def coin_bet(wager,call):
    result = coin_event()
    if call==result:
        return wager
    else:
        return -wager



def main():
    global money

    print("First Game: Coin Flip Game\n")

    while True:
        wager = int(input("Please enter the amount of your wager: "))
        if wager > money:
            print("The amount is exceeding your wallet, Please try again.")
            continue
        else:
            break

    # wager = int(input("Please enter the amount of your wager: "))
    # print("You have wagered for $" + str(wager) + ".")

    call = input("Please enter your call: ")
    print("Your call was " + call + ".\n")

    amount = coin_bet(wager,call)
    if amount >= 0:
        print("Congratulations! You have won $" + str(amount) + ".")
        print("Now you have $" + str(amount + money) + " in your wallet.")
    else:
        print("Bummer! You have lost $" + str(amount) + ".")
        print("Now you have $" + str(amount + money) + " in your wallet.")

if __name__=="__main__":
    main()

##############################
###### END of Coin Flip ######
##############################













