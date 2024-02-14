import random  # we are importing the random 

def roll_dice():
    #Simulate rolling two dice and return the result.
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1, die2 #returning the values in tuple form

def main():
    print("Welcome to the Dice Rolling Simulator!")
    while True:                                                                                                        #using while loop to execute the untill user whats to execute
        input("Press Enter to roll the dice...")  # Wait for user input
        die1, die2 = roll_dice()
        print(f"You rolled: {die1} and {die2}")
        play_again = input("Roll again? (start): ").lower()
        if play_again != 'start':   # if user enter anything rather than start , it wouldn't end
            print("Thanks for playing!")
            break
        

if __name__ == "__main__":
    main()
