import numpy as np

class NumberGuess:
    def __init__(self,high=101):
        ''' Initialize the function and generates a random number based on the
        optional argument'''

        self.number = np.random.randint(1,high=high)
        self.high = high

    def result(self,guess):
        '''Calculates the result of a guess'''

        if guess < self.number:
            return "Too low."
        elif guess > self.number:
            return "Too high."
        else:
            return True
