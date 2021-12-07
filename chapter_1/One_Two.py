"""
Check Permutation:  Given two strings, write a method to decide if one is a permutation of the other.
"""


class CheckPermutation:
    def __init__(self, s1, s2):
        self.target_string_1 = s1
        self.target_string_2 = s2

    # Total time complexity O(n)
    def is_unique(self):
        unique = True

        seen = set([])  # Using a hash set because of O(1) retrieval
        for c in self.target_string:
            if c in seen:
                return False
            seen.add(c)
        return True




