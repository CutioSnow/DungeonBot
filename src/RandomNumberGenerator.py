from numpy import random, ndarray

class RandomNumberGenerator:
    '''
    The RandomNumberGenerator class is a helper class designed to organize and
    simplify the process of generating random number sets using the NumPy
    BitGenerator
    '''
    def __init__(self) -> None:
        pass

    def randomIntDefault(low:int,high:int,size:int) -> ndarray:
        '''
        The randomIntDefault method produces a set of random Integers of a 
        specified range (inclusive) and a specified size, then returns the set
        as a NumPy array.

        Parameters:
            low: Lowest value in the generated range (inclusive)
            high: Highest Value in the generated range (inclusive)
            size: Non-zero value for the number of generated Integers

        Returns:
            set: Set of random Integers contained in a NumPy.ndarray
        '''
        #Initialize the Default NumPy random number generator
        rng = random.default_rng()
        #Generates a set of random Integers of a defined size
        set = rng.integers(low=low,high=high+1,size=size)
        #returns the set of generated Integers
        return set

