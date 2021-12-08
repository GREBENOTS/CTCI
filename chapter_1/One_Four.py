"""
Palindrome Permutation:  Given a string, write a function to check if it is a permutation of a palindrome.  A palindrome
is a rearrangement of letters.  The palindrome is a word or phrase that is the same forwards and backwards.
A permutation is a rearrangement of letters.  The palindrome does not need to be limited to just dictionary words.
You can ignore casing and non-letter characters.

Input:  Tact Coa
Output:  True (permutations:  "taco cat", "atco cta", etc.)
"""


class PalindromePermutation:
    def __init__(self):
        self.target_string = ''

    def is_palindrome(self, s):
        # if length is odd, remove middle character
        char_array = list(s)
        length = len(char_array)
        if length % 2 == 1:
            char_array.pop(length // 2)  # This will always round down, giving the correct index for middle
            length -= 1

        low = 0
        high = length - 1

        while low < high:
            if char_array[low] == char_array[high]:
                low += 1
                high -= 1
                continue
            else:
                return False

        return True


        pass

    def is_permutation(self):
        # maybe?
        pass




