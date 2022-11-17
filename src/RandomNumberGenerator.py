from numpy import random, ndarray, array
import random as ran

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
        #TODO: Write documentation https://www.geeksforgeeks.org/python-lists-vs-numpy-arrays/
        rng = random.default_rng()
        #Generates a set of random Integers of a defined size
        set:ndarray = rng.integers(low=low,high=high+1,size=size)
        #returns the set of generated Integers
        return set

    def randomIntWeightedHigh(low:int,high:int,size:int) -> ndarray:
        '''
        The randomIntWeightedHigh method generates a set of random integers in 
        a specified range (inclusive) and size weighted to prefer higher valued
        integers (i.e. low=1 and high=20 will favor values >10).

        Parameters:
            low: Lowest value in the generated range (inclusive)
            high: Highest Value in the generated range (inclusive)
            size: Non-zero value for the number of generated Integers
        
        Returns:
            set: Weighted set of random Integers in a NumPy.ndarray
        '''
        #Initializes list to contain generated random numbers
        

    def weightGenerate():
        ''''''

