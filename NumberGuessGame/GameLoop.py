from NumberGuess import NumberGuess

class Game(NumberGuess):
    def __init__(self,guesses = 5, high=100):
        print("Type object_name.howto() for instructions on how to play")
        self.guesses = guesses
        self.high = high

    def howto(self):
        print("\nIn this game, the program will choose a number and your job is to guess")
        print("the number. You have 5 guesses and at each guess the computer will tell")
        print("you if the number you guesed is above or below the number that was picked.")
        print("The number picked will be between 1 and 100. \n")

        print("To change any of the default values to customize your game type")
        print("object_name.change_guesses(your_guess) and change_high(new_high)")
        print("to change the number of guesses in a game or the highest possible")
        print("value the computer will pick (still choosing from 1 to new_high).\n")

        print("To start the game run object_name.game_start(). Have fun!\n")

    def change_guesses(self,new_guess):
        self.guesses = new_guess

    def change_high(self,new_high):
        self.high = new_high

    def game_start(self):
        numguess = NumberGuess(self.high)
        for i in range(self.guesses):
            print("Please take a guess ({} left): ".format(self.guesses-i))
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

            elif(i == self.guesses-1):
                result = numguess.result(int(guess))
                print(result)
                print("Better luck next time!")

            elif(int(guess) > numguess.high or int(guess) <= 0):
                print("That's not a valid guess. Remember you're guessing between 1 and {}".format(numguess.high -1))

            else:
                result = numguess.result(int(guess))
                print(result)
                continue
