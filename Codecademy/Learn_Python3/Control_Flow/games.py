import random
import time
import module1

money = 100

#######################
###### Coin Flip ######
#######################

def again():
    if money > 0:
        for i in range(3):
            print(".", end = "")
            time.sleep(1)
        while True:
            time.sleep(0.5)
            command = input("\nDo you want to play again? ")
            if command == "Yes":
                break
            elif command == "No":
                break
            else:
                print("I didn't get that. Was that 'Yes' or 'No' ?")
                continue

        if command == "Yes":
            for i in range(3):
                print(".", end = "")
                time.sleep(1)
            print("\n\nWelcome back!!\n")
            time.sleep(1)
            main()
        elif command == "No":
            for i in range(3):
                print(".", end = "")
                time.sleep(1)
            print("\n\nFarewell\n")
            time.sleep(1)
            exit()
    else:
        for i in range(3):
            print(".", end = "")
            time.sleep(1)
        print("\nYOU HAVE NO MONEY!!!")
        time.sleep(1)
        print("GET THE HELL OUT OF MY CASCINO!!!")
        time.sleep(2)
        exit()



def coin_event():
    a = random.randint(0,1)
    if a==0:
        for i in range(3):
            print(".", end = "")
            time.sleep(1)
        print("""
 _   _ _____    _    ____  ____
| | | | ____|  / \  |  _ \/ ___|
| |_| |  _|   / _ \ | | | \___ \ 
|  _  | |___ / ___ \| |_| |___) |
|_| |_|_____/_/   \_\____/|____/
""")
        for i in range(3):
            print(".", end = "")
            time.sleep(1)
        print("\n")
        return "Heads"
    else:
        for i in range(3):
            print(".", end = "")
            time.sleep(1)
        print("""
 _____  _    ___ _     ____
|_   _|/ \  |_ _| |   / ___|
  | | / _ \  | || |   \___ \ 
  | |/ ___ \ | || |___ ___) |
  |_/_/   \_\___|_____|____/
  """)
        for i in range(3):
            print(".", end = "")
            time.sleep(1)
        print("\n")
        return "Tails"

def coin_bet(wager,call):
    result = coin_event()
    if call==result:
        return wager
    else:
        return -wager


module1.welcome()
module1.choose()
def main():
    global money

    while True:
        time.sleep(0.5)
        print("\nCash = "+ str(money))
        wager = int(input("Please enter your bet: "))
        if (wager > money) or (wager <0):
            print("That was funny. Try again.")
            continue
        else:
            print("You bet for $" + str(wager) + ".")
            break
    
    while True:
        call = input("\nPlease enter your call: ")
        time.sleep(0.5)
        if (call == "Heads") or (call == "Tails"):
            print("Your call was " + call + ".\n")
            break
        else:
            print("I didn't quite get it. Was that 'Heads' or 'Tails' ?")
            
            
        

    amount = coin_bet(wager,call)
    money += amount
    if amount >= 0:
        print("Congratulations! You have won $" + str(amount) + ".")
        print("Now you have $" + str(money) + " in your wallet.")
    else:
        print("Bummer! You have lost $" + str(amount) + ".")
        print("Now you have $" + str(money) + " in your wallet.")
    again()

if __name__=="__main__":
    main()






##############################
###### END of Coin Flip ######
##############################

