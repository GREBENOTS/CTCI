"""
Is Unique:  Implement an algorithm to determine if a string has all unique characters.  What if you cannot use
additional data structures?
"""


class IsUnique:
    def __init__(self, s):
        self.target_string = s

    # Total time complexity O(n)
    def is_unique(self):
        unique = True

        seen = set([])  # Using a hash set because of O(1) retrieval
        for c in self.target_string:
            if c in seen:
                return False
            seen.add(c)
        return True




