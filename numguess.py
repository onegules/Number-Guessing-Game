import computerguess

class NumberGuess:
    def __init__(self,high=100):
    ''' Initialize the function and generates a random number based on the
    optional argument'''
        number = np.random.randint(1,high=high)

    def result(self,guess):
        if guess < number:
            return "Too low, try again."
        elif guess > number:
            return "Too high, try again."
        else:
            return True
