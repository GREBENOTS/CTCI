"""
String Compression:  Implement a method to perform basic string compression using the counts of repeated characters.
For example, the string aabcccccaaa would become a2b1c5a3.  If the compressed string would not become smaller than the
original string, your method should return the original string.  You can assume the string has only uppercase and
lowercase letters (a-z).
"""


class StringCompression:
    def __init__(self):
        self.target_string = ''

    # Total time complexity O(n)
    def compress(self, s):
        self.target_string = s
        seen = set([])  # Using a hash set because of O(1) retrieval
        for c in self.target_string:
            if c in seen:
                return False
            seen.add(c)
        return True




