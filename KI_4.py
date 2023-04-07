
import random as r #import for random number generation

def random_number(): #define a function that returns a number between zero and 100
    number = r.randint(1,100)
    return number

rounds = 0 #counter to give out how many rounds the user played in one session
guess = 0 #count how many tries the user needed to guess the right number
best = 10000 #start value 10000, store the best guess and overwrite if better

player = input("What is your Username? ") #Welcome
print(f"Hello {player}!\n")

startgame_input = input("Welcome! If you want to start the game type in 'start'. You can exit the game at any time by typing in 'exit'. Have fun!\n") #start of the game

while True:
    if str(guess) == "exit": #exit game
        break
    if rounds > 0: #in the first round the user gets more information with startgame_input, but after the start the next rounds get a shorter welcome
        print("Best: ",best,"\n") #give highscore
        startgame_input = input("For a new game press enter. If you want to leave type in 'exit'") #if the user wants to start a new game he just has to press enter
    if startgame_input == "start" or startgame_input == "":
        print("You started a new game...")
        rounds = rounds+1 #count the rounds
        number = random_number() #call random number function to give out a new random number every round
        counter = 1 #reset counter
        while guess != number: #loop so long till user guesses the number
            guess = input("Guess a number between 1 and 100: ") #input guess from user
            if str(guess) == "exit":
                print("You quit the game...")
                break
            else:
                if guess.isdigit() == True: #validate if the input of the user is a number than turn in an integer
                    guess = int(guess)
                    if guess < 1 or guess > 100: #validate if the input is between one and 100
                        print("Your number was out of the intervall. Please enter a number between 1 and 100.")
                    else:
                        deviation = abs(number - guess) #calculate how far the user is away from the actual number
                        higher = number > guess
                        if deviation == 0: #check if the user guessed the number correct
                            print("Your guess was right!")
                            print("The number was: " + str(number)) #give out the correct number
                            print("You needed " + str(counter) + " guesses!")
                            if counter < best: #check if this round was better than the last and overwrite highscore
                                best = counter
                            else:
                                best = best
                        elif deviation < 8: #different cases whether the guess was really close to the right number
                            counter = counter + 1
                            if higher == True: #check if the guessed number is too low or too high
                                print("That was close, but your guess was too low. Try again!")
                            else: print("That was close, but your guess was too high. Try again!")
                        else:
                            counter = counter + 1
                            if higher == True: #check if the guessed number is too low or too high
                                print("Your guess was too low. Try again!")
                            else: print("Your guess was too high. Try again!")
                elif guess.isdigit() == False: #check if the input is a number
                    print("Please enter a number.")
    elif startgame_input == "exit": #quit game
        print("You will leave the game.")
        break
    else:
        print("Invalid input. Please type 'start' to start a new game.")
