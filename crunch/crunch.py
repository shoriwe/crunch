# Python 3.7

from itertools import product
from string import ascii_letters, digits, punctuation, whitespace

reference = ascii_letters + digits + punctuation + whitespace

# Check if the input is iterable or not
def is_iter(n):
    try:
        iter(n)
        return True
    except:
        return False

# Crunch class
# letters (string) => reference for permutations
# remove (iterable) => remove it's values from letters
class Crunch:
    def __init__(self,letters=reference,remove=None):
        if not is_iter(remove):
            remove = ''
        self.letter = ''.join(char for char in letters if char not in remove)


    # Generate permutation and execute execute a function with it's values
    def __generate_block(self,lenght, f):

        for value in product(reference, repeat=lenght):
            f(value)

    # Loop that creates a block for each size
    def __generate(self, min_lenght, max_lenght, f):
        # number = size of the actual permutation
        # Example 4 => permutate letters like aaaa aaab aaac aaad ... 9999 ...
        for number in range(min_lenght, max_lenght+1):
            self.__generate_block(number, f)


    # Note that the function recieve the word generated as a tuple Example: ('a','a','a','a')
    def generate(self, min_lenght, max_lenght=None, f=None):
        # When only want to generate in a specific range
        if not max_lenght:
            max_lenght = min_lenght
        # If none function has been entered do nothing with the word generated
        if not type(f):
            f = lambda x: None
        self.__generate(min_lenght, max_lenght, f)