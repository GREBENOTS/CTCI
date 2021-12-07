"""
Check Permutation:  Given two strings, write a method to decide if one is a permutation of the other.
"""


class CheckPermutation:
    def __init__(self):
        self.target_string_1 = ''
        self.target_string_2 = ''

    #  Time complexity O(n) Huzzah!
    def is_permutation(self, s1, s2):
        self.target_string_1 = s1
        self.target_string_2 = s2

        if len(self.target_string_1) != len(self.target_string_2):
            return False

        #  Add all characters to a dict, values being the number of times they exist - O(1) insertion, O(1) retrieval
        seen_1 = {}  # k,v (character, num)
        for s in s1:
            if s not in seen_1:
                seen_1[s] = 0
            seen_1[s] += 1

        seen_2 = {}  # k,v (character, num)
        for s in s2:
            if s not in seen_2:
                seen_2[s] = 0
            seen_2[s] += 1

        #  Here we check the number of times each character was seen
        for s in seen_1:
            if seen_1[s] != seen_2[s]:
                return False

        return True





