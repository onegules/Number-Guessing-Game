from numguess import NumberGuess

print("In this game, the program will choose a number and your job is to guess")
print("the number. You have 5 guesses and at each guess the computer will tell")
print("you if the number you guesed is above or below the number that was picked.")
print("The number picked will be between 1 and 100. Would you like to raise the")
print("highest possible value? [y/n]")

answer = input()

if(answer == 'y'):
    print("What would you like the new highest value to be?")
    try:
        new_high = int(input())
        numguess = NumberGuess(high=new_high+1)
        print("\n")
    except ValueError:
        print("\nSeems you put in something I didn't understand. So I'll just initialize as the default\n")
        numguess = NumberGuess()

elif(answer == 'n'):
    print("Alright then, let's move on. \n")
    numguess = NumberGuess()

else:
    print("\nSince I'm not sure what you typed, I will initialize using the default settings.\n")
    numguess = NumberGuess()

print("Would you like to adjust the number of guesses? [y/n]")
answer = input()

if(answer == 'y'):
    print("Please input the number of guesses for this session.")
    try:
        new_guesses = int(input())
        guesses = new_guesses
        print("\n")
    except ValueError:
        print("\nSeems you put in something I didn't understand. So I'll just initialize as the default\n")
        guesses = 5

elif(answer == 'n'):
    print("Alright then, let's move on the game!\n")
    guesses = 5

else:
    print("\nSince I'm not sure what you typed, I will initialize using the default settings.\n")
    guesses = 5


for i in range(guesses):
    print("Please take a guess ({} left): ".format(guesses-i))
    guess = input()
    while True:
        try:
            int(guess)
        except ValueError:
            print("Unfortunately that's not a number, please try again: ")
            guess = input()
            continue
        break
    if(numguess.result(int(guess)) == True):
        print("Congratulations! You guessed right!")
        break

    elif(i == guesses-1):
        result = numguess.result(int(guess))
        print(result)
        print("Better luck next time!")

    else:
        result = numguess.result(int(guess))
        print(result)
        continue

exit()
