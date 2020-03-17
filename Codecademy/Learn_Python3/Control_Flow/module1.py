import time
import winsound



def welcome():

    """
    ...
    Welcome
    ...
    """
    for i in range(3):
        print(".", end = "")
        time.sleep(1)
    print("\nW", end = "")
    time.sleep(0.3)
    print("e", end = "")
    time.sleep(0.3)
    print("l", end = "")
    time.sleep(0.3)
    print("c", end = "")
    time.sleep(0.3)
    print("o", end = "")
    time.sleep(0.3)
    print("m", end = "")
    time.sleep(0.3)
    print("e\n", end = "")
    time.sleep(0.3)
    for i in range(3):
        print(".", end = "")
        time.sleep(1)

    """

    You're in a cascino.

    ...
    """
    print("\n\nY",end ="")
    time.sleep(0.3)
    print("o",end ="")
    time.sleep(0.29)
    print("u",end ="")
    time.sleep(0.28)
    print("'",end ="")
    time.sleep(0.27)
    print("r",end ="")
    time.sleep(0.26)
    print("e",end ="")
    time.sleep(0.25)
    print(" ",end ="")
    time.sleep(0.24)
    print("i",end ="")
    time.sleep(0.23)
    print("n",end ="")
    time.sleep(0.22)
    print(" ",end ="")
    time.sleep(0.21)
    print("a",end ="")
    time.sleep(0.20)
    print(" ",end ="")
    time.sleep(0.19)
    print("c",end ="")
    time.sleep(0.18)
    print("a",end ="")
    time.sleep(0.17)
    print("s",end ="")
    time.sleep(0.16)
    print("c",end ="")
    time.sleep(0.15)
    print("i",end ="")
    time.sleep(0.14)
    print("n",end ="")
    time.sleep(0.13)
    print("o",end ="")
    time.sleep(0.12)
    print(".\n\n",end ="")
    time.sleep(0.3)
    for i in range(3):
        print(".", end = "")
        time.sleep(1)

    """

    YOU HAVE $100 !!

    """
    print("\n\nYOU", end = "")
    time.sleep(0.6)
    print(" HAVE", end = "")
    time.sleep(0.6)
    print(" $100", end = "")
    time.sleep(0.6)
    print(" !!", end = "")
    time.sleep(0.6)

    """

    WIN AS MUCH AS YOU CAN !!
    GOOD LUCK !!

    """
    print("\nWIN", end = "")
    time.sleep(0.2)
    print(" AS", end = "")
    time.sleep(0.2)
    print(" MUCH", end = "")
    time.sleep(0.2)
    print(" AS", end = "")
    time.sleep(0.2)
    print(" YOU", end = "")
    time.sleep(0.2)
    print(" CAN", end = "")
    time.sleep(0.2)
    print(" !!", end = "")
    time.sleep(2)
    print("\nGOOD", end = "")
    time.sleep(0.2)
    print(" LUCK", end = "")
    time.sleep(0.2)
    print(" !!", end = "")
    time.sleep(0.2)
    duration = 1000  # milliseconds
    freq = 440  # Hz
    winsound.Beep(freq, duration)


    for i in range(3):
        print(".", end = "")
        time.sleep(1)

    print("\n\nPlease choose:")
    time.sleep(1)




def choose():

    while True:
        time.sleep(1)
        print("\n\n###########################\n\n")
        time.sleep(0.3)

        print("1 Coin Flip\n")
        time.sleep(0.1)
        print("2 Chan-Ho\n")
        time.sleep(0.1)
        print("3 Roulette\n")
        time.sleep(0.3)
        num = input("Please enter the number of your game of chance: ")
        print("\n")
        for i in range(3):
            print(".", end = "")
            time.sleep(1)
        print("\n")
        if str(2) <= num <= str(3):
            print("Sorry, game not available. Please choose another game.")
            continue
        elif num == str(1):
            for i in range(3):
                print(".", end = "")
                time.sleep(1)
            print("\n\nGame found. Joining lobby", end = "")
            duration = 1000  # milliseconds
            freq = 440  # Hz
            winsound.Beep(freq, duration)
            for i in range(3):
                print(".", end = "")
                time.sleep(1)
            print("\n\n")
            break
        else:
            print("Not a valid entry. Please Try Again.")
            continue





