
def welcome():
    print("1 Coin Flip \n 2 Chan-Ho \n 3 Roulette")
    while True:
        num = int(input("Please enter the number of your game of chance: "))
        if 2 <= num <= 3:
            print("Sorry, this game is not available at the moment. \n Please choose another game.")
            continue
        elif num == 1:
            print("Game found. Joining lobby ...")
            break
        else:
            print("Not a valid entry. Please Try Again.")
            continue
        
